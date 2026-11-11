import ollama

# Choose a chat-capable model (ensured it is pulled)
model_name = 'gemma3:4b'

# Define the system prompt
system_prompt = """You are interviewing a ski resort owner. Ask short questions to understand their needs and priorities."""



# Start the conversation with an initial message
initial_message = """What do you want your new online system to do?"""

# Initialize conversation with a system prompt and a user message
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": initial_message},
]

# First response from the bot
response = ollama.chat(model=model_name, messages=messages)
print("Bot:", response['message']['content'])
messages.append({"role": "assistant", "content": response['message']['content']})

# Continue the conversation:
while True:
    user_input = input("You: ")
    if not user_input:
        break  # exit loop on empty input
    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model=model_name, messages=messages)
    answer = response['message']['content']
    print("Bot:", answer)
    messages.append({"role": "assistant", "content": answer})
