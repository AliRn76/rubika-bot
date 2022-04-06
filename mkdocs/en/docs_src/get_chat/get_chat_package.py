from rubika_bot.requests import get_chat
from rubika_bot.models import Chat

chat: Chat = get_chat(
    token='SUPER_SECRET_TOKEN',
    chat_id='CHAT_ID',
)