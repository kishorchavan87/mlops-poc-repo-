from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.python import PythonOperator
import kfp

PROJECT_ID = "your-project"
REGION = "us-central1"
REPO = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/my-docker-repo"

def trigger_kubeflow():
    client = kfp.Client(host="http://kubeflow-endpoint")
    client.create_run_from_pipeline_package(
        "kfp_pipelines/train_pipeline.py",
        arguments={}
    )

with DAG("etl_and_train", start_date=days_ago(1), schedule_interval=None) as dag:
    etl_task = KubernetesPodOperator(
        namespace="default",
        image=f"{REPO}/etl:latest",
        name="etl-job",
        task_id="etl_task",
        get_logs=True,
        in_cluster=True,
    )

    trigger_pipeline = PythonOperator(
        task_id="trigger_pipeline",
        python_callable=trigger_kubeflow
    )

    etl_task >> trigger_pipeline
