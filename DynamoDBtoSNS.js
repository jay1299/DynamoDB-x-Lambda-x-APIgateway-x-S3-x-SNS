var AWS = require("aws-sdk");
var sns = new AWS.SNS();

exports.handler = async (event) => {           //Since SNS calls are async w.r.t to Lambda
    await sns.publish({
        "Message": JSON.stringify(event.Records[0].dynamodb.NewImage),
        //"Message": JSON.stringify(event.Records[0].dynamodb.OldImage) --> You can use this when new and old
                                                                        //  image is configured in DynamoDB streams
        "TopicArn": "arn:aws:sns:us-east-1:017435043832:DynamoDBxSNSxLambda"
    }).promise();
};