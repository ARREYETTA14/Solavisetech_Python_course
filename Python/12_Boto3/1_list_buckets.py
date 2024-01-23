### List s3 buckets
import boto3

client = boto3.client('s3')

response = client.list_buckets()

for i in response["Buckets"]:
    print(i["Name"])


# import boto3

# client = boto3.client('s3')

# # response = client.list_buckets()

# # for i in response["Buckets"]:
# #     print(i["Name"])

# response = client.create_bucket(
#     Bucket='testsolle1',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'eu-west-1'
#     }
# )

# print(response) 





