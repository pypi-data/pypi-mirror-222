'''
# cadiaz-bucket-uno-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Cadiaz::Bucket::Uno::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Cadiaz::Bucket::Uno::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Cadiaz::Bucket::Uno::MODULE \
  --publisher-id c812060033ed3bad51a82f3aa9ad5ef18ea8ed0d \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/c812060033ed3bad51a82f3aa9ad5ef18ea8ed0d/Cadiaz-Bucket-Uno-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Cadiaz::Bucket::Uno::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fcadiaz-bucket-uno-module+v1.0.0).
* Issues related to `Cadiaz::Bucket::Uno::MODULE` should be reported to the [publisher](undefined).

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


class CfnUnoModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/cadiaz-bucket-uno-module.CfnUnoModule",
):
    '''A CloudFormation ``Cadiaz::Bucket::Uno::MODULE``.

    :cloudformationResource: Cadiaz::Bucket::Uno::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnUnoModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnUnoModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Cadiaz::Bucket::Uno::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a9af4de95ff3730e8d888760178140ae0f3e96fc2ad04bcca6a2cb7392b1ce)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUnoModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUnoModuleProps":
        '''Resource props.'''
        return typing.cast("CfnUnoModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/cadiaz-bucket-uno-module.CfnUnoModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnUnoModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnUnoModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnUnoModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type Cadiaz::Bucket::Uno::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnUnoModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnUnoModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnUnoModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c24dd707afe528882e2bd96a82eae964c79bfbbe9cfe8432e64bbea3fa6773)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnUnoModulePropsParameters"]:
        '''
        :schema: CfnUnoModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnUnoModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnUnoModulePropsResources"]:
        '''
        :schema: CfnUnoModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnUnoModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUnoModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/cadiaz-bucket-uno-module.CfnUnoModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"bucket_custom_name": "bucketCustomName"},
)
class CfnUnoModulePropsParameters:
    def __init__(
        self,
        *,
        bucket_custom_name: typing.Optional[typing.Union["CfnUnoModulePropsParametersBucketCustomName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_custom_name: Name for the bucket.

        :schema: CfnUnoModulePropsParameters
        '''
        if isinstance(bucket_custom_name, dict):
            bucket_custom_name = CfnUnoModulePropsParametersBucketCustomName(**bucket_custom_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b00fab427ecbba9f93792d160f544e48d415f353a547b0a59e44b4f8a81782)
            check_type(argname="argument bucket_custom_name", value=bucket_custom_name, expected_type=type_hints["bucket_custom_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_custom_name is not None:
            self._values["bucket_custom_name"] = bucket_custom_name

    @builtins.property
    def bucket_custom_name(
        self,
    ) -> typing.Optional["CfnUnoModulePropsParametersBucketCustomName"]:
        '''Name for the bucket.

        :schema: CfnUnoModulePropsParameters#BucketCustomName
        '''
        result = self._values.get("bucket_custom_name")
        return typing.cast(typing.Optional["CfnUnoModulePropsParametersBucketCustomName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUnoModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/cadiaz-bucket-uno-module.CfnUnoModulePropsParametersBucketCustomName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnUnoModulePropsParametersBucketCustomName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name for the bucket.

        :param description: 
        :param type: 

        :schema: CfnUnoModulePropsParametersBucketCustomName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4a1e9ef2332dbd08f8cd9b4bba4e5269e49854cc45c0566debf0d61411cd28c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnUnoModulePropsParametersBucketCustomName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnUnoModulePropsParametersBucketCustomName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUnoModulePropsParametersBucketCustomName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/cadiaz-bucket-uno-module.CfnUnoModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"s3_bucket": "s3Bucket"},
)
class CfnUnoModulePropsResources:
    def __init__(
        self,
        *,
        s3_bucket: typing.Optional[typing.Union["CfnUnoModulePropsResourcesS3Bucket", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_bucket: 

        :schema: CfnUnoModulePropsResources
        '''
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnUnoModulePropsResourcesS3Bucket(**s3_bucket)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4a349be452e4e8784aeb07332a31ef855308d7154238da60957f1e514ba3c6a)
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnUnoModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnUnoModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnUnoModulePropsResourcesS3Bucket"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUnoModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/cadiaz-bucket-uno-module.CfnUnoModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnUnoModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnUnoModulePropsResourcesS3Bucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3079977264cbe439a7283287a8d821a2cff8dc20aeaa6e151609362fab876c)
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
        :schema: CfnUnoModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUnoModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUnoModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnUnoModule",
    "CfnUnoModuleProps",
    "CfnUnoModulePropsParameters",
    "CfnUnoModulePropsParametersBucketCustomName",
    "CfnUnoModulePropsResources",
    "CfnUnoModulePropsResourcesS3Bucket",
]

publication.publish()

def _typecheckingstub__70a9af4de95ff3730e8d888760178140ae0f3e96fc2ad04bcca6a2cb7392b1ce(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnUnoModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnUnoModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c24dd707afe528882e2bd96a82eae964c79bfbbe9cfe8432e64bbea3fa6773(
    *,
    parameters: typing.Optional[typing.Union[CfnUnoModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnUnoModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b00fab427ecbba9f93792d160f544e48d415f353a547b0a59e44b4f8a81782(
    *,
    bucket_custom_name: typing.Optional[typing.Union[CfnUnoModulePropsParametersBucketCustomName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a1e9ef2332dbd08f8cd9b4bba4e5269e49854cc45c0566debf0d61411cd28c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a349be452e4e8784aeb07332a31ef855308d7154238da60957f1e514ba3c6a(
    *,
    s3_bucket: typing.Optional[typing.Union[CfnUnoModulePropsResourcesS3Bucket, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3079977264cbe439a7283287a8d821a2cff8dc20aeaa6e151609362fab876c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
