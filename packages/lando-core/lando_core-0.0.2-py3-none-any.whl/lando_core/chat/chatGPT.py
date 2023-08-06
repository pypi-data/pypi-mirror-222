import openai


class OpenaiChat:
    def __init__(self, model="gpt-3.5-turbo-16k"):
        self.model = model

    async def _stream_chat(self, messages, temperature, **kwargs):
        params = {
            'model': self.model,
            'messages': messages,
            'temperature': temperature,
            'top_p': 1,
            'stream': True,
            **kwargs
        }
        resp = await openai.ChatCompletion.acreate(**params)
        async for delta in resp:
            yield delta['choices'][0]['delta'].get('content', '')

    async def _chat(self, messages, temperature, stream, **kwargs):
        call = self._stream_chat(messages, temperature, **kwargs)
        if stream:
            return call
        return ''.join([delta async for delta in call])

    async def chat(self, messages, temperature=0.0, stream=False, **kwargs):
        pass


class Gpt3Chat(OpenaiChat):
    def __init__(self):
        super().__init__("gpt-3.5-turbo-16k")

    async def chat(self, messages, temperature=0.0, stream=False, **kwargs):
        return await self._chat(messages, temperature, stream, **kwargs)


class Gpt4Chat(OpenaiChat):
    def __init__(self):
        super().__init__("gpt-4")

    async def chat(self, messages, temperature=0.0, stream=False, **kwargs):
        return await self._chat(messages, temperature, stream, **kwargs)
