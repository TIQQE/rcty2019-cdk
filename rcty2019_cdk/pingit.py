from aws_cdk import (
    core,
    aws_ecs as _ecs,
    aws_ec2 as _ec2
)


class PingIt(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, ping_url: str, tps: int, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = _ec2.Vpc(self, 'ClusterVpc', max_azs=2)
        cluster = _ecs.Cluster(self, 'Cluster', vpc=vpc)

        taskdef = _ecs.FargateTaskDefinition(self, 'PingItTask')
        env = {'PING_URL': ping_url}
        taskdef.add_container('PingIt',
                              image=_ecs.ContainerImage.from_asset('./pingit'),
                              environment=env)
        _ecs.FargateService(self,
                            'PingItService',
                            cluster=cluster,
                            task_definition=taskdef,
                            desired_count=tps)