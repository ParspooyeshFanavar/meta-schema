from typing import TypedDict
from typing import Optional
from enum import Enum
from typing import NewType
from typing import Any
from typing import List
from typing import Mapping
from typing import Union

class Openrpc(Enum):
    1.2.6 = 0
    1.2.5 = 1
    1.2.4 = 2
    1.2.3 = 3
    1.2.2 = 4
    1.2.1 = 5
    1.2.0 = 6
    1.1.12 = 7
    1.1.11 = 8
    1.1.10 = 9
    1.1.9 = 10
    1.1.8 = 11
    1.1.7 = 12
    1.1.6 = 13
    1.1.5 = 14
    1.1.4 = 15
    1.1.3 = 16
    1.1.2 = 17
    1.1.1 = 18
    1.1.0 = 19
    1.0.0 = 20
    1.0.0-RC1 = 21
    1.0.0-RC0 = 22

InfoObjectProperties = NewType("InfoObjectProperties", str)

InfoObjectDescription = NewType("InfoObjectDescription", str)

InfoObjectTermsOfService = NewType("InfoObjectTermsOfService", str)

InfoObjectVersion = NewType("InfoObjectVersion", str)

ContactObjectName = NewType("ContactObjectName", str)

ContactObjectEmail = NewType("ContactObjectEmail", str)

ContactObjectUrl = NewType("ContactObjectUrl", str)

AnyL9Fw4VUO = NewType("AnyL9Fw4VUO", Any)

class ContactObject(TypedDict):
    name: Optional[ContactObjectName]
    email: Optional[ContactObjectEmail]
    url: Optional[ContactObjectUrl]

LicenseObjectName = NewType("LicenseObjectName", str)

LicenseObjectUrl = NewType("LicenseObjectUrl", str)

class LicenseObject(TypedDict):
    name: Optional[LicenseObjectName]
    url: Optional[LicenseObjectUrl]

class InfoObject(TypedDict):
    title: Optional[InfoObjectProperties]
    description: Optional[InfoObjectDescription]
    termsOfService: Optional[InfoObjectTermsOfService]
    version: Optional[InfoObjectVersion]
    contact: Optional[ContactObject]
    license: Optional[LicenseObject]

ExternalDocumentationObjectDescription = NewType("ExternalDocumentationObjectDescription", str)

ExternalDocumentationObjectUrl = NewType("ExternalDocumentationObjectUrl", str)
"""information about external documentation
"""
class ExternalDocumentationObject(TypedDict):
    description: Optional[ExternalDocumentationObjectDescription]
    url: Optional[ExternalDocumentationObjectUrl]

ServerObjectUrl = NewType("ServerObjectUrl", str)

ServerObjectName = NewType("ServerObjectName", str)

ServerObjectDescription = NewType("ServerObjectDescription", str)

ServerObjectSummary = NewType("ServerObjectSummary", str)

ServerObjectVariableDefault = NewType("ServerObjectVariableDefault", str)

ServerObjectVariableDescription = NewType("ServerObjectVariableDescription", str)

ServerObjectVariableEnumItem = NewType("ServerObjectVariableEnumItem", str)

ServerObjectVariableEnum = NewType("ServerObjectVariableEnum", List[ServerObjectVariableEnumItem])

class ServerObjectVariable(TypedDict):
    default: Optional[ServerObjectVariableDefault]
    description: Optional[ServerObjectVariableDescription]
    enum: Optional[ServerObjectVariableEnum]

ServerObjectVariables = NewType("ServerObjectVariables", Mapping[Any, Any])

class ServerObject(TypedDict):
    url: Optional[ServerObjectUrl]
    name: Optional[ServerObjectName]
    description: Optional[ServerObjectDescription]
    summary: Optional[ServerObjectSummary]
    variables: Optional[ServerObjectVariables]

Servers = NewType("Servers", List[ServerObject])
"""The cannonical name for the method. The name MUST be unique within the methods array.
"""
MethodObjectName = NewType("MethodObjectName", str)
"""A verbose explanation of the method behavior. GitHub Flavored Markdown syntax MAY be used for rich text representation.
"""
MethodObjectDescription = NewType("MethodObjectDescription", str)
"""A short summary of what the method does.
"""
MethodObjectSummary = NewType("MethodObjectSummary", str)

