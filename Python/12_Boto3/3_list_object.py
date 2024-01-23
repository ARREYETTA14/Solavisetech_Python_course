import boto3


client = boto3.client('s3')
s3 = boto3.client('s3')

Bucket_name = "testsolle"

response = client.list_objects(
    Bucket=Bucket_name,
    Delimiter='string',
    EncodingType='url',
    Marker='string',
    MaxKeys=123,
    Prefix='string',
    RequestPayer='requester',
    OptionalObjectAttributes=[
        'RestoreStatus'
    ]
)


print(response)
