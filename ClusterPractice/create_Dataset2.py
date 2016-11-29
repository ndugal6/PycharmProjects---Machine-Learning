#!/usr/bin/python3


class CustomDataSet:

    def __init__(self, **kwargs):
        self.properties = dict(data=[],target=[])


    def loadInfo(self):
        return self.properties

    def get_properties(self):
        return self.properties

    def get_properties(self, key):
        return self.properties.get(key, None)

    @property
    def data(self):
        return self.properties['data']

    @data.setter
    def data(self, key):
        datas = self.properties['data']
        self.properties.update(data=datas + key)

    @data.deleter
    def data(self):
        del self.properties['data']

    @property
    def target(self):
        return self.properties['target']

    @target.setter
    def target(self, key):
        self.properties['target'] = key
        #tars = self.properties['target']
        #self.properties.update(target=tars+key)

    @target.deleter
    def target(self):
        del self.properties['target']

def main():
    dic = dict(data=[1, 2], target=[3,4])
    ds = CustomDataSet()
    ds.target = dic['target']
    ds.data = dic['data']
    ds.data = dic['data']

    ds.loadInfo()
    var = ds.data
    print(var)
    print(ds.target)

if __name__ == "__main__": main()

