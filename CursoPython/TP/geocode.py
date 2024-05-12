import phonenumbers
from phonenumbers import geocoder

from phonenumbers import carrier
from phonenumbers import number_type, PhoneNumberType
from phonenumbers import region_code_for_number


phone1 = phonenumbers.parse("+5493385522998")
print ("\nLocacion de tel 1: ", geocoder.description_for_number(phone1, "es"))
print (geocoder.description_for_number(phone1, "es"))

operator_name = carrier.name_for_number(phone1, 'es')
print(operator_name)
phone_type = number_type(phone1)
if phone_type == PhoneNumberType.MOBILE:
    print("El número es móvil")
elif phone_type == PhoneNumberType.FIXED_LINE:
    print("El número es fijo")

region = region_code_for_number(phone1)
print(region)