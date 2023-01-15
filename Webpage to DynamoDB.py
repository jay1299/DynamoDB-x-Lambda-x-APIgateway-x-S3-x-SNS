import json # importing JSON package to be used when fetching <script> data from S3 index.html
import boto3 # importing this AWS SDK for Python 
from time import gmtime, strftime # importing these two packages for date formatting

dynamodb = boto3.resource('dynamodb') # create a DynamoDB object using the AWS SDK for using DynamoDB commands
table_name = dynamodb.Table('DynamoDBWriterBoard') # Mention your table name here
date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) # store the current time in a human readable format in a variable date

def lambda_handler(event, context):
# extracting values from the event object we got from the Lambda service and storing in below variables
    Name = event['Name']
    Age = event['Age']
    Location = event['Location']
# writing the above variables into DynamoDB table and saving response in the below variable
    response = table_name.put_item( #putItem() method writes an item into the DynamoDB table 
        Item={
            'ID': Name, #Since Partition key is "ID"
            'Age': Age,
            'Location' : Location,
            'Time':date
            })
# This is return a response when you click the "Submit" button only when you have configured everything properly
    return {
        'statusCode': 200,
        'body': json.dumps('Hey, ' + Name+ '. Your data has been saved and will be notified to you on your created SNS protocol :)')
    }