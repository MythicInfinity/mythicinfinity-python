import os
import sys
import unittest

import io
import pytest
import wave

file_dir = os.path.dirname(
    os.path.abspath(
        os.path.realpath(__file__)))


class MythicInfinityClientTestCases(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        # These values are checked for presence here but are picked up automatically by the client.
        api_key = os.getenv("MYTHICINFINITY_API_KEY")
        if api_key is None:
            raise Exception("No API Key present in env.")

        # Ensure that we can import the sdk package from the source tree
        sys.path.append(f'{file_dir}/../')

    def _assert_audio_bytes(self, audio_bytes):
        assert audio_bytes is not None
        assert isinstance(audio_bytes, bytes)
        assert len(audio_bytes) > 44, "expected at least more than 44 byte header"

        with io.BytesIO(audio_bytes) as wav_file:
            with wave.open(wav_file, 'rb') as wf:
                # Get WAV file parameters
                nchannels = wf.getnchannels()
                sampwidth = wf.getsampwidth()
                framerate = wf.getframerate()
                nframes = wf.getnframes()
                comptype = wf.getcomptype()
                compname = wf.getcompname()

                # Read the audio frames
                frames = wf.readframes(nframes)

                # assert framerate == 24_000
                assert nchannels == 1
                assert sampwidth == 2

    def test_nonstreaming_inference_with_sync_client(self):
        from mythicinfinity import MythicInfinityClient

        # api_key, base_url are set via environment variable
        client = MythicInfinityClient()

        ## Test .generate(stream=False)
        audio_bytes = client.tts.generate("Mythic Infinity is awesome!", stream=False)
        self._assert_audio_bytes(audio_bytes)

    def test_streaming_inference_with_sync_client(self):
        from mythicinfinity import MythicInfinityClient

        # api_key, base_url are set via environment variable
        client = MythicInfinityClient()

        ## Test .generate(stream=True)
        audio_gen = client.tts.generate("Mythic Infinity is awesome!", stream=True)
        audio_bytes = b''.join(list(audio_gen))

        self._assert_audio_bytes(audio_bytes)

    @pytest.mark.asyncio
    async def test_nonstreaming_inference_with_async_client(self):
        from mythicinfinity import AsyncMythicInfinityClient

        # api_key, base_url are set via environment variable
        client = AsyncMythicInfinityClient()

        ## Test .generate(stream=False)
        audio_bytes = await client.tts.generate("Mythic Infinity is awesome!", stream=False)
        self._assert_audio_bytes(audio_bytes)

    @pytest.mark.asyncio
    async def test_streaming_inference_with_async_client(self):
        from mythicinfinity import AsyncMythicInfinityClient

        # api_key, base_url are set via environment variable
        client = AsyncMythicInfinityClient()

        ## Test .generate(stream=True)
        audio_gen = await client.tts.generate("Mythic Infinity is awesome!", stream=True)
        audio_bytes = b''.join([x async for x in audio_gen])

        self._assert_audio_bytes(audio_bytes)

    @pytest.mark.asyncio
    async def test_voices(self):
        from mythicinfinity import AsyncMythicInfinityClient

        # api_key, base_url are set via environment variable
        client = AsyncMythicInfinityClient()

        all_voices = await client.tts.voices.list()
        assert len(all_voices) > 0

        voice = await client.tts.voices.get(all_voices[0].voice_id)
        assert voice is not None
