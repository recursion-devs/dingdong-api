
import json


def handler(event, context):

  queryStringParams = event['queryStringParams']
  path = event['requestContext']['resourcePath']
  httpMethod = event['httpMethod']
  pathParams = event['pathParameters']
  pathSegments = path.split('/')
  evenBody = event['body']

  return {
    'statusCode' : 200,
    'body' : json.dumps({
      'msg' : 'OK'
    })
  }








