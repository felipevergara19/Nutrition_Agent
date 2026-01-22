import  os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def consultar_ia_gemini(list_ingredientes: list) -> str:

    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        ingredientes_texto = ", ".join([ing.name for ing in list_ingredientes])    

        prompt = f"""
        Actúa como un nutricionista experto y chef.
        Tengo estos ingredientes: {ingredientes_texto}.
        
        Por favor:
        1. Crea una receta saludable usando estos ingredientes.
        2. Explica brevemente por qué es buena para alguien que cuida su insulina.
        3. Si hay algún ingrediente peligroso (alto IG), adviértelo.
        
        Responde en formato corto y directo.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al consultar IA: {str(e)}"
    