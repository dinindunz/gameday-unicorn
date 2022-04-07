from aws_cdk import (
    core as cdk
)
from gameday_unicorn.stacks.unicorn_app_stack import UnicornAppStack
from common.get_environment import GetEnvironment

class DeployStacks(cdk.Stage):

    def __init__(self, scope: cdk.Construct, id: str, aws_account, **kwargs):
        super().__init__(scope, id, **kwargs)

        tooling_env=GetEnvironment.aws_enviromnet('tooling')
        dev_env=GetEnvironment.aws_enviromnet('dev')
        prod_env=GetEnvironment.aws_enviromnet('prod')

        UnicornAppStack(self, 'UnicornAppStack', aws_account, env=tooling_env[0])