from datetime import datetime
from aws_cdk import core as cdk

#Common Tags
class CommonTags:
    def add(vpc, resource, application, stack_name, stack_version):
        
        app=cdk.App()
        tags=app.node.try_get_context('tags')

        cdk.Tags.of(resource).add('Application', application)
        cdk.Tags.of(resource).add('Owner', tags['owner'])
        cdk.Tags.of(resource).add('Created-By', tags['created_by'])
        cdk.Tags.of(resource).add('Deployed-via', tags['deployed_via'])
        cdk.Tags.of(resource).add('CFN-Stack', stack_name)
        cdk.Tags.of(resource).add('Environment', vpc)
        cdk.Tags.of(resource).add('Version', stack_version)
        #cdk.Tags.of(resource).add('Created-Date', str(datetime.utcnow())+' UTC')

#Custom S3 Tags
class S3Tags:
    def add(vpc, s3_bucket, bucket_name, stack_name, stack_version, tag_obj_trans, tag_obj_exp):
        
        CommonTags.add(vpc, s3_bucket, bucket_name, stack_name, stack_version)
        cdk.Tags.of(s3_bucket).add('Lifecycle - Object Transition', tag_obj_trans)
        cdk.Tags.of(s3_bucket).add('Lifecycle - Object Expiration', tag_obj_exp)