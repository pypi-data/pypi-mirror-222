from collections import OrderedDict

from huggingface_hub import hf_hub_download
from omegaconf import OmegaConf

from ..constants import DEFAULT_PREPROCESSOR_SUBFOLDER, RegistryType, RepoType
from ..utils import get_module_class, list_repo_files


class Preprocessor:
    """
    Base class for all data preprocessors.

    Args:
        config: Preprocessor properties
    """

    preprocessor_subfolder = DEFAULT_PREPROCESSOR_SUBFOLDER

    def __init__(self, config, **kwargs):
        self.config = config.update(kwargs)

    def __call__(self, inputs, **kwargs):
        """
        An abstract call method for a preprocessor. All preprocessors must implement this.

        Args:
            inputs: Raw inputs to process. Usually a list or a dict
            **kwargs: Extra keyword arguments depending on the preprocessor
        """
        raise NotImplementedError

    def save(self, path, **kwargs):
        raise NotImplementedError

    def push_to_hub(self, hub_path):
        raise NotImplementedError

    @classmethod
    def load(
        cls,
        hub_or_local_path,
        subfolder: str = None,
        force_return_dict: bool = False,
        **kwargs
    ):
        """
        Load a preprocessor or a pipeline of preprocessors from a local or Hub path. This method automatically detects
        any preprocessor in the path. If there's only one preprocessor, returns it and if there are more, returns a
        dictionary of preprocessors.

        This method must also be overriden by subclasses as it internally calls this method for every possible
        preprocessor found in the repo.

        Args:
            hub_or_local_path: Path to hub or local repo
            subfolder: Subfolder for the preprocessor.
            force_return_dict: Whether to return a dict even if there's only one preprocessor available on the repo
            **kwargs: Extra kwargs

        Returns:
            A Preprocessor subclass or a dict of Preprocessor subclass instances
        """
        subfolder = subfolder or cls.preprocessor_subfolder
        preprocessor_files = list_repo_files(hub_or_local_path, subfolder=subfolder)
        preprocessors = OrderedDict()
        for f in preprocessor_files:
            if f.endswith(".yaml"):
                config_file = hf_hub_download(
                    hub_or_local_path,
                    filename=f,
                    subfolder=subfolder,
                    repo_type=RepoType.MODEL
                )
                config = OmegaConf.load(config_file)
                name = config.get("name", None)
                if name:
                    preprocessor_cls = get_module_class(name, module_type=RegistryType.PREPROCESSOR)
                    preprocessor = preprocessor_cls.load(hub_or_local_path, subfolder=subfolder)
                    preprocessors[name] = preprocessor
                else:
                    raise ValueError(f"The config file `{config_file}` does not have the property `name`!")
        if len(preprocessors) == 1 and not force_return_dict:
            return list(preprocessors.values())[0]

        return preprocessors
