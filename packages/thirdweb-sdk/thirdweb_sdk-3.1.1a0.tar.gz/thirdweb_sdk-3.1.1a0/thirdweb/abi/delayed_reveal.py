"""Generated wrapper for DelayedReveal Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for DelayedReveal below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DelayedRevealValidator,
    )
except ImportError:

    class DelayedRevealValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class EncryptDecryptMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the encryptDecrypt method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, data: Union[bytes, str], key: Union[bytes, str]
    ):
        """Validate the inputs to the encryptDecrypt method."""
        self.validator.assert_valid(
            method_name="encryptDecrypt",
            parameter_name="data",
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name="encryptDecrypt",
            parameter_name="key",
            argument_value=key,
        )
        return (data, key)

    def call(
        self,
        data: Union[bytes, str],
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data, key) = self.validate_and_normalize_inputs(data, key)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data, key).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        data: Union[bytes, str],
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data, key) = self.validate_and_normalize_inputs(data, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, key).transact(tx_params.as_dict())

    def build_transaction(
        self,
        data: Union[bytes, str],
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data, key) = self.validate_and_normalize_inputs(data, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, key).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        data: Union[bytes, str],
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (data, key) = self.validate_and_normalize_inputs(data, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, key).estimateGas(
            tx_params.as_dict()
        )


class EncryptedDataMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the encryptedData method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the encryptedData method."""
        self.validator.assert_valid(
            method_name="encryptedData",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class GetRevealUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRevealURI method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, batch_id: int, key: Union[bytes, str]
    ):
        """Validate the inputs to the getRevealURI method."""
        self.validator.assert_valid(
            method_name="getRevealURI",
            parameter_name="_batchId",
            argument_value=batch_id,
        )
        # safeguard against fractional inputs
        batch_id = int(batch_id)
        self.validator.assert_valid(
            method_name="getRevealURI",
            parameter_name="_key",
            argument_value=key,
        )
        return (batch_id, key)

    def call(
        self,
        batch_id: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (batch_id, key) = self.validate_and_normalize_inputs(batch_id, key)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(batch_id, key).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        batch_id: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (batch_id, key) = self.validate_and_normalize_inputs(batch_id, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(batch_id, key).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        batch_id: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (batch_id, key) = self.validate_and_normalize_inputs(batch_id, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(batch_id, key).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        batch_id: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (batch_id, key) = self.validate_and_normalize_inputs(batch_id, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(batch_id, key).estimateGas(
            tx_params.as_dict()
        )


class IsEncryptedBatchMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isEncryptedBatch method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, batch_id: int):
        """Validate the inputs to the isEncryptedBatch method."""
        self.validator.assert_valid(
            method_name="isEncryptedBatch",
            parameter_name="_batchId",
            argument_value=batch_id,
        )
        # safeguard against fractional inputs
        batch_id = int(batch_id)
        return batch_id

    def call(
        self, batch_id: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (batch_id) = self.validate_and_normalize_inputs(batch_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(batch_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, batch_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (batch_id) = self.validate_and_normalize_inputs(batch_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(batch_id).transact(tx_params.as_dict())

    def build_transaction(
        self, batch_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (batch_id) = self.validate_and_normalize_inputs(batch_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(batch_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, batch_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (batch_id) = self.validate_and_normalize_inputs(batch_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(batch_id).estimateGas(
            tx_params.as_dict()
        )


class RevealMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the reveal method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, identifier: int, key: Union[bytes, str]
    ):
        """Validate the inputs to the reveal method."""
        self.validator.assert_valid(
            method_name="reveal",
            parameter_name="identifier",
            argument_value=identifier,
        )
        # safeguard against fractional inputs
        identifier = int(identifier)
        self.validator.assert_valid(
            method_name="reveal",
            parameter_name="key",
            argument_value=key,
        )
        return (identifier, key)

    def call(
        self,
        identifier: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (identifier, key) = self.validate_and_normalize_inputs(identifier, key)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(identifier, key).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        identifier: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (identifier, key) = self.validate_and_normalize_inputs(identifier, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(identifier, key).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        identifier: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (identifier, key) = self.validate_and_normalize_inputs(identifier, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(identifier, key).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        identifier: int,
        key: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (identifier, key) = self.validate_and_normalize_inputs(identifier, key)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(identifier, key).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DelayedReveal:
    """Wrapper class for DelayedReveal Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    encrypt_decrypt: EncryptDecryptMethod
    """Constructor-initialized instance of
    :class:`EncryptDecryptMethod`.
    """

    encrypted_data: EncryptedDataMethod
    """Constructor-initialized instance of
    :class:`EncryptedDataMethod`.
    """

    get_reveal_uri: GetRevealUriMethod
    """Constructor-initialized instance of
    :class:`GetRevealUriMethod`.
    """

    is_encrypted_batch: IsEncryptedBatchMethod
    """Constructor-initialized instance of
    :class:`IsEncryptedBatchMethod`.
    """

    reveal: RevealMethod
    """Constructor-initialized instance of
    :class:`RevealMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DelayedRevealValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = DelayedRevealValidator(
                web3_or_provider, contract_address
            )

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware["function"],
                        layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=DelayedReveal.abi(),
        ).functions

        self.encrypt_decrypt = EncryptDecryptMethod(
            web3_or_provider,
            contract_address,
            functions.encryptDecrypt,
            validator,
        )

        self.encrypted_data = EncryptedDataMethod(
            web3_or_provider,
            contract_address,
            functions.encryptedData,
            validator,
        )

        self.get_reveal_uri = GetRevealUriMethod(
            web3_or_provider,
            contract_address,
            functions.getRevealURI,
            validator,
        )

        self.is_encrypted_batch = IsEncryptedBatchMethod(
            web3_or_provider,
            contract_address,
            functions.isEncryptedBatch,
            validator,
        )

        self.reveal = RevealMethod(
            web3_or_provider, contract_address, functions.reveal, validator
        )

    def get_token_uri_revealed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokenURIRevealed event.

        :param tx_hash: hash of transaction emitting TokenURIRevealed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DelayedReveal.abi(),
            )
            .events.TokenURIRevealed()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"index","type":"uint256"},{"indexed":false,"internalType":"string","name":"revealedURI","type":"string"}],"name":"TokenURIRevealed","type":"event"},{"inputs":[{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"bytes","name":"key","type":"bytes"}],"name":"encryptDecrypt","outputs":[{"internalType":"bytes","name":"result","type":"bytes"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"encryptedData","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_batchId","type":"uint256"},{"internalType":"bytes","name":"_key","type":"bytes"}],"name":"getRevealURI","outputs":[{"internalType":"string","name":"revealedURI","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_batchId","type":"uint256"}],"name":"isEncryptedBatch","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"identifier","type":"uint256"},{"internalType":"bytes","name":"key","type":"bytes"}],"name":"reveal","outputs":[{"internalType":"string","name":"revealedURI","type":"string"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
