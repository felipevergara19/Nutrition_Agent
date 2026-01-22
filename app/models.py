from pydantic import BaseModel
from typing import List, Optional


class Ingrediente(BaseModel):
    name: str
    ig: int
    category: str
    stock: Optional[int] = 0


class RecetaRequest(BaseModel):
    usuario_id: str
    lista_ingredientes: List[Ingrediente]

