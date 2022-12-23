import phonenumbers
from phonenumbers.geocoder import area_description_for_number
phone_number = phonenumbers.parse(input())
Region = phonenumbers.geocoder.description_for_number(phone_number, 'ru')
print(Region)