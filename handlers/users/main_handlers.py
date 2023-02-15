from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from states import Cases 
from datetime import datetime
from loader import dp, scheduler, bot 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

dt = datetime.today()
case = "!"
hour = 12 
hour2 = 12
minute = 30
minute2 = 30
user_id = 36378
case2 = "!"
hour3 = 12
minute3 = 30
case3 = "!"
hour4 = 12
minute4 = 30
case4 = "!"
hour5 = 12
minute5 = 30
case5 = "!"

btnDoneRem = InlineKeyboardButton(text="Add ✅", callback_data="reminderdone")

checkRemMenu = InlineKeyboardMarkup(row_width=3)
checkRemMenu.insert(btnDoneRem)

@dp.message_handler(text="/start")
async def start_bot(message):
	await message.answer("Список команд:\n/start Запустити бота\n/newcase Додати нове завдання/справу\n/mycases Всі заплановані справи\n/exit  Скасовує поточну дію")
	
@dp.message_handler(text="/exit", state="*")
async def exit(message, state: FSMContext):
	await message.answer(text="Дію відхилено ❌")
	await state.reset_state(with_data=True)

@dp.message_handler(text="/newcase")
async def add_case(message, state: FSMContext):
	await message.answer("Напишіть справу яку ви хочете додати")	
	await Cases.C1.set()
	
@dp.message_handler(text="/newcase", state=Cases.NOT_ALL)
async def add_case(message, state: FSMContext):
	await message.answer("Напишіть справу яку ви хочете додати")	
	await Cases.C2.set() 
	
@dp.message_handler(text="/newcase", state=Cases.AFTER_NOT_ALL)
async def add_case(message, state: FSMContext):
	await message.answer("Напишіть справу яку ви хочете додати")	
	await Cases.C3.set()
	
@dp.message_handler(text="/newcase", state=Cases.NEW1)
async def add_case(message, state: FSMContext):
	await message.answer("Напишіть справу яку ви хочете додати")	
	await Cases.C4.set()
	
@dp.message_handler(text="/newcase", state=Cases.NEW2)
async def add_case(message, state: FSMContext):
	await message.answer("Напишіть останню справу яку ви хочете додати\nУвага!!! ця справа має бути найпізнішою в вашому списку.")	
	await Cases.C5.set()

@dp.message_handler(state=Cases.C5)
async def get_case(message, state: FSMContext):
	answer = message.text
	await state.update_data(case5=answer)
	await message.answer("Вкажіть годину для нагадування справ(Тільки годину, хвилини ви вкажете в наступному повідомленні)") 
	await Cases.H5.set()

@dp.message_handler(state=Cases.C4)
async def get_case(message, state: FSMContext):
	answer = message.text
	await state.update_data(case4=answer)
	await message.answer("Вкажіть годину для нагадування справ(Тільки годину, хвилини ви вкажете в наступному повідомленні)") 
	await Cases.H4.set() 

@dp.message_handler(state=Cases.C3)
async def get_case(message, state: FSMContext):
	answer = message.text
	await state.update_data(case3=answer)
	await message.answer("Вкажіть годину для нагадування справ(Тільки годину, хвилини ви вкажете в наступному повідомленні)") 
	await Cases.H3.set() 
		
@dp.message_handler(state=Cases.C2)
async def get_case(message, state: FSMContext):
	answer = message.text
	await state.update_data(case2=answer)
	await message.answer("Вкажіть годину для нагадування справ(Тільки годину, хвилини ви вкажете в наступному повідомленні)") 
	await Cases.H2.set() 

@dp.message_handler(state=Cases.C1)
async def get_case(message, state: FSMContext):
	answer = message.text
	await state.update_data(case=answer)
	await message.answer("Вкажіть годину для нагадування справ(Тільки годину, хвилини ви вкажете в наступному повідомленні)") 
	await Cases.H1.set() 

@dp.message_handler(state=Cases.H1)
async def get_hour(message, state: FSMContext):
	answer = message.text
	await state.update_data(hour=answer)
	await message.answer("Тепер вкажіть хвилину для нагадування справ") 
	await Cases.M1.set() 
	
@dp.message_handler(state=Cases.H2)
async def get_hour(message, state: FSMContext):
	answer = message.text
	await state.update_data(hour2=answer)
	await message.answer("Тепер вкажіть хвилину для нагадування справ") 
	await Cases.M2.set() 
	
@dp.message_handler(state=Cases.H3)
async def get_hour(message, state: FSMContext):
	answer = message.text
	await state.update_data(hour3=answer)
	await message.answer("Тепер вкажіть хвилину для нагадування справ") 
	await Cases.M3.set() 

