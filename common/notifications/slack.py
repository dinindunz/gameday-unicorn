from typing import Sequence
from aws_cdk import (
    core as cdk,
    aws_chatbot as _chatbot,
    aws_sns as _sns
)

class SlackNotifications(cdk.Stack):
    
    def slack_channel(
        self,
        notification_name: str,
        slack_workspace_id: str,
        slack_channel_id: str,
        logging_level: _chatbot.LoggingLevel):

            slack_sns_topic = _sns.Topic(
                self, 'slack_sns_topic',
                topic_name='%s-Slack-SNS' % notification_name
            )

            slack_channel=_chatbot.SlackChannelConfiguration(
                self, 'slack_channel',
                slack_channel_configuration_name=notification_name,
                slack_workspace_id=slack_workspace_id,
                slack_channel_id=slack_channel_id,
                logging_level=logging_level
            )
            slack_channel.add_notification_topic(slack_sns_topic)

            return slack_channel