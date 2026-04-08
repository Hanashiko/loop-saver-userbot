# loop-saver-userbot

A Telegram userbot that listens to all incoming messages and saves them to a local JSON file.

## Setup

1. Install dependencies:
   ```bash
   pip install pyrogram
   ```

2. Get your `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).

3. Fill in `api_id`, `api_hash`, and `session_name` in `main.py`.

## Usage

```bash
python main.py
```

Messages are saved to `messages.json` (one JSON object per line) with the following fields: `message_id`, `from_user`, `chat_id`, `chat_title`, `date`, `text`.
