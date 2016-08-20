from main.task import TaskType
from main.data.DataSchema import DataSchema
from main.common import DataConfig
APPEND_WRITE = 'append'
PARQUET_FORMAT = 'parquet'
PARTITION_EVERY_UPDATE = 1

class DataParquetWriter():
    def __init__(self, sqlContext, data, taskType, code):
        self.sqlContext = sqlContext
        self.data = data
        self.taskType = taskType
        pass

    def get_writer(self, dfInSpark):
        # TODO: ktype - dataInterval
        # include write mode and partitionby here
        return {
            TaskType.MACRO: dfInSpark.coalesce(PARTITION_EVERY_UPDATE)
                .write.mode(APPEND_WRITE)
                .partitionBy('code'),
            TaskType.MICRO_STOCK_DAY_VAL: dfInSpark.coalesce(PARTITION_EVERY_UPDATE)
                .write.mode(APPEND_WRITE)
                .partitionBy(**TaskType.MICRO_STOCK_DAY_VAL.MICRO_STOCK_VALUE_DAY_DATA.value.partitionByColumns),
            TaskType.MICRO_STOCK_VOL: dfInSpark.coalesce(PARTITION_EVERY_UPDATE)
                .write.mode(APPEND_WRITE)
                .partitionBy(**TaskType.MICRO_STOCK_VOL.MICRO_STOCK_VOLUME_DATA.value.partitionByColumns)
        }[self.taskType]

    def data_path(self):
        return DataConfig.DATA_ROOT

    def write(self):
        # TODO: path
        path = self.data_path()
        dfInSpark = self.sqlContext.createDataFrame(self.data)
        dfWriter = self.get_writer(dfInSpark)
        dfWriter.save(path, format=PARQUET_FORMAT)
