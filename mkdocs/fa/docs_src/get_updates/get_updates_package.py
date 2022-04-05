from rubika_bot.requests import get_updates
from rubika_bot.models import Update

updates, _ = get_updates(
    token='SUPER_SECRET_TOKEN',
    limit=10,
)