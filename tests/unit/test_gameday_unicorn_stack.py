import aws_cdk as core
import aws_cdk.assertions as assertions

from gameday_unicorn.gameday_unicorn_stack import GamedayUnicornStack

# example tests. To run these tests, uncomment this file along with the example
# resource in gameday_unicorn/gameday_unicorn_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = GamedayUnicornStack(app, "gameday-unicorn")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
