from glchat_sdk import GLChat

client = GLChat()
response = client.message.create(
    chatbot_id="no-op",
    message="Hello! How can I assist you today?",
    stream=False
)

print(response.message)
