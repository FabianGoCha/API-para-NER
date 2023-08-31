## API-para-NER
Una Api en la que se pueden consultar oraciones guardadas, así como agregar nuevas para despues extraer las entidades de cada oración guardada.

# Dpendencias
Se requiere installar Spacy, FastAPI, Pydantic y uvicorn.

# Correr
Una vez instalado lo anterior se correra el comando en anaconda o miniconda
```
uvicorn ner:app --reload
```

Despues de esto en la segunda linea aparecerá lo siguiente:

```
[32mINFO←[0m:     Uvicorn running on ←[1m[enlace]←[0m (Press CTRL+C to quit)
```
Se entra al enlace desde el navegador (si no aparece nada agregar "/docs" al final del enlace).

Apoareceran las 3 Funciones, la primera para observar la lista existente, la segunda para agregar una nueva oración y la tercera para obtener las entidades.

Debe seleccionarse "Try out".
