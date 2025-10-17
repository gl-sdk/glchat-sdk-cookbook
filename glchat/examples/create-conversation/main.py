from glchat_sdk import GLChat

client = GLChat()

conversation = client.conversation.create(
    user_id="your-user-id",
    chatbot_id="your-chatbot-id",
    title="My First Conversation"
)

print(f"Created conversation: {conversation}")
