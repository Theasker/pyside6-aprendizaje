"""Breve: Recorre recursivamente estructuras anidadas (diccionarios y listas)
e imprime su contenido en consola con indentación. Ejemplo didáctico.
"""

data = {
    "empresa": "Gobierno de Aragón",
    "departamentos": {
        "Tecnología": {
            "responsable": "Mauricio Segura",
            "equipo": ["Ana", "Luis", "Marta"]
        },
        "Compras": {
            "responsable": "Elena",
            "presupuesto": 125000
        }
    },
    "inventario": {
        "portátiles": [
            {"marca": "Dell", "serie": "ABC123"},
            {"marca": "HP", "serie": "XYZ456"}
        ],
        "monitores": 42
    }
}

# Entender "if isinsdatatance"
ident = 2

def recursivo(item,level=0):
    if isinstance(item, dict): # Si es un diccionario
        for key, value in item.items():
            print(f"{" "*ident*level}{key}:")
            recursivo(value, level + 1)
    elif isinstance(item, list): # Si es una lista
        for value in item:
            recursivo(value, level + 1)
    else:
        print(f"{" "*ident*level}- {item}")

recursivo(data)