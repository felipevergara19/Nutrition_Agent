# Nutrition Agent 🥑

Bienvenido al repositorio de **Nutrition Agent**. Este proyecto es un asistente de nutrición inteligente diseñado para ayudar a personas con **resistencia a la insulina** o que buscan controlar su índice glucémico (IG) a tomar mejores decisiones alimenticias.

El agente analiza una lista de ingredientes disponibles (simulando una despensa o respuesta de API), filtra aquellos que son seguros según un umbral de IG configurado y sugiere recetas saludables.

## 🚀 Funcionalidades Principales

*   **Filtrado de Ingredientes**: Analiza ingredientes basándose en su Índice Glucémico (IG).
*   **Seguridad Alimentaria**: Permite configurar un `max_ig_allowed` (IG máximo permitido) para personalizar el filtro según las necesidades del usuario.
*   **Sugerencia de Recetas**: Tana los ingredientes seguros y genera una propuesta de receta (actualmente simulada).

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```text
Nutrition_Agent/
├── src/
│   ├── agents.py       # Lógica del agente (Filtros y generación de recetas)
│   ├── data_models.py  # Datos simulados (Ingredientes de ejemplo)
│   └── main.py         # Punto de entrada de la aplicación
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Requisitos e Instalación

1.  **Clonar el repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd Nutrition_Agent
    ```

2.  **Requisitos**:
    *   Python 3.x instalado.

3.  **Entorno Virtual (Opcional pero recomendado)**:
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    ```

## ▶️ Ejecución

Para iniciar el agente y ver cómo procesa los datos de prueba:

```bash
# Estando en la raiz del proyecto
python src/main.py
```

o si usas el lanzador `py` en Windows:

```bash
py src/main.py
```

### Ejemplo de Salida

```text
Bienvenido al asistente de nutricion
Recibidos 5 ingredientes
Filtrado 2 ingredientes
[{'name': 'Huevos', 'ig': 0, 'category': 'protein'}, {'name': 'Palta', 'ig': 10, 'category': 'fat'}]
 Agente: Pensando receta con... Huevos, Palta
Receta sugerida:
{'recipe_name': 'Tostadas con queso y aguacate', ...}
```

## 🧠 Cómo funciona

1.  **Datos**: `data_models.py` provee una lista de ingredientes con su IG y categoría.
2.  **Agente**: En `agents.py`, la clase `NutritionAgent` se inicializa con un límite de IG (por defecto 50 en el ejemplo).
3.  **Proceso**:
    *   El método `filter_safe_ingredients` recorre la lista y descarta los alimentos con IG alto (ej. azúcar, pan blanco).
    *   El método `suggest_recipe` toma los ingredientes seguros y simula la creación de una receta apta para el usuario.

## 📝 Próximos Pasos

*   Conectar con una API real de alimentos/recetas.
*   Implementar un LLM real para la generación dinámica de recetas en `suggest_recipe`.
*   Añadir más filtros (calorías, alergias, etc.).

---

