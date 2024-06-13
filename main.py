from pyrogram import Client, filters
import json

api_id = ''
api_hash = ''
session_name = ''

app = Client(session_name, api_id=api_id, api_hash=api_hash)

def save_message(message):
    with open('messages.json', 'a', encoding='utf-8') as f:
        json_message = {
            "message_id": message.id,
            "from_user": message.from_user.username if message.from_user else None,
            "chat_id": message.chat.id,
            "chat_title": message.chat.title,
            "date": str(message.date),
            "text": message.text
        }
        f.write(json.dumps(json_message, ensure_ascii=False) + '\n')

@app.on_message(filters.all)
def handle_new_message(client, message):
    print(f"New message from {message.chat.title if message.chat else 'Private'}: {message.text}")
    save_message(message)

if __name__ == '__main__':
    print("Starting the client...")
    app.run()
