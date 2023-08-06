"""Generated wrapper for Drop1155 Solidity contract."""

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
# constructor for Drop1155 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        Drop1155Validator,
    )
except ImportError:

    class Drop1155Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IClaimConditionClaimCondition(TypedDict):
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

    quantityLimitPerWallet: int

    merkleRoot: Union[bytes, str]

    pricePerToken: int

    currency: str

    metadata: str


class IDrop1155AllowlistProof(TypedDict):
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

    proof: List[Union[bytes, str]]

    quantityLimitPerWallet: int

    pricePerToken: int

    currency: str


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
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        data: Union[bytes, str],
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
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
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
            parameter_name="_allowlistProof",
            argument_value=allowlist_proof,
        )
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="_data",
            argument_value=data,
        )
        return (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )

    def call(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).estimateGas(tx_params.as_dict())


class ClaimConditionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the claimCondition method."""

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
        """Validate the inputs to the claimCondition method."""
        self.validator.assert_valid(
            method_name="claimCondition",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

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


class GetActiveClaimConditionIdMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getActiveClaimConditionId method."""

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

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getActiveClaimConditionId method."""
        self.validator.assert_valid(
            method_name="getActiveClaimConditionId",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return token_id

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(
            tx_params.as_dict()
        )


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

    def validate_and_normalize_inputs(self, token_id: int, condition_id: int):
        """Validate the inputs to the getClaimConditionById method."""
        self.validator.assert_valid(
            method_name="getClaimConditionById",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="getClaimConditionById",
            parameter_name="_conditionId",
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        return (token_id, condition_id)

    def call(
        self,
        token_id: int,
        condition_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> IClaimConditionClaimCondition:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, condition_id) = self.validate_and_normalize_inputs(
            token_id, condition_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id, condition_id).call(
            tx_params.as_dict()
        )
        return IClaimConditionClaimCondition(
            startTimestamp=returned[0],
            maxClaimableSupply=returned[1],
            supplyClaimed=returned[2],
            quantityLimitPerWallet=returned[3],
            merkleRoot=returned[4],
            pricePerToken=returned[5],
            currency=returned[6],
            metadata=returned[7],
        )

    def send_transaction(
        self,
        token_id: int,
        condition_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, condition_id) = self.validate_and_normalize_inputs(
            token_id, condition_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        token_id: int,
        condition_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, condition_id) = self.validate_and_normalize_inputs(
            token_id, condition_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, condition_id
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_id: int,
        condition_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, condition_id) = self.validate_and_normalize_inputs(
            token_id, condition_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id).estimateGas(
            tx_params.as_dict()
        )


class GetSupplyClaimedByWalletMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getSupplyClaimedByWallet method."""

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
        self, token_id: int, condition_id: int, claimer: str
    ):
        """Validate the inputs to the getSupplyClaimedByWallet method."""
        self.validator.assert_valid(
            method_name="getSupplyClaimedByWallet",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="getSupplyClaimedByWallet",
            parameter_name="_conditionId",
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        self.validator.assert_valid(
            method_name="getSupplyClaimedByWallet",
            parameter_name="_claimer",
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        return (token_id, condition_id, claimer)

    def call(
        self,
        token_id: int,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(
            token_id, condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            token_id, condition_id, claimer
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        token_id: int,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(
            token_id, condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, condition_id, claimer
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        token_id: int,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(
            token_id, condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, condition_id, claimer
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_id: int,
        condition_id: int,
        claimer: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(
            token_id, condition_id, claimer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, condition_id, claimer
        ).estimateGas(tx_params.as_dict())


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
        token_id: int,
        conditions: List[IClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
    ):
        """Validate the inputs to the setClaimConditions method."""
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="_conditions",
            argument_value=conditions,
        )
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="_resetClaimEligibility",
            argument_value=reset_claim_eligibility,
        )
        return (token_id, conditions, reset_claim_eligibility)

    def call(
        self,
        token_id: int,
        conditions: List[IClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            token_id,
            conditions,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, conditions, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            token_id, conditions, reset_claim_eligibility
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        token_id: int,
        conditions: List[IClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            token_id,
            conditions,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, conditions, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, conditions, reset_claim_eligibility
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        token_id: int,
        conditions: List[IClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            token_id,
            conditions,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, conditions, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, conditions, reset_claim_eligibility
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_id: int,
        conditions: List[IClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            token_id,
            conditions,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, conditions, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, conditions, reset_claim_eligibility
        ).estimateGas(tx_params.as_dict())


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
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
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
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
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
            parameter_name="_allowlistProof",
            argument_value=allowlist_proof,
        )
        return (
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        )

    def call(
        self,
        condition_id: int,
        claimer: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self,
        condition_id: int,
        claimer: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        condition_id: int,
        claimer: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        condition_id: int,
        claimer: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDrop1155AllowlistProof,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ) = self.validate_and_normalize_inputs(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            condition_id,
            claimer,
            token_id,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Drop1155:
    """Wrapper class for Drop1155 Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    claim: ClaimMethod
    """Constructor-initialized instance of
    :class:`ClaimMethod`.
    """

    claim_condition: ClaimConditionMethod
    """Constructor-initialized instance of
    :class:`ClaimConditionMethod`.
    """

    get_active_claim_condition_id: GetActiveClaimConditionIdMethod
    """Constructor-initialized instance of
    :class:`GetActiveClaimConditionIdMethod`.
    """

    get_claim_condition_by_id: GetClaimConditionByIdMethod
    """Constructor-initialized instance of
    :class:`GetClaimConditionByIdMethod`.
    """

    get_supply_claimed_by_wallet: GetSupplyClaimedByWalletMethod
    """Constructor-initialized instance of
    :class:`GetSupplyClaimedByWalletMethod`.
    """

    set_claim_conditions: SetClaimConditionsMethod
    """Constructor-initialized instance of
    :class:`SetClaimConditionsMethod`.
    """

    verify_claim: VerifyClaimMethod
    """Constructor-initialized instance of
    :class:`VerifyClaimMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: Drop1155Validator = None,
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
            validator = Drop1155Validator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=Drop1155.abi()
        ).functions

        self.claim = ClaimMethod(
            web3_or_provider, contract_address, functions.claim, validator
        )

        self.claim_condition = ClaimConditionMethod(
            web3_or_provider,
            contract_address,
            functions.claimCondition,
            validator,
        )

        self.get_active_claim_condition_id = GetActiveClaimConditionIdMethod(
            web3_or_provider,
            contract_address,
            functions.getActiveClaimConditionId,
            validator,
        )

        self.get_claim_condition_by_id = GetClaimConditionByIdMethod(
            web3_or_provider,
            contract_address,
            functions.getClaimConditionById,
            validator,
        )

        self.get_supply_claimed_by_wallet = GetSupplyClaimedByWalletMethod(
            web3_or_provider,
            contract_address,
            functions.getSupplyClaimedByWallet,
            validator,
        )

        self.set_claim_conditions = SetClaimConditionsMethod(
            web3_or_provider,
            contract_address,
            functions.setClaimConditions,
            validator,
        )

        self.verify_claim = VerifyClaimMethod(
            web3_or_provider,
            contract_address,
            functions.verifyClaim,
            validator,
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
                abi=Drop1155.abi(),
            )
            .events.ClaimConditionsUpdated()
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
                abi=Drop1155.abi(),
            )
            .events.TokensClaimed()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerWallet","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"string","name":"metadata","type":"string"}],"indexed":false,"internalType":"struct IClaimCondition.ClaimCondition[]","name":"claimConditions","type":"tuple[]"},{"indexed":false,"internalType":"bool","name":"resetEligibility","type":"bool"}],"name":"ClaimConditionsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"claimConditionIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"claimer","type":"address"},{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"quantityClaimed","type":"uint256"}],"name":"TokensClaimed","type":"event"},{"inputs":[{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"components":[{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"},{"internalType":"uint256","name":"quantityLimitPerWallet","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDrop1155.AllowlistProof","name":"_allowlistProof","type":"tuple"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"claimCondition","outputs":[{"internalType":"uint256","name":"currentStartId","type":"uint256"},{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getActiveClaimConditionId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_conditionId","type":"uint256"}],"name":"getClaimConditionById","outputs":[{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerWallet","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"string","name":"metadata","type":"string"}],"internalType":"struct IClaimCondition.ClaimCondition","name":"condition","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"}],"name":"getSupplyClaimedByWallet","outputs":[{"internalType":"uint256","name":"supplyClaimedByWallet","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerWallet","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"string","name":"metadata","type":"string"}],"internalType":"struct IClaimCondition.ClaimCondition[]","name":"_conditions","type":"tuple[]"},{"internalType":"bool","name":"_resetClaimEligibility","type":"bool"}],"name":"setClaimConditions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"components":[{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"},{"internalType":"uint256","name":"quantityLimitPerWallet","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDrop1155.AllowlistProof","name":"_allowlistProof","type":"tuple"}],"name":"verifyClaim","outputs":[{"internalType":"bool","name":"isOverride","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
