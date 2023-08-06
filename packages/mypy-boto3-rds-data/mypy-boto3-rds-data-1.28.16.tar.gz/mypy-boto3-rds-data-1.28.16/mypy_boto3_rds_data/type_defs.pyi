"""
Type annotations for rds-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_rds_data.type_defs import ArrayValueOutputTypeDef

    data: ArrayValueOutputTypeDef = ...
    ```
"""
import sys
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import DecimalReturnTypeType, LongReturnTypeType, RecordsFormatTypeType, TypeHintType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArrayValueOutputTypeDef",
    "ArrayValueTypeDef",
    "ResponseMetadataTypeDef",
    "BeginTransactionRequestRequestTypeDef",
    "BlobTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "ExecuteSqlRequestRequestTypeDef",
    "ResultSetOptionsTypeDef",
    "FieldOutputTypeDef",
    "RecordTypeDef",
    "RollbackTransactionRequestRequestTypeDef",
    "StructValueTypeDef",
    "ValueTypeDef",
    "BeginTransactionResponseTypeDef",
    "CommitTransactionResponseTypeDef",
    "RollbackTransactionResponseTypeDef",
    "FieldTypeDef",
    "ResultSetMetadataTypeDef",
    "ExecuteStatementResponseTypeDef",
    "UpdateResultTypeDef",
    "SqlParameterTypeDef",
    "ResultFrameTypeDef",
    "BatchExecuteStatementResponseTypeDef",
    "BatchExecuteStatementRequestRequestTypeDef",
    "ExecuteStatementRequestRequestTypeDef",
    "SqlStatementResultTypeDef",
    "ExecuteSqlResponseTypeDef",
)

ArrayValueOutputTypeDef = TypedDict(
    "ArrayValueOutputTypeDef",
    {
        "booleanValues": List[bool],
        "longValues": List[int],
        "doubleValues": List[float],
        "stringValues": List[str],
        "arrayValues": List[Dict[str, Any]],
    },
    total=False,
)

ArrayValueTypeDef = TypedDict(
    "ArrayValueTypeDef",
    {
        "booleanValues": Sequence[bool],
        "longValues": Sequence[int],
        "doubleValues": Sequence[float],
        "stringValues": Sequence[str],
        "arrayValues": Sequence[Dict[str, Any]],
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

_RequiredBeginTransactionRequestRequestTypeDef = TypedDict(
    "_RequiredBeginTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
    },
)
_OptionalBeginTransactionRequestRequestTypeDef = TypedDict(
    "_OptionalBeginTransactionRequestRequestTypeDef",
    {
        "database": str,
        "schema": str,
    },
    total=False,
)

class BeginTransactionRequestRequestTypeDef(
    _RequiredBeginTransactionRequestRequestTypeDef, _OptionalBeginTransactionRequestRequestTypeDef
):
    pass

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": str,
        "type": int,
        "typeName": str,
        "label": str,
        "schemaName": str,
        "tableName": str,
        "isAutoIncrement": bool,
        "isSigned": bool,
        "isCurrency": bool,
        "isCaseSensitive": bool,
        "nullable": int,
        "precision": int,
        "scale": int,
        "arrayBaseColumnType": int,
    },
    total=False,
)

CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

_RequiredExecuteSqlRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteSqlRequestRequestTypeDef",
    {
        "dbClusterOrInstanceArn": str,
        "awsSecretStoreArn": str,
        "sqlStatements": str,
    },
)
_OptionalExecuteSqlRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteSqlRequestRequestTypeDef",
    {
        "database": str,
        "schema": str,
    },
    total=False,
)

class ExecuteSqlRequestRequestTypeDef(
    _RequiredExecuteSqlRequestRequestTypeDef, _OptionalExecuteSqlRequestRequestTypeDef
):
    pass

ResultSetOptionsTypeDef = TypedDict(
    "ResultSetOptionsTypeDef",
    {
        "decimalReturnType": DecimalReturnTypeType,
        "longReturnType": LongReturnTypeType,
    },
    total=False,
)

