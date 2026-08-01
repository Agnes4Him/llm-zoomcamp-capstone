messages = []

while True:
    user_input = input("\nUser: ")
    
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append(
        (
            "user",
            user_input
        )
    )

    response = agent.invoke(
        {
            "messages": messages
        }
    )

# print(response["messages"][-1].content)
print("\nAssistant:", response["messages"][-1].content[1]["text"])
print("input_tokens", response["messages"][-1].usage_metadata["input_tokens"])
print("output_tokens", response["messages"][-1].usage_metadata["output_tokens"])
print("total_tokens", response["messages"][-1].usage_metadata["total_tokens"])