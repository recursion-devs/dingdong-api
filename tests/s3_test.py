
from controllers import s3

S3 = s3.S3('dingdong-app')
content = S3.load_resource_content('metadata')

print(content)


