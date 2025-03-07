import boto3
import botocore
import os
import uuid

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET")
)

## allow users to upload a file with the same name by applying a unique name once uploaded



ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"

BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"http://{BUCKET_NAME}.s3.amazonaws.com/"

## Now let's write the function that you'll need to actually upload the file to your AWS S3 Bucket 
## and return the new public URL for the file uploaded to the bucket if the upload is successful


def upload_file_to_s3(file, acl="public-read"):
    print("Did you get called")
    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.name,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        print("FILE", file)
        print("FileName", file.name)
    except Exception as e:
        # in case the your s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.name}"}

##When you call the upload_file_to_s3 helper function from your route, 
# make sure to print the variable you are storing the return value to, 
# as the error messages from AWS are extremely helpful. You won't see the helpful error messages if you don't print them or return them to your frontend.


## You will also want to implement a similar helper function to remove files you already uploaded to your S3 Bucket,
#  as you don't want to store images for resources that have been deleted. (you can use the upload_file_to_s3 and remove_file_from_s3 together to handle update functionality too!)

def remove_file_from_s3(image_url):
    # AWS needs the image file name, not the URL, 
    # so you split that out of the URL
    key = image_url.rsplit("/", 1)[1]
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True