@dp.message_handler(state=Cases.H4)
async def get_hour(message, state: FSMContext):
	answer = message.text
	await state.update_data(hour4=answer)
	await message.answer("Тепер вкажіть хвилину для нагадування справ") 
	await Cases.M4.set() 
	
@dp.message_handler(state=Cases.H5)
async def get_hour(message, state: FSMContext):
	answer = message.text
	await state.update_data(hour5=answer)
	await message.answer("Тепер вкажіть хвилину для нагадування справ") 
	await Cases.M5.set() 	

@dp.message_handler(state=Cases.M1)
async def get_minute(message, state: FSMContext):
	answer = message.text
	await state.update_data(minute=answer)
	await message.answer("Вашу справу успішно додано ✅", reply_markup=checkRemMenu)
	await Cases.AFTER_ALL.set()

@dp.message_handler(state=Cases.M2)
async def get_minute(message, state: FSMContext):
	answer = message.text
	await state.update_data(minute2=answer)
	await message.answer("Вашу справу успішно додано ✅", reply_markup=checkRemMenu)
	await Cases.AFTER_ALL.set()
	
@dp.message_handler(state=Cases.M3)
async def get_minute(message, state: FSMContext):
	answer = message.text
	await state.update_data(minute3=answer)
	await message.answer("Вашу справу успішно додано ✅", reply_markup=checkRemMenu)
	await Cases.AFTER_ALL.set()
	
@dp.message_handler(state=Cases.M4)
async def get_minute(message, state: FSMContext):
	answer = message.text
	await state.update_data(minute4=answer)
	await message.answer("Вашу справу успішно додано ✅", reply_markup=checkRemMenu)
	await Cases.AFTER_ALL.set()
	
@dp.message_handler(state=Cases.M5)
async def get_minute(message, state: FSMContext):
	answer = message.text
	await state.update_data(minute5=answer)
	await message.answer("Вашу справу успішно додано ✅", reply_markup=checkRemMenu)
	await Cases.AFTER_ALL.set()
	
@dp.message_handler(text="/mycases", state=Cases.NOT_ALL)
async def show_case(message, state: FSMContext):
	global minute 
	global minute2
	global minute3
	global minute4
	global minute5
	global hour 
	global hour2
	global hour3
	global hour4
	global hour5
	global case
	global user_id
	global case2
	global case3
	global case4
	global case5
	user_id = message.from_user.id
	data = await state.get_data()
	case = data.get("case")
	case2 = data.get("case2")
	hour = data.get("hour")
	hour2 = data.get("hour2")
	minute = data.get("minute")
	minute2 = data.get("minute2")
	case3 = data.get("case3")
	hour3 = data.get("hour3")
	minute3 = data.get("minute3")
	case4 = data.get("case4")
	hour4 = data.get("hour4")
	minute4 = data.get("minute4")
	case5 = data.get("case5")
	hour5 = data.get("hour5")
	minute5 = data.get("minute5")
	await message.answer(f"Ваші справи на сьогодні:")
	if case != None:
		await message.answer(f"1.{case}. Нагадування: {hour}:{minute}")
		schedule_jobs(dp, case, hour, minute)
		if case2 != None:
			await message.answer(f"2.{case2}. Нагадування: {hour2}:{minute2}")
			schedule_jobs2(dp, case2, hour2, minute2)
			await Cases.AFTER_NOT_ALL.set()
		if case3 != None:
			await message.answer(f"3.{case3}. Нагадування: {hour3}:{minute3}")
			schedule_jobs3(dp, case3, hour3, minute3)
			await Cases.NEW1.set()
		if case4 != None:
			await message.answer(f"4.{case4}. Нагадування: {hour4}:{minute4}")
			schedule_jobs4(dp, case4, hour4, minute4)
			await Cases.NEW2.set()
		if case5 != None:
			await message.answer(f"5.{case5}. Reminder: {hour5}:{minute5}\n\n It is the last case for now, next cases you'll be able to write after last reminder")
			schedule_jobs5(dp, case5, hour5, minute5)
			await state.reset_state(with_data=True)						
async def send_message_to_user(message, dp: Dispatcher):
	text = "‼️REMINDER‼️\n" + case + "!"
	await dp.bot.send_message(chat_id=user_id, text=text)
async def send_message_to_user2(message, dp: Dispatcher):
	text = "‼️REMINDER‼️\n" + case2 + "!"
	await dp.bot.send_message(chat_id=user_id, text=text)
async def send_message_to_user3(message, dp: Dispatcher):
	text = "‼️REMINDER‼️\n" + case3 + "!"
	await dp.bot.send_message(chat_id=user_id, text=text)
async def send_message_to_user4(message, dp: Dispatcher):
	text = "‼️REMINDER‼️\n" + case4 + "!"
	await dp.bot.send_message(chat_id=user_id, text=text)
async def send_message_to_user5(message, dp: Dispatcher):
	text = "‼️ REMINDER ‼️\n" + case5 + "!"
	await dp.bot.send_message(chat_id=user_id, text=text)
		
@dp.callback_query_handler(text="reminderdone", state=Cases.AFTER_ALL)
async def reminderdone(message, state: FSMContext):
	user_id=message.from_user.id
	message_id=message.message.message_id
	await bot.delete_message(user_id, message_id)
	await bot.send_message(chat_id=user_id, text="Send command /mycases")
	await Cases.NOT_ALL.set()

def schedule_jobs(dp, case, hour, minute):
	if minute == "01":
		minute = 1
	elif minute == "02":
		minute = 2
	elif minute == "03":
		minute = 3
	elif minute == "04":
		minute = 4
	elif minute == "05":
		minute = 5
	elif minute == "06":
		minute = 6
	elif minute == "07":
		minute = 7
	elif minute == "08":
		minute = 8
	elif minute == "09":
		minute = 9
	hour_ua = int(hour) - 2
	scheduler.add_job(send_message_to_user, "date", run_date=datetime(dt.year, dt.month, dt.day, hour_ua, int(minute)), args=(dp, dp,))
	
def schedule_jobs2(dp, case2, hour2, minute2):
	if minute2 == "01":
		minute2 = 1
	elif minute2 == "02":
		minute2 = 2
	elif minute2 == "03":
		minute2 = 3
	elif minute2 == "04":
		minute2 = 4
	elif minute2 == "05":
		minute2 = 5
	elif minute2 == "06":
		minute2 = 6
	elif minute2 == "07":
		minute2 = 7
	elif minute2 == "08":
		minute2 = 8
	elif minute2 == "09":
		minute2 = 9
	hour_ua = int(hour2) - 2
	scheduler.add_job(send_message_to_user2, "date", run_date=datetime(dt.year, dt.month, dt.day, hour_ua, int(minute2)), args=(dp, dp,))
	
def schedule_jobs3(dp, case3, hour3, minute3):
	if minute3 == "01":
		minute3 = 1
	elif minute3 == "02":
		minute3 = 2
	elif minute3 == "03":
		minute3 = 3
	elif minute3 == "04":
		minute3 = 4
	elif minute3 == "05":
		minute3 = 5
	elif minute3 == "06":
		minute3 = 6
	elif minute3 == "07":
		minute3 = 7
	elif minute3 == "08":
		minute3 = 8
	elif minute3 == "09":
		minute3 = 9
	hour_ua = int(hour3) - 2
	scheduler.add_job(send_message_to_user3, "date", run_date=datetime(dt.year, dt.month, dt.day, hour_ua, int(minute3)), args=(dp, dp,))

def schedule_jobs4(dp, case4, hour4, minute4):
	if minute4 == "01":
		minute4 = 1
	elif minute4 == "02":
		minute4 = 2
	elif minute4 == "03":
		minute4 = 3
	elif minute4 == "04":
		minute4 = 4
	elif minute4 == "05":
		minute4 = 5
	elif minute4 == "06":
		minute4 = 6
	elif minute4 == "07":
		minute4 = 7
	elif minute4 == "08":
		minute4 = 8
	elif minute4 == "09":
		minute4 = 9
	hour_ua = int(hour4) - 2	
	scheduler.add_job(send_message_to_user4, "date", run_date=datetime(dt.year, dt.month, dt.day, hour_ua, int(minute4)), args=(dp, dp,))	
def schedule_jobs5(dp, case5, hour5, minute5):
	if minute5 == "01":
		minute5 = 1
	elif minute5 == "02":
		minute5 = 2
	elif minute5 == "03":
		minute5 = 3
	elif minute5 == "04":
		minute5 = 4
	elif minute5 == "05":
		minute5 = 5
	elif minute5 == "06":
		minute5 = 6
	elif minute5 == "07":
		minute5 = 7
	elif minute5 == "08":
		minute5 = 8
	elif minute5 == "09":
		minute5 = 9
	hour_ua = int(hour5) - 2
	scheduler.add_job(send_message_to_user5, "date", run_date=datetime(dt.year, dt.month, dt.day, hour_ua, int(minute5)), args=(dp, dp,))
	

