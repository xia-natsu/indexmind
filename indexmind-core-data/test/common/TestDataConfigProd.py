import unittest

from main.common import DataConfig

class TestDataConfigProd(unittest.TestCase):
    def setup(self):
        #TODO: switch to prod config here
        pass

    def test_shouldGetProdConfigs(self):
        #IMPORTANT: NEVER ADD CREDENTIALS TO YOUR CODE
        self.assertEqual(DataConfig.S3_ACCOUNT, "xia")
        self.assertEqual(DataConfig.FILE_SYSTEM, "s3")
        self.assertEqual(DataConfig.DATA_ROOT,"s3n://indexmind.data/prod/market")
        list1 = DataConfig.SYMBOL_LIST
        print(list1)
