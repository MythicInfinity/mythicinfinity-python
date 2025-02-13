<!-- PROJECT LOGO -->

<p align="center">
  <a href="https://www.mythicinfinity.com">
    <img src="https://www.mythicinfinity.com/app/assets/email-logo.png" 
     alt="Logo" height="36">
  </a>

  <h3 align="center">MythicInfinity Python Client</h3>

  <p align="center">
    <img src="https://img.shields.io/pypi/v/mythicinfinity" alt="pypi version" />
    <img src="https://img.shields.io/pypi/pyversions/mythicinfinity" alt="supported python versions" />
    <img src="https://img.shields.io/github/license/mythicinfinity/mythicinfinity-python" alt="license">
  </p>

  <p align="center">
    Ultra-low latency realtime AI Text to Speech.
    <br />
    <a href="https://www.mythicinfinity.com/app/register"><strong>Sign Up for an API Key »</strong></a>
    <br />
    <br />
    <a href="https://www.mythicinfinity.com/docs">Read the docs</a>
    ·
    <a href="https://github.com/mythicinfinity/mythicinfinity-python/issues">Report Bug</a>
  </p>
</p>

### Overview

 - Easy installation with pip.
 - Streaming audio bytes and non-streaming both supported.
 - Async/await and standard sync code both supported.

## Installation

Install the python package as a dependency of your application.

```bash
$ pip install mythicinfinity
```

## Basic Examples

```python
from mythicinfinity import MythicInfinityClient


def main():
    # Instantiate the client with your api key
    client = MythicInfinityClient(api_key="YOUR_API_KEY")
    
    # Call the TTS API. By default, stream is False.
    audio_bytes = client.tts.generate(text="Hello world.")
    
    with open('my_audio.wav', 'wb') as f:
        f.write(audio_bytes)

if __name__ == "__main__":
    main()
```

This sample calls the Text-To-Speech service and saves the resultant audio bytes to a file.

### Streaming Example

```python
from mythicinfinity import MythicInfinityClient


def main():
    # Instantiate the client with your api key
    client = MythicInfinityClient(api_key="YOUR_API_KEY")
    
    # Call the TTS API with stream=True.
    # This will stream the audio bytes in real-time, 
    #   as they become available from the AI model.
    audio_bytes_generator = client.tts.generate(text="Hello world.", stream=True)
    
    with open('my_audio.wav', 'wb') as f:
        for audio_bytes in audio_bytes_generator:
            f.write(audio_bytes)

if __name__ == "__main__":
    main()
```


### Async Support

- Code relying on `async / await` patterns is fully supported.

```python
import asyncio
from mythicinfinity import AsyncMythicInfinityClient


async def main():
    # Instantiate the client with your api key
    client = AsyncMythicInfinityClient(api_key="YOUR_API_KEY")
    
    # Call the TTS API with stream=False.
    audio_bytes = await client.tts.generate(text="Hello world.")
    
    with open('my_async_audio_1.wav', 'wb') as f:
        f.write(audio_bytes)
    
    # Call the TTS API with stream=True.
    # This will stream the audio bytes in real-time, 
    #   as they become available from the AI model.
    audio_bytes_generator = await client.tts.generate(text="Hello world.", stream=True)
    
    with open('my_async_audio_2.wav', 'wb') as f:
        async for audio_bytes in audio_bytes_generator:
            f.write(audio_bytes)

if __name__ == "__main__":
    asyncio.run(main())
```

This sample first calls the `client.tts.generate` method without streaming using `await` and then does the same with 
streaming enabled.