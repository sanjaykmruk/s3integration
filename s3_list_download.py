import os

import boto3

output_dir = "./output/"
input_dir = './input/'
data_file_name = "dynomodata.json"

# create input and output files with directory

os.makedirs(name=os.path.dirname(input_dir + data_file_name), exist_ok=True)
os.makedirs(name=os.path.dirname(output_dir + data_file_name), exist_ok=True)

# Let's use Amazon S3
aws_access_key_id = ''
aws_secret_access_key = ''
s3Client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key)
s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

# Dowlaoding all the files from the S3 bucket

print('Listing all the buckets')
for bucket in s3.buckets.all():
    print('Bucket name' + bucket.name)
    data_bucket = s3.Bucket(bucket.name)

    print('Listing all the files in the bucket.')
    for s3_file in data_bucket.objects.all():
        print('File name: ' + s3_file.key)  # prints the contents of bucket
        with open(input_dir + s3_file.key, 'wb') as gz_f:
            print('Downloading the file.')
            s3Client.download_fileobj(bucket.name, s3_file.key, gz_f)



# unzip the gz file

# with gzip.open('yzd4yireta7czlezr3naboqqde.json.gz', 'rb') as f_in:
#     with open(input_dir + data_file_name, 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

# Opening JSON file

# with open(output_dir + data_file_name, 'w') as output_json_file:
#     with open(input_dir + data_file_name) as input_json_file:
#         for jsonObj in input_json_file:
#             data = json.loads(jsonObj)
#
#             # Print the type of data variable
#             print("Type:", type(data))
#
#             TOKEN_STRING = data['Item']['TOKEN_STRING']['S']
#             OWNER = data['Item']['TOKEN_DATA']['M']['owner']['S']
#             SOURCE = data['Item']['SOURCE']['S']
#             EXPIRY_TIME = data['Item']['EXPIRY_TIME']['N']
#             CREATION_TIME = data['Item']['TOKEN_DATA']['M']['creationTime']['N']
#             # Print the data of dictionary
#             # print("\nTOKEN_STRING:", TOKEN_STRING)
#             # print("\nOWNER:", OWNER)
#             # print("\nSOURCE:", SOURCE)
#             # print("\nEXPIRY_TIME:", EXPIRY_TIME)
#             # print("\nCREATION_TIME:", CREATION_TIME)
#
#             newdata = '{"_id":"' + str(TOKEN_STRING) + '","owner":"' + str(OWNER) + '","source":"' + str(
#                 SOURCE) + '","creationtime":"' + str(CREATION_TIME) + '","expirytime":"' + str(EXPIRY_TIME) + '" }\n'
#             # print(newdata)
#             output_json_file.write(newdata)
