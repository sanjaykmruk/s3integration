import os
import gzip
import shutil
import json
from multiprocessing import Pool

THREAD_POOL = 5
output_dir = '../output/'
input_dir = '../input/'
# data_file_name = "dynomodata.json"
# Specify the directory path to read all the gzip files
gz_directory_path = "./"

# Get all entries in the directory
gz_entries = os.listdir(gz_directory_path)

# create input and output files with directory

os.makedirs(name=os.path.dirname(input_dir), exist_ok=True)
os.makedirs(name=os.path.dirname(output_dir), exist_ok=True)

# function to parallel process the file
def processfile(gz_file_name):
# for gz_file in gz_entries:
#     if os.path.isfile(os.path.join(gz_directory_path, gz_file)):
#         print(gz_file)
        
        print(gz_file_name)
        
        data_file_name= os.path.splitext(gz_file_name)[0]
        print(data_file_name)

        # unzip the gz file
        with gzip.open(gz_directory_path + gz_file_name, 'rb') as gz_in:
            with open(input_dir + data_file_name, 'wb') as json_out:
                shutil.copyfileobj(gz_in, json_out)

        # Opening JSON file

        with open(output_dir + data_file_name, 'w') as output_json_file:
            with open(input_dir + data_file_name) as input_json_file:
                for jsonObj in input_json_file:
                    data = json.loads(jsonObj)

                    TOKEN_STRING = data['Item']['TOKEN_STRING']['S']
                    OWNER = data['Item']['TOKEN_DATA']['M']['owner']['S']
                    SOURCE = data['Item']['SOURCE']['S']
                    EXPIRY_TIME = data['Item']['EXPIRY_TIME']['N']
                    CREATION_TIME = data['Item']['TOKEN_DATA']['M']['creationTime']['N']

                    newdata = '{"_id":"' + str(TOKEN_STRING) + '","owner":"' + str(OWNER) + '","source":"' + str(
                        SOURCE) + '","roles":["customer"],"extraData":{},"creationtime":{"$date":{"$numberLong":"' + str(CREATION_TIME) + '"}},"expirytime":{"$date":{"$numberLong":"' + str(EXPIRY_TIME)+'"}} }\n'
                    # print(newdata)
                    output_json_file.write(newdata)


if __name__ == '__main__':
    with Pool(THREAD_POOL) as p:
        p.map(processfile, gz_entries)