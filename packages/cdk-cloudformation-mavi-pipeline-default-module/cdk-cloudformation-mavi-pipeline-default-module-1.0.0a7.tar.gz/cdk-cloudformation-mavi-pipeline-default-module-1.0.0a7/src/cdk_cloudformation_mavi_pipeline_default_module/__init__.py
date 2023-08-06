'''
# mavi-pipeline-default-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `MAVI::Pipeline::Default::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type MAVI::Pipeline::Default::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name MAVI::Pipeline::Default::MODULE \
  --publisher-id c812060033ed3bad51a82f3aa9ad5ef18ea8ed0d \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/c812060033ed3bad51a82f3aa9ad5ef18ea8ed0d/MAVI-Pipeline-Default-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `MAVI::Pipeline::Default::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fmavi-pipeline-default-module+v1.0.0).
* Issues related to `MAVI::Pipeline::Default::MODULE` should be reported to the [publisher](undefined).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnDefaultModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModule",
):
    '''A CloudFormation ``MAVI::Pipeline::Default::MODULE``.

    :cloudformationResource: MAVI::Pipeline::Default::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnDefaultModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnDefaultModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``MAVI::Pipeline::Default::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8661d854e7e2f80918a2cc08b2d7704967c7188c9fa034e24ff501d2ff605e10)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDefaultModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDefaultModuleProps":
        '''Resource props.'''
        return typing.cast("CfnDefaultModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnDefaultModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnDefaultModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnDefaultModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type MAVI::Pipeline::Default::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnDefaultModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnDefaultModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnDefaultModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d65405b5d693f1d82d6adc2c1be93f1bd853606b94e1d191595055cf6207a1c)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnDefaultModulePropsParameters"]:
        '''
        :schema: CfnDefaultModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnDefaultModulePropsResources"]:
        '''
        :schema: CfnDefaultModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnDefaultModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "branch_name": "branchName",
        "bucket_artifact_store": "bucketArtifactStore",
        "build_project": "buildProject",
        "repository_name": "repositoryName",
        "role_cloud_formation_default": "roleCloudFormationDefault",
        "role_event_bridge_default": "roleEventBridgeDefault",
        "role_pipeline_full_clone": "rolePipelineFullClone",
        "stack_name": "stackName",
    },
)
class CfnDefaultModulePropsParameters:
    def __init__(
        self,
        *,
        branch_name: typing.Optional[typing.Union["CfnDefaultModulePropsParametersBranchName", typing.Dict[builtins.str, typing.Any]]] = None,
        bucket_artifact_store: typing.Optional[typing.Union["CfnDefaultModulePropsParametersBucketArtifactStore", typing.Dict[builtins.str, typing.Any]]] = None,
        build_project: typing.Optional[typing.Union["CfnDefaultModulePropsParametersBuildProject", typing.Dict[builtins.str, typing.Any]]] = None,
        repository_name: typing.Optional[typing.Union["CfnDefaultModulePropsParametersRepositoryName", typing.Dict[builtins.str, typing.Any]]] = None,
        role_cloud_formation_default: typing.Optional[typing.Union["CfnDefaultModulePropsParametersRoleCloudFormationDefault", typing.Dict[builtins.str, typing.Any]]] = None,
        role_event_bridge_default: typing.Optional[typing.Union["CfnDefaultModulePropsParametersRoleEventBridgeDefault", typing.Dict[builtins.str, typing.Any]]] = None,
        role_pipeline_full_clone: typing.Optional[typing.Union["CfnDefaultModulePropsParametersRolePipelineFullClone", typing.Dict[builtins.str, typing.Any]]] = None,
        stack_name: typing.Optional[typing.Union["CfnDefaultModulePropsParametersStackName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param branch_name: Rama del repositorio.
        :param bucket_artifact_store: Bucket default en la region us-east-1 para mavi.
        :param build_project: Nombre del build a usar.
        :param repository_name: Repositorio para el pipeline.
        :param role_cloud_formation_default: Rol que inbest nos creo para cloudFormation.
        :param role_event_bridge_default: Rol que detona el inicio del pipeline.
        :param role_pipeline_full_clone: Rol que permite tener un full clone de codecommit (para poder realizar release automatico).
        :param stack_name: Nombre del stack que se usara en cloudFormation.

        :schema: CfnDefaultModulePropsParameters
        '''
        if isinstance(branch_name, dict):
            branch_name = CfnDefaultModulePropsParametersBranchName(**branch_name)
        if isinstance(bucket_artifact_store, dict):
            bucket_artifact_store = CfnDefaultModulePropsParametersBucketArtifactStore(**bucket_artifact_store)
        if isinstance(build_project, dict):
            build_project = CfnDefaultModulePropsParametersBuildProject(**build_project)
        if isinstance(repository_name, dict):
            repository_name = CfnDefaultModulePropsParametersRepositoryName(**repository_name)
        if isinstance(role_cloud_formation_default, dict):
            role_cloud_formation_default = CfnDefaultModulePropsParametersRoleCloudFormationDefault(**role_cloud_formation_default)
        if isinstance(role_event_bridge_default, dict):
            role_event_bridge_default = CfnDefaultModulePropsParametersRoleEventBridgeDefault(**role_event_bridge_default)
        if isinstance(role_pipeline_full_clone, dict):
            role_pipeline_full_clone = CfnDefaultModulePropsParametersRolePipelineFullClone(**role_pipeline_full_clone)
        if isinstance(stack_name, dict):
            stack_name = CfnDefaultModulePropsParametersStackName(**stack_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02baba08f7ffa224380ce9ea87d0723f63ffa28ae83704924d3fc087dbe38f34)
            check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
            check_type(argname="argument bucket_artifact_store", value=bucket_artifact_store, expected_type=type_hints["bucket_artifact_store"])
            check_type(argname="argument build_project", value=build_project, expected_type=type_hints["build_project"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument role_cloud_formation_default", value=role_cloud_formation_default, expected_type=type_hints["role_cloud_formation_default"])
            check_type(argname="argument role_event_bridge_default", value=role_event_bridge_default, expected_type=type_hints["role_event_bridge_default"])
            check_type(argname="argument role_pipeline_full_clone", value=role_pipeline_full_clone, expected_type=type_hints["role_pipeline_full_clone"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if branch_name is not None:
            self._values["branch_name"] = branch_name
        if bucket_artifact_store is not None:
            self._values["bucket_artifact_store"] = bucket_artifact_store
        if build_project is not None:
            self._values["build_project"] = build_project
        if repository_name is not None:
            self._values["repository_name"] = repository_name
        if role_cloud_formation_default is not None:
            self._values["role_cloud_formation_default"] = role_cloud_formation_default
        if role_event_bridge_default is not None:
            self._values["role_event_bridge_default"] = role_event_bridge_default
        if role_pipeline_full_clone is not None:
            self._values["role_pipeline_full_clone"] = role_pipeline_full_clone
        if stack_name is not None:
            self._values["stack_name"] = stack_name

    @builtins.property
    def branch_name(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsParametersBranchName"]:
        '''Rama del repositorio.

        :schema: CfnDefaultModulePropsParameters#BranchName
        '''
        result = self._values.get("branch_name")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersBranchName"], result)

    @builtins.property
    def bucket_artifact_store(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsParametersBucketArtifactStore"]:
        '''Bucket default en la region us-east-1 para mavi.

        :schema: CfnDefaultModulePropsParameters#BucketArtifactStore
        '''
        result = self._values.get("bucket_artifact_store")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersBucketArtifactStore"], result)

    @builtins.property
    def build_project(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsParametersBuildProject"]:
        '''Nombre del build a usar.

        :schema: CfnDefaultModulePropsParameters#BuildProject
        '''
        result = self._values.get("build_project")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersBuildProject"], result)

    @builtins.property
    def repository_name(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsParametersRepositoryName"]:
        '''Repositorio para el pipeline.

        :schema: CfnDefaultModulePropsParameters#RepositoryName
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersRepositoryName"], result)

    @builtins.property
    def role_cloud_formation_default(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsParametersRoleCloudFormationDefault"]:
        '''Rol que inbest nos creo para cloudFormation.

        :schema: CfnDefaultModulePropsParameters#RoleCloudFormationDefault
        '''
        result = self._values.get("role_cloud_formation_default")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersRoleCloudFormationDefault"], result)

    @builtins.property
    def role_event_bridge_default(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsParametersRoleEventBridgeDefault"]:
        '''Rol que detona el inicio del pipeline.

        :schema: CfnDefaultModulePropsParameters#RoleEventBridgeDefault
        '''
        result = self._values.get("role_event_bridge_default")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersRoleEventBridgeDefault"], result)

    @builtins.property
    def role_pipeline_full_clone(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsParametersRolePipelineFullClone"]:
        '''Rol que permite tener un full clone de codecommit (para poder realizar release automatico).

        :schema: CfnDefaultModulePropsParameters#RolePipelineFullClone
        '''
        result = self._values.get("role_pipeline_full_clone")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersRolePipelineFullClone"], result)

    @builtins.property
    def stack_name(self) -> typing.Optional["CfnDefaultModulePropsParametersStackName"]:
        '''Nombre del stack que se usara en cloudFormation.

        :schema: CfnDefaultModulePropsParameters#StackName
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional["CfnDefaultModulePropsParametersStackName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersBranchName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersBranchName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Rama del repositorio.

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersBranchName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a1508d14a097d13be657d0e7db40e48e4a28eaa0669528bb48de3fc9785c451)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersBranchName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersBranchName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersBranchName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersBucketArtifactStore",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersBucketArtifactStore:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Bucket default en la region us-east-1 para mavi.

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersBucketArtifactStore
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f9c38248339f1c4c01caaeef4417484150e573823fe6c91bee89ee13d0c4c6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersBucketArtifactStore#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersBucketArtifactStore#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersBucketArtifactStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersBuildProject",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersBuildProject:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Nombre del build a usar.

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersBuildProject
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822899e0e06b7592581ec83a24e4217efea1f202b23431fe70b5bd876e15ef08)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersBuildProject#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersBuildProject#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersBuildProject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersRepositoryName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersRepositoryName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Repositorio para el pipeline.

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersRepositoryName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__183c81eb1ad0add6166e86eed7ba2a2d08f219de4eb1ff35f638cf503b3e5b71)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRepositoryName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRepositoryName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersRepositoryName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersRoleCloudFormationDefault",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersRoleCloudFormationDefault:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Rol que inbest nos creo para cloudFormation.

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersRoleCloudFormationDefault
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a178a6c4cfdbf5040c7b8c88e5c7e672e277774ecfa394ab6dd109259ed8ae)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRoleCloudFormationDefault#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRoleCloudFormationDefault#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersRoleCloudFormationDefault(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersRoleEventBridgeDefault",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersRoleEventBridgeDefault:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Rol que detona el inicio del pipeline.

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersRoleEventBridgeDefault
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdd454d781497f9215757598a3741683cbe6211c1610579341f69ccbc13a7f75)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRoleEventBridgeDefault#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRoleEventBridgeDefault#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersRoleEventBridgeDefault(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersRolePipelineFullClone",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersRolePipelineFullClone:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Rol que permite tener un full clone de codecommit (para poder realizar release automatico).

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersRolePipelineFullClone
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74609a4567fae3b98a30f8ac2ec8ad8bf14258569295989572b8690811366550)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRolePipelineFullClone#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersRolePipelineFullClone#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersRolePipelineFullClone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsParametersStackName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDefaultModulePropsParametersStackName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Nombre del stack que se usara en cloudFormation.

        :param description: 
        :param type: 

        :schema: CfnDefaultModulePropsParametersStackName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6f348df4bb876f2dcd82dd333656a2f1d501ac18415b1cf167587d1b2f50f9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersStackName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDefaultModulePropsParametersStackName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsParametersStackName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"aws_event_rule": "awsEventRule", "aws_pipeline": "awsPipeline"},
)
class CfnDefaultModulePropsResources:
    def __init__(
        self,
        *,
        aws_event_rule: typing.Optional[typing.Union["CfnDefaultModulePropsResourcesAwsEventRule", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_pipeline: typing.Optional[typing.Union["CfnDefaultModulePropsResourcesAwsPipeline", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_event_rule: 
        :param aws_pipeline: 

        :schema: CfnDefaultModulePropsResources
        '''
        if isinstance(aws_event_rule, dict):
            aws_event_rule = CfnDefaultModulePropsResourcesAwsEventRule(**aws_event_rule)
        if isinstance(aws_pipeline, dict):
            aws_pipeline = CfnDefaultModulePropsResourcesAwsPipeline(**aws_pipeline)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__761849bc9c1ba36313bd4f7dc413833fab57378ef02dc7d61a211d4e61e9ef47)
            check_type(argname="argument aws_event_rule", value=aws_event_rule, expected_type=type_hints["aws_event_rule"])
            check_type(argname="argument aws_pipeline", value=aws_pipeline, expected_type=type_hints["aws_pipeline"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_event_rule is not None:
            self._values["aws_event_rule"] = aws_event_rule
        if aws_pipeline is not None:
            self._values["aws_pipeline"] = aws_pipeline

    @builtins.property
    def aws_event_rule(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsResourcesAwsEventRule"]:
        '''
        :schema: CfnDefaultModulePropsResources#AwsEventRule
        '''
        result = self._values.get("aws_event_rule")
        return typing.cast(typing.Optional["CfnDefaultModulePropsResourcesAwsEventRule"], result)

    @builtins.property
    def aws_pipeline(
        self,
    ) -> typing.Optional["CfnDefaultModulePropsResourcesAwsPipeline"]:
        '''
        :schema: CfnDefaultModulePropsResources#AwsPipeline
        '''
        result = self._values.get("aws_pipeline")
        return typing.cast(typing.Optional["CfnDefaultModulePropsResourcesAwsPipeline"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsResourcesAwsEventRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDefaultModulePropsResourcesAwsEventRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDefaultModulePropsResourcesAwsEventRule
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__692ca158822e4d4386cab759f895198840245922df820c576b77b338a14b3d63)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnDefaultModulePropsResourcesAwsEventRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDefaultModulePropsResourcesAwsEventRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsResourcesAwsEventRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mavi-pipeline-default-module.CfnDefaultModulePropsResourcesAwsPipeline",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDefaultModulePropsResourcesAwsPipeline:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDefaultModulePropsResourcesAwsPipeline
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b21e49783d9819144a1b4bb51b477cc613775433bc3e91fe8d62a42fa303185)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnDefaultModulePropsResourcesAwsPipeline#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDefaultModulePropsResourcesAwsPipeline#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDefaultModulePropsResourcesAwsPipeline(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDefaultModule",
    "CfnDefaultModuleProps",
    "CfnDefaultModulePropsParameters",
    "CfnDefaultModulePropsParametersBranchName",
    "CfnDefaultModulePropsParametersBucketArtifactStore",
    "CfnDefaultModulePropsParametersBuildProject",
    "CfnDefaultModulePropsParametersRepositoryName",
    "CfnDefaultModulePropsParametersRoleCloudFormationDefault",
    "CfnDefaultModulePropsParametersRoleEventBridgeDefault",
    "CfnDefaultModulePropsParametersRolePipelineFullClone",
    "CfnDefaultModulePropsParametersStackName",
    "CfnDefaultModulePropsResources",
    "CfnDefaultModulePropsResourcesAwsEventRule",
    "CfnDefaultModulePropsResourcesAwsPipeline",
]

publication.publish()

def _typecheckingstub__8661d854e7e2f80918a2cc08b2d7704967c7188c9fa034e24ff501d2ff605e10(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnDefaultModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnDefaultModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d65405b5d693f1d82d6adc2c1be93f1bd853606b94e1d191595055cf6207a1c(
    *,
    parameters: typing.Optional[typing.Union[CfnDefaultModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnDefaultModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02baba08f7ffa224380ce9ea87d0723f63ffa28ae83704924d3fc087dbe38f34(
    *,
    branch_name: typing.Optional[typing.Union[CfnDefaultModulePropsParametersBranchName, typing.Dict[builtins.str, typing.Any]]] = None,
    bucket_artifact_store: typing.Optional[typing.Union[CfnDefaultModulePropsParametersBucketArtifactStore, typing.Dict[builtins.str, typing.Any]]] = None,
    build_project: typing.Optional[typing.Union[CfnDefaultModulePropsParametersBuildProject, typing.Dict[builtins.str, typing.Any]]] = None,
    repository_name: typing.Optional[typing.Union[CfnDefaultModulePropsParametersRepositoryName, typing.Dict[builtins.str, typing.Any]]] = None,
    role_cloud_formation_default: typing.Optional[typing.Union[CfnDefaultModulePropsParametersRoleCloudFormationDefault, typing.Dict[builtins.str, typing.Any]]] = None,
    role_event_bridge_default: typing.Optional[typing.Union[CfnDefaultModulePropsParametersRoleEventBridgeDefault, typing.Dict[builtins.str, typing.Any]]] = None,
    role_pipeline_full_clone: typing.Optional[typing.Union[CfnDefaultModulePropsParametersRolePipelineFullClone, typing.Dict[builtins.str, typing.Any]]] = None,
    stack_name: typing.Optional[typing.Union[CfnDefaultModulePropsParametersStackName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a1508d14a097d13be657d0e7db40e48e4a28eaa0669528bb48de3fc9785c451(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f9c38248339f1c4c01caaeef4417484150e573823fe6c91bee89ee13d0c4c6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822899e0e06b7592581ec83a24e4217efea1f202b23431fe70b5bd876e15ef08(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__183c81eb1ad0add6166e86eed7ba2a2d08f219de4eb1ff35f638cf503b3e5b71(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a178a6c4cfdbf5040c7b8c88e5c7e672e277774ecfa394ab6dd109259ed8ae(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdd454d781497f9215757598a3741683cbe6211c1610579341f69ccbc13a7f75(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74609a4567fae3b98a30f8ac2ec8ad8bf14258569295989572b8690811366550(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6f348df4bb876f2dcd82dd333656a2f1d501ac18415b1cf167587d1b2f50f9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__761849bc9c1ba36313bd4f7dc413833fab57378ef02dc7d61a211d4e61e9ef47(
    *,
    aws_event_rule: typing.Optional[typing.Union[CfnDefaultModulePropsResourcesAwsEventRule, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_pipeline: typing.Optional[typing.Union[CfnDefaultModulePropsResourcesAwsPipeline, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__692ca158822e4d4386cab759f895198840245922df820c576b77b338a14b3d63(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b21e49783d9819144a1b4bb51b477cc613775433bc3e91fe8d62a42fa303185(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
