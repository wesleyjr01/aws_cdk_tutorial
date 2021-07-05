#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_tutorial.aws_cdk_tutorial_stack import AwsCdkTutorialStack


app = core.App()
AwsCdkTutorialStack(app, "aws-cdk-tutorial")

app.synth()
