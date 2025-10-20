## ⚙️ Prerequisites

Please refer to prerequisites [here](../../README.md#️-prerequisites).

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/gl-sdk/glchat-sdk-cookbook.git
   cd glchat-sdk-cookbook/glchat/examples/create-conversation
   ```

2. **Run the example**

   ```bash
   uv run main.py
   ```

3. **Expected Output**

   You should see a response from the GLChat SDK, similar to:

   ```
   Created conversation: {
      "conversation": {
         "id": "9f419f9d-b443-4cde-8e91-a83573cf0d38",
         "user_id": "your-user-id",
         "title": "My First Conversation",
         "created_time": "2025-09-23T02:43:40.189316Z",
         "updated_time": "2025-09-23T02:43:40.189320Z",
         "is_active": True,
         "is_anonymized": True,
         "chatbot_id": "your-chatbot-id",
         "deanonymized_mapping": {},
         "first_matching_message_id": None,
         "first_matching_message": None
      }
   }
   ```

## 📚 Reference

This example is based on the [GLChat SDK documentation](https://gdplabs.gitbook.io/glchat/sdk/how-to-guides/create-conversation).
