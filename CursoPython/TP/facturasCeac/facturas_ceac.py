import os
from datetime import datetime
import locale
import re
import requests
directorio_actual = os.path.dirname(os.path.abspath(__file__))
os.chdir(directorio_actual)
print(f"El directorio actual es {os.getcwd()}")
#nombrar carpeta con el mes actual
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
mes = str(datetime.now().strftime("%B %Y")).upper()
nombre_carpeta = f"Comprobantes CEAC {mes}"

#crear carpeta nueva

directorio_carpeta = os.path.join(directorio_actual, nombre_carpeta)
carpeta_nueva_pdfs = os.path.join(nombre_carpeta, " PDFs")
os.makedirs(carpeta_nueva_pdfs, exist_ok=True)

#leer mensaje
print(f"os.getcwd() {os.getcwd()}")
directorio_mensaje = os.path.join(os.getcwd(), "mensaje.txt")
with open(directorio_mensaje, "r") as archivo:
    mensaje = archivo.read()
#trabajando con el mensaje
patrones_mensajes = re.compile(
    r'(?P<tipo>Agua|Cable|Energia|Internet)\s+Venc\.: (?P<vencimiento>\d{2}/\d{2}/\d{4}) \$'
    r'(?P<saldo>[\d,.]+)\s+(?P<pdf_url>https://levalle\.micoop\.com\.ar/impresion\?\w+)\s+Pagar\s+'
    r'(?P<pay_url>https://levalle\.micoop\.com\.ar/comprobantes\?[\w=&\[\]]+)',
    re.MULTILINE
)

#guardamos en listas los datos que nos interesan

pdfs = []
for match in patrones_mensajes.finditer(mensaje):
    pdfs.append(match.groupdict())

links_pdf = [c["pdf_url"] for c in pdfs]
#print(links_pdf)
links_pago = [c["pay_url"] for c in pdfs]
#print(links_pago)
saldos = [c["saldo"] for c in pdfs]
#print(saldos)
vencimiento = [c["vencimiento"] for c in pdfs]
#print(vencimiento)
tipo = [c["tipo"] for c in pdfs]
#print(tipo)

#Saldo total
saldo_total = sum([float(s.replace(".","").replace(",", ".")) for s in saldos])
saldo_total = round(saldo_total, 2)
print(f"Saldo total: {saldo_total}")

#Descargar PDF
def descargar_pdf(pdf_url, carpeta_pdfs):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        with open(carpeta_pdfs, "wb") as archivo:
            archivo.write(response.content)
        print(f"PDF descargado: {carpeta_pdfs}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el PDF: {e}")
descargar_pdf(links_pdf, carpeta_nueva_pdfs )