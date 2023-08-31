
# Importación de librerias (incluida la de la carpeta model).

import uvicorn                      # Servicio web de python.
from fastapi import FastAPI         # importacion de la API.
from model import ner_main          # libreria propia.
from pydantic import BaseModel      # Clases tipadas.

# Definir el nombre de la API, así como su descripción.

app = FastAPI(
    title = "NER API",
    description = "Agregar y Extraer etiquetas del texto"
)

# Clase sobre cómo se guardarán las nuevas oraciones.

class Oraciones(BaseModel):
    oracion: str

# Lista dónde están guardadas las oraciones (notese que ya hay una guardada).

lista_de_oraciones = [Oraciones(oracion="Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.")
                      ]

# Operación get que muestra la lista de oraciones.

@app.get("/oraciones")
async def oraciones_lista():
    return lista_de_oraciones

# Operación get donde se obtienen las entidades de cada oración.

@app.get("/ner")
def entidades():
    resultado = []
    for texto in lista_de_oraciones:
        output=list(ner_main.ner_spacy(texto.oracion))
        resultado.append({"Oracion:": texto.oracion, "Entidades:": output})
    return {"Resultado: ": resultado}

# Operación Post para agregar mas oraciones a la lista de oraciones.

@app.post("/oraciones")
def oracion(texto: str):
    lista_de_oraciones.append(Oraciones(oracion=texto))