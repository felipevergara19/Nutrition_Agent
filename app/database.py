import boto3
from datetime import datetime
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('RecetasHistoria')

def guardar_receta_db(usuario_id: str, receta_texto: str, ingredientes: list):
    
    try:
        fecha_actual = datetime.now().isoformat()
        lista_nombres = [ing.name for ing in ingredientes]
        
        response = table.put_item(
            Item={
                'usuario_id': usuario_id,
                'fecha_creacion': fecha_actual,
                'receta': receta_texto,
                'ingredientes': lista_nombres,
                'origen': 'IA Generativa'
            }
        )
        return True, fecha_actual

    except ClientError as e:
        print(f"Error al guardar la receta: {e.response['Error']['Message']}")
        return False, None
