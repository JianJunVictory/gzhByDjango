import json
import os
file=os.path.split(os.path.realpath(__file__))[0]+'\\wechat.txt'
class Option(object):
    def __init__(self):
        self.appId="wx2e0eb153224d114c"
        self.appsecret="756ba0d940017ccd4658894cea69c630"
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
