"""matatika module"""

import abc
import json
from dataclasses import asdict
from typing import Dict


class Resource(abc.ABC):
    """Base class for resource objects"""

    @property
    def version(self) -> str:
        """Resource version identifier"""

    @property
    def attr_translations(self) -> Dict[str, str]:
        """Attribution translations to perform when converting from resource to Python object"""

    def to_dict(self, filter_none=True, apply_translations=True):
        """Converts the resource object to a dictionary"""
        dict_repr = asdict(self)

        if apply_translations:
            for attr, translation in self.attr_translations.items():
                dict_repr = {
                    attr if k == translation else k: v for k, v in dict_repr.items()
                }

        if filter_none:
            dict_repr = {k: v for k, v in dict_repr.items() if v is not None}

        return dict_repr

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, resource_dict: dict):
        """Resolves a resource object from a dictionary"""
        resource = cls()

        # set version if not delared by the resource object type
        if not cls.version:
            resource.version = resource_dict.get("version")

        return resource

    def to_json_str(self, filter_none=True):
        """Converts the resource object to a JSON string"""
        return json.dumps(self.to_dict(filter_none))
