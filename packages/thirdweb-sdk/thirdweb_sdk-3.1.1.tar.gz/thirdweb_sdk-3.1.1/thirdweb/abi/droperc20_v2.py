"""Generated wrapper for DropERC20_V2 Solidity contract."""

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
# constructor for DropERC20_V2 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DropERC20_V2Validator,
    )
except ImportError:

    class DropERC20_V2Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IDropClaimCondition_V2ClaimCondition(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    startTimestamp: int

    maxClaimableSupply: int

    supplyClaimed: int

    quantityLimitPerTransaction: int

    waitTimeInSecondsBetweenClaims: int

    merkleRoot: Union[bytes, str]

    pricePerToken: int

    currency: str


class ERC20VotesUpgradeableCheckpoint(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    fromBlock: int

    votes: int


class DefaultAdminRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the DEFAULT_ADMIN_ROLE method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class DomainSeparatorMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the DOMAIN_SEPARATOR method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class AllowanceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the allowance method."""

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

    def validate_and_normalize_inputs(self, owner: str, spender: str):
        """Validate the inputs to the allowance method."""
        self.validator.assert_valid(
            method_name="allowance",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="allowance",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        return (owner, spender)

    def call(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, spender).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).estimateGas(
            tx_params.as_dict()
        )


class ApproveMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the approve method."""

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

    def validate_and_normalize_inputs(self, spender: str, amount: int):
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (spender, amount)

    def call(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(spender, amount).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).estimateGas(
            tx_params.as_dict()
        )


class BalanceOfMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the balanceOf method."""

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

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class BurnMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burn method."""

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

    def validate_and_normalize_inputs(self, amount: int):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return amount

    def call(self, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(amount).call(tx_params.as_dict())

    def send_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).transact(tx_params.as_dict())

    def build_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).estimateGas(tx_params.as_dict())


class BurnFromMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burnFrom method."""

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

    def validate_and_normalize_inputs(self, account: str, amount: int):
        """Validate the inputs to the burnFrom method."""
        self.validator.assert_valid(
            method_name="burnFrom",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="burnFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (account, amount)

    def call(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, amount).call(tx_params.as_dict())

    def send_transaction(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).estimateGas(
            tx_params.as_dict()
        )


class CheckpointsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the checkpoints method."""

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

    def validate_and_normalize_inputs(self, account: str, pos: int):
        """Validate the inputs to the checkpoints method."""
        self.validator.assert_valid(
            method_name="checkpoints",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="checkpoints",
            parameter_name="pos",
            argument_value=pos,
        )
        return (account, pos)

    def call(
        self, account: str, pos: int, tx_params: Optional[TxParams] = None
    ) -> ERC20VotesUpgradeableCheckpoint:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, pos) = self.validate_and_normalize_inputs(account, pos)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, pos).call(
            tx_params.as_dict()
        )
        return ERC20VotesUpgradeableCheckpoint(
            fromBlock=returned[0],
            votes=returned[1],
        )

    def send_transaction(
        self, account: str, pos: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, pos) = self.validate_and_normalize_inputs(account, pos)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, pos).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, account: str, pos: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, pos) = self.validate_and_normalize_inputs(account, pos)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, pos).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, pos: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, pos) = self.validate_and_normalize_inputs(account, pos)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, pos).estimateGas(
            tx_params.as_dict()
        )


class ClaimMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the claim method."""

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
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
    ):
        """Validate the inputs to the claim method."""
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="_receiver",
            argument_value=receiver,
        )
        receiver = self.validate_and_checksum_address(receiver)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="_pricePerToken",
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="_proofs",
            argument_value=proofs,
        )
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="_proofMaxQuantityPerTransaction",
            argument_value=proof_max_quantity_per_transaction,
        )
        # safeguard against fractional inputs
        proof_max_quantity_per_transaction = int(
            proof_max_quantity_per_transaction
        )
        return (
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )

    def call(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).estimateGas(tx_params.as_dict())


class ClaimConditionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the claimCondition method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class ContractTypeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractType method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class ContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractURI method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class ContractVersionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractVersion method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class DecimalsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the decimals method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class DecreaseAllowanceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the decreaseAllowance method."""

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
        self, spender: str, subtracted_value: int
    ):
        """Validate the inputs to the decreaseAllowance method."""
        self.validator.assert_valid(
            method_name="decreaseAllowance",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name="decreaseAllowance",
            parameter_name="subtractedValue",
            argument_value=subtracted_value,
        )
        # safeguard against fractional inputs
        subtracted_value = int(subtracted_value)
        return (spender, subtracted_value)

    def call(
        self,
        spender: str,
        subtracted_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (spender, subtracted_value) = self.validate_and_normalize_inputs(
            spender, subtracted_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(spender, subtracted_value).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        spender: str,
        subtracted_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, subtracted_value) = self.validate_and_normalize_inputs(
            spender, subtracted_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, subtracted_value).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        spender: str,
        subtracted_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, subtracted_value) = self.validate_and_normalize_inputs(
            spender, subtracted_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            spender, subtracted_value
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        spender: str,
        subtracted_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (spender, subtracted_value) = self.validate_and_normalize_inputs(
            spender, subtracted_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, subtracted_value).estimateGas(
            tx_params.as_dict()
        )


class DelegateMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the delegate method."""

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

    def validate_and_normalize_inputs(self, delegatee: str):
        """Validate the inputs to the delegate method."""
        self.validator.assert_valid(
            method_name="delegate",
            parameter_name="delegatee",
            argument_value=delegatee,
        )
        delegatee = self.validate_and_checksum_address(delegatee)
        return delegatee

    def call(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(delegatee).call(tx_params.as_dict())

    def send_transaction(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(delegatee).transact(tx_params.as_dict())

    def build_transaction(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(delegatee).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(delegatee).estimateGas(
            tx_params.as_dict()
        )


class DelegateBySigMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the delegateBySig method."""

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
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
    ):
        """Validate the inputs to the delegateBySig method."""
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="delegatee",
            argument_value=delegatee,
        )
        delegatee = self.validate_and_checksum_address(delegatee)
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="nonce",
            argument_value=nonce,
        )
        # safeguard against fractional inputs
        nonce = int(nonce)
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="expiry",
            argument_value=expiry,
        )
        # safeguard against fractional inputs
        expiry = int(expiry)
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="v",
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="r",
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="s",
            argument_value=s,
        )
        return (delegatee, nonce, expiry, v, r, s)

    def call(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(delegatee, nonce, expiry, v, r, s).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            delegatee, nonce, expiry, v, r, s
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            delegatee, nonce, expiry, v, r, s
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            delegatee, nonce, expiry, v, r, s
        ).estimateGas(tx_params.as_dict())


class DelegatesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the delegates method."""

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

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the delegates method."""
        self.validator.assert_valid(
            method_name="delegates",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class GetActiveClaimConditionIdMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getActiveClaimConditionId method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GetClaimConditionByIdMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getClaimConditionById method."""

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

    def validate_and_normalize_inputs(self, condition_id: int):
        """Validate the inputs to the getClaimConditionById method."""
        self.validator.assert_valid(
            method_name="getClaimConditionById",
            parameter_name="_conditionId",
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        return condition_id

    def call(
        self, condition_id: int, tx_params: Optional[TxParams] = None
    ) -> IDropClaimCondition_V2ClaimCondition:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (condition_id) = self.validate_and_normalize_inputs(condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(condition_id).call(
            tx_params.as_dict()
        )
        return IDropClaimCondition_V2ClaimCondition(
            startTimestamp=returned[0],
            maxClaimableSupply=returned[1],
            supplyClaimed=returned[2],
            quantityLimitPerTransaction=returned[3],
            waitTimeInSecondsBetweenClaims=returned[4],
            merkleRoot=returned[5],
            pricePerToken=returned[6],
            currency=returned[7],
        )

    def send_transaction(
        self, condition_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (condition_id) = self.validate_and_normalize_inputs(condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, condition_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (condition_id) = self.validate_and_normalize_inputs(condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, condition_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (condition_id) = self.validate_and_normalize_inputs(condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id).estimateGas(
            tx_params.as_dict()
        )


class GetClaimTimestampMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getClaimTimestamp method."""

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

    def validate_and_normalize_inputs(self, condition_id: int, claimer: str):
        """Validate the inputs to the getClaimTimestamp method."""
        self.validator.assert_valid(
            method_name="getClaimTimestamp",
            parameter_name="_conditionId",
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        self.validator.assert_valid(
            method_name="getClaimTimestamp",
            parameter_name="_claimer",
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        return (condition_id, claimer)

    def call(
        self,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (condition_id, claimer) = self.validate_and_normalize_inputs(
            condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(condition_id, claimer).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (condition_id, claimer) = self.validate_and_normalize_inputs(
            condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (condition_id, claimer) = self.validate_and_normalize_inputs(
            condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (condition_id, claimer) = self.validate_and_normalize_inputs(
            condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer).estimateGas(
            tx_params.as_dict()
        )


class GetPastTotalSupplyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getPastTotalSupply method."""

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

    def validate_and_normalize_inputs(self, block_number: int):
        """Validate the inputs to the getPastTotalSupply method."""
        self.validator.assert_valid(
            method_name="getPastTotalSupply",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        return block_number

    def call(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(block_number).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).estimateGas(
            tx_params.as_dict()
        )


class GetPastVotesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getPastVotes method."""

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

    def validate_and_normalize_inputs(self, account: str, block_number: int):
        """Validate the inputs to the getPastVotes method."""
        self.validator.assert_valid(
            method_name="getPastVotes",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="getPastVotes",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        return (account, block_number)

    def call(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, block_number).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).estimateGas(
            tx_params.as_dict()
        )


class GetPlatformFeeInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getPlatformFeeInfo method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GetRoleAdminMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleAdmin method."""

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

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleAdmin method."""
        self.validator.assert_valid(
            method_name="getRoleAdmin",
            parameter_name="role",
            argument_value=role,
        )
        return role

    def call(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())


class GetRoleMemberMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleMember method."""

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
        self, role: Union[bytes, str], index: int
    ):
        """Validate the inputs to the getRoleMember method."""
        self.validator.assert_valid(
            method_name="getRoleMember",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="getRoleMember",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (role, index)

    def call(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, index).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).estimateGas(
            tx_params.as_dict()
        )


class GetRoleMemberCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleMemberCount method."""

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

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleMemberCount method."""
        self.validator.assert_valid(
            method_name="getRoleMemberCount",
            parameter_name="role",
            argument_value=role,
        )
        return role

    def call(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())


class GetVotesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getVotes method."""

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

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the getVotes method."""
        self.validator.assert_valid(
            method_name="getVotes",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class GrantRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the grantRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the grantRole method."""
        self.validator.assert_valid(
            method_name="grantRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="grantRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class HasRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the hasRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the hasRole method."""
        self.validator.assert_valid(
            method_name="hasRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="hasRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, account).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class IncreaseAllowanceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the increaseAllowance method."""

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

    def validate_and_normalize_inputs(self, spender: str, added_value: int):
        """Validate the inputs to the increaseAllowance method."""
        self.validator.assert_valid(
            method_name="increaseAllowance",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name="increaseAllowance",
            parameter_name="addedValue",
            argument_value=added_value,
        )
        # safeguard against fractional inputs
        added_value = int(added_value)
        return (spender, added_value)

    def call(
        self,
        spender: str,
        added_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (spender, added_value) = self.validate_and_normalize_inputs(
            spender, added_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(spender, added_value).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        spender: str,
        added_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, added_value) = self.validate_and_normalize_inputs(
            spender, added_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, added_value).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        spender: str,
        added_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, added_value) = self.validate_and_normalize_inputs(
            spender, added_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, added_value).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        spender: str,
        added_value: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (spender, added_value) = self.validate_and_normalize_inputs(
            spender, added_value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, added_value).estimateGas(
            tx_params.as_dict()
        )


class InitializeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

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
        self,
        default_admin: str,
        name: str,
        symbol: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        primary_sale_recipient: str,
        platform_fee_recipient: str,
        platform_fee_bps: int,
    ):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_defaultAdmin",
            argument_value=default_admin,
        )
        default_admin = self.validate_and_checksum_address(default_admin)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_name",
            argument_value=name,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_symbol",
            argument_value=symbol,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_contractURI",
            argument_value=contract_uri,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_trustedForwarders",
            argument_value=trusted_forwarders,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_primarySaleRecipient",
            argument_value=primary_sale_recipient,
        )
        primary_sale_recipient = self.validate_and_checksum_address(
            primary_sale_recipient
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_platformFeeRecipient",
            argument_value=platform_fee_recipient,
        )
        platform_fee_recipient = self.validate_and_checksum_address(
            platform_fee_recipient
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_platformFeeBps",
            argument_value=platform_fee_bps,
        )
        # safeguard against fractional inputs
        platform_fee_bps = int(platform_fee_bps)
        return (
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        )

    def call(
        self,
        default_admin: str,
        name: str,
        symbol: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        primary_sale_recipient: str,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        default_admin: str,
        name: str,
        symbol: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        primary_sale_recipient: str,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        default_admin: str,
        name: str,
        symbol: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        primary_sale_recipient: str,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        default_admin: str,
        name: str,
        symbol: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        primary_sale_recipient: str,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_admin,
            name,
            symbol,
            contract_uri,
            trusted_forwarders,
            primary_sale_recipient,
            platform_fee_recipient,
            platform_fee_bps,
        ).estimateGas(tx_params.as_dict())


class IsTrustedForwarderMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isTrustedForwarder method."""

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

    def validate_and_normalize_inputs(self, forwarder: str):
        """Validate the inputs to the isTrustedForwarder method."""
        self.validator.assert_valid(
            method_name="isTrustedForwarder",
            parameter_name="forwarder",
            argument_value=forwarder,
        )
        forwarder = self.validate_and_checksum_address(forwarder)
        return forwarder

    def call(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(forwarder).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).transact(tx_params.as_dict())

    def build_transaction(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).estimateGas(
            tx_params.as_dict()
        )


class MaxTotalSupplyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the maxTotalSupply method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class MaxWalletClaimCountMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the maxWalletClaimCount method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class MulticallMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the multicall method."""

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

    def validate_and_normalize_inputs(self, data: List[Union[bytes, str]]):
        """Validate the inputs to the multicall method."""
        self.validator.assert_valid(
            method_name="multicall",
            parameter_name="data",
            argument_value=data,
        )
        return data

    def call(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())


class NameMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the name method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class NoncesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the nonces method."""

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

    def validate_and_normalize_inputs(self, owner: str):
        """Validate the inputs to the nonces method."""
        self.validator.assert_valid(
            method_name="nonces",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        return owner

    def call(self, owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).transact(tx_params.as_dict())

    def build_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).estimateGas(tx_params.as_dict())


class NumCheckpointsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the numCheckpoints method."""

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

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the numCheckpoints method."""
        self.validator.assert_valid(
            method_name="numCheckpoints",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class PermitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the permit method."""

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
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
    ):
        """Validate the inputs to the permit method."""
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="deadline",
            argument_value=deadline,
        )
        # safeguard against fractional inputs
        deadline = int(deadline)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="v",
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="r",
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="s",
            argument_value=s,
        )
        return (owner, spender, value, deadline, v, r, s)

    def call(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(owner, spender, value, deadline, v, r, s).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            owner, spender, value, deadline, v, r, s
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            owner, spender, value, deadline, v, r, s
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            owner, spender, value, deadline, v, r, s
        ).estimateGas(tx_params.as_dict())


class PrimarySaleRecipientMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the primarySaleRecipient method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class RenounceRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the renounceRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the renounceRole method."""
        self.validator.assert_valid(
            method_name="renounceRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="renounceRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class RevokeRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the revokeRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the revokeRole method."""
        self.validator.assert_valid(
            method_name="revokeRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="revokeRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class SetClaimConditionsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setClaimConditions method."""

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
        self,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
    ):
        """Validate the inputs to the setClaimConditions method."""
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="_phases",
            argument_value=phases,
        )
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="_resetClaimEligibility",
            argument_value=reset_claim_eligibility,
        )
        return (phases, reset_claim_eligibility)

    def call(
        self,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(phases, reset_claim_eligibility).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            phases, reset_claim_eligibility
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            phases, reset_claim_eligibility
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            phases, reset_claim_eligibility
        ).estimateGas(tx_params.as_dict())


class SetContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setContractURI method."""

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

    def validate_and_normalize_inputs(self, uri: str):
        """Validate the inputs to the setContractURI method."""
        self.validator.assert_valid(
            method_name="setContractURI",
            parameter_name="_uri",
            argument_value=uri,
        )
        return uri

    def call(self, uri: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri).call(tx_params.as_dict())

    def send_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).transact(tx_params.as_dict())

    def build_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).estimateGas(tx_params.as_dict())


class SetMaxTotalSupplyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setMaxTotalSupply method."""

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

    def validate_and_normalize_inputs(self, max_total_supply: int):
        """Validate the inputs to the setMaxTotalSupply method."""
        self.validator.assert_valid(
            method_name="setMaxTotalSupply",
            parameter_name="_maxTotalSupply",
            argument_value=max_total_supply,
        )
        # safeguard against fractional inputs
        max_total_supply = int(max_total_supply)
        return max_total_supply

    def call(
        self, max_total_supply: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (max_total_supply) = self.validate_and_normalize_inputs(
            max_total_supply
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(max_total_supply).call(tx_params.as_dict())

    def send_transaction(
        self, max_total_supply: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (max_total_supply) = self.validate_and_normalize_inputs(
            max_total_supply
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(max_total_supply).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, max_total_supply: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (max_total_supply) = self.validate_and_normalize_inputs(
            max_total_supply
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(max_total_supply).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, max_total_supply: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (max_total_supply) = self.validate_and_normalize_inputs(
            max_total_supply
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(max_total_supply).estimateGas(
            tx_params.as_dict()
        )


class SetMaxWalletClaimCountMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setMaxWalletClaimCount method."""

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

    def validate_and_normalize_inputs(self, count: int):
        """Validate the inputs to the setMaxWalletClaimCount method."""
        self.validator.assert_valid(
            method_name="setMaxWalletClaimCount",
            parameter_name="_count",
            argument_value=count,
        )
        # safeguard against fractional inputs
        count = int(count)
        return count

    def call(self, count: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (count) = self.validate_and_normalize_inputs(count)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(count).call(tx_params.as_dict())

    def send_transaction(
        self, count: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (count) = self.validate_and_normalize_inputs(count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(count).transact(tx_params.as_dict())

    def build_transaction(
        self, count: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (count) = self.validate_and_normalize_inputs(count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(count).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, count: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (count) = self.validate_and_normalize_inputs(count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(count).estimateGas(tx_params.as_dict())


class SetPlatformFeeInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setPlatformFeeInfo method."""

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
        self, platform_fee_recipient: str, platform_fee_bps: int
    ):
        """Validate the inputs to the setPlatformFeeInfo method."""
        self.validator.assert_valid(
            method_name="setPlatformFeeInfo",
            parameter_name="_platformFeeRecipient",
            argument_value=platform_fee_recipient,
        )
        platform_fee_recipient = self.validate_and_checksum_address(
            platform_fee_recipient
        )
        self.validator.assert_valid(
            method_name="setPlatformFeeInfo",
            parameter_name="_platformFeeBps",
            argument_value=platform_fee_bps,
        )
        # safeguard against fractional inputs
        platform_fee_bps = int(platform_fee_bps)
        return (platform_fee_recipient, platform_fee_bps)

    def call(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(platform_fee_recipient, platform_fee_bps).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            platform_fee_recipient, platform_fee_bps
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            platform_fee_recipient, platform_fee_bps
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            platform_fee_recipient, platform_fee_bps
        ).estimateGas(tx_params.as_dict())


class SetPrimarySaleRecipientMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setPrimarySaleRecipient method."""

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

    def validate_and_normalize_inputs(self, sale_recipient: str):
        """Validate the inputs to the setPrimarySaleRecipient method."""
        self.validator.assert_valid(
            method_name="setPrimarySaleRecipient",
            parameter_name="_saleRecipient",
            argument_value=sale_recipient,
        )
        sale_recipient = self.validate_and_checksum_address(sale_recipient)
        return sale_recipient

    def call(
        self, sale_recipient: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sale_recipient).call(tx_params.as_dict())

    def send_transaction(
        self, sale_recipient: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sale_recipient).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, sale_recipient: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sale_recipient).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, sale_recipient: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sale_recipient).estimateGas(
            tx_params.as_dict()
        )


class SetWalletClaimCountMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setWalletClaimCount method."""

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

    def validate_and_normalize_inputs(self, claimer: str, count: int):
        """Validate the inputs to the setWalletClaimCount method."""
        self.validator.assert_valid(
            method_name="setWalletClaimCount",
            parameter_name="_claimer",
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        self.validator.assert_valid(
            method_name="setWalletClaimCount",
            parameter_name="_count",
            argument_value=count,
        )
        # safeguard against fractional inputs
        count = int(count)
        return (claimer, count)

    def call(
        self, claimer: str, count: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (claimer, count) = self.validate_and_normalize_inputs(claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(claimer, count).call(tx_params.as_dict())

    def send_transaction(
        self, claimer: str, count: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (claimer, count) = self.validate_and_normalize_inputs(claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(claimer, count).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, claimer: str, count: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (claimer, count) = self.validate_and_normalize_inputs(claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(claimer, count).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, claimer: str, count: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (claimer, count) = self.validate_and_normalize_inputs(claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(claimer, count).estimateGas(
            tx_params.as_dict()
        )


class SupportsInterfaceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the supportsInterface method."""

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

    def validate_and_normalize_inputs(self, interface_id: Union[bytes, str]):
        """Validate the inputs to the supportsInterface method."""
        self.validator.assert_valid(
            method_name="supportsInterface",
            parameter_name="interfaceId",
            argument_value=interface_id,
        )
        return interface_id

    def call(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(interface_id).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).estimateGas(
            tx_params.as_dict()
        )


class SymbolMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the symbol method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class TotalSupplyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalSupply method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class TransferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the transfer method."""

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

    def validate_and_normalize_inputs(self, to: str, amount: int):
        """Validate the inputs to the transfer method."""
        self.validator.assert_valid(
            method_name="transfer",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="transfer",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (to, amount)

    def call(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(to, amount).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).estimateGas(
            tx_params.as_dict()
        )


class TransferFromMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the transferFrom method."""

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

    def validate_and_normalize_inputs(self, _from: str, to: str, amount: int):
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (_from, to, amount)

    def call(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_from, to, amount).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).estimateGas(
            tx_params.as_dict()
        )


class VerifyClaimMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the verifyClaim method."""

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
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        verify_max_quantity_per_transaction: bool,
    ):
        """Validate the inputs to the verifyClaim method."""
        self.validator.assert_valid(
            method_name="verifyClaim",
            parameter_name="_conditionId",
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        self.validator.assert_valid(
            method_name="verifyClaim",
            parameter_name="_claimer",
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        self.validator.assert_valid(
            method_name="verifyClaim",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="verifyClaim",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="verifyClaim",
            parameter_name="_pricePerToken",
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name="verifyClaim",
            parameter_name="verifyMaxQuantityPerTransaction",
            argument_value=verify_max_quantity_per_transaction,
        )
        return (
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        )

    def call(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        verify_max_quantity_per_transaction: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        verify_max_quantity_per_transaction: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        verify_max_quantity_per_transaction: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        verify_max_quantity_per_transaction: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            quantity,
            currency,
            price_per_token,
            verify_max_quantity_per_transaction,
        ).estimateGas(tx_params.as_dict())


class VerifyClaimMerkleProofMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the verifyClaimMerkleProof method."""

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
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
    ):
        """Validate the inputs to the verifyClaimMerkleProof method."""
        self.validator.assert_valid(
            method_name="verifyClaimMerkleProof",
            parameter_name="_conditionId",
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        self.validator.assert_valid(
            method_name="verifyClaimMerkleProof",
            parameter_name="_claimer",
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        self.validator.assert_valid(
            method_name="verifyClaimMerkleProof",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="verifyClaimMerkleProof",
            parameter_name="_proofs",
            argument_value=proofs,
        )
        self.validator.assert_valid(
            method_name="verifyClaimMerkleProof",
            parameter_name="_proofMaxQuantityPerTransaction",
            argument_value=proof_max_quantity_per_transaction,
        )
        # safeguard against fractional inputs
        proof_max_quantity_per_transaction = int(
            proof_max_quantity_per_transaction
        )
        return (
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        )

    def call(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[bool, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        condition_id: int,
        claimer: str,
        quantity: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            quantity,
            proofs,
            proof_max_quantity_per_transaction,
        ).estimateGas(tx_params.as_dict())


class WalletClaimCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the walletClaimCount method."""

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

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the walletClaimCount method."""
        self.validator.assert_valid(
            method_name="walletClaimCount",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DropERC20_V2:
    """Wrapper class for DropERC20_V2 Solidity contract."""

    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    domain_separator: DomainSeparatorMethod
    """Constructor-initialized instance of
    :class:`DomainSeparatorMethod`.
    """

    allowance: AllowanceMethod
    """Constructor-initialized instance of
    :class:`AllowanceMethod`.
    """

    approve: ApproveMethod
    """Constructor-initialized instance of
    :class:`ApproveMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
    """

    burn_from: BurnFromMethod
    """Constructor-initialized instance of
    :class:`BurnFromMethod`.
    """

    checkpoints: CheckpointsMethod
    """Constructor-initialized instance of
    :class:`CheckpointsMethod`.
    """

    claim: ClaimMethod
    """Constructor-initialized instance of
    :class:`ClaimMethod`.
    """

    claim_condition: ClaimConditionMethod
    """Constructor-initialized instance of
    :class:`ClaimConditionMethod`.
    """

    contract_type: ContractTypeMethod
    """Constructor-initialized instance of
    :class:`ContractTypeMethod`.
    """

    contract_uri: ContractUriMethod
    """Constructor-initialized instance of
    :class:`ContractUriMethod`.
    """

    contract_version: ContractVersionMethod
    """Constructor-initialized instance of
    :class:`ContractVersionMethod`.
    """

    decimals: DecimalsMethod
    """Constructor-initialized instance of
    :class:`DecimalsMethod`.
    """

    decrease_allowance: DecreaseAllowanceMethod
    """Constructor-initialized instance of
    :class:`DecreaseAllowanceMethod`.
    """

    delegate: DelegateMethod
    """Constructor-initialized instance of
    :class:`DelegateMethod`.
    """

    delegate_by_sig: DelegateBySigMethod
    """Constructor-initialized instance of
    :class:`DelegateBySigMethod`.
    """

    delegates: DelegatesMethod
    """Constructor-initialized instance of
    :class:`DelegatesMethod`.
    """

    get_active_claim_condition_id: GetActiveClaimConditionIdMethod
    """Constructor-initialized instance of
    :class:`GetActiveClaimConditionIdMethod`.
    """

    get_claim_condition_by_id: GetClaimConditionByIdMethod
    """Constructor-initialized instance of
    :class:`GetClaimConditionByIdMethod`.
    """

    get_claim_timestamp: GetClaimTimestampMethod
    """Constructor-initialized instance of
    :class:`GetClaimTimestampMethod`.
    """

    get_past_total_supply: GetPastTotalSupplyMethod
    """Constructor-initialized instance of
    :class:`GetPastTotalSupplyMethod`.
    """

    get_past_votes: GetPastVotesMethod
    """Constructor-initialized instance of
    :class:`GetPastVotesMethod`.
    """

    get_platform_fee_info: GetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`GetPlatformFeeInfoMethod`.
    """

    get_role_admin: GetRoleAdminMethod
    """Constructor-initialized instance of
    :class:`GetRoleAdminMethod`.
    """

    get_role_member: GetRoleMemberMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberMethod`.
    """

    get_role_member_count: GetRoleMemberCountMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberCountMethod`.
    """

    get_votes: GetVotesMethod
    """Constructor-initialized instance of
    :class:`GetVotesMethod`.
    """

    grant_role: GrantRoleMethod
    """Constructor-initialized instance of
    :class:`GrantRoleMethod`.
    """

    has_role: HasRoleMethod
    """Constructor-initialized instance of
    :class:`HasRoleMethod`.
    """

    increase_allowance: IncreaseAllowanceMethod
    """Constructor-initialized instance of
    :class:`IncreaseAllowanceMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    max_total_supply: MaxTotalSupplyMethod
    """Constructor-initialized instance of
    :class:`MaxTotalSupplyMethod`.
    """

    max_wallet_claim_count: MaxWalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`MaxWalletClaimCountMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

    nonces: NoncesMethod
    """Constructor-initialized instance of
    :class:`NoncesMethod`.
    """

    num_checkpoints: NumCheckpointsMethod
    """Constructor-initialized instance of
    :class:`NumCheckpointsMethod`.
    """

    permit: PermitMethod
    """Constructor-initialized instance of
    :class:`PermitMethod`.
    """

    primary_sale_recipient: PrimarySaleRecipientMethod
    """Constructor-initialized instance of
    :class:`PrimarySaleRecipientMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    set_claim_conditions: SetClaimConditionsMethod
    """Constructor-initialized instance of
    :class:`SetClaimConditionsMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_max_total_supply: SetMaxTotalSupplyMethod
    """Constructor-initialized instance of
    :class:`SetMaxTotalSupplyMethod`.
    """

    set_max_wallet_claim_count: SetMaxWalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`SetMaxWalletClaimCountMethod`.
    """

    set_platform_fee_info: SetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`SetPlatformFeeInfoMethod`.
    """

    set_primary_sale_recipient: SetPrimarySaleRecipientMethod
    """Constructor-initialized instance of
    :class:`SetPrimarySaleRecipientMethod`.
    """

    set_wallet_claim_count: SetWalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`SetWalletClaimCountMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    symbol: SymbolMethod
    """Constructor-initialized instance of
    :class:`SymbolMethod`.
    """

    total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    transfer: TransferMethod
    """Constructor-initialized instance of
    :class:`TransferMethod`.
    """

    transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """

    verify_claim: VerifyClaimMethod
    """Constructor-initialized instance of
    :class:`VerifyClaimMethod`.
    """

    verify_claim_merkle_proof: VerifyClaimMerkleProofMethod
    """Constructor-initialized instance of
    :class:`VerifyClaimMerkleProofMethod`.
    """

    wallet_claim_count: WalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`WalletClaimCountMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DropERC20_V2Validator = None,
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
            validator = DropERC20_V2Validator(
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
            abi=DropERC20_V2.abi(),
        ).functions

        self.default_admin_role = DefaultAdminRoleMethod(
            web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE
        )

        self.domain_separator = DomainSeparatorMethod(
            web3_or_provider, contract_address, functions.DOMAIN_SEPARATOR
        )

        self.allowance = AllowanceMethod(
            web3_or_provider, contract_address, functions.allowance, validator
        )

        self.approve = ApproveMethod(
            web3_or_provider, contract_address, functions.approve, validator
        )

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.burn = BurnMethod(
            web3_or_provider, contract_address, functions.burn, validator
        )

        self.burn_from = BurnFromMethod(
            web3_or_provider, contract_address, functions.burnFrom, validator
        )

        self.checkpoints = CheckpointsMethod(
            web3_or_provider,
            contract_address,
            functions.checkpoints,
            validator,
        )

        self.claim = ClaimMethod(
            web3_or_provider, contract_address, functions.claim, validator
        )

        self.claim_condition = ClaimConditionMethod(
            web3_or_provider, contract_address, functions.claimCondition
        )

        self.contract_type = ContractTypeMethod(
            web3_or_provider, contract_address, functions.contractType
        )

        self.contract_uri = ContractUriMethod(
            web3_or_provider, contract_address, functions.contractURI
        )

        self.contract_version = ContractVersionMethod(
            web3_or_provider, contract_address, functions.contractVersion
        )

        self.decimals = DecimalsMethod(
            web3_or_provider, contract_address, functions.decimals
        )

        self.decrease_allowance = DecreaseAllowanceMethod(
            web3_or_provider,
            contract_address,
            functions.decreaseAllowance,
            validator,
        )

        self.delegate = DelegateMethod(
            web3_or_provider, contract_address, functions.delegate, validator
        )

        self.delegate_by_sig = DelegateBySigMethod(
            web3_or_provider,
            contract_address,
            functions.delegateBySig,
            validator,
        )

        self.delegates = DelegatesMethod(
            web3_or_provider, contract_address, functions.delegates, validator
        )

        self.get_active_claim_condition_id = GetActiveClaimConditionIdMethod(
            web3_or_provider,
            contract_address,
            functions.getActiveClaimConditionId,
        )

        self.get_claim_condition_by_id = GetClaimConditionByIdMethod(
            web3_or_provider,
            contract_address,
            functions.getClaimConditionById,
            validator,
        )

        self.get_claim_timestamp = GetClaimTimestampMethod(
            web3_or_provider,
            contract_address,
            functions.getClaimTimestamp,
            validator,
        )

        self.get_past_total_supply = GetPastTotalSupplyMethod(
            web3_or_provider,
            contract_address,
            functions.getPastTotalSupply,
            validator,
        )

        self.get_past_votes = GetPastVotesMethod(
            web3_or_provider,
            contract_address,
            functions.getPastVotes,
            validator,
        )

        self.get_platform_fee_info = GetPlatformFeeInfoMethod(
            web3_or_provider, contract_address, functions.getPlatformFeeInfo
        )

        self.get_role_admin = GetRoleAdminMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleAdmin,
            validator,
        )

        self.get_role_member = GetRoleMemberMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleMember,
            validator,
        )

        self.get_role_member_count = GetRoleMemberCountMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleMemberCount,
            validator,
        )

        self.get_votes = GetVotesMethod(
            web3_or_provider, contract_address, functions.getVotes, validator
        )

        self.grant_role = GrantRoleMethod(
            web3_or_provider, contract_address, functions.grantRole, validator
        )

        self.has_role = HasRoleMethod(
            web3_or_provider, contract_address, functions.hasRole, validator
        )

        self.increase_allowance = IncreaseAllowanceMethod(
            web3_or_provider,
            contract_address,
            functions.increaseAllowance,
            validator,
        )

        self.initialize = InitializeMethod(
            web3_or_provider, contract_address, functions.initialize, validator
        )

        self.is_trusted_forwarder = IsTrustedForwarderMethod(
            web3_or_provider,
            contract_address,
            functions.isTrustedForwarder,
            validator,
        )

        self.max_total_supply = MaxTotalSupplyMethod(
            web3_or_provider, contract_address, functions.maxTotalSupply
        )

        self.max_wallet_claim_count = MaxWalletClaimCountMethod(
            web3_or_provider, contract_address, functions.maxWalletClaimCount
        )

        self.multicall = MulticallMethod(
            web3_or_provider, contract_address, functions.multicall, validator
        )

        self.name = NameMethod(
            web3_or_provider, contract_address, functions.name
        )

        self.nonces = NoncesMethod(
            web3_or_provider, contract_address, functions.nonces, validator
        )

        self.num_checkpoints = NumCheckpointsMethod(
            web3_or_provider,
            contract_address,
            functions.numCheckpoints,
            validator,
        )

        self.permit = PermitMethod(
            web3_or_provider, contract_address, functions.permit, validator
        )

        self.primary_sale_recipient = PrimarySaleRecipientMethod(
            web3_or_provider, contract_address, functions.primarySaleRecipient
        )

        self.renounce_role = RenounceRoleMethod(
            web3_or_provider,
            contract_address,
            functions.renounceRole,
            validator,
        )

        self.revoke_role = RevokeRoleMethod(
            web3_or_provider, contract_address, functions.revokeRole, validator
        )

        self.set_claim_conditions = SetClaimConditionsMethod(
            web3_or_provider,
            contract_address,
            functions.setClaimConditions,
            validator,
        )

        self.set_contract_uri = SetContractUriMethod(
            web3_or_provider,
            contract_address,
            functions.setContractURI,
            validator,
        )

        self.set_max_total_supply = SetMaxTotalSupplyMethod(
            web3_or_provider,
            contract_address,
            functions.setMaxTotalSupply,
            validator,
        )

        self.set_max_wallet_claim_count = SetMaxWalletClaimCountMethod(
            web3_or_provider,
            contract_address,
            functions.setMaxWalletClaimCount,
            validator,
        )

        self.set_platform_fee_info = SetPlatformFeeInfoMethod(
            web3_or_provider,
            contract_address,
            functions.setPlatformFeeInfo,
            validator,
        )

        self.set_primary_sale_recipient = SetPrimarySaleRecipientMethod(
            web3_or_provider,
            contract_address,
            functions.setPrimarySaleRecipient,
            validator,
        )

        self.set_wallet_claim_count = SetWalletClaimCountMethod(
            web3_or_provider,
            contract_address,
            functions.setWalletClaimCount,
            validator,
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

        self.symbol = SymbolMethod(
            web3_or_provider, contract_address, functions.symbol
        )

        self.total_supply = TotalSupplyMethod(
            web3_or_provider, contract_address, functions.totalSupply
        )

        self.transfer = TransferMethod(
            web3_or_provider, contract_address, functions.transfer, validator
        )

        self.transfer_from = TransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.transferFrom,
            validator,
        )

        self.verify_claim = VerifyClaimMethod(
            web3_or_provider,
            contract_address,
            functions.verifyClaim,
            validator,
        )

        self.verify_claim_merkle_proof = VerifyClaimMerkleProofMethod(
            web3_or_provider,
            contract_address,
            functions.verifyClaimMerkleProof,
            validator,
        )

        self.wallet_claim_count = WalletClaimCountMethod(
            web3_or_provider,
            contract_address,
            functions.walletClaimCount,
            validator,
        )

    def get_approval_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Approval event.

        :param tx_hash: hash of transaction emitting Approval event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.Approval()
            .processReceipt(tx_receipt)
        )

    def get_claim_conditions_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ClaimConditionsUpdated event.

        :param tx_hash: hash of transaction emitting ClaimConditionsUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.ClaimConditionsUpdated()
            .processReceipt(tx_receipt)
        )

    def get_contract_uri_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ContractURIUpdated event.

        :param tx_hash: hash of transaction emitting ContractURIUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.ContractURIUpdated()
            .processReceipt(tx_receipt)
        )

    def get_delegate_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for DelegateChanged event.

        :param tx_hash: hash of transaction emitting DelegateChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.DelegateChanged()
            .processReceipt(tx_receipt)
        )

    def get_delegate_votes_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for DelegateVotesChanged event.

        :param tx_hash: hash of transaction emitting DelegateVotesChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.DelegateVotesChanged()
            .processReceipt(tx_receipt)
        )

    def get_initialized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Initialized event.

        :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.Initialized()
            .processReceipt(tx_receipt)
        )

    def get_max_total_supply_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MaxTotalSupplyUpdated event.

        :param tx_hash: hash of transaction emitting MaxTotalSupplyUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.MaxTotalSupplyUpdated()
            .processReceipt(tx_receipt)
        )

    def get_max_wallet_claim_count_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MaxWalletClaimCountUpdated event.

        :param tx_hash: hash of transaction emitting MaxWalletClaimCountUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.MaxWalletClaimCountUpdated()
            .processReceipt(tx_receipt)
        )

    def get_platform_fee_info_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PlatformFeeInfoUpdated event.

        :param tx_hash: hash of transaction emitting PlatformFeeInfoUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.PlatformFeeInfoUpdated()
            .processReceipt(tx_receipt)
        )

    def get_primary_sale_recipient_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PrimarySaleRecipientUpdated event.

        :param tx_hash: hash of transaction emitting
            PrimarySaleRecipientUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.PrimarySaleRecipientUpdated()
            .processReceipt(tx_receipt)
        )

    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.RoleAdminChanged()
            .processReceipt(tx_receipt)
        )

    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.RoleGranted()
            .processReceipt(tx_receipt)
        )

    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.RoleRevoked()
            .processReceipt(tx_receipt)
        )

    def get_tokens_claimed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensClaimed event.

        :param tx_hash: hash of transaction emitting TokensClaimed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.TokensClaimed()
            .processReceipt(tx_receipt)
        )

    def get_transfer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Transfer event.

        :param tx_hash: hash of transaction emitting Transfer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.Transfer()
            .processReceipt(tx_receipt)
        )

    def get_wallet_claim_count_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for WalletClaimCountUpdated event.

        :param tx_hash: hash of transaction emitting WalletClaimCountUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DropERC20_V2.abi(),
            )
            .events.WalletClaimCountUpdated()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"indexed":false,"internalType":"struct IDropClaimCondition_V2.ClaimCondition[]","name":"claimConditions","type":"tuple[]"}],"name":"ClaimConditionsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"prevURI","type":"string"},{"indexed":false,"internalType":"string","name":"newURI","type":"string"}],"name":"ContractURIUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegator","type":"address"},{"indexed":true,"internalType":"address","name":"fromDelegate","type":"address"},{"indexed":true,"internalType":"address","name":"toDelegate","type":"address"}],"name":"DelegateChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegate","type":"address"},{"indexed":false,"internalType":"uint256","name":"previousBalance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newBalance","type":"uint256"}],"name":"DelegateVotesChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"maxTotalSupply","type":"uint256"}],"name":"MaxTotalSupplyUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"count","type":"uint256"}],"name":"MaxWalletClaimCountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"platformFeeRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"platformFeeBps","type":"uint256"}],"name":"PlatformFeeInfoUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"}],"name":"PrimarySaleRecipientUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"claimConditionIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"claimer","type":"address"},{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityClaimed","type":"uint256"}],"name":"TokensClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"wallet","type":"address"},{"indexed":false,"internalType":"uint256","name":"count","type":"uint256"}],"name":"WalletClaimCountUpdated","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint32","name":"pos","type":"uint32"}],"name":"checkpoints","outputs":[{"components":[{"internalType":"uint32","name":"fromBlock","type":"uint32"},{"internalType":"uint224","name":"votes","type":"uint224"}],"internalType":"struct ERC20VotesUpgradeable.Checkpoint","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"bytes32[]","name":"_proofs","type":"bytes32[]"},{"internalType":"uint256","name":"_proofMaxQuantityPerTransaction","type":"uint256"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"claimCondition","outputs":[{"internalType":"uint256","name":"currentStartId","type":"uint256"},{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"}],"name":"delegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"delegateBySig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"delegates","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getActiveClaimConditionId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_conditionId","type":"uint256"}],"name":"getClaimConditionById","outputs":[{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDropClaimCondition_V2.ClaimCondition","name":"condition","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"}],"name":"getClaimTimestamp","outputs":[{"internalType":"uint256","name":"lastClaimTimestamp","type":"uint256"},{"internalType":"uint256","name":"nextValidClaimTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPlatformFeeInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultAdmin","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"string","name":"_contractURI","type":"string"},{"internalType":"address[]","name":"_trustedForwarders","type":"address[]"},{"internalType":"address","name":"_primarySaleRecipient","type":"address"},{"internalType":"address","name":"_platformFeeRecipient","type":"address"},{"internalType":"uint256","name":"_platformFeeBps","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxWalletClaimCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"numCheckpoints","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"primarySaleRecipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDropClaimCondition_V2.ClaimCondition[]","name":"_phases","type":"tuple[]"},{"internalType":"bool","name":"_resetClaimEligibility","type":"bool"}],"name":"setClaimConditions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxTotalSupply","type":"uint256"}],"name":"setMaxTotalSupply","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"setMaxWalletClaimCount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_platformFeeRecipient","type":"address"},{"internalType":"uint256","name":"_platformFeeBps","type":"uint256"}],"name":"setPlatformFeeInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_saleRecipient","type":"address"}],"name":"setPrimarySaleRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_claimer","type":"address"},{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"setWalletClaimCount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"bool","name":"verifyMaxQuantityPerTransaction","type":"bool"}],"name":"verifyClaim","outputs":[],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"bytes32[]","name":"_proofs","type":"bytes32[]"},{"internalType":"uint256","name":"_proofMaxQuantityPerTransaction","type":"uint256"}],"name":"verifyClaimMerkleProof","outputs":[{"internalType":"bool","name":"validMerkleProof","type":"bool"},{"internalType":"uint256","name":"merkleProofIndex","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"walletClaimCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
