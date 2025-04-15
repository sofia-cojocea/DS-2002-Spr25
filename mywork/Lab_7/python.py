import boto3
#variables
bucket_name = "ds2002-pcr5jx"
file_name = "dog.png"

s3 = boto3.client("s3", region_name="us-east-1")

#file uploade
try:
    with open(file_name, "rb") as f:
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=f,
            ACL="public-read"  
        )
    print(f"Uploaded {file_name} to s3://{bucket_name}/{file_name}")
except Exception as e:
    print(f"Upload failed: {e}")

#generate url
try:
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": file_name},
        ExpiresIn=3600  # valid for 1 hour
  )
    print("Presigned URL:", url)
except Exception as e:
    print(f"URL generation failed: {e}")

