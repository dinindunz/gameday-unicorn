from aws_cdk import (
    core as cdk,
    aws_codepipeline as _codepipeline,
    aws_codepipeline_actions as _codepipeline_actions,
    aws_codecommit as _codecommit,
    pipelines as _pipelines,
    aws_chatbot as _chatbot,
    aws_codestarnotifications as _notifications,
)
from deploy_stacks import DeployStacks
from common.notifications.slack import SlackNotifications
from common.notifications.alexa import AlexaNotifications
from common.get_environment import GetEnvironment

class CdkCodePipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, config, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tooling_env=GetEnvironment.aws_enviromnet('tooling')
        dev_env=GetEnvironment.aws_enviromnet('dev')
        prod_env=GetEnvironment.aws_enviromnet('prod')
        stack_version='1.0.0'

        repo=_codecommit.Repository(
            self, 'repo',
            repository_name=config['repo_name']
        )

        cloud_assembly_artifact=_codepipeline.Artifact()
        source_artifact=_codepipeline.Artifact()

        deploy_pipeline=_pipelines.CdkPipeline(
            self, 'deploy_pipeline',
            pipeline_name=self.stack_name,
            cloud_assembly_artifact=cloud_assembly_artifact,
            source_action=_codepipeline_actions.CodeCommitSourceAction(
                action_name='CodeCommit',
                output=source_artifact,
                repository=repo,
                trigger=_codepipeline_actions.CodeCommitTrigger.EVENTS
            ),
            synth_action=_pipelines.SimpleSynthAction(
                install_commands=[
                    'npm install -g aws-cdk',
                    'python3 -m pip install -r requirements.txt'
                ],
                synth_command='npx cdk synth',
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact
            )
        )

        #deploy_pipeline.add_application_stage(
        #    DeployModules(self, 'Deploy-Tooling', 'tooling', env=tooling_env[0])
        #)

        deploy_pipeline.add_application_stage(
            DeployStacks(self, 'Deploy-Dev', 'dev', env=dev_env[0])
        )

        #deploy_pipeline.add_application_stage(
        #    DeployModules(self, 'Deploy-Prod', 'prod', env=prod_env[0])
        #)

        codepipeline_notifications=config['codepipeline_notifications']
        notification_name='%s-Notifications' % self.stack_name

        slack_channel=SlackNotifications.slack_channel(
            self,
            notification_name=notification_name,
            slack_workspace_id=codepipeline_notifications['slack_workspace_id'],
            slack_channel_id=codepipeline_notifications['slack_channel_id'],
            logging_level=_chatbot.LoggingLevel.ERROR
        )

        notifications_rule=_notifications.NotificationRule(
            self, 'notifications_rule',
            notification_rule_name=notification_name,
            source=deploy_pipeline.code_pipeline,
            events=codepipeline_notifications['code_pipeline_events'],
            targets=[slack_channel]
        )

        if codepipeline_notifications['enable_alexa_notifications']==True:
            alexa_sns_topic=AlexaNotifications.alexa_api(
                self,
                notification_name=self.stack_name
            )
            notifications_rule.add_target(alexa_sns_topic)