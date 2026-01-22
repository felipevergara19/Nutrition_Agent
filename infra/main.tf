# 1. EL PROVEEDOR
# Le decimos al robot: "Vas a construir en Amazon (AWS), en la zona de Virginia (us-east-1)"
provider "aws" {
  region = "us-east-1"
}

# 2. EL RECURSO (La Base de Datos)
resource "aws_dynamodb_table" "tabla_recetas" {
  # Nombre de la tabla en la nube
  name           = "RecetasHistoria"
  
  # IMPORTANTE PARA FREE TIER:
  # "PAY_PER_REQUEST" significa que no alquilas el servidor por hora.
  # Solo pagas si guardas datos. Si no la usas, cuesta $0.
  billing_mode   = "PAY_PER_REQUEST"
  
  # LA LLAVE (Como organizamos los datos)
  # Imagina un archivador:
  # - hash_key: La etiqueta del cajón (El ID del usuario)
  # - range_key: El orden de las carpetas dentro del cajón (La fecha)
  hash_key       = "usuario_id"
  range_key      = "fecha_creacion"

  # Definimos que ambos datos son Texto (S = String)
  attribute {
    name = "usuario_id"
    type = "S"
  }

  attribute {
    name = "fecha_creacion"
    type = "S"
  }

  # Etiquetas para que sepas qué es esto si lo ves en 6 meses
  tags = {
    Environment = "Dev"
    Project     = "NutritionAgent"
  }
}