#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import boto3
import requests

s3=boto3.client('s3')

def download_file(url, file_path):
        response = requests.get(url) 
        with open(file_path, 'wb') as file:
                file.write(response.content)

URL = "https://upload.wikimedia.org/wikipedia/commons/2/2c/Rotating_earth_%28large%29.gif"
FILE_NAME = "Download.gif"
BUCKET_NAME = "ds2002-fyr5ht"
EXPIRATION = 60

download_file(URL, FILE_NAME) 

s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME,
ExtraArgs={"ContentType": "image/gif"}
)

PRESIGNED_URL = s3.generate_presigned_url(
	"get_object", Params={"Bucket": BUCKET_NAME, "Key": FILE_NAME}, ExpiresIn=EXPIRATION
)

print(f"Presigned URL: {PRESIGNED_URL}")

 

