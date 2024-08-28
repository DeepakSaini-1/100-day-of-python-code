import pywhatkit as pyw
import pyautogui as auto
pyw.sendwhatmsg('+918273208605','Hello',20,5)
pyw.sendwhats_image("+918273208605", "WIN_20230917_19_32_27_Pro.jpg") 
# for i in range (100):
#     auto.typewrite("Hello")
#     auto.press("enter")
# print("Hello")
# pyw.sendwhatimg()
# ___________________________________
# import phonenumbers
# from phonenumbers import geocoder
# phone_number2=phonenumbers.parse("+919027654170")
# phone_number1=phonenumbers.parse("+918273208605")
# phone_number3=phonenumbers.parse("+917055464176")
# phone_number4=phonenumbers.parse("+917500437769")

# print(geocoder.description_for_number(phone_number1,"en"));
# print(geocoder.description_for_number(phone_number2,"en"));
# print(geocoder.description_for_number(phone_number3,"en"));
# print(geocoder.description_for_number(phone_number4,"en"));
# ________________________________________________________________________________

import phonenumbers
from phonenumbers import geocoder

number="+92457894545"
ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))
# number="+918273208605"
# ch_number=phonenumbers.parse(number,"CH")
# print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_name=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_name,"en"))