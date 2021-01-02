from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.meta import Meta
from typing import cast



def _get_kwargs(
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Meta]:
    if response.status_code == 200:
        response_200 = Meta.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Meta]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,

) -> Response[Meta]:
    kwargs = _get_kwargs(
        client=client,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,

) -> Optional[Meta]:
    """ Show metadata for the site. """

    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,

) -> Response[Meta]:
    kwargs = _get_kwargs(
        client=client,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,

) -> Optional[Meta]:
    """ Show metadata for the site. """

    return (await asyncio_detailed(
        client=client,

    )).parsed
