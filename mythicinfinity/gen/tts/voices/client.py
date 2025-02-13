# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from ...types.voice import Voice
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.client_wrapper import AsyncClientWrapper


class VoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        model_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Voice]:
        """
        Parameters
        ----------
        model_id : typing.Optional[str]
            (optional) Filter voices by this model ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Voice]
            Successful Response

        Examples
        --------
        from Mythic_Infinity import MythicInfinityClient

        client = MythicInfinityClient(
            api_key="YOUR_API_KEY",
        )
        client.tts.voices.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/audio/voices",
            method="GET",
            params={
                "model_id": model_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Voice],
                    parse_obj_as(
                        type_=typing.List[Voice],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, voice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Voice:
        """
        Parameters
        ----------
        voice_id : str
            (optional) Return only data for this voice ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Voice
            Successful Response

        Examples
        --------
        from Mythic_Infinity import MythicInfinityClient

        client = MythicInfinityClient(
            api_key="YOUR_API_KEY",
        )
        client.tts.voices.get(
            voice_id="voice_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/audio/voices/{jsonable_encoder(voice_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Voice,
                    parse_obj_as(
                        type_=Voice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncVoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        model_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Voice]:
        """
        Parameters
        ----------
        model_id : typing.Optional[str]
            (optional) Filter voices by this model ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Voice]
            Successful Response

        Examples
        --------
        import asyncio

        from Mythic_Infinity import AsyncMythicInfinityClient

        client = AsyncMythicInfinityClient(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tts.voices.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/audio/voices",
            method="GET",
            params={
                "model_id": model_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Voice],
                    parse_obj_as(
                        type_=typing.List[Voice],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, voice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Voice:
        """
        Parameters
        ----------
        voice_id : str
            (optional) Return only data for this voice ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Voice
            Successful Response

        Examples
        --------
        import asyncio

        from Mythic_Infinity import AsyncMythicInfinityClient

        client = AsyncMythicInfinityClient(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tts.voices.get(
                voice_id="voice_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/audio/voices/{jsonable_encoder(voice_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Voice,
                    parse_obj_as(
                        type_=Voice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
