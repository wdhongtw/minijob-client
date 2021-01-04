from typing import Any, Dict, List, Union

import attr

from ..types import UNSET, Unset


@attr.s(auto_attribs=True)
class Meta:
    """ Metadata for the server. """

    version: Union[Unset, str] = "0.1.0"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Meta":
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        meta = Meta(
            version=version,
        )

        meta.additional_properties = d
        return meta

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
