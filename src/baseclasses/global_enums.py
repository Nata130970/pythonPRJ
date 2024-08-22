from enum import Enum


class GlobalErrorMesages(Enum):
    WRONG_STATUS_CODE = "Eхxpected status code not equal 200"
    WRONG_FIELD_COLOR_IN_SCHEMA = 'Field color not contains #'
    WRONG_COUNT_PRESENTED_DAY = 'Count day equal 0'