TagObjectName = NewType("TagObjectName", str)

TagObjectDescription = NewType("TagObjectDescription", str)

class TagObject(TypedDict):
    name: Optional[TagObjectName]
    description: Optional[TagObjectDescription]
    externalDocs: Optional[ExternalDocumentationObject]

$Id = NewType("$Id", str)

$Schema = NewType("$Schema", str)

$Ref = NewType("$Ref", str)

$Comment = NewType("$Comment", str)

Title = NewType("Title", str)

Description = NewType("Description", str)
AlwaysTrue = NewType("AlwaysTrue", Any)

ReadOnly = NewType("ReadOnly", bool)

Examples = NewType("Examples", List[AlwaysTrue])

MultipleOf = NewType("MultipleOf", float)

Maximum = NewType("Maximum", float)

ExclusiveMaximum = NewType("ExclusiveMaximum", float)

Minimum = NewType("Minimum", float)

ExclusiveMinimum = NewType("ExclusiveMinimum", float)

NonNegativeInteger = NewType("NonNegativeInteger", int)

DefaultZero = NewType("DefaultZero", Any)

NonNegativeIntegerDefaultZero = NewType("NonNegativeIntegerDefaultZero", Mapping[Any, Any])

Pattern = NewType("Pattern", str)

SchemaArray = NewType("SchemaArray", List[JSONSchema])

Items = NewType("Items", Union[JSONSchema, SchemaArray])

UniqueItems = NewType("UniqueItems", bool)

StringDoaGddGA = NewType("StringDoaGddGA", str)

StringArray = NewType("StringArray", List[StringDoaGddGA])

Definitions = NewType("Definitions", Mapping[Any, Any])

Properties = NewType("Properties", Mapping[Any, Any])

PatternProperties = NewType("PatternProperties", Mapping[Any, Any])

DependenciesSet = NewType("DependenciesSet", Union[JSONSchema, StringArray])

Dependencies = NewType("Dependencies", Mapping[Any, Any])

Enum = NewType("Enum", List[AlwaysTrue])

SimpleTypes = NewType("SimpleTypes", Any)

ArrayOfSimpleTypes = NewType("ArrayOfSimpleTypes", List[SimpleTypes])

Type = NewType("Type", Union[SimpleTypes, ArrayOfSimpleTypes])

Format = NewType("Format", str)

ContentMediaType = NewType("ContentMediaType", str)

ContentEncoding = NewType("ContentEncoding", str)

class JSONSchemaObject(TypedDict):
    $id: Optional[$Id]
    $schema: Optional[$Schema]
    $ref: Optional[$Ref]
    $comment: Optional[$Comment]
    title: Optional[Title]
    description: Optional[Description]
    default: Optional[AlwaysTrue]
    readOnly: Optional[ReadOnly]
    examples: Optional[Examples]
    multipleOf: Optional[MultipleOf]
    maximum: Optional[Maximum]
    exclusiveMaximum: Optional[ExclusiveMaximum]
    minimum: Optional[Minimum]
    exclusiveMinimum: Optional[ExclusiveMinimum]
    maxLength: Optional[NonNegativeInteger]
    minLength: Optional[NonNegativeIntegerDefaultZero]
    pattern: Optional[Pattern]
    additionalItems: Optional[JSONSchema]
    items: Optional[Items]
    maxItems: Optional[NonNegativeInteger]
    minItems: Optional[NonNegativeIntegerDefaultZero]
    uniqueItems: Optional[UniqueItems]
    contains: Optional[JSONSchema]
    maxProperties: Optional[NonNegativeInteger]
    minProperties: Optional[NonNegativeIntegerDefaultZero]
    required: Optional[StringArray]
    additionalProperties: Optional[JSONSchema]
    definitions: Optional[Definitions]
    properties: Optional[Properties]
    patternProperties: Optional[PatternProperties]
    dependencies: Optional[Dependencies]
    propertyNames: Optional[JSONSchema]
    const: Optional[AlwaysTrue]
    enum: Optional[Enum]
    type: Optional[Type]
    format: Optional[Format]
    contentMediaType: Optional[ContentMediaType]
    contentEncoding: Optional[ContentEncoding]
    if: Optional[JSONSchema]
    then: Optional[JSONSchema]
    else: Optional[JSONSchema]
    allOf: Optional[SchemaArray]
    anyOf: Optional[SchemaArray]
    oneOf: Optional[SchemaArray]
    not: Optional[JSONSchema]
