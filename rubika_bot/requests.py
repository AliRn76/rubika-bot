import json
import requests
from typing import Literal, List, Optional, Tuple, Final, Union
from rubika_bot.exceptions import APIException
from rubika_bot.models import Bot, Keypad, Chat, Update, BotCommand


def _send_request(token: str, method: str, data: dict) -> dict:
    url = f'https://messengerg2b1.iranlms.ir/v3/{token}/{method}'
    res = requests.post(url=url, data=json.dumps(data), timeout=10)
    body = json.loads(res.text or '{}')
    if res.status_code != 200 or body.get('status') != 'OK':
        raise APIException(f'Response(status_code: {res.status_code}, body: {body}')
    return body['data']


def _send_multipart_request(url: str, form_data) -> dict:
    res = requests.post(url, files=form_data, verify=False)
    if res.status_code != 200:
        print(f'\nResponse(status_code: {res.status_code}, body: {res.content})')
        raise APIException(f'Response(status_code: {res.status_code}, body: {res.content}')
    return json.loads(res.text or '{}')['data']  # TODO


def get_me(token: str) -> Bot:
    bot = _send_request(token=token, method='getMe', data={})
    return Bot(**bot)


def send_message(
        token: str,
        chat_id: str,
        text: str,
        chat_keypad: Optional[Keypad] = None,
        disable_notification: bool = False,
        inline_keypad: Optional[Keypad] = None,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: Literal[None, 'New', 'Remove'] = None,
) -> str:
    data = {
        'text': text,
        'chat_id': chat_id,
        'disable_notification': disable_notification
    }
    if chat_keypad:
        data['chat_keypad'] = chat_keypad.dict()
        data['chat_keypad_type'] = chat_keypad_type
    if inline_keypad:
        data['inline_keypad'] = inline_keypad.dict()
    if reply_to_message_id:
        data['reply_to_message_id'] = reply_to_message_id

    res = _send_request(token=token, method='sendMessage', data=data)
    message_id = res['message_id']
    return message_id


def send_poll(
        token: str,
        chat_id: str,
        question: str,
        options: List[str],
        chat_keypad: Optional[Keypad] = None,
        disable_notification: bool = False,
        inline_keypad: Optional[Keypad] = None,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: Literal[None, 'New', 'Remove'] = None,
) -> str:
    data = {
        'chat_id': chat_id,
        'options': options,
        'question': question,
        'chat_keypad': chat_keypad,
        'inline_keypad': inline_keypad,
        'chat_keypad_type': chat_keypad_type,
        'reply_to_message_id': reply_to_message_id,
        'disable_notification': disable_notification,
    }

    res = _send_request(token=token, method='sendPoll', data=data)
    message_id = res['message_id']
    return message_id


def send_location(
        token: str,
        chat_id: str,
        latitude: str,
        longitude: str,
        chat_keypad: Optional[Keypad] = None,
        disable_notification: bool = False,
        inline_keypad: Optional[Keypad] = None,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: Literal[None, 'New', 'Remove'] = None,
) -> str:
    data = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
        'chat_keypad': chat_keypad,
        'disable_notification': disable_notification,
        'inline_keypad': inline_keypad,
        'reply_to_message_id': reply_to_message_id,
        'chat_keypad_type': chat_keypad_type,
    }

    res = _send_request(token=token, method='sendLocation', data=data)
    message_id = res['message_id']
    return message_id


def send_sticker(
        token: str,
        chat_id: str,
        sticker_id: str,
        chat_keypad: Optional[Keypad] = None,
        disable_notification: bool = False,
        inline_keypad: Optional[Keypad] = None,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: Literal[None, 'New', 'Remove'] = None,

) -> str:
    data = {
        'chat_id': chat_id,
        'sticker_id': sticker_id,
        'chat_keypad': chat_keypad,
        'disable_notification': disable_notification,
        'inline_keypad': inline_keypad,
        'reply_to_message_id': reply_to_message_id,
        'chat_keypad_type': chat_keypad_type,
    }

    res = _send_request(token=token, method='sendSticker', data=data)
    message_id = res['message_id']
    return message_id


def send_contact(
        token: str,
        chat_id: str,
        first_name: str,
        last_name: str,
        phone_number: str,
        chat_keypad: Optional[Keypad] = None,
        disable_notification: bool = False,
        inline_keypad: Optional[Keypad] = None,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: Literal[None, 'New', 'Remove'] = None,

) -> str:
    data = {
        'chat_id': chat_id,
        'last_name': last_name,
        'first_name': first_name,
        'chat_keypad': chat_keypad,
        'phone_number': phone_number,
        'inline_keypad': inline_keypad,
        'chat_keypad_type': chat_keypad_type,
        'reply_to_message_id': reply_to_message_id,
        'disable_notification': disable_notification,
    }

    res = _send_request(token=token, method='sendContact', data=data)
    message_id = res['message_id']
    return message_id


