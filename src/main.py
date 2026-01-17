from agents import NutritionAgent
from data_models import incomming_pantry_data

def main():
    print("Bienvenido al asistente de nutricion")
    nutrition_agent = NutritionAgent(max_ig_allowed=50)

    print(f"Recibidos {len(incomming_pantry_data)} ingredientes")
    safe_list = nutrition_agent.filter_safe_ingredients(incomming_pantry_data)
    print(f"Filtrado {len(safe_list)} ingredientes")
    print(safe_list)

    if len(safe_list) > 0:
        recipe = nutrition_agent.suggest_recipe(safe_list)
        print("Receta sugerida:")
        print(recipe)
    else:
        print("No hay ingredientes seguros")

if __name__ == "__main__":
    main()