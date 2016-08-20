import logging

import tushare

from task import TaskType
from main.data import DataSchema
from main.data.DataSchema import DataDomain
from main.data.DataSchema import DataType

logger = logging.getLogger(__name__)

class DataDownloader():
    def __init__(self,ktype,symbol,start,end,task_type):
        self.ktype = ktype
        self.symbol = symbol
        self.start = start
        self.end = end
        self.task_type = task_type
        self.MAX_RETRY = 3

    def download_data(self):
        # Download Data within MAX_RETRY times
        retry = 0
        data = None
        while retry < self.MAX_RETRY and data is None:
            try:
                if self.task_type == TaskType.MICRO_STOCK_DAY_VAL :
                    data = self.download_DAY_data_from_Tushare(symbol=self.symbol, ktype=self.ktype, start=self.start, end=self.end)
                elif self.task_type == TaskType.MICRO_STOCK_VOL:
                    data = self.download_VOL_data_from_Tushare(symbol=self.symbol, ktype="VOL", start=self.start, end=self.end)
                else:
                    logger.error("Invalid Task Type: {task_type}".format(task_type=self.task_type))
                    return None
            except Exception as e:
                logger.error("Got unexpected error and try again with {ktype},{symbol},{start},{end}... {message}"
                             .format(ktype=self.ktype, symbol=self.symbol, start=self.start,end=self.end,message=e.message))
            finally:
                retry += 1
        if data is None:
            logger.warn("{symbol}'s data may not exist (or update-to-date) for {start} - {end}. Please Check.".format(symbol=self.symbol, start=self.start, end=self.end))
            return None
        else:
            return data

    #TODO docu - data should look like...
    def download_DAY_data_from_Tushare(self, symbol, ktype, start, end):
        #Check
        if start == end:
            return None
        #Download
        k_data = tushare.get_h_data(code=symbol, start=start, end=end, retry_count=5, pause=5)
        if k_data is None:
            raise Exception("Tushare.get_hist_data({symbol},{ktype},{start},{end} returns None."
                         .format(symbol=symbol,ktype=ktype,start=start,end=end))
        #Adjust Fields
        k_data = k_data.sort_index().reset_index()
        return DataSchema.addIntrinsicColumnsToData(data=k_data, code=symbol, domain=DataDomain.MICRO, type=DataType.K_DAY)

    # TODO docu - data should look like...
    def download_VOL_data_from_Tushare(self, symbol, ktype, start, end):
        #Check
        if start != end:
            raise Exception("Got an invalid tick_data download task, start-{start} != end{end} as tushare.get_tick_data only accept query by one day."
                            .format(start=start,end=end))
        #Download
        tick_data = tushare.get_tick_data(code=symbol, date=start, retry_count=5, pause=5)
        if tick_data is None:
            raise Exception("Tushare.get_tick_data({symbol},{date} returns None."
                            .format(symbol=symbol, date=start))
        #Adjust Fields
        tick_data = tick_data.sort_values(by=['time'], ascending=1)
        tick_data['date'] = start
        tick_data['DateAndTime'] = tick_data['date'] + ' ' + tick_data['time']
        tick_data = tick_data.reset_index()
        tick_data.drop('index', axis=1, inplace=True)
        return DataSchema.addIntrinsicColumnsToData(data=tick_data, code=symbol, domain=DataDomain.MICRO, type=DataType.TICK_VOL)
