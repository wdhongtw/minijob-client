from typing import Any, Dict, List

import attr


@attr.s(auto_attribs=True)
class ItemMeta:
    """ The item metadata model. """

    item_id: str
    length: int
    timestamp: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id
        length = self.length
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "length": length,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "ItemMeta":
        d = src_dict.copy()
        item_id = d.pop("item_id")

        length = d.pop("length")

        timestamp = d.pop("timestamp")

        item_meta = ItemMeta(
            item_id=item_id,
            length=length,
            timestamp=timestamp,
        )

        item_meta.additional_properties = d
        return item_meta

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
