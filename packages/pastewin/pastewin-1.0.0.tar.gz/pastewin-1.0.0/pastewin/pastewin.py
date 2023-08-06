import sys
import os
import boto3
import mimetypes


from . import __bucket__
from botocore.exceptions import ClientError


def upload_file(file_name, object_name):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: None, or error
    """

    # If S3 object_name was not specified, use file_name
    if not object_name:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        content_type, _ = mimetypes.guess_type(file_name)

        s3_client.upload_file(file_name, __bucket__, object_name, ExtraArgs={
                              'ContentType': content_type})

        location = s3_client.get_bucket_location(Bucket=__bucket__)[
            'LocationConstraint']

        return f"https://s3-{location}.amazonaws.com/{__bucket__}/{object_name}"
    except ClientError as e:
        return e


def main():
    _, file_name, *object_name = sys.argv
    object_name = object_name[0] if object_name else ""
    print(upload_file(file_name, object_name))


if __name__ == '__main__':
    main()
