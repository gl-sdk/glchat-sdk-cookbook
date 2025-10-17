from pathlib import Path
from glchat_sdk import GLChat

client = GLChat()

response = client.message.create(
   chatbot_id="app-id",
   message="What is in this file?",
   files=[Path("/path/to/your/file.txt")],
   user_id="user@example.com",
   conversation_id="conversation-id"
)

for chunk in response:
   print(chunk.decode("utf-8"), end="")
