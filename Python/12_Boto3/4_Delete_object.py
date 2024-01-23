import boto3


client = boto3.client('s3')
s3 = boto3.client('s3')

Bucket_name = "testsolle"

response = client.delete_object(
    Bucket=Bucket_name,
    Key='test.txt',
    RequestPayer='requester',
    # ExpectedBucketOwner='default'
)

print(response)