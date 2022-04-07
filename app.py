#!/usr/bin/env python3
import os
from aws_cdk import core as cdk

from common.cdk_code_pipeline_stack import CdkCodePipelineStack
from common.get_environment import GetEnvironment

app=cdk.App()

env=GetEnvironment.aws_enviromnet('tooling')
CdkCodePipelineStack(app, 'Gameday-Unicorn-CDK-Pipeline', env[1]['cdk_codepipeline_config'], env=env[0])

app.synth()
