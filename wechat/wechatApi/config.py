import json
import os
file=os.path.split(os.path.realpath(__file__))[0]+'\\wechat.txt'
class Option(object):
    def __init__(self):
        self.appId="**********************"
        self.appsecret="************************"
        self.token="guangxinxi"
        
    def getAccessToken(self):
        f=open(file,'r')
        accessToken=f.read()
        resu=json.loads(accessToken)
        f.close()
        return resu
    def saveAccessToken(self,data):
        strData=json.dumps(data);
        f=open(file,'w')
        f.write(strData)
        f.close()