FieldOutputTypeDef = TypedDict(
    "FieldOutputTypeDef",
    {
        "isNull": bool,
        "booleanValue": bool,
        "longValue": int,
        "doubleValue": float,
        "stringValue": str,
        "blobValue": bytes,
        "arrayValue": "ArrayValueOutputTypeDef",
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "values": List["ValueTypeDef"],
    },
    total=False,
)

RollbackTransactionRequestRequestTypeDef = TypedDict(
    "RollbackTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

StructValueTypeDef = TypedDict(
    "StructValueTypeDef",
    {
        "attributes": List[Dict[str, Any]],
    },
    total=False,
)

ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "isNull": bool,
        "bitValue": bool,
        "bigIntValue": int,
        "intValue": int,
        "doubleValue": float,
        "realValue": float,
        "stringValue": str,
        "blobValue": bytes,
        "arrayValues": List[Dict[str, Any]],
        "structValue": Dict[str, Any],
    },
    total=False,
)

BeginTransactionResponseTypeDef = TypedDict(
    "BeginTransactionResponseTypeDef",
    {
        "transactionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RollbackTransactionResponseTypeDef = TypedDict(
    "RollbackTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "isNull": bool,
        "booleanValue": bool,
        "longValue": int,
        "doubleValue": float,
        "stringValue": str,
        "blobValue": BlobTypeDef,
        "arrayValue": "ArrayValueTypeDef",
    },
    total=False,
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "columnCount": int,
        "columnMetadata": List[ColumnMetadataTypeDef],
    },
    total=False,
)

ExecuteStatementResponseTypeDef = TypedDict(
    "ExecuteStatementResponseTypeDef",
    {
        "records": List[List[FieldOutputTypeDef]],
        "columnMetadata": List[ColumnMetadataTypeDef],
        "numberOfRecordsUpdated": int,
        "generatedFields": List[FieldOutputTypeDef],
        "formattedRecords": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "generatedFields": List[FieldOutputTypeDef],
    },
    total=False,
)

SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": str,
        "value": FieldTypeDef,
        "typeHint": TypeHintType,
    },
    total=False,
)

ResultFrameTypeDef = TypedDict(
    "ResultFrameTypeDef",
    {
        "resultSetMetadata": ResultSetMetadataTypeDef,
        "records": List[RecordTypeDef],
    },
    total=False,
)

BatchExecuteStatementResponseTypeDef = TypedDict(
    "BatchExecuteStatementResponseTypeDef",
    {
        "updateResults": List[UpdateResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBatchExecuteStatementRequestRequestTypeDef = TypedDict(
    "_RequiredBatchExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
    },
)
_OptionalBatchExecuteStatementRequestRequestTypeDef = TypedDict(
    "_OptionalBatchExecuteStatementRequestRequestTypeDef",
    {
        "database": str,
        "schema": str,
        "parameterSets": Sequence[Sequence[SqlParameterTypeDef]],
        "transactionId": str,
    },
    total=False,
)

class BatchExecuteStatementRequestRequestTypeDef(
    _RequiredBatchExecuteStatementRequestRequestTypeDef,
    _OptionalBatchExecuteStatementRequestRequestTypeDef,
):
    pass

_RequiredExecuteStatementRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
    },
)
_OptionalExecuteStatementRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementRequestRequestTypeDef",
    {
        "database": str,
        "schema": str,
        "parameters": Sequence[SqlParameterTypeDef],
        "transactionId": str,
        "includeResultMetadata": bool,
        "continueAfterTimeout": bool,
        "resultSetOptions": ResultSetOptionsTypeDef,
        "formatRecordsAs": RecordsFormatTypeType,
    },
    total=False,
)

class ExecuteStatementRequestRequestTypeDef(
    _RequiredExecuteStatementRequestRequestTypeDef, _OptionalExecuteStatementRequestRequestTypeDef
):
    pass

SqlStatementResultTypeDef = TypedDict(
    "SqlStatementResultTypeDef",
    {
        "resultFrame": ResultFrameTypeDef,
        "numberOfRecordsUpdated": int,
    },
    total=False,
)

ExecuteSqlResponseTypeDef = TypedDict(
    "ExecuteSqlResponseTypeDef",
    {
        "sqlStatementResults": List[SqlStatementResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