"""Always valid if true. Never valid if false. Is constant.
"""
JSONSchemaBoolean = NewType("JSONSchemaBoolean", bool)

JSONSchema = NewType("JSONSchema", Union[JSONSchemaObject, JSONSchemaBoolean])

class ReferenceObject(TypedDict):
    $ref: Optional[JSONSchema]

OneOfReferenceObjectTagObjectMTCfXRqB = NewType("OneOfReferenceObjectTagObjectMTCfXRqB", Union[TagObject, ReferenceObject])

MethodObjectTags = NewType("MethodObjectTags", List[OneOfReferenceObjectTagObjectMTCfXRqB])
"""Format the server expects the params. Defaults to 'either'.
"""
class MethodObjectParamStructure(Enum):
    BY-POSITION = 0
    BY-NAME = 1
    EITHER = 2

ContentDescriptorObjectName = NewType("ContentDescriptorObjectName", str)

ContentDescriptorObjectDescription = NewType("ContentDescriptorObjectDescription", str)

ContentDescriptorObjectSummary = NewType("ContentDescriptorObjectSummary", str)

ContentDescriptorObjectRequired = NewType("ContentDescriptorObjectRequired", bool)

ContentDescriptorObjectDeprecated = NewType("ContentDescriptorObjectDeprecated", bool)

class ContentDescriptorObject(TypedDict):
    name: Optional[ContentDescriptorObjectName]
    description: Optional[ContentDescriptorObjectDescription]
    summary: Optional[ContentDescriptorObjectSummary]
    schema: Optional[JSONSchema]
    required: Optional[ContentDescriptorObjectRequired]
    deprecated: Optional[ContentDescriptorObjectDeprecated]

OneOfContentDescriptorObjectReferenceObjectI0Ye8PrQ = NewType("OneOfContentDescriptorObjectReferenceObjectI0Ye8PrQ", Union[ContentDescriptorObject, ReferenceObject])

MethodObjectParams = NewType("MethodObjectParams", List[OneOfContentDescriptorObjectReferenceObjectI0Ye8PrQ])

MethodObjectResult = NewType("MethodObjectResult", Union[ContentDescriptorObject, ReferenceObject])
"""A Number that indicates the error type that occurred. This MUST be an integer. The error codes from and including -32768 to -32000 are reserved for pre-defined errors. These pre-defined errors SHOULD be assumed to be returned from any JSON-RPC api.
"""
ErrorObjectCode = NewType("ErrorObjectCode", int)
"""A String providing a short description of the error. The message SHOULD be limited to a concise single sentence.
"""
ErrorObjectMessage = NewType("ErrorObjectMessage", str)
"""A Primitive or Structured value that contains additional information about the error. This may be omitted. The value of this member is defined by the Server (e.g. detailed error information, nested errors etc.).
"""
ErrorObjectData = NewType("ErrorObjectData", Any)
"""Defines an application level error.
"""
class ErrorObject(TypedDict):
    code: Optional[ErrorObjectCode]
    message: Optional[ErrorObjectMessage]
    data: Optional[ErrorObjectData]

OneOfErrorObjectReferenceObject1KnseVEO = NewType("OneOfErrorObjectReferenceObject1KnseVEO", Union[ErrorObject, ReferenceObject])
"""Defines an application level error.
"""
MethodObjectErrors = NewType("MethodObjectErrors", List[OneOfErrorObjectReferenceObject1KnseVEO])

LinkObjectName = NewType("LinkObjectName", str)

LinkObjectSummary = NewType("LinkObjectSummary", str)

LinkObjectMethod = NewType("LinkObjectMethod", str)

LinkObjectDescription = NewType("LinkObjectDescription", str)

LinkObjectParams = NewType("LinkObjectParams", Any)

class LinkObject(TypedDict):
    name: Optional[LinkObjectName]
    summary: Optional[LinkObjectSummary]
    method: Optional[LinkObjectMethod]
    description: Optional[LinkObjectDescription]
    params: Optional[LinkObjectParams]
    server: Optional[ServerObject]

