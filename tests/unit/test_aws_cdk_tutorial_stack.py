import json
import pytest

from aws_cdk import core
from aws_cdk_tutorial.aws_cdk_tutorial_stack import AwsCdkTutorialStack


def get_template():
    app = core.App()
    AwsCdkTutorialStack(app, "aws-cdk-tutorial")
    return json.dumps(app.synth().get_stack("aws-cdk-tutorial").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
