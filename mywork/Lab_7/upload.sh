!/bin/bash

if ["$#" -ne 3]; then
        echo "Usage: $0 <local_file_name> <bucket_name>  <expiration_seconds>
        exit 1
fi

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

#check if file exists
if [ ! -f "$LOCAL_FILE"]; then
        echo "ERROR: FILE '$LOCAL_FILE' not found."
        exit 2
fi

#if exists upload to S3
echo "Uploading $LOCAL_FILE to s3://$BUCKET_NAME/..."
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/"

if [ $? -ne 0 ]; then
    echo "Upload failed. Exiting."
    exit 3
fi

echo "Creating pre-signed URL valid for $EXPIRATION seconds..."
URL=$(aws s3 presign "s3://$BUCKET_NAME/$LOCAL_FILE" --expires-in "$EXPIRATION")

echo " Pre-signed URL:"
echo "$URL"

