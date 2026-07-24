from app.ai.openai_provider import OpenAIProvider


class ProviderFactory:

    @staticmethod
    def create():

        return OpenAIProvider()