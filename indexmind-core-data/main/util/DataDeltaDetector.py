

class DataDeltaDetector():
    def __init__(self, dataType, newData, code):
        # Basic Type
        self.dataType = dataType
        self.code = code
        # New & Old Data
        self.newData = newData
        self.hasOldData, self.oldData = readOldData()


    def diff(self, newData, code):
        # Read Old Data
        oldData = readOldData(code)
        #
        sql = diffSQL(self.dataType)


    def readOldData(self):
        pass



    def diffSQL(self):
        return {
            'a':1,
            'b':2
        }[self.dataType]
