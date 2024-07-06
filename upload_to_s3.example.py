import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Upload of {file_name} to {bucket}/{object_name} successful")
    except NoCredentialsError:
        print("Credentials not available")

if __name__ == "__main__":
    upload_to_s3('images/github_tetris.gif', '<your-bucket-name>', 'github_tetris.gif')
