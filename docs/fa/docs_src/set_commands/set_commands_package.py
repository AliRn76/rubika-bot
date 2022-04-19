from rubika_bot.requests import set_commands
from rubika_bot.models import BotCommand

commands = [
    BotCommand(command='command1', description='description 1'),
    BotCommand(command='command2', description='description 2'),
]
set_commands(token='SUPER_SECRET_TOKEN', bot_commands=commands)
