from fastapi import FastAPI
from app.models import RecetaRequest
from app.services import consultar_ia_gemini
from app.database import guardar_receta_db


app = FastAPI(title="Nutrition Agent", version="0.0.1" , description="API para sugerir recetas")

@app.get("/")
def root():
    return {"message": "API para sugerir recetas esta funcionando correctamente"}     

@app.post("/receta")
def sugerir_receta(payload: RecetaRequest):

    print(f"Usuario Solicitante: {payload.usuario_id}")

    respuesta_ia = consultar_ia_gemini(payload.lista_ingredientes)
    print("2. Guardando receta en la nube")
    exito, fecha = guardar_receta_db(
        usuario_id = payload.usuario_id, 
        receta_texto = respuesta_ia, 
        ingredientes = payload.lista_ingredientes
    )

    mensaje_db = "Receta guardada en AWS exitosamente" if exito else "Error al guardar la receta"


    return {
        "usuario": payload.usuario_id,
        "receta_generada": respuesta_ia,
        "estado_nube": mensaje_db,
        "fecha_registro": fecha
    }
    

    
