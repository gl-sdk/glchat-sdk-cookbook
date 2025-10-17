from glchat_sdk import GLChat

client = GLChat(base_url="https://custom-glchat.foobar.com/api/proxy/")
response = client.message.create(
    chatbot_id="no-op",
    message="Hello!"
)

for chunk in response:
    print(chunk.decode("utf-8"), end="")