import unittest
from main.data.DataSchema import DataSchema


class TestDataSchema(unittest.TestCase):
    def test_shouldDataSchemaPreSet(self):
        self.assertEqual(DataSchema.MICRO_STOCK_VALUE_K_DATA.value.sortedAllColumns,
                         ['close', 'date', 'high', 'low', 'ma10', 'ma20', 'ma5',
                          'open',
                          'p_change', 'price_change', 'turnover', 'v_ma10', 'v_ma20',
                          'v_ma5',
                          'volume'])
        self.assertEqual(DataSchema.MICRO_STOCK_VALUE_K_DATA.value.partitionByColumns, ['code', 'kType'])
        self.assertEqual(DataSchema.MICRO_STOCK_VALUE_K_DATA.value.identifyColumn, 'date')

        self.assertEqual(DataSchema.MICRO_STOCK_VOLUME_DATA.value.sortedAllColumns,
                         ['DateAndTime', 'amount', 'change', 'date', 'price', 'time',
                          'type', 'volume'])
        self.assertEqual(DataSchema.MICRO_STOCK_VOLUME_DATA.value.partitionByColumns, ['code', 'kType'])
        self.assertEqual(DataSchema.MICRO_STOCK_VOLUME_DATA.value.identifyColumn, 'DateAndTime')
