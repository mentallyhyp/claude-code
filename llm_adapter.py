from llm_adapter import create_message

response = create_message(
    model="llama3.2:latest",
    messages=[
        {"role": "user", "content": "Say hello in one sentence"}
    ]
)

print(response)
