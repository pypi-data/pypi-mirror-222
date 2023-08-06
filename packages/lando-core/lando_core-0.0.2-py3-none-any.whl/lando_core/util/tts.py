import edge_tts


class TTS:
    @staticmethod
    async def tts(content, timbre):
        communicate = edge_tts.Communicate(content, timbre)
        chunks = [message["data"] async for message in communicate.stream() if message["type"] == "audio"]
        return b''.join(chunks)

    @staticmethod
    async def list_voices():
        return await edge_tts.list_voices()
