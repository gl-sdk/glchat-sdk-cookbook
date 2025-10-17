## ⚙️ Prerequisites

Please refer to prerequisites [here](../../README.md#️-prerequisites).

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/gl-sdk/glchat-sdk-cookbook.git
   cd glchat-sdk-cookbook/glchat/examples/send-message-with-files
   ```

2. **Run the example**

   ```bash
   uv run main.py
   ```

3. **Expected Output**

   You should see a response from the GLChat SDK, similar to:

   ```json
   data:{
      "status": "data",
      "message": "{\"data_type\": \"process\", \"data_value\": {\"id\": \"33c9ee090404be9f7390431911e2fd676cc89a98cb355c102159e8646d4ea332\", \"message\": \"Processing file(s)\", \"status\": \"running\", \"time\": 0.0}}",
      "conversation_id": "c0d932a8-41f2-4229-93e1-383bcac75740",
      "user_message_id": "52829b05-527f-40ca-b907-cf5e4acf9a73",
      "assistant_message_id": "44bf008f-40f2-40f2-98d8-a911ebf668fb",
      "created_date": 1758598033163
   }

   ...

   data:{
      "status": "response",
      "message": "The file is an informational summary about Pikachu. Main points:\n\n- Pronunciation: /\u02c8pi\u02d0k\u0259t\u0283u\u02d0/ and Japanese name \u30d4\u30ab\u30c1\u30e5\u30a6 (Hepburn: Pikach\u016b).  \n- Role: a Pok\u00e9mon species and the franchise mascot for Nintendo and Game Freak's Pok\u00e9mon.  \n- Origin: first introduced in the video games Pok\u00e9mon Red and Blue.  \n- Creation: designed by Atsuko Nishida at Ken Sugimori\u2019s request; final design by Ken Sugimori.  \n- Appearances: appears in multiple games (including Pok\u00e9mon Go), the Pok\u00e9mon Trading Card Game, and various merchandise.  \n- Voice actors: primarily voiced by Ikue \u014ctani; other credited actors include Kate Bristol, Ryan Reynolds, Kaiji Tang, Hidetoshi Nishijima, T\u014dru \u014ckawa, and Koichi Yamadera.",
      "conversation_id": "c0d932a8-41f2-4229-93e1-383bcac75740",
      "user_message_id": "52829b05-527f-40ca-b907-cf5e4acf9a73",
      "assistant_message_id": "44bf008f-40f2-40f2-98d8-a911ebf668fb",
      "created_date": 1758598044957
   }

   ...

   data:{
      "status": "data",
      "message": "{\"data_type\": \"process\", \"data_value\": {\"id\": \"795cbe2fa5b99ceac92c100e8d498fb2758852afc5cf0848d55e74640db4f084\", \"message\": \"Determining relevant sources\", \"status\": \"running\", \"time\": 12.33}}",
      "conversation_id": "c0d932a8-41f2-4229-93e1-383bcac75740",
      "user_message_id": "52829b05-527f-40ca-b907-cf5e4acf9a73",
      "assistant_message_id": "44bf008f-40f2-40f2-98d8-a911ebf668fb",
      "created_date": 1758598045488
   }

   ...

   data:{
      "status": "data",
      "message": "{\"data_type\": \"reference\", \"data_value\": {\"id\": \"c0d932a8-41f2-4229-93e1-383bcac75740-5f32005e97d7c958bb421fd51daa20c626828305e391f4dc71538b1c8e94c5ab\", \"title\": \"\", \"name\": \"pikachu.pdf\", \"type\": \"pdf\", \"content\": \"Pikachu (/\\u02c8pi\\u02d0k\\u0259t\\u0283u\\u02d0/ \\u24d8; Japanese: \\u30d4\\u30ab\\u30c1\\u30e5\\u30a6, Hepburn: Pikach\\u016b) is a Pok\\u00e9mon species in Nintendo and Game Freak's Pok\\u00e9mon media franchise, and the franchise's mascot. First introduced in the video games Pok\\u00e9mon Red and Blue, it was created by Atsuko Nishida at the request of lead designer Ken Sugimori, with the design finalized by Sugimori. Since Pikachu's debut, it has appeared in multiple games including Pok\\u00e9mon Go and the Pok\\u00e9mon Trading Card Game, as well as various merchandise. While Pikachu has been primarily voiced in media by Ikue \\u014ctani, other actors have also voiced the character including Kate Bristol, Ryan Reynolds, Kaiji Tang, Hidetoshi Nishijima, T\\u014dru \\u014ckawa, and Koichi Yamadera.\\n\\n- source: pikachu.pdf\\n- file_id: c0d932a8-41f2-4229-93e1-383bcac75740-5f32005e97d7c958bb421fd51daa20c626828305e391f4dc71538b1c8e94c5ab\", \"url\": \"https://gl-chat-prod.s3.ap-southeast-1.amazonaws.com/c0d932a8-41f2-4229-93e1-383bcac75740/c0d932a8-41f2-4229-93e1-383bcac75740-5f32005e97d7c958bb421fd51daa20c626828305e391f4dc71538b1c8e94c5ab?response-content-disposition=inline%3B%20filename%3D%22pikachu.pdf%22&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4ZVANHPEWTCO5XDI%2F20250923%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20250923T032727Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9a960506e687d5593697815e4c69144ebdaf0748354fb1a477af43d6b4ec41bb\", \"position\": [{\"coordinates\": [72, 543, 186, 72], \"page_number\": 1}]}}",
      "conversation_id": "c0d932a8-41f2-4229-93e1-383bcac75740",
      "user_message_id": "52829b05-527f-40ca-b907-cf5e4acf9a73",
      "assistant_message_id": "44bf008f-40f2-40f2-98d8-a911ebf668fb",
      "created_date": 1758598047460
   }
   ```
