
import json


def handler(event, context):

  queryStringParams = event['queryStringParameters']
  path = event['requestContext']['resourcePath']
  httpMethod = event['httpMethod']
  pathParams = event['pathParameters']
  pathSegments = path.split('/')
  eventBody = event['body']

  servicename = pathSegments[1] 
  modulePath = servicename + '.service'
  serviceModule = __import__(modulePath, fromlist=['service'] )

  resp = serviceModule._exec(pathParams, queryStringParams, eventBody, httpMethod)
  if resp:
    return resp

  return {
    'statusCode' : 400,
    'body' : json.dumps({
      'msg' : 'Bad Request'
    })
  }


