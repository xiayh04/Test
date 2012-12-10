'''
Created on 2012-11-2

@author: yhxia
'''
import json
def getJsonStr():
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    print 'DATA:', repr(data)
    data_string = json.dumps(data)
    print 'dumps(data, separators):', json.dumps(data, separators=(',',':'))#只保留':',','作为分隔符
    print 'JSON:', data_string
if __name__ == '__main__':
    getJsonStr()