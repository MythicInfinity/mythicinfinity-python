import typing

from . import VoiceOptions
from .gen.core import RequestOptions
from .gen.tts.client import TtsClient, OMIT, AsyncTtsClient


DEFAULT_MODEL_ID = "infinity_catalyst_lite_v1"
DEFAULT_VOICE_ID = "kiera"

class StreamingTTSClient(TtsClient):
    @typing.overload
    def generate(
        self,
        text: str,
        *,
        stream: typing.Literal[False],
        model_id: str=DEFAULT_MODEL_ID,
        voice_id: str=DEFAULT_VOICE_ID,
        voice_options: typing.Optional[VoiceOptions] = OMIT,
        format: typing.Optional[typing.Literal["wav_24000"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bytes:
        """
        Primary text to speech endpoint.

        Parameters
        ----------
        model_id : str
            (required) The model ID to generate speech audio with.

        text : str
            (required) The desired text spoken in the generated audio.

        voice_id : str
            (required) The voice ID to use for generating audio.

        voice_options : typing.Optional[VoiceOptions]

        format : typing.Optional[typing.Literal["wav_24000"]]
            (optional) The audio format of the output audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        ------
        bytes
            Returns the audio bytes.
        """
        ...

    @typing.overload
    def generate(
        self,
        text: str,
        *,
        stream: typing.Literal[True],
        model_id: str=DEFAULT_MODEL_ID,
        voice_id: str=DEFAULT_VOICE_ID,
        voice_options: typing.Optional[VoiceOptions] = OMIT,
        format: typing.Optional[typing.Literal["wav_24000"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Primary text to speech endpoint.

        Parameters
        ----------
        model_id : str
            (required) The model ID to generate speech audio with.

        text : str
            (required) The desired text spoken in the generated audio.

        voice_id : str
            (required) The voice ID to use for generating audio.

        voice_options : typing.Optional[VoiceOptions]

        format : typing.Optional[typing.Literal["wav_24000"]]
            (optional) The audio format of the output audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.Iterator[bytes]
            Returns a stream of audio bytes.
        """
        ...

    def generate(
        self,
        text: str,
        *,
        stream: bool = False,
        model_id: str=DEFAULT_MODEL_ID,
        voice_id: str=DEFAULT_VOICE_ID,
        voice_options: typing.Optional[VoiceOptions] = OMIT,
        format: typing.Optional[typing.Literal["wav_24000"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[bytes, typing.Iterator[bytes]]:
        result_generator = super().generate_internal(model_id=model_id, text=text, voice_id=voice_id, voice_options=voice_options,
                               format=format, request_options=request_options)

        if stream:
            return result_generator

        audio_bytes = b''.join(result_generator)

        return audio_bytes


class AsyncStreamingTTSClient(AsyncTtsClient):
    @typing.overload
    async def generate(
        self,
        text: str,
        *,
        stream: typing.Literal[False],
        model_id: str=DEFAULT_MODEL_ID,
        voice_id: str=DEFAULT_VOICE_ID,
        voice_options: typing.Optional[VoiceOptions] = OMIT,
        format: typing.Optional[typing.Literal["wav_24000"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bytes:
        """
        Primary text to speech endpoint.

        Parameters
        ----------
        model_id : str
            (required) The model ID to generate speech audio with.

        text : str
            (required) The desired text spoken in the generated audio.

        voice_id : str
            (required) The voice ID to use for generating audio.

        voice_options : typing.Optional[VoiceOptions]

        format : typing.Optional[typing.Literal["wav_24000"]]
            (optional) The audio format of the output audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        ------
        bytes
            Returns the audio bytes.
        """
        ...

    @typing.overload
    async def generate(
        self,
        text: str,
        *,
        stream: typing.Literal[True],
        model_id: str=DEFAULT_MODEL_ID,
        voice_id: str=DEFAULT_VOICE_ID,
        voice_options: typing.Optional[VoiceOptions] = OMIT,
        format: typing.Optional[typing.Literal["wav_24000"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Primary text to speech endpoint.

        Parameters
        ----------
        model_id : str
            (required) The model ID to generate speech audio with.

        text : str
            (required) The desired text spoken in the generated audio.

        voice_id : str
            (required) The voice ID to use for generating audio.

        voice_options : typing.Optional[VoiceOptions]

        format : typing.Optional[typing.Literal["wav_24000"]]
            (optional) The audio format of the output audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.AsyncIterator[bytes]
            Returns a stream of audio bytes.
        """
        ...

    async def generate(
        self,
        text: str,
        *,
        stream: bool = False,
        model_id: str=DEFAULT_MODEL_ID,
        voice_id: str=DEFAULT_VOICE_ID,
        voice_options: typing.Optional[VoiceOptions] = OMIT,
        format: typing.Optional[typing.Literal["wav_24000"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[bytes, typing.AsyncIterator[bytes]]:
        async_result_generator = super().generate_internal(model_id=model_id, text=text, voice_id=voice_id, voice_options=voice_options,
                               format=format, request_options=request_options)

        if stream:
            return async_result_generator

        audio_bytes = b''.join([chunk async for chunk in async_result_generator])

        return audio_bytes