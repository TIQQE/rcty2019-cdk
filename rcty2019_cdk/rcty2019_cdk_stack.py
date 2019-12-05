import os
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as _apigw
)
from rcty2019_cdk.hitcounter import HitCounter
from cdk_watchful import Watchful

class Rcty2019CdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, alarm_email: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        functions_path = os.path.join(os.path.dirname(__file__), '../lambda')
        backend = _lambda.Function(self,
                                   'BackendFunction',
                                   handler='backend.handler',
                                   runtime=_lambda.Runtime.PYTHON_3_7,
                                   code=_lambda.Code.from_asset(functions_path))
        hit_count_handler = HitCounter(self, 'HitCountHandler', downstream_function=backend).handler
        desc = 'A simple example REST API backed by lambda using CDK'
        api = _apigw.LambdaRestApi(self,
                                   'RestApi',
                                   handler=hit_count_handler,
                                   description=desc)
        watch = Watchful(self, 'my-monitoring', alarm_email=alarm_email)
        watch.watch_scope(self)

