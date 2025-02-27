#!/bin/bash

FILE_NAME="$1"
BUCKET_NAME="$2"
EXPIRATION="$3"

aws s3 cp "$FILE_NAME" "s3://$BUCKET_NAME/"

PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET_NAME/$FILE_NAME" --expires-in "$EXPIRATION")

echo "Presigned URL (valid for $EXPIRATION seconds): $PRESIGNED_URL"



