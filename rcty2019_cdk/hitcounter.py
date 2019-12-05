import os
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_dynamodb as _ddb
)


class HitCounter(core.Construct):

    @property
    def handler(self):
        return self._handler

    def __init__(self, scope: core.Construct, id: str, downstream_function: _lambda.IFunction) -> None:
        super().__init__(scope, id)

        self._table = _ddb.Table(self,
                                 'HitsTable',
                                 partition_key=_ddb.Attribute( name='path', type=_ddb.AttributeType.STRING))

        functions_path = os.path.join(os.path.dirname(__file__), '../lambda')
        self._handler = _lambda.Function(
            self, 'HitCountHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler='hitcount.handler',
            code=_lambda.Code.from_asset(functions_path),
            environment={
                'DOWNSTREAM_FUNCTION': downstream_function.function_name,
                'HITS_TABLE_NAME': self._table.table_name,
            }
        )
        downstream_function.grant_invoke(self.handler)
        self._table.grant_read_write_data(self.handler)
