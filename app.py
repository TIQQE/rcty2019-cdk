#!/usr/bin/env python3

from aws_cdk import core

from rcty2019_cdk.rcty2019_cdk_stack import Rcty2019CdkStack


app = core.App()
Rcty2019CdkStack(app, "rcty2019-cdk")

app.synth()
