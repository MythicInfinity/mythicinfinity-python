import os
import typing

import httpx

from . import MythicInfinityClientEnvironment
from .gen.base_client import MythicInfinityBaseClient, AsyncMythicInfinityBaseClient
from .streaming_tts_client import StreamingTTSClient, AsyncStreamingTTSClient


class MythicInfinityClient(MythicInfinityBaseClient):
    def __init__(self, *, base_url: typing.Optional[str] = os.getenv("MYTHICINFINITY_BASE_ENDPOINT"),
                 environment: MythicInfinityClientEnvironment = MythicInfinityClientEnvironment.PRODUCTION,
                 api_key: typing.Optional[
                     typing.Union[str, typing.Callable[[], str]]
                 ] = os.getenv("MYTHICINFINITY_API_KEY"), timeout: typing.Optional[float] = None,
                 follow_redirects: typing.Optional[bool] = True, httpx_client: typing.Optional[httpx.Client] = None):
        super().__init__(base_url=base_url, environment=environment, api_key=api_key, timeout=timeout,
                         follow_redirects=follow_redirects, httpx_client=httpx_client)

        self.tts = StreamingTTSClient(client_wrapper=self._client_wrapper)


class AsyncMythicInfinityClient(AsyncMythicInfinityBaseClient):
    def __init__(self, *, base_url: typing.Optional[str] = None,
                 environment: MythicInfinityClientEnvironment = MythicInfinityClientEnvironment.PRODUCTION,
                 api_key: typing.Optional[
                     typing.Union[str, typing.Callable[[], str]]
                 ] = os.getenv("MYTHICINFINITY_API_KEY"), timeout: typing.Optional[float] = None,
                 follow_redirects: typing.Optional[bool] = True,
                 httpx_client: typing.Optional[httpx.AsyncClient] = None):
        super().__init__(base_url=base_url, environment=environment, api_key=api_key, timeout=timeout,
                         follow_redirects=follow_redirects, httpx_client=httpx_client)

        self.tts = AsyncStreamingTTSClient(client_wrapper=self._client_wrapper)
