from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from my_btns import main_menu
from my_btns import Food_menu

api = '8012775338:AAHUlBzKnjjrCBIwdkhJe9mshK9khIPvvgQ'
bot = Bot(api)
dp=Dispatcher()

@dp.message(Command('start'))
async def send_hi(sms:types.Message):
    await sms.answer(text='Hello',
                     reply_markup=main_menu)

@dp.callback_query(F.data=='awqat')
async def send_reaction(call:types.CallbackQuery):
    await call.message.answer(text='Bizde:',
                              reply_markup=Food_menu)

@dp.callback_query(F.data=='ishiw')
async def send_reaction(call:types.CallbackQuery):
    await call.answer(text='Bizde')

@dp.callback_query(F.data=='FF')
async def send_reaction(call:types.CallbackQuery):
    await call.answer(text='Bizde:')

async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())