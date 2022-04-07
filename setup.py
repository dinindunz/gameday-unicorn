import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="gameday_unicorn",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "gameday_unicorn"},
    packages=setuptools.find_packages(where="gameday_unicorn"),

    install_requires=[
        "aws-cdk.core==1.132.0",
        "aws-cdk.pipelines==1.132.0",
        "aws-cdk.aws_codecommit==1.132.0",
        "aws-cdk.aws_ec2==1.132.0",
        "aws-cdk.aws_ecr_assets==1.132.0",
        "aws-cdk.aws_ecs==1.132.0",
        "aws-cdk.aws_ecs_patterns==1.132.0",
        "aws-cdk.aws_ecr==1.132.0",
        "aws-cdk.aws_lambda==1.132.0",
        "aws-cdk.aws_apigateway==1.132.0",
        "aws-cdk.aws_dynamodb==1.132.0",
        "cdk-dynamo-table-view==0.1.139",
        "aws-cdk.aws_sns==1.132.0",
        "aws-cdk.aws_chatbot==1.132.0",
        "aws-cdk.aws_sns_subscriptions==1.132.0",
        "aws-cdk.aws_codestarnotifications==1.132.0",
        "cdk-alexa-skill==0.0.1",
        "cdk-ecr-deployment==0.0.80"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
