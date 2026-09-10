from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'constanza_palacios',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def check_raw_files():
    print("Verificando existencia de nuevos archivos en la ruta raw de S3...")

def process_glue_job():
    print("Ejecutando proceso de transformación y limpieza con AWS Glue...")

with DAG(
    'security_logs_etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL diario para logs de ciberseguridad',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id='check_s3_files',
        python_callable=check_raw_files,
    )

    t2 = PythonOperator(
        task_id='run_aws_glue_job',
        python_callable=process_glue_job,
    )

    t1 >> t2
