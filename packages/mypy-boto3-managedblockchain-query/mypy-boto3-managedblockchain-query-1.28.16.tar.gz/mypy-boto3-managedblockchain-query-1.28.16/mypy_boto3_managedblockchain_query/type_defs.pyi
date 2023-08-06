"""
Type annotations for managedblockchain-query service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/type_defs/)

Usage::

    ```python
    from mypy_boto3_managedblockchain_query.type_defs import BlockchainInstantOutputTypeDef

    data: BlockchainInstantOutputTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ErrorTypeType,
    QueryNetworkType,
    QueryTransactionEventTypeType,
    QueryTransactionStatusType,
    SortOrderType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BlockchainInstantOutputTypeDef",
    "OwnerIdentifierTypeDef",
    "TokenIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "GetTransactionInputRequestTypeDef",
    "TransactionTypeDef",
    "OwnerFilterTypeDef",
    "PaginatorConfigTypeDef",
    "TokenFilterTypeDef",
    "ListTransactionEventsInputRequestTypeDef",
    "TransactionEventTypeDef",
    "ListTransactionsSortTypeDef",
    "TransactionOutputItemTypeDef",
    "BatchGetTokenBalanceErrorItemTypeDef",
    "BatchGetTokenBalanceOutputItemTypeDef",
    "TokenBalanceTypeDef",
    "GetTokenBalanceOutputTypeDef",
    "BlockchainInstantTypeDef",
    "GetTransactionOutputTypeDef",
    "ListTransactionEventsInputListTransactionEventsPaginateTypeDef",
    "ListTokenBalancesInputListTokenBalancesPaginateTypeDef",
    "ListTokenBalancesInputRequestTypeDef",
    "ListTransactionEventsOutputTypeDef",
    "ListTransactionsOutputTypeDef",
    "BatchGetTokenBalanceOutputTypeDef",
    "ListTokenBalancesOutputTypeDef",
    "BatchGetTokenBalanceInputItemTypeDef",
    "BlockchainInstantUnionTypeDef",
    "GetTokenBalanceInputRequestTypeDef",
    "ListTransactionsInputListTransactionsPaginateTypeDef",
    "ListTransactionsInputRequestTypeDef",
    "BatchGetTokenBalanceInputRequestTypeDef",
)

BlockchainInstantOutputTypeDef = TypedDict(
    "BlockchainInstantOutputTypeDef",
    {
        "time": datetime,
    },
    total=False,
)

OwnerIdentifierTypeDef = TypedDict(
    "OwnerIdentifierTypeDef",
    {
        "address": str,
    },
)

_RequiredTokenIdentifierTypeDef = TypedDict(
    "_RequiredTokenIdentifierTypeDef",
    {
        "network": QueryNetworkType,
    },
)
_OptionalTokenIdentifierTypeDef = TypedDict(
    "_OptionalTokenIdentifierTypeDef",
    {
        "contractAddress": str,
        "tokenId": str,
    },
    total=False,
)

class TokenIdentifierTypeDef(_RequiredTokenIdentifierTypeDef, _OptionalTokenIdentifierTypeDef):
    pass

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

TimestampTypeDef = Union[datetime, str]
GetTransactionInputRequestTypeDef = TypedDict(
    "GetTransactionInputRequestTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
    },
)

_RequiredTransactionTypeDef = TypedDict(
    "_RequiredTransactionTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "transactionTimestamp": datetime,
        "transactionIndex": int,
        "numberOfTransactions": int,
        "status": QueryTransactionStatusType,
        "to": str,
    },
)
_OptionalTransactionTypeDef = TypedDict(
    "_OptionalTransactionTypeDef",
    {
        "blockHash": str,
        "blockNumber": str,
        "from": str,
        "contractAddress": str,
        "gasUsed": str,
        "cumulativeGasUsed": str,
        "effectiveGasPrice": str,
        "signatureV": int,
        "signatureR": str,
        "signatureS": str,
        "transactionFee": str,
        "transactionId": str,
    },
    total=False,
)

class TransactionTypeDef(_RequiredTransactionTypeDef, _OptionalTransactionTypeDef):
    pass

OwnerFilterTypeDef = TypedDict(
    "OwnerFilterTypeDef",
    {
        "address": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredTokenFilterTypeDef = TypedDict(
    "_RequiredTokenFilterTypeDef",
    {
        "network": QueryNetworkType,
    },
)
_OptionalTokenFilterTypeDef = TypedDict(
    "_OptionalTokenFilterTypeDef",
    {
        "contractAddress": str,
        "tokenId": str,
    },
    total=False,
)

class TokenFilterTypeDef(_RequiredTokenFilterTypeDef, _OptionalTokenFilterTypeDef):
    pass

_RequiredListTransactionEventsInputRequestTypeDef = TypedDict(
    "_RequiredListTransactionEventsInputRequestTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
    },
)
_OptionalListTransactionEventsInputRequestTypeDef = TypedDict(
    "_OptionalListTransactionEventsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTransactionEventsInputRequestTypeDef(
    _RequiredListTransactionEventsInputRequestTypeDef,
    _OptionalListTransactionEventsInputRequestTypeDef,
):
    pass

_RequiredTransactionEventTypeDef = TypedDict(
    "_RequiredTransactionEventTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "eventType": QueryTransactionEventTypeType,
    },
)
_OptionalTransactionEventTypeDef = TypedDict(
    "_OptionalTransactionEventTypeDef",
    {
        "from": str,
        "to": str,
        "value": str,
        "contractAddress": str,
        "tokenId": str,
        "transactionId": str,
        "voutIndex": int,
    },
    total=False,
)

class TransactionEventTypeDef(_RequiredTransactionEventTypeDef, _OptionalTransactionEventTypeDef):
    pass

ListTransactionsSortTypeDef = TypedDict(
    "ListTransactionsSortTypeDef",
    {
        "sortBy": Literal["TRANSACTION_TIMESTAMP"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

TransactionOutputItemTypeDef = TypedDict(
    "TransactionOutputItemTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
        "transactionTimestamp": datetime,
    },
)

_RequiredBatchGetTokenBalanceErrorItemTypeDef = TypedDict(
    "_RequiredBatchGetTokenBalanceErrorItemTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "errorType": ErrorTypeType,
    },
)
_OptionalBatchGetTokenBalanceErrorItemTypeDef = TypedDict(
    "_OptionalBatchGetTokenBalanceErrorItemTypeDef",
    {
        "tokenIdentifier": TokenIdentifierTypeDef,
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "atBlockchainInstant": BlockchainInstantOutputTypeDef,
    },
    total=False,
)

class BatchGetTokenBalanceErrorItemTypeDef(
    _RequiredBatchGetTokenBalanceErrorItemTypeDef, _OptionalBatchGetTokenBalanceErrorItemTypeDef
):
    pass

_RequiredBatchGetTokenBalanceOutputItemTypeDef = TypedDict(
    "_RequiredBatchGetTokenBalanceOutputItemTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": BlockchainInstantOutputTypeDef,
    },
)
_OptionalBatchGetTokenBalanceOutputItemTypeDef = TypedDict(
    "_OptionalBatchGetTokenBalanceOutputItemTypeDef",
    {
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "tokenIdentifier": TokenIdentifierTypeDef,
        "lastUpdatedTime": BlockchainInstantOutputTypeDef,
    },
    total=False,
)

class BatchGetTokenBalanceOutputItemTypeDef(
    _RequiredBatchGetTokenBalanceOutputItemTypeDef, _OptionalBatchGetTokenBalanceOutputItemTypeDef
):
    pass

_RequiredTokenBalanceTypeDef = TypedDict(
    "_RequiredTokenBalanceTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": BlockchainInstantOutputTypeDef,
    },
)
_OptionalTokenBalanceTypeDef = TypedDict(
    "_OptionalTokenBalanceTypeDef",
    {
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "tokenIdentifier": TokenIdentifierTypeDef,
        "lastUpdatedTime": BlockchainInstantOutputTypeDef,
    },
    total=False,
)

class TokenBalanceTypeDef(_RequiredTokenBalanceTypeDef, _OptionalTokenBalanceTypeDef):
    pass

GetTokenBalanceOutputTypeDef = TypedDict(
    "GetTokenBalanceOutputTypeDef",
    {
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "tokenIdentifier": TokenIdentifierTypeDef,
        "balance": str,
        "atBlockchainInstant": BlockchainInstantOutputTypeDef,
        "lastUpdatedTime": BlockchainInstantOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BlockchainInstantTypeDef = TypedDict(
    "BlockchainInstantTypeDef",
    {
        "time": TimestampTypeDef,
    },
    total=False,
)

GetTransactionOutputTypeDef = TypedDict(
    "GetTransactionOutputTypeDef",
    {
        "transaction": TransactionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListTransactionEventsInputListTransactionEventsPaginateTypeDef = TypedDict(
    "_RequiredListTransactionEventsInputListTransactionEventsPaginateTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
    },
)
_OptionalListTransactionEventsInputListTransactionEventsPaginateTypeDef = TypedDict(
    "_OptionalListTransactionEventsInputListTransactionEventsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListTransactionEventsInputListTransactionEventsPaginateTypeDef(
    _RequiredListTransactionEventsInputListTransactionEventsPaginateTypeDef,
    _OptionalListTransactionEventsInputListTransactionEventsPaginateTypeDef,
):
    pass

_RequiredListTokenBalancesInputListTokenBalancesPaginateTypeDef = TypedDict(
    "_RequiredListTokenBalancesInputListTokenBalancesPaginateTypeDef",
    {
        "tokenFilter": TokenFilterTypeDef,
    },
)
_OptionalListTokenBalancesInputListTokenBalancesPaginateTypeDef = TypedDict(
    "_OptionalListTokenBalancesInputListTokenBalancesPaginateTypeDef",
    {
        "ownerFilter": OwnerFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListTokenBalancesInputListTokenBalancesPaginateTypeDef(
    _RequiredListTokenBalancesInputListTokenBalancesPaginateTypeDef,
    _OptionalListTokenBalancesInputListTokenBalancesPaginateTypeDef,
):
    pass

_RequiredListTokenBalancesInputRequestTypeDef = TypedDict(
    "_RequiredListTokenBalancesInputRequestTypeDef",
    {
        "tokenFilter": TokenFilterTypeDef,
    },
)
_OptionalListTokenBalancesInputRequestTypeDef = TypedDict(
    "_OptionalListTokenBalancesInputRequestTypeDef",
    {
        "ownerFilter": OwnerFilterTypeDef,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTokenBalancesInputRequestTypeDef(
    _RequiredListTokenBalancesInputRequestTypeDef, _OptionalListTokenBalancesInputRequestTypeDef
):
    pass

ListTransactionEventsOutputTypeDef = TypedDict(
    "ListTransactionEventsOutputTypeDef",
    {
        "events": List[TransactionEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTransactionsOutputTypeDef = TypedDict(
    "ListTransactionsOutputTypeDef",
    {
        "transactions": List[TransactionOutputItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchGetTokenBalanceOutputTypeDef = TypedDict(
    "BatchGetTokenBalanceOutputTypeDef",
    {
        "tokenBalances": List[BatchGetTokenBalanceOutputItemTypeDef],
        "errors": List[BatchGetTokenBalanceErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTokenBalancesOutputTypeDef = TypedDict(
    "ListTokenBalancesOutputTypeDef",
    {
        "tokenBalances": List[TokenBalanceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBatchGetTokenBalanceInputItemTypeDef = TypedDict(
    "_RequiredBatchGetTokenBalanceInputItemTypeDef",
    {
        "tokenIdentifier": TokenIdentifierTypeDef,
        "ownerIdentifier": OwnerIdentifierTypeDef,
    },
)
_OptionalBatchGetTokenBalanceInputItemTypeDef = TypedDict(
    "_OptionalBatchGetTokenBalanceInputItemTypeDef",
    {
        "atBlockchainInstant": BlockchainInstantTypeDef,
    },
    total=False,
)

class BatchGetTokenBalanceInputItemTypeDef(
    _RequiredBatchGetTokenBalanceInputItemTypeDef, _OptionalBatchGetTokenBalanceInputItemTypeDef
):
    pass

BlockchainInstantUnionTypeDef = Union[BlockchainInstantTypeDef, BlockchainInstantOutputTypeDef]
_RequiredGetTokenBalanceInputRequestTypeDef = TypedDict(
    "_RequiredGetTokenBalanceInputRequestTypeDef",
    {
        "tokenIdentifier": TokenIdentifierTypeDef,
        "ownerIdentifier": OwnerIdentifierTypeDef,
    },
)
_OptionalGetTokenBalanceInputRequestTypeDef = TypedDict(
    "_OptionalGetTokenBalanceInputRequestTypeDef",
    {
        "atBlockchainInstant": BlockchainInstantTypeDef,
    },
    total=False,
)

class GetTokenBalanceInputRequestTypeDef(
    _RequiredGetTokenBalanceInputRequestTypeDef, _OptionalGetTokenBalanceInputRequestTypeDef
):
    pass

_RequiredListTransactionsInputListTransactionsPaginateTypeDef = TypedDict(
    "_RequiredListTransactionsInputListTransactionsPaginateTypeDef",
    {
        "address": str,
        "network": QueryNetworkType,
    },
)
_OptionalListTransactionsInputListTransactionsPaginateTypeDef = TypedDict(
    "_OptionalListTransactionsInputListTransactionsPaginateTypeDef",
    {
        "fromBlockchainInstant": BlockchainInstantTypeDef,
        "toBlockchainInstant": BlockchainInstantTypeDef,
        "sort": ListTransactionsSortTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListTransactionsInputListTransactionsPaginateTypeDef(
    _RequiredListTransactionsInputListTransactionsPaginateTypeDef,
    _OptionalListTransactionsInputListTransactionsPaginateTypeDef,
):
    pass

_RequiredListTransactionsInputRequestTypeDef = TypedDict(
    "_RequiredListTransactionsInputRequestTypeDef",
    {
        "address": str,
        "network": QueryNetworkType,
    },
)
_OptionalListTransactionsInputRequestTypeDef = TypedDict(
    "_OptionalListTransactionsInputRequestTypeDef",
    {
        "fromBlockchainInstant": BlockchainInstantTypeDef,
        "toBlockchainInstant": BlockchainInstantTypeDef,
        "sort": ListTransactionsSortTypeDef,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTransactionsInputRequestTypeDef(
    _RequiredListTransactionsInputRequestTypeDef, _OptionalListTransactionsInputRequestTypeDef
):
    pass

BatchGetTokenBalanceInputRequestTypeDef = TypedDict(
    "BatchGetTokenBalanceInputRequestTypeDef",
    {
        "getTokenBalanceInputs": Sequence[BatchGetTokenBalanceInputItemTypeDef],
    },
    total=False,
)
