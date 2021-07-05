from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    core,
)


class AwsCdkTutorialStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
        bucket = s3.Bucket(self, "deletemelater-20210705")
