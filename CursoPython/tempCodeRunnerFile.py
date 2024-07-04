texto = "Este es un ejemplo de texto con palabras clave."
palabras_clave = ["ejemplo", "texto", "clave"]

palabra_detectada = next(palabra for palabra in palabras_clave if palabra in texto)

print(f"Palabra detectada: {palabra_detectada}")  # Salida: Palabra detectada: ejemplo
