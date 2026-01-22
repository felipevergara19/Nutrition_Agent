import json

class   NutritionAgent:
    def __init__(self, max_ig_allowed):
        self.max_ig_allowed = max_ig_allowed
    
    def filter_safe_ingredients(self, ingredients_list):
        """
        RECIBE UNA LISTA DE INGREFIENTES Y DEVUELVE SOLO LOS SEGUROS.
        SAFE = ig menor  o igual a self.max_ig_allowed
        """
        safe_food = []

        for ingredient in ingredients_list:
            if ingredient["ig"] <= self.max_ig_allowed:
                safe_food.append(ingredient)
        
        return  safe_food
        
    def suggest_recipe(self, safe_ingredients):
        """
        RECIBE UNA LISTA DE INGREFIENTES SEGUROS Y DEVUELVE UNA RECETA.
        """
        ingredient_names = [item["name"] for item in safe_ingredients]
        ingredients_str = ", ".join(ingredient_names)

        prompt = f"Soy resistente a la insulina. Tengo estos ingredientes: {ingredients_str}. Crea una receta de desayuno"
        print(f" Agente: Pensando receta con... {ingredients_str}")

        fake_api_response = {
            "recipe_name": "Tostadas con queso y aguacate",
            "steps": ["batir huevo", "agregar queso", "agregar aguacate"],
            "calories": 200,
        }

        return fake_api_response
    
        


