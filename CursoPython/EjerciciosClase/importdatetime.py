# import datetime
# # Obtener la fecha actual
# fecha_actual = datetime.date.today()
# print(f"la fecha actuar es: {fecha_actual}")

# fecha_formateada = fecha_actual.strftime("%d_%m")
# print(f"la fecha actuar es: {fecha_formateada}")
# dia = fecha_formateada[0:2]
# print(f"El dia es: {dia}")


# dia_formateado = fecha_actual.strftime("%d")
# print(f"El dia formateado: {dia_formateado}")

# hora_actual = datetime.datetime.now()
# print(f"La hora actual sin formato: {hora_actual}")
# hora_formateada = hora_actual.strftime('%H:%M')
# print(f"La hora con formato: {hora_formateada}")


from datetime import date, datetime

# Calcular edad
fecha_nacimiento = date(1980, 5,16 )  # Año, mes, día
hoy = date.today()
edad = hoy.year - fecha_nacimiento.year
if hoy.month < fecha_nacimiento.month or (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
    edad -= 1
print(f"Edad: {edad} años")

# Calcular próximo cumpleaños
proximo_cumple = datetime(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)
if proximo_cumple < datetime.now():
    proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)
diferencia = proximo_cumple - datetime.now()
print(f"Próximo cumpleaños en: {diferencia.days} días")
