from decimal import Decimal
from typing import Any, Dict

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True
EXAMPLE_PAIR = "USDT-BIDR"

DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.001"),
    taker_percent_fee_decimal=Decimal("0.001"),
    buy_percent_fee_deducted_from_returns=True
)


def get_flight_order_client_id_from_exchange_order_id(dicts: Dict, exchange_order_id: any):
    key = None
    for order in dicts.values():
        if order.exchange_order_id == exchange_order_id:
            key = order.client_order_id
    return key


def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
    """
    Verifies if a trading pair is enabled to operate with based on its exchange information
    :param exchange_info: the exchange information for a trading pair
    :return: True if the trading pair is enabled, False otherwise
    """
    return exchange_info.get("status", None) == "TRADING" and "SPOT" in exchange_info.get("permissions", list())


class TokocryptoConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="tokocrypto", const=True, client_data=None)
    tokocrypto_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Tokocrypto API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    tokocrypto_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Tokocrypto API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "tokocrypto"


KEYS = TokocryptoConfigMap.construct()
