#!/usr/bin/env python3

from aws_cdk import core

from rcty2019_cdk.rcty2019_cdk_stack import Rcty2019CdkStack
from rcty2019_cdk.pingit import PingIt

app = core.App()
alarm_email = app.node.try_get_context('alarm_email')
Rcty2019CdkStack(app, "rcty2019-cdk", alarm_email=alarm_email)

url = app.node.try_get_context('ping_url')
tps = app.node.try_get_context('tps')
PingIt(app, "ping-it", ping_url=url, tps=tps)

app.synth()
