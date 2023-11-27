from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit
from hummingbot.core.data_type.in_flight_order import OrderState

CONNECTOR_NAME = "tokocrypto"
DEFAULT_DOMAIN = "com"

HBOT_ORDER_ID_PREFIX = "xTKOTC"
MAX_ORDER_ID_LEN = 32

# Base URL
REST_PRIVATE_URL = "https://www.tokocrypto.{}/open/"
REST_URL_TKO = "https://www.tokocrypto.{}/open/"
REST_URL = "https://api.binance.{}/api/"
WSS_URL = "wss://stream-cloud.binanceru.net/ws"

PUBLIC_API_VERSION = "v3"
PRIVATE_API_VERSION = "v1"

# Public API endpoints or TokocryptoClient function
TICKER_PRICE_CHANGE_PATH_URL = "/ticker/24hr"
TICKER_BOOK_PATH_URL = "/ticker/bookTicker"
EXCHANGE_INFO_PATH_URL = "/exchangeInfo"
PING_PATH_URL = "/ping"
SNAPSHOT_PATH_URL = "/market/depth"
SERVER_TIME_PATH_URL = "/common/time"
SERVER_TIME_2_PATH_URL = "/time"

# Private API endpoints or TokocryptoClient function
ACCOUNTS_PATH_URL = "/account/spot"
MY_TRADES_PATH_URL = "/orders/trades"
ORDER_PATH_URL = "/orders/detail"
ORDER_BUY_URL = "/orders"
ORDER_CANCEL_URL = "/orders/cancel"
TOKOCRYPTO_USER_STREAM_PATH_URL = "/user-data-stream"

WS_HEARTBEAT_TIME_INTERVAL = 30

# Tokocrypto params

SIDE_BUY = '0'
SIDE_SELL = '1'

TIME_IN_FORCE_GTC = 'GTC'  # Good till cancelled
TIME_IN_FORCE_IOC = 'IOC'  # Immediate or cancel
TIME_IN_FORCE_FOK = 'FOK'  # Fill or kill

# Rate Limit Type
REQUEST_WEIGHT = "REQUEST_WEIGHT"
ORDERS = "ORDERS"
ORDERS_24HR = "ORDERS_24HR"
RAW_REQUESTS = "RAW_REQUESTS"

# Rate Limit time intervals
ONE_MINUTE = 60
ONE_SECOND = 1
ONE_DAY = 86400

MAX_REQUEST = 5000

# Order States
ORDER_STATE = {
    -2: OrderState.PENDING_CREATE,
    0: OrderState.OPEN,
    1: OrderState.PARTIALLY_FILLED,
    2: OrderState.FILLED,
    3: OrderState.CANCELED,
    4: OrderState.OPEN,
    5: OrderState.FAILED,
    6: OrderState.FAILED,
}
ORDER_STATE_2 = {
    "PENDING": ORDER_STATE[-2],
    "NEW": ORDER_STATE[0],
    "FILLED": ORDER_STATE[2],
    "PARTIALLY_FILLED": ORDER_STATE[1],
    "PENDING_CANCEL": ORDER_STATE[4],
    "CANCELED": ORDER_STATE[3],
    "REJECTED": ORDER_STATE[5],
    "EXPIRED": ORDER_STATE[6],
}

# Websocket event types
DIFF_EVENT_TYPE = "depthUpdate"
TRADE_EVENT_TYPE = "trade"

RATE_LIMITS = [
    # Pools
    RateLimit(limit_id=REQUEST_WEIGHT, limit=1200, time_interval=ONE_MINUTE),
    RateLimit(limit_id=ORDERS, limit=50, time_interval=10 * ONE_SECOND),
    RateLimit(limit_id=ORDERS_24HR, limit=160000, time_interval=ONE_DAY),
    RateLimit(limit_id=RAW_REQUESTS, limit=6100, time_interval= 5 * ONE_MINUTE),
    # Weighted Limits
    RateLimit(limit_id=TICKER_PRICE_CHANGE_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 40),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=TICKER_BOOK_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 2),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=EXCHANGE_INFO_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 10),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=SNAPSHOT_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 50),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=TOKOCRYPTO_USER_STREAM_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 1),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=SERVER_TIME_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 1),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=SERVER_TIME_2_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 1),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=PING_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 1),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=ACCOUNTS_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 10),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=MY_TRADES_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 10),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=ORDER_PATH_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 5),
                             LinkedLimitWeightPair(ORDERS, 1),
                             LinkedLimitWeightPair(ORDERS_24HR, 1),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=ORDER_BUY_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 2),
                             LinkedLimitWeightPair(ORDERS, 1),
                             LinkedLimitWeightPair(ORDERS_24HR, 1),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)]),
    RateLimit(limit_id=ORDER_CANCEL_URL, limit=MAX_REQUEST, time_interval=ONE_MINUTE,
              linked_limits=[LinkedLimitWeightPair(REQUEST_WEIGHT, 2),
                             LinkedLimitWeightPair(ORDERS, 1),
                             LinkedLimitWeightPair(ORDERS_24HR, 1),
                             LinkedLimitWeightPair(RAW_REQUESTS, 1)])
]
