#!/usr/bin/env python3
import yaml
from aws_cdk import core

from rcty2019_cdk.rcty2019_cdk_stack import Rcty2019CdkStack
from rcty2019_cdk.pingit import PingIt

app = core.App()
alarm_email = app.node.try_get_context('alarm_email')
Rcty2019CdkStack(app, "rcty2019-cdk", alarm_email=alarm_email)

url = app.node.try_get_context('ping_url')
tps = app.node.try_get_context('tps')
PingIt(app, "ping-it", ping_url=url, tps=tps)

app_env = app.node.try_get_context('Environment')

with open('tags.yml', 'rb') as stream:
    try:
        all_tags = yaml.safe_load(stream)
        env_tags = all_tags[app_env]
        core.Tag.add(app, 'Environment', app_env)
        for tag_key, tag_value in env_tags.items():
            core.Tag.add(app, tag_key, tag_value)
    except yaml.YAMLError as ex:
        print(ex)

app.synth()
