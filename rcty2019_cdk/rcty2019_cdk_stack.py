import os
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as _apigw
)


class Rcty2019CdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        functions_path = os.path.join(os.path.dirname(__file__), '../lambda')
        backend = _lambda.Function(self,
                                   'BackendFunction',
                                   handler='backend.handler',
                                   runtime=_lambda.Runtime.PYTHON_3_7,
                                   code=_lambda.Code.from_asset(functions_path))
        desc = 'A simple example REST API backed by lambda using CDK'
        api = _apigw.LambdaRestApi(self,
                                   'RestApi',
                                   handler=backend,
                                   description=desc)

