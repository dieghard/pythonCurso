# Para importar pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import number_type, PhoneNumberType
from phonenumbers import region_code_for_number
from phonenumbers import PhoneNumberFormat


tel = input ("Ingrese un número de teléfono con código de país(ejemplo +549 Argentina Claro): ")
numero_telfono = phonenumbers.parse(tel, "AR")  # Asume Argentina si no se proporciona un código de país

# Verificación de validez
if phonenumbers.is_valid_number(numero_telfono):
    print("Número válido")
else:
    print("Número no válido")

# Formato internacional
formato_internacional = phonenumbers.format_number(numero_telfono, PhoneNumberFormat.INTERNATIONAL)
print(f"Formato internacional: {formato_internacional}")

# Formato nacional (asumiendo Argentina)
formato_nacional = phonenumbers.format_number(numero_telfono, phonenumbers.PhoneNumberFormat.NATIONAL)
print(f"Formato nacional: {formato_nacional}")
 # Formato E164
formato_e164 = phonenumbers.format_number(numero_telfono, PhoneNumberFormat.E164)
print(f"Formato E164: {formato_e164}")
# Código de región
codigo_region = phonenumbers.region_code_for_number(numero_telfono)

location = geocoder.description_for_number(numero_telfono, "es")
print(f"Lugar de donde llama: {location}")
operator_name = carrier.name_for_number(numero_telfono, 'es')
print(f"Nombre de operadora: {operator_name}")

 # Tipo de teléfono
phone_type = number_type(numero_telfono)
if phone_type == PhoneNumberType.MOBILE:
    print("Llama desde un teléfono móvil")
elif phone_type == PhoneNumberType.FIXED_LINE:
    print("Llama desde un teléfono fijo")
elif phone_type == PhoneNumberType.VOIP:
    print("Llama desde un servicio VoIP")
elif phone_type == PhoneNumberType.PREMIUM_RATE:
    print("Llama desde un número de tarifa premium")
elif phone_type == PhoneNumberType.TOLL_FREE:
    print("Llama desde un número de tarifa gratuita")
else:
    print("Tipo de teléfono desconocido")


# Comprobar si el número puede recibir SMS
if phone_type in (PhoneNumberType.MOBILE, PhoneNumberType.FIXED_LINE_OR_MOBILE, PhoneNumberType.VOIP):
    print("El número puede recibir SMS")
else:
    print("El número no puede recibir SMS")

# Comprobar si el número ha sido portado
if phonenumbers.is_possible_number(numero_telfono):
    print("El número es posible y puede haber sido portado")
else:
    print("El número no parece haber sido portado")

pais = region_code_for_number(numero_telfono)
print(f"Nombre de operadora: {pais}")
