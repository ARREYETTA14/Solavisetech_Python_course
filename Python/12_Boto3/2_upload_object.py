import boto3


client = boto3.client('s3')
s3 = boto3.client('s3')

Bucket_name = "testsolle"
file_upload = s3.upload_file('test.txt', Bucket_name, 'test.txt')


print(file_upload)