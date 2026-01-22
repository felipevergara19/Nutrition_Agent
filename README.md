# Nutrition Agent 🥑

**Nutrition Agent** is an intelligent nutrition assistant designed for individuals with **insulin resistance** or those monitoring their Glycemic Index (GI). It helps users make better dietary decisions by analyzing ingredients and suggesting healthy, low-GI recipes.

The agent takes a list of ingredients, evaluates them based on nutritional safety, and leverages **Google Gemini AI** to generate personalized meal suggestions, which are then stored in **AWS DynamoDB** for history tracking.

## 🚀 Core Features

*   **Intelligent Recipe Generation**: Uses **Gemini 2.5 Flash Lite** to create nutritionist-approved recipes.
*   **GI Safety Check**: Filters or warns about high-GI ingredients to protect users with insulin resistance.
*   **Persistent History**: Automatically saves generated recipes to **AWS DynamoDB** for future reference.
*   **FastAPI Backend**: A robust and scalable API to handle requests and integrations.

## 📂 Project Structure

```text
Nutrition_Agent/
├── app/
│   ├── main.py         # FastAPI application and routes
│   ├── agents.py       # Core logic for ingredient filtering (Legacy/Logic)
│   ├── services.py     # External integrations (Gemini AI)
│   ├── database.py     # Database operations (AWS DynamoDB)
│   ├── models.py       # Pydantic data schemas
│   └── __init__.py
├── infra/              # Infrastructure scripts
├── requirements.txt    # Python dependencies
└── README.md
```

## 🛠️ Requirements & Installation

1.  **Clone the repository**:
    ```bash
    git clone <REPOSITORY_URL>
    cd Nutrition_Agent
    ```

2.  **Prerequisites**:
    *   Python 3.9+
    *   An AWS account with DynamoDB access.
    *   A Google AI (Gemini) API Key.

3.  **Setup Environment Variables**:
    Create a `.env` file in the root directory:
    ```env
    GOOGLE_API_KEY=your_gemini_api_key_here
    AWS_ACCESS_KEY_ID=your_aws_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret
    ```

4.  **Virtual Environment (Recommended)**:
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

5.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Execution

To start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can access the interactive documentation at `/docs`.

### Example Request (`POST /receta`)

**Body**:
```json
{
  "usuario_id": "user123",
  "lista_ingredientes": [
    {"name": "Eggs", "ig": 0, "category": "protein"},
    {"name": "Avocado", "ig": 10, "category": "fat"}
  ]
}
```

## 🧠 How It Works

1.  **API Entry**: The request is received by the FastAPI endpoint.
2.  **AI Consultation**: The `services.py` module sends the ingredient list to **Google Gemini** with a specific prompt tailored for insulin resistance.
3.  **Storage**: The resulting recipe is saved to the `RecetasHistoria` table in **DynamoDB**, linked to the `usuario_id`.
4.  **Response**: The system returns the generated recipe and the database status to the user.

## 📝 Roadmap

*   [ ] Connect to real food databases (e.g., Nutritionix).
*   [ ] Implement user authentication and profiles.
*   [ ] Add more advanced filtering (allergies, keto, vegan).
*   [ ] Front-end application for mobile/web users.

---
