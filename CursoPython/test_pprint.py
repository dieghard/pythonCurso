import json
import pprint

# Crear un diccionario con algunos datos
data = {
    "empresa": "Tech Solutions",
    "ubicacion": {
        "pais": "España",
        "ciudad": "Barcelona",
        "direccion": {
            "calle": "Calle Falsa",
            "numero": 123,
            "codigo_postal": "08001"
        }
    },
    "empleados": [
        {
            "nombre": "Juan Pérez",
            "edad": 30,
            "departamento": "Desarrollo",
            "skills": ["Python", "JavaScript", "SQL"],
            "proyectos": [
                {
                    "nombre": "Sistema de gestión",
                    "estado": "en progreso",
                    "duracion_meses": 6
                },
                {
                    "nombre": "Aplicación móvil",
                    "estado": "completado",
                    "duracion_meses": 4
                }
            ]
        },
        {
            "nombre": "María García",
            "edad": 28,
            "departamento": "Marketing",
            "skills": ["SEO", "Content Marketing", "Google Analytics"],
            "proyectos": [
                {
                    "nombre": "Campaña de verano",
                    "estado": "completado",
                    "duracion_meses": 3
                },
                {
                    "nombre": "Rebranding",
                    "estado": "en progreso",
                    "duracion_meses": 5
                }
            ]
        }
    ],
    "productos": [
        {
            "nombre": "Software de gestión",
            "version": "2.1.0",
            "fecha_lanzamiento": "2023-03-15",
            "caracteristicas": ["Gestión de inventarios", "Facturación", "Reportes"]
        },
        {
            "nombre": "App móvil",
            "version": "1.0.3",
            "fecha_lanzamiento": "2022-11-21",
            "caracteristicas": ["Notificaciones push", "Iniciar sesión con redes sociales", "Modo oscuro"]
        }
    ],
    "clientes": [
        {
            "nombre": "Empresa A",
            "contacto": {
                "nombre": "Luis Fernández",
                "telefono": "+34 123 456 789",
                "email": "luis.fernandez@empresaA.com"
            },
            "contratos": [
                {
                    "producto": "Software de gestión",
                    "fecha_inicio": "2023-01-01",
                    "fecha_fin": "2023-12-31"
                }
            ]
        },
        {
            "nombre": "Empresa B",
            "contacto": {
                "nombre": "Ana Martínez",
                "telefono": "+34 987 654 321",
                "email": "ana.martinez@empresaB.com"
            },
            "contratos": [
                {
                    "producto": "App móvil",
                    "fecha_inicio": "2022-10-01",
                    "fecha_fin": "2023-09-30"
                },
                {
                    "producto": "Software de gestión",
                    "fecha_inicio": "2023-02-01",
                    "fecha_fin": "2024-01-31"
                }
            ]
        }
    ]
}

print(data)
pprint.pprint(data)
