import boto3

# Créer un client S3
s3_client = boto3.client('s3', region_name='eu-west-1')

# Créer un bucket S3 avec le nom "demo-bucket-ar-74700"
s3_client.create_bucket(Bucket='demo-bucket-ar-74700', CreateBucketConfiguration={
    'LocationConstraint': 'eu-west-1'
})
