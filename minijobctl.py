import argparse
import base64
from typing import Optional, List, Union

import pydantic
import tabulate

from minijob_client import Client
import minijob_client.models as models
import minijob_client.api.default.create_item_items__post as create_item_items__post
import minijob_client.api.default.retrieve_all_item_detail_items__get as retrieve_all_item_detail_items__get


class Options(pydantic.BaseModel):
    # path of file to be upload
    upload_file: Optional[str]

    # should I list file?
    list_file: bool

    server_url: str


def parse_arguments() -> Options:
    parser = argparse.ArgumentParser(description="control tool for minijob")
    parser.add_argument("-s", "--server-url", type=str, required=True)
    parser.add_argument("--list-file", action="store_true")
    parser.add_argument("--upload-file", type=str)

    args = parser.parse_args()
    return Options(**vars(args))


def upload_file(client: Client, path: str) -> None:
    with open(path, "rb") as file_:
        content = file_.read()
    encoded = base64.b64encode(content).decode()

    item = models.Item(path=path, content=encoded)

    result: Optional[Union[models.ItemId, models.HTTPValidationError]] = create_item_items__post.sync(
        client=client, json_body=item
    )
    if not result or isinstance(result, models.HTTPValidationError):
        print("Fail to post item")
        return

    print("Item posted with ID: {}".format(result.item_id))


def list_file(client: Client) -> None:
    items: Optional[List[models.ItemMeta]] = retrieve_all_item_detail_items__get.sync(client=client)
    if not items:
        print("Fail to retrieve items")
        return

    print(tabulate.tabulate([item.to_dict() for item in items], headers="keys"))


def main():
    options = parse_arguments()
    client = Client(base_url=options.server_url)

    if options.upload_file:
        upload_file(client, options.upload_file)
    if options.list_file:
        list_file(client)


if __name__ == "__main__":
    main()
