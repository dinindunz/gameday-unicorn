from aws_cdk import (
  core as cdk,
  aws_ec2 as _ec2,
  aws_ecr as _ecr,
  aws_ecr_assets as _ecr_assets,
  aws_ecs as _ecs,
  aws_ecs_patterns as _ecs_patterns
)
import cdk_ecr_deployment as _ecr_deployment

class UnicornAppStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, aws_account, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
      
        ecr_repo_name='gameday/unicorn'
        image_tag='1.0.0'

        ecr_repo=_ecr.Repository(
          self, 'ecr_repo',
          repository_name=ecr_repo_name
        )
        docker_image=_ecr_assets.DockerImageAsset(
          self, 'docker_image',
          directory='gameday_unicorn/src/unicorn_app'
        )  
        ecr_deployment=_ecr_deployment.ECRDeployment(
          self, 'ecr_deployment',
          src=_ecr_deployment.DockerImageName(docker_image.image_uri),
          dest=_ecr_deployment.DockerImageName('%s.dkr.ecr.%s.amazonaws.com/%s:%s' %(self.account, self.region, ecr_repo_name, image_tag))
        )

        vpc=_ec2.Vpc(
          self, 'vpc',
          max_azs=3
        )
        cluster=_ecs.Cluster(
          self, 'cluster',
          vpc=vpc
        )
        task_definition=_ecs.FargateTaskDefinition(
          self, 'UnicornServiceTask',
          family='UnicornServiceTask'
        )
        container=task_definition.add_container(
          'app',
          image=_ecs.ContainerImage.from_ecr_repository(ecr_repo, image_tag)
        )
        container.add_port_mappings(_ecs.PortMapping(container_port=8080))
        
        fargate_service=_ecs_patterns.ApplicationLoadBalancedFargateService(
          self, 'fargate_service',
          cluster=cluster,
          cpu=256,
          desired_count=1,
          task_definition=task_definition,
          memory_limit_mib=512,
          public_load_balancer=True
        )
