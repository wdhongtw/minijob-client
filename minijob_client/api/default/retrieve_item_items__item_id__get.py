from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.http_validation_error import HTTPValidationError
from typing import cast
from ...models.item import Item



def _get_kwargs(
    *,
    client: Client,
    item_id: str,

) -> Dict[str, Any]:
    url = "{}/items/{item_id}".format(
        client.base_url,item_id=item_id)

    headers: Dict[str, Any] = client.get_headers()

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[
    Item,
    HTTPValidationError
]]:
    if response.status_code == 200:
        response_200 = Item.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[
    Item,
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
    item_id: str,

) -> Response[Union[
    Item,
    HTTPValidationError
]]:
    kwargs = _get_kwargs(
        client=client,
item_id=item_id,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    item_id: str,

) -> Optional[Union[
    Item,
    HTTPValidationError
]]:
    """ Retrieve item. """

    return sync_detailed(
        client=client,
item_id=item_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    item_id: str,

) -> Response[Union[
    Item,
    HTTPValidationError
]]:
    kwargs = _get_kwargs(
        client=client,
item_id=item_id,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    item_id: str,

) -> Optional[Union[
    Item,
    HTTPValidationError
]]:
    """ Retrieve item. """

    return (await asyncio_detailed(
        client=client,
item_id=item_id,

    )).parsed
