import os
from google.cloud import storage

RAW_BUCKET = os.getenv("RAW_BUCKET", "your-raw-bucket")
PROCESSED_BUCKET = os.getenv("PROCESSED_BUCKET", "your-processed-bucket")

def process_images():
    client = storage.Client()
    raw_bucket = client.bucket(RAW_BUCKET)
    processed_bucket = client.bucket(PROCESSED_BUCKET)

    for blob in raw_bucket.list_blobs():
        print(f"Processing {blob.name}")
        # Here you could apply preprocessing with cv2 or numpy
        processed_blob = processed_bucket.blob(blob.name)
        processed_blob.upload_from_string(blob.download_as_bytes())

if __name__ == "__main__":
    process_images()