OneOfLinkObjectReferenceObjectXyKfUxb0 = NewType("OneOfLinkObjectReferenceObjectXyKfUxb0", Union[LinkObject, ReferenceObject])

MethodObjectLinks = NewType("MethodObjectLinks", List[OneOfLinkObjectReferenceObjectXyKfUxb0])

ExamplePairingObjectName = NewType("ExamplePairingObjectName", str)

ExamplePairingObjectDescription = NewType("ExamplePairingObjectDescription", str)

ExampleObjectSummary = NewType("ExampleObjectSummary", str)

ExampleObjectValue = NewType("ExampleObjectValue", Any)

ExampleObjectDescription = NewType("ExampleObjectDescription", str)

ExampleObjectName = NewType("ExampleObjectName", str)

class ExampleObject(TypedDict):
    summary: Optional[ExampleObjectSummary]
    value: Optional[ExampleObjectValue]
    description: Optional[ExampleObjectDescription]
    name: Optional[ExampleObjectName]

OneOfExampleObjectReferenceObject5DJ6EmZt = NewType("OneOfExampleObjectReferenceObject5DJ6EmZt", Union[ExampleObject, ReferenceObject])

ExamplePairingObjectParams = NewType("ExamplePairingObjectParams", List[OneOfExampleObjectReferenceObject5DJ6EmZt])

ExamplePairingObjectresult = NewType("ExamplePairingObjectresult", Union[ExampleObject, ReferenceObject])

class ExamplePairingObject(TypedDict):
    name: Optional[ExamplePairingObjectName]
    description: Optional[ExamplePairingObjectDescription]
    params: Optional[ExamplePairingObjectParams]
    result: Optional[ExamplePairingObjectresult]

OneOfExamplePairingObjectReferenceObjectWEBfRSyK = NewType("OneOfExamplePairingObjectReferenceObjectWEBfRSyK", Union[ExamplePairingObject, ReferenceObject])

MethodObjectExamples = NewType("MethodObjectExamples", List[OneOfExamplePairingObjectReferenceObjectWEBfRSyK])

MethodObjectDeprecated = NewType("MethodObjectDeprecated", bool)

class MethodObject(TypedDict):
    name: Optional[MethodObjectName]
    description: Optional[MethodObjectDescription]
    summary: Optional[MethodObjectSummary]
    servers: Optional[Servers]
    tags: Optional[MethodObjectTags]
    paramStructure: Optional[MethodObjectParamStructure]
    params: Optional[MethodObjectParams]
    result: Optional[MethodObjectResult]
    errors: Optional[MethodObjectErrors]
    links: Optional[MethodObjectLinks]
    examples: Optional[MethodObjectExamples]
    deprecated: Optional[MethodObjectDeprecated]
    externalDocs: Optional[ExternalDocumentationObject]

Methods = NewType("Methods", List[MethodObject])

SchemaComponents = NewType("SchemaComponents", Mapping[Any, Any])

LinkComponents = NewType("LinkComponents", Mapping[Any, Any])

ObjectTfFA84LI = NewType("ObjectTfFA84LI", Mapping[Any, Any])

ExampleComponents = NewType("ExampleComponents", Mapping[Any, Any])

ExamplePairingComponents = NewType("ExamplePairingComponents", Mapping[Any, Any])

ContentDescriptorComponents = NewType("ContentDescriptorComponents", Mapping[Any, Any])

TagComponents = NewType("TagComponents", Mapping[Any, Any])

class Components(TypedDict):
    schemas: Optional[SchemaComponents]
    links: Optional[LinkComponents]
    errors: Optional[ObjectTfFA84LI]
    examples: Optional[ExampleComponents]
    examplePairings: Optional[ExamplePairingComponents]
    contentDescriptors: Optional[ContentDescriptorComponents]
    tags: Optional[TagComponents]

class OpenrpcDocument(TypedDict):
    openrpc: undefined
    info: Optional[InfoObject]
    externalDocs: Optional[ExternalDocumentationObject]
    servers: Optional[Servers]
    methods: undefined
    components: Optional[Components]