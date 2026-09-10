import boto3
from botocore.exceptions import NoCredentialsError
import os

def upload_to_aws(local_file, bucket_name, s3_file_name):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket_name, s3_file_name)
        print(f"Subida exitosa: {local_file} a s3://{bucket_name}/{s3_file_name}")
        return True
    except FileNotFoundError:
        print("El archivo local no fue encontrado.")
        return False
    except NoCredentialsError:
        print("Credenciales de AWS no encontradas o inválidas.")
        return False

if __name__ == "__main__":
    # Ejemplo de uso estructurado
    LOCAL_FILE = "security_logs.csv"
    BUCKET = "mi-bucket-seguridad-cenco-demo"
    S3_PATH = "raw/security_logs/security_logs.csv"

    if os.path.exists(LOCAL_FILE):
        upload_to_aws(LOCAL_FILE, BUCKET, S3_PATH)
    else:
        print("Ejecuta primero el generador de logs.")
