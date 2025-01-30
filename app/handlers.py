from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

import app.keyborad as kb 

router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.reply('asdf!', reply_markup  = kb.startkey)

@router.message(F.text=="Поставить напоминание")
async def reminding(message:Message):
    await message.reply('\n Поставлено напоминание на каждый час')

@router.message(F.text=="Набор тренировок для глаз")
async def show_info(message:Message):
    await message.reply('\n Набор тренировок для глаз можно найти тут: https://t.me/EyesSecurity')
