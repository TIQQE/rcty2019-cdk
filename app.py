#!/usr/bin/env python3

from aws_cdk import core

from rcty2019_cdk.rcty2019_cdk_stack import Rcty2019CdkStack

app = core.App()
alarm_email = app.node.try_get_context('alarm_email')
Rcty2019CdkStack(app, "rcty2019-cdk", alarm_email=alarm_email)

app.synth()
