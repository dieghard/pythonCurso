
from datetime import datetime

fecha_hora_actual = datetime.now()
fecha_formateada = fecha_hora_actual.strftime("%d/%m/%Y")

print(f"Fecha y hora actual: {fecha_formateada}")

#Calcular la fecha de un día específico:

año = 2024
mes = 5
dia = 12

fecha_especifica = datetime(año, mes, dia)
print(f"Fecha específica: {fecha_especifica}")

#Formatear fechas:
fecha_hora_actual = datetime.now()
fecha_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha y hora formateada: {fecha_formateada}")
