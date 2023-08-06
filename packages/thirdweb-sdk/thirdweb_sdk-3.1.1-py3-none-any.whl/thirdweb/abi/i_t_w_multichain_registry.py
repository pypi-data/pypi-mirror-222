"""Generated wrapper for ITWMultichainRegistry Solidity contract."""

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
# constructor for ITWMultichainRegistry below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ITWMultichainRegistryValidator,
    )
except ImportError:

    class ITWMultichainRegistryValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ITWMultichainRegistryDeployment(TypedDict):
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

    deploymentAddress: str

    chainId: int

    metadataURI: str


class AddMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the add method."""

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
        self, deployer: str, deployment: str, chain_id: int, metadata_uri: str
    ):
        """Validate the inputs to the add method."""
        self.validator.assert_valid(
            method_name="add",
            parameter_name="_deployer",
            argument_value=deployer,
        )
        deployer = self.validate_and_checksum_address(deployer)
        self.validator.assert_valid(
            method_name="add",
            parameter_name="_deployment",
            argument_value=deployment,
        )
        deployment = self.validate_and_checksum_address(deployment)
        self.validator.assert_valid(
            method_name="add",
            parameter_name="_chainId",
            argument_value=chain_id,
        )
        # safeguard against fractional inputs
        chain_id = int(chain_id)
        self.validator.assert_valid(
            method_name="add",
            parameter_name="metadataUri",
            argument_value=metadata_uri,
        )
        return (deployer, deployment, chain_id, metadata_uri)

    def call(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            deployer,
            deployment,
            chain_id,
            metadata_uri,
        ) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id, metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            deployer, deployment, chain_id, metadata_uri
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            deployer,
            deployment,
            chain_id,
            metadata_uri,
        ) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id, metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            deployer, deployment, chain_id, metadata_uri
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            deployer,
            deployment,
            chain_id,
            metadata_uri,
        ) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id, metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            deployer, deployment, chain_id, metadata_uri
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            deployer,
            deployment,
            chain_id,
            metadata_uri,
        ) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id, metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            deployer, deployment, chain_id, metadata_uri
        ).estimateGas(tx_params.as_dict())


class CountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the count method."""

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

    def validate_and_normalize_inputs(self, deployer: str):
        """Validate the inputs to the count method."""
        self.validator.assert_valid(
            method_name="count",
            parameter_name="_deployer",
            argument_value=deployer,
        )
        deployer = self.validate_and_checksum_address(deployer)
        return deployer

    def call(self, deployer: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(deployer).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, deployer: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer).transact(tx_params.as_dict())

    def build_transaction(
        self, deployer: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, deployer: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer).estimateGas(
            tx_params.as_dict()
        )


class GetAllMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAll method."""

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

    def validate_and_normalize_inputs(self, deployer: str):
        """Validate the inputs to the getAll method."""
        self.validator.assert_valid(
            method_name="getAll",
            parameter_name="_deployer",
            argument_value=deployer,
        )
        deployer = self.validate_and_checksum_address(deployer)
        return deployer

    def call(
        self, deployer: str, tx_params: Optional[TxParams] = None
    ) -> List[ITWMultichainRegistryDeployment]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(deployer).call(tx_params.as_dict())
        return [
            ITWMultichainRegistryDeployment(
                deploymentAddress=element[0],
                chainId=element[1],
                metadataURI=element[2],
            )
            for element in returned
        ]

    def send_transaction(
        self, deployer: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer).transact(tx_params.as_dict())

    def build_transaction(
        self, deployer: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, deployer: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (deployer) = self.validate_and_normalize_inputs(deployer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer).estimateGas(
            tx_params.as_dict()
        )


class GetMetadataUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getMetadataUri method."""

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

    def validate_and_normalize_inputs(self, chain_id: int, deployment: str):
        """Validate the inputs to the getMetadataUri method."""
        self.validator.assert_valid(
            method_name="getMetadataUri",
            parameter_name="_chainId",
            argument_value=chain_id,
        )
        # safeguard against fractional inputs
        chain_id = int(chain_id)
        self.validator.assert_valid(
            method_name="getMetadataUri",
            parameter_name="_deployment",
            argument_value=deployment,
        )
        deployment = self.validate_and_checksum_address(deployment)
        return (chain_id, deployment)

    def call(
        self,
        chain_id: int,
        deployment: str,
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (chain_id, deployment) = self.validate_and_normalize_inputs(
            chain_id, deployment
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(chain_id, deployment).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        chain_id: int,
        deployment: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (chain_id, deployment) = self.validate_and_normalize_inputs(
            chain_id, deployment
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, deployment).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        chain_id: int,
        deployment: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (chain_id, deployment) = self.validate_and_normalize_inputs(
            chain_id, deployment
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, deployment).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        chain_id: int,
        deployment: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (chain_id, deployment) = self.validate_and_normalize_inputs(
            chain_id, deployment
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, deployment).estimateGas(
            tx_params.as_dict()
        )


class RemoveMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the remove method."""

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
        self, deployer: str, deployment: str, chain_id: int
    ):
        """Validate the inputs to the remove method."""
        self.validator.assert_valid(
            method_name="remove",
            parameter_name="_deployer",
            argument_value=deployer,
        )
        deployer = self.validate_and_checksum_address(deployer)
        self.validator.assert_valid(
            method_name="remove",
            parameter_name="_deployment",
            argument_value=deployment,
        )
        deployment = self.validate_and_checksum_address(deployment)
        self.validator.assert_valid(
            method_name="remove",
            parameter_name="_chainId",
            argument_value=chain_id,
        )
        # safeguard against fractional inputs
        chain_id = int(chain_id)
        return (deployer, deployment, chain_id)

    def call(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (deployer, deployment, chain_id) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(deployer, deployment, chain_id).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (deployer, deployment, chain_id) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            deployer, deployment, chain_id
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (deployer, deployment, chain_id) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            deployer, deployment, chain_id
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        deployer: str,
        deployment: str,
        chain_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (deployer, deployment, chain_id) = self.validate_and_normalize_inputs(
            deployer, deployment, chain_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            deployer, deployment, chain_id
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ITWMultichainRegistry:
    """Wrapper class for ITWMultichainRegistry Solidity contract."""

    add: AddMethod
    """Constructor-initialized instance of
    :class:`AddMethod`.
    """

    count: CountMethod
    """Constructor-initialized instance of
    :class:`CountMethod`.
    """

    get_all: GetAllMethod
    """Constructor-initialized instance of
    :class:`GetAllMethod`.
    """

    get_metadata_uri: GetMetadataUriMethod
    """Constructor-initialized instance of
    :class:`GetMetadataUriMethod`.
    """

    remove: RemoveMethod
    """Constructor-initialized instance of
    :class:`RemoveMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ITWMultichainRegistryValidator = None,
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
            validator = ITWMultichainRegistryValidator(
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
            abi=ITWMultichainRegistry.abi(),
        ).functions

        self.add = AddMethod(
            web3_or_provider, contract_address, functions.add, validator
        )

        self.count = CountMethod(
            web3_or_provider, contract_address, functions.count, validator
        )

        self.get_all = GetAllMethod(
            web3_or_provider, contract_address, functions.getAll, validator
        )

        self.get_metadata_uri = GetMetadataUriMethod(
            web3_or_provider,
            contract_address,
            functions.getMetadataUri,
            validator,
        )

        self.remove = RemoveMethod(
            web3_or_provider, contract_address, functions.remove, validator
        )

    def get_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Added event.

        :param tx_hash: hash of transaction emitting Added event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ITWMultichainRegistry.abi(),
            )
            .events.Added()
            .processReceipt(tx_receipt)
        )

    def get_deleted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Deleted event.

        :param tx_hash: hash of transaction emitting Deleted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ITWMultichainRegistry.abi(),
            )
            .events.Deleted()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"deployer","type":"address"},{"indexed":true,"internalType":"address","name":"deployment","type":"address"},{"indexed":true,"internalType":"uint256","name":"chainId","type":"uint256"},{"indexed":false,"internalType":"string","name":"metadataUri","type":"string"}],"name":"Added","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"deployer","type":"address"},{"indexed":true,"internalType":"address","name":"deployment","type":"address"},{"indexed":true,"internalType":"uint256","name":"chainId","type":"uint256"}],"name":"Deleted","type":"event"},{"inputs":[{"internalType":"address","name":"_deployer","type":"address"},{"internalType":"address","name":"_deployment","type":"address"},{"internalType":"uint256","name":"_chainId","type":"uint256"},{"internalType":"string","name":"metadataUri","type":"string"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_deployer","type":"address"}],"name":"count","outputs":[{"internalType":"uint256","name":"deploymentCount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_deployer","type":"address"}],"name":"getAll","outputs":[{"components":[{"internalType":"address","name":"deploymentAddress","type":"address"},{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"string","name":"metadataURI","type":"string"}],"internalType":"struct ITWMultichainRegistry.Deployment[]","name":"allDeployments","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_chainId","type":"uint256"},{"internalType":"address","name":"_deployment","type":"address"}],"name":"getMetadataUri","outputs":[{"internalType":"string","name":"metadataUri","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_deployer","type":"address"},{"internalType":"address","name":"_deployment","type":"address"},{"internalType":"uint256","name":"_chainId","type":"uint256"}],"name":"remove","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
