provider "google" {
  credentials = file("path-to-your-service-account-key.json")
  project     = "euro2024-dashboard"
  region      = "us-central1"
}

resource "google_storage_bucket" "airflow_bucket" {
  name          = "your-gcs-bucket-name"
  location      = "US"
  force_destroy = true
}

resource "google_storage_bucket_object" "dag_object" {
  name   = "dags/your-dag-file.py"
  bucket = google_storage_bucket.airflow_bucket.name
  source = "path-to-your-dag-file.py"
}

resource "google_bigquery_dataset" "uefa_dataset" {
  dataset_id = "uefa_data"
  location   = "US"
}