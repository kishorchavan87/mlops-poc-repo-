# MLOps POC (Airflow + Kubeflow + MLflow + Voxel51)

## Steps
1. Build & push containers:
   ```bash
   gcloud builds submit --config cloudbuild.yaml --substitutions=_REGION=us-central1,PROJECT_ID=your-project .




