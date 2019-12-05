import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(json.dumps(event))
    http_method = event['httpMethod']
    if http_method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps('API invoked successfully with {}!'.format(http_method))
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported HTTP method {}'.format(http_method))
        }
