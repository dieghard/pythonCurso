import phonenumbers
from phonenumbers import geocoder


phone1 = phonenumbers.parse("+543385522998")
print ("\nPhone numeber locations")
print (geocoder.description_for_number(phone1, "en"))
