import json
from trism import TritonLMModel


async def main(prompt: str):

    pipeline = TritonLMModel(
        model="vllm.model",
        version=1,
        url="localhost:1235",
        stream=True
    )

    sampling_parameters = {
        "temperature": 0.7,
        "max_tokens": 4096,
    }
    async for token in pipeline.run(
        prompt,
        sampling_parameters=sampling_parameters,
        show_thinking=True,
    ):
        print(token) # Check output
    await pipeline._serverclient.close()


if __name__ == "__main__":

    input_prompt = input("Enter your prompt: ")

    import asyncio
    asyncio.run(main(prompt=input_prompt))