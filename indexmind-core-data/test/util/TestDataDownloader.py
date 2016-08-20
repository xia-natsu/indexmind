import unittest

from main.util import DataDownloader
from main.data.DataSchema import DataSchema
from main.task import TaskType


class TestDataDownloader(unittest.TestCase):
    def setUp(self):
        #dummy
        self.seq = range(10)

    def test_downloadDayData_normal(self):
        downloader = DataDownloader.DataDownloader('D', '600006', '2016-01-01', '2016-01-10', TaskType.MICRO_STOCK_DAY_VAL)
        actualData = downloader.download_data()
        # check columns
        actualColumns = set(actualData.columns.values.tolist())
        expectColumns = set(DataSchema.MICRO_STOCK_VALUE_DAY_DATA.value.allColumns())
        self.assertEqual(actualColumns, expectColumns,
                         "should have the same column names")
        # check rows
        self.assertEqual(actualData['open'].count(), 5, "should have 5 rows")
        # check first row
        self.assertEqual(str(actualData['date'][0]), "2016-01-04 00:00:00", "should start with 2016-01-04")


    def test_downloadKData_updateToDate(self):
        downloader = DataDownloader.DataDownloader('D', '600006', '2016-01-10', '2016-01-10',TaskType.MICRO_STOCK_DAY_VAL)
        actualData = downloader.download_data()
        self.assertEqual(actualData, None,
                         "should have return none for up-to-date data (inefficient query)")

    def test_downloadVOLData(self):
        downloader = DataDownloader.DataDownloader('VOL', '600007', '2016-01-05', '2016-01-05', TaskType.MICRO_STOCK_VOL)
        actualData = downloader.download_data()
        # check columns
        actualColumns = set(actualData.columns.values.tolist())
        expectColumns = set(DataSchema.MICRO_STOCK_VOLUME_DATA.value.allColumns())
        self.assertEqual(actualColumns, expectColumns,
                         "should have the same column names")
        # check rows
        self.assertEqual(actualData['amount'].count(), 1490, "should have 1490 rows")
        # check first row
        self.assertEqual(actualData['time'][0], "09:25:04", "should start with 09AM")