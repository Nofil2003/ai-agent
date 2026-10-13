import os
from dotenv import load_dotenv
from openai import OpenAI, responses
from openai.types.completion_usage import PromptTokensDetails
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)


def main():
    print("Hello from ai-agent!")
    if not api_key:
        raise RuntimeError("API key is none!")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[{"role": "user", "content": args.user_prompt}],
    )
    if response.usage == None:
        raise RuntimeError("Usage is None!")

    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {completion_tokens}")

    print(f"Response: \n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
