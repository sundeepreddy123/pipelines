import json
import os
import boto3


sns = boto3.client("sns")

SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]


def lambda_handler(event, context):

    print("Received SQS event:")
    print(json.dumps(event))

    for record in event["Records"]:

        order = json.loads(record["body"])

        print(f"Processing order: {order['order_id']}")

        order["status"] = "COMPLETED"

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=json.dumps(order),
            Subject="Order Completed"
        )

        print(
            f"Order completed and notification sent: "
            f"{order['order_id']}"
        )

    return {
        "statusCode": 200,
        "body": "Orders processed successfully"
    }
