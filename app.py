#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_iam_lab_stack import CdkIamLabStack

app = cdk.App()
CdkIamLabStack(app, "CdkIamLabStack")
app.synth()
