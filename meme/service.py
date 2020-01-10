
import json
import random
from controllers import s3

def get_memes(s3Obj):
  ret = []
  metaData = s3Obj.load_resource_content('metadata')
  metaDataJson = json.loads(metaData)
  memeCount = metaDataJson['count']
  for i in range(0, memeCount):
    countIndex = str(i + 1)
    memeData = s3Obj.load_resource_content('celeb-memes/'+countIndex+'.meta')
    memeJson = json.loads(memeData)
    ret.append({
      'img' : 'https://dingdong-app.s3-ap-southeast-1.amazonaws.com/celeb-memes/' + countIndex + '.png',
      'name' : str(i+1) + '.png',
      'ans' : memeJson['name'],
      'level' : memeJson['level'],
      'credit' : memeJson['credit'],
      "link" : memeJson['link']
    })

  return ret

def _exec(pathParams, queryStringParams, eventBody, httpMethod):
  s3Obj = s3.S3('dingdong-app')

  if httpMethod == 'GET':
    ret = get_memes(s3Obj)

    return {
      'statusCode' : 200,
      'body' : json.dumps({
        'memes' : ret
      })
    }

  return None





