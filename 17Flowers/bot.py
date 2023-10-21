
!pip install telebot

import cv2
import telebot
import numpy as np
import tensorflow as tf
from telebot import types

# my_keyboard = types.ReplyKeyboardMarkup(row_width=1)
# key1 = types.KeyboardButton("چت بات ")
# key2 = types.KeyboardButton("تشخیص گل")


# my_keyboard.add(key1 , key2)

mybot = telebot.TeleBot("6519012268:AAEINyLy7-5cJ7knRlKDbZCKm6MYMtvWBV8", parse_mode=None)

model = tf.keras.models.load_model('/content/drive/MyDrive/weights/flowerـrecognition_model.h5')

flowers = ['bluebell', 'buttercup', 'coltsfoot', 'cowslip', 'crocus', 'daffodil',
                    'daisy', 'dandelion', 'fritillary', 'iris', 'lilyvalley',
                    'pansy', 'snowdrop', 'sunflower', 'tigerlily', 'tulip',
                    'windflower']

import tensorflow as tf
import telebot
import cv2
from keras.models import load_model
import numpy as np

mybot = telebot.TeleBot("6519012268:AAEINyLy7-5cJ7knRlKDbZCKm6MYMtvWBV8")


@mybot.message_handler(commands=['start'])
def send_welcome(message):
    msg = mybot.send_message(message.chat.id,"Hi "+str(message.chat.first_name)+" Welcome to flower Recognition bot"+" \n"+
                            "/RecognitionFlowers"+'\n'+
                            '/help- Please send me a picture of a flower')

@mybot.message_handler(commands=['help'])
def send_welcome(message):
  mybot.reply_to(message,"what to do? what not to do?")



@mybot.message_handler(commands=['RecognitionFlowers'])
def send_photo(message):
    msg = mybot.reply_to(message,"Please send me photo")
    mybot.register_next_step_handler(msg,recognize_flowers)

def recognize_flowers(message):
    model = load_model('/content/drive/MyDrive/weights/flowerـrecognition_model.h5', compile=False)

    fileID = message.photo[-1].file_id
    file_info = mybot.get_file(fileID)
    downloaded_file = mybot.download_file(file_info.file_path)
    width = height = 224


    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    img = cv2.imread("image.jpg")
    image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cv2.resize(image ,(width,height))
    img = img / 255
    img = img.reshape(1,width,height,3)
    flowers = ['bluebell', 'buttercup', 'coltsfoot', 'cowslip', 'crocus', 'daffodil',
                    'daisy', 'dandelion', 'fritillary', 'iris', 'lilyvalley', 'pansy', 'snowdrop', 'sunflower', 'tigerlily', 'tulip', 'windflower']
    result = np.argmax(model.predict(img))
    print(result)
    mybot.send_message(message.chat.id,flowers[result])


@mybot.message_handler(func=lambda m: True)
def echo_all(message):
	#bot.reply_to(message, "سلام.چطوری گل؟")
  if message.text == "سلام" :
      mybot.send_message(message.chat.id,"سلام گل")
      photo = open("/content/drive/MyDrive/arasto.jpg","rb")
      mybot.send_photo(message.chat.id , photo)

  elif message.text == "خوبی" :
     mybot.send_message(message.chat.id,"من به فدای تو بشم.خوبم گل")

  elif message.text == "دوستت دارم" or message.text == "عاشقتم"  or message.text == "خیلی گلی"  :
     mybot.send_message(message.chat.id, "گل فرمایش میکنی")
     mybot.send_message(message.chat.id,"❤︎")

  elif message.text == "دستت درد نکنه" or message.text == "مرسی"  or message.text == "ممنون" or message.text == "ممنونم" :
    mybot.send_message(message.chat.id,"خواهش میکنم گل")

  elif message.text == "باش" or message.text == "برو بابا" :
    mybot.send_message(message.chat.id,"با یه حبس کشیده درست صحبت کن")

  elif message.text == "خوبه"  or message.text == "کارت درسته" or message.text == "عالی":
   photo = open("/content/drive/MyDrive/dataset/nody-قد-همسر-احمد-مهرانفر-1633185633.jpg","rb")
   mybot.send_photo(message.chat.id,photo)
  else :
    # mybot.send_message(message.chat.id,"من دیگه رد دادم", reply_markup=my_keyboard)
    mybot.send_message(message.chat.id,"من دیگه رد دادم")


mybot.enable_save_next_step_handlers(delay=2)
mybot.load_next_step_handlers()

mybot.polling()