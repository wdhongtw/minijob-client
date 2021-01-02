from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.http_validation_error import HTTPValidationError
from ...models.item import Item
from typing import Dict
from typing import cast
from ...models.item_id import ItemId



def _get_kwargs(
    *,
    client: Client,
    json_body: Item,

) -> Dict[str, Any]:
    url = "{}/items/".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    

    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[
    ItemId,
    HTTPValidationError
]]:
    if response.status_code == 200:
        response_200 = ItemId.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[
    ItemId,
    HTTPValidationError
]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Item,

) -> Response[Union[
    ItemId,
    HTTPValidationError
]]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    json_body: Item,

) -> Optional[Union[
    ItemId,
    HTTPValidationError
]]:
    """ Allocate new item. """

    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    json_body: Item,

) -> Response[Union[
    ItemId,
    HTTPValidationError
]]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    json_body: Item,

) -> Optional[Union[
    ItemId,
    HTTPValidationError
]]:
    """ Allocate new item. """

    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed
