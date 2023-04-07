import datetime
import telebot
import dotenv
import os
import sqlite3
import json

from apscheduler.schedulers.background import BackgroundScheduler


dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))
scheduler = BackgroundScheduler()
commands = [
    telebot.types.BotCommand("start", "Start the bot"),
    telebot.types.BotCommand("newtask", "Add new task"),
    telebot.types.BotCommand("mytasks", "Show scheduled tasks"),
]

def send_scheduled_message(id, task):
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM tasks WHERE task_id={int(task[0])}')
    bot.send_message(chat_id=id, text=task[1])
    connection.commit()
    connection.close()

@bot.message_handler(commands=['start'])
def start_bot(message):
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    bot.reply_to(message, "List of commands:\n/start Start bot\n/newtask Add new task\n/mytasks All scheduled tasks")
    try:
        cursor.execute('''INSERT INTO users VALUES (?, ?) ''', [message.chat.id, message.from_user.username])
    except sqlite3.IntegrityError:
        pass
    connection.commit()
    connection.close()

@bot.message_handler(commands=['newtask'])
def start_case(message):
    
    bot.reply_to(message, 'Write the task you want to add')
    bot.register_next_step_handler(message, get_case)

def get_case(message):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO tasks (description, user_id) VALUES (?, ?) ''', [message.text, message.chat.id])
    bot.reply_to(message, 'Write the time when I should remind you of this task, format: XX:XX')
    bot.register_next_step_handler(message, get_time, message.text)
    conn.commit()
    conn.close()

def get_time(message, name):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    hour, minute = message.text.split(':')
    cur.execute(f'''UPDATE tasks SET hour={int(hour)}, minute={int(minute)} WHERE user_id={message.chat.id} AND description='{name}' ''')
    conn.commit()
    cur.execute(f"SELECT * FROM tasks WHERE user_id={message.chat.id} AND description='{name}' AND hour={int(hour)} AND minute={int(minute)}")
    today = datetime.datetime.today()
    scheduled_time = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=int(hour), minute=int(minute))
    scheduler.add_job(send_scheduled_message, args=[message.chat.id, cur.fetchone()], trigger='date', run_date=scheduled_time)
    bot.reply_to(message, 'Task was added succesfully')
    conn.close()

@bot.message_handler(commands=['mytasks'])
def show_tasks(message):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM tasks WHERE user_id={message.chat.id}')
    for i, task in enumerate(cur.fetchall(), 1):
        keyboard = telebot.types.InlineKeyboardMarkup()
        delete = telebot.types.InlineKeyboardButton(
            text="Delete", 
            callback_data=json.dumps({
                'delete': True,
                'task_id': task[0],
            })
        )
        keyboard.add(delete)
        hour = str(task[3])
        if len(hour) == 1:
            hour = '0' + hour
        minute = str(task[4])
        if len(minute) == 1:
            minute = '0' + minute
        bot.send_message(message.chat.id, f'{i}. {task[1]} at {hour}:{minute}', reply_markup=keyboard)
    conn.close()

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    data = json.loads(call.data)
    if 'delete' in data:
        cur.execute(f'DELETE FROM tasks WHERE task_id={data["task_id"]}')
        conn.commit()
        bot.send_message(call.message.chat.id, 'Succesfuly deleted')
    conn.close()

scheduler.start()
bot.set_my_commands(commands)
bot.infinity_polling()