def get_chat(token: str, chat_id: str) -> Chat:
    data = {'chat_id': chat_id}
    chat = _send_request(token=token, method='getChat', data=data)
    return Chat(**chat['chat'])


def get_updates(token: str, limit: int = 10, offset_id: Optional[str] = None) -> Tuple[List[Update], str]:
    data = {
        'limit': limit,
    }
    if offset_id:
        data['offset_id'] = offset_id

    res = _send_request(token=token, method='getUpdates', data=data)
    return [Update(**update) for update in res['updates']], res['next_offset_id']


def forward_message(
        token: str,
        from_chat_id: str,
        message_id: str,
        to_chat_id: str,
        disable_notification: bool = False
) -> str:
    data = {
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'to_chat_id': to_chat_id,
        'disable_notification': disable_notification,
    }
    res = _send_request(token=token, method='forwardMessage', data=data)
    return res['new_message_id']


def edit_message_text(token: str, chat_id: str, message_id: str, text: str) -> None:
    data = {
        'text': text,
        'chat_id': chat_id,
        'message_id': message_id,
    }
    _send_request(token=token, method='editMessageText', data=data)


def edit_message_keypad(token: str, chat_id: str, message_id: str, inline_keypad: Keypad) -> None:
    data = {
        'chat_id': chat_id,
        'message_id': message_id,
        'inline_keypad': inline_keypad.dict(),
    }
    _send_request(token=token, method='editMessageKeypad', data=data)


def delete_message(token: str, chat_id: str, message_id: str) -> None:
    data = {
        'chat_id': chat_id,
        'message_id': message_id,
    }
    _send_request(token=token, method='deleteMessage', data=data)


def send_file(
        token: str,
        chat_id: str,
        file_id: str,
        chat_keypad: Optional[Keypad] = None,
        disable_notification: bool = False,
        inline_keypad: Optional[Keypad] = None,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: Literal[None, 'New', 'Remove'] = None,
) -> str:
    data = {
        'chat_id': chat_id,
        'file_id': file_id,
        'chat_keypad': chat_keypad,
        'disable_notification': disable_notification,
        'inline_keypad': inline_keypad,
        'reply_to_message_id': reply_to_message_id,
        'chat_keypad_type': chat_keypad_type,

    }
    res = _send_request(token=token, method='sendFile', data=data)
    return res['message_id']


def request_send_file(token: str, type: Literal['File', 'Image', 'Voice', 'Music', 'Gif']) -> str:
    data = {
        'type': type,
    }
    res = _send_request(token=token, method='requestSendFile', data=data)
    return res['upload_url']


def upload(url: str, file_name: str, file_path: str) -> str:
    res = _send_multipart_request(url=url, form_data={'file': (file_name, open(file_path, 'rb'))})
    return res['file_id']


def get_file(token: str, file_id: str) -> str:
    data = {'file_id': file_id}
    res = _send_request(token=token, method='getFile', data=data)
    return res['download_url']


def set_commands(token: str, bot_commands: List[BotCommand]) -> None:
    data = {'bot_commands': [command.dict() for command in bot_commands]}
    _send_request(token=token, method='setCommands', data=data)


def edit_chat_keypad(token: str, chat_id: str, chat_keypad: Keypad) -> None:
    data = {
        'chat_id': chat_id,
        'chat_keypad_type': 'New',
        'chat_keypad': chat_keypad.dict(),
    }
    _send_request(token=token, method='editChatKeypad', data=data)


def remove_chat_keypad(token: str, chat_id: str) -> None:
    data = {
        'chat_id': chat_id,
        'chat_keypad_type': 'Remove',
    }
    _send_request(token=token, method='editChatKeypad', data=data)


def update_bot_endpoint(
        token: str,
        url: str,
        type: Literal['ReceiveUpdate', 'ReceiveInlineMessage', 'ReceiveQuery',
                      'GetSelectionItem', 'SearchSelectionItems'],
) -> Final[Union['Done', 'InvalidUrl']]:
    data = {
        'url': url,
        'type': type,
    }
    res = _send_request(token=token, method='updateBotEndpoints', data=data)
    return res['status']
