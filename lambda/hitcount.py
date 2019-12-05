import json, os, logging, boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ddb = boto3.resource('dynamodb')
_lambda = boto3.client('lambda')

table = ddb.Table(os.environ['HITS_TABLE_NAME'])


def handler(event, context):
    logger.info(json.dumps(event))
    table.update_item(
        Key={'path': event['path']},
        UpdateExpression='ADD hits :incr',
        ExpressionAttributeValues={':incr': 1}
    )

    rsp = _lambda.invoke(
        FunctionName=os.environ['DOWNSTREAM_FUNCTION'],
        Payload=json.dumps(event)
    )

    body = rsp['Payload'].read()
    logger.info('Downstream response: {}'.format(body))
    return json.loads(body)