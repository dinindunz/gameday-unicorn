from aws_cdk import (
    core as cdk,
    aws_iam as _iam,
    aws_sns as _sns,
    aws_lambda as _lambda,
    aws_sns_subscriptions as _subs,
)

class AlexaNotifications(cdk.Stack):

    def alexa_api(self, notification_name: str):

        alexa_sns_topic=_sns.Topic(
            self, 'alexa_sns_topic',
            topic_name='%s-Notifications-Alexa-SNS' % notification_name
        )

        notify_alexa_lambda_role=_iam.Role(
            self, 'notify_alexa_lambda_role',
            assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal('lambda.amazonaws.com')),
            role_name='%s-Notifications-Alexa-Lamba-Role' % notification_name
        )

        notify_alexa_lambda_role.add_to_policy(_iam.PolicyStatement(
            actions=[
                'sns:*'
            ],
            effect=_iam.Effect.ALLOW,
            resources=[alexa_sns_topic.topic_arn])
        )
        notify_alexa_lambda_role.add_to_policy(_iam.PolicyStatement(
            actions=[
                'lambda:*'
            ],
            effect=_iam.Effect.ALLOW,
            resources=['*'])
        )
        notify_alexa_lambda_role.add_to_policy(_iam.PolicyStatement(
            actions=[
                'logs:*'
            ],
            effect=_iam.Effect.ALLOW,
            resources=['*'])
        )

        notify_alexa_lambda=_lambda.Function(
            self, 'notify_alexa_lambda',
            runtime=_lambda.Runtime.PYTHON_3_8,
            function_name='%s-Notifications-Alexa-Lambda' % notification_name,
            description='Send Messages to Alexa Notifications API',
            code=_lambda.Code.from_asset('common/notifications/lambda'),
            handler='notify_alexa.lambda_handler',
            role=notify_alexa_lambda_role,
            timeout=cdk.Duration.seconds(900),
            memory_size=128
        )

        alexa_sns_topic.add_subscription(subscription=_subs.LambdaSubscription(notify_alexa_lambda))

        return alexa_sns_topic