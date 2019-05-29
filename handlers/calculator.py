import asyncio
import logging
import re

from .utils import Event, log

__all__ = ['handle_eval']
logger = logging.getLogger(__name__)


@log
async def handle_eval(event: Event):
    expression = re.sub(r'[^\d+\-*/().,%&|{}\[\]\s]', '', event.pattern_match.expression)

    if not 0 < len(expression) < 100:
        await event.reply("Bad expression.")
        return
    try:
        answer = eval(expression)
        if answer == set():
            answer = '{}'
        msg = f'```{expression}\n> {answer}```'
    except Exception as e:
        logger.error(f"error in expression: {expression}")
        logger.exception(e)
        msg = f"`{expression}`\nBad expression."
    await asyncio.gather(
        event.delete(),
        event.respond(msg),
    )
