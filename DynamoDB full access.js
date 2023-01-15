{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:UpdateItem",
                "dynamodb:GetShardIterator",
                "dynamodb:GetRecords",
                "dynamodb:DescribeStream",
                "dynamodb:ListStreams"
            ],
            "Resource": "*"
        }
    ]
}