from enum import Enum, unique

### Intrinsic Columns
INTRINSIC_COLNAME_DATA_DOMAIN = "DataDomain"
INTRINSIC_COLNAME_DATA_TYPE = "DataType"
INTRINSIC_COLNAME_CODE = "Code"
INTRINSIC_COLUMNS = [INTRINSIC_COLNAME_DATA_DOMAIN, INTRINSIC_COLNAME_DATA_TYPE, INTRINSIC_COLNAME_CODE]
def addIntrinsicColumnsToData(data, domain, type, code):
    data[INTRINSIC_COLNAME_DATA_DOMAIN] = domain
    data[INTRINSIC_COLNAME_DATA_TYPE] = type
    data[INTRINSIC_COLNAME_CODE] = code
    return data

### Domain
class DataDomain(Enum):
    MICRO = "MICRO"
    MACRO = "MACRO"

### Data Type ###
class DataType(Enum):
    K_DAY = "D"
    TICK_VOL = "TICK"

### Schema Class ###
class DataSchemaType():
    def __init__(self, sortedAllColumns, intrinsicColumns, partitionByColumns, identifyColumn):
        self.sortedAllColumns = sortedAllColumns
        self.intrinsicColumns = intrinsicColumns
        self.partitionByColumns = partitionByColumns
        self.identifyColumn = identifyColumn

    def allColumns(self):
        return self.sortedAllColumns + self.intrinsicColumns


@unique
class DataSchema(Enum):
    MICRO_STOCK_VALUE_K_DATA = DataSchemaType(
        sortedAllColumns=['close', 'date', 'high', 'low', 'ma10', 'ma20', 'ma5',
                          'open',
                          'p_change', 'price_change', 'turnover', 'v_ma10', 'v_ma20',
                          'v_ma5',
                          'volume'],
        intrinsicColumns=INTRINSIC_COLUMNS,
        partitionByColumns=[INTRINSIC_COLNAME_CODE, INTRINSIC_COLNAME_DATA_TYPE],
        identifyColumn='date')
    MICRO_STOCK_VALUE_DAY_DATA = DataSchemaType(
        sortedAllColumns=['amount', 'close', 'date', 'high', 'low', 'open', 'volume'],
        intrinsicColumns=INTRINSIC_COLUMNS,
        partitionByColumns=[INTRINSIC_COLNAME_CODE, INTRINSIC_COLNAME_DATA_TYPE],
        identifyColumn='date')
    MICRO_STOCK_VOLUME_DATA = DataSchemaType(
        sortedAllColumns=['DateAndTime', 'amount', 'change', 'date', 'price', 'time',
                          'type', 'volume'],
        intrinsicColumns=INTRINSIC_COLUMNS,
        partitionByColumns=[INTRINSIC_COLNAME_CODE, INTRINSIC_COLNAME_DATA_TYPE],
        identifyColumn='DateAndTime')
