import os
from dotenv import load_dotenv
from openai import OpenAI, responses
from openai.types.completion_usage import PromptTokensDetails

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)


def main():
    print("Hello from ai-agent!")
    if not api_key:
        raise RuntimeError("API key is none!")

    if response.usage == None:
        raise RuntimeError("Usage is None!")

    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {completion_tokens}")

    print(f"Response: \n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
