from aiogram import executor
from bot import dp, on_startup, on_shutdown
from handlers import client, admin, other


client.register_handlers()
admin.register_handlers()
other.register_handlers()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
