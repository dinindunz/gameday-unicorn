from aws_cdk import core as cdk

class GetEnvironment:
    
    def aws_enviromnet(aws_account):
        app=cdk.App()
        #vpc=app.node.try_get_context('env')
        env_context=app.node.try_get_context(aws_account)
        aws_account_id=env_context['aws_account_id']
        aws_region=env_context['aws_region']
        env=cdk.Environment(account=aws_account_id, region=aws_region)
        return env, env_context