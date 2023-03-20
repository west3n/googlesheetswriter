from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

import configurations.config as cfg
import asyncio
import logging


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'[%(asctime)s] - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")

    bot = Bot(config("BOT_TOKEN"), parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    cfg.register_handlers(dp)

    await cfg.set_default_commands(dp)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
