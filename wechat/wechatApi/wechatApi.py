from .config import Option
import time
import requests
import json
from .menu import menu
#https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
#https://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN
Prefix="https://api.weixin.qq.com/cgi-bin/"

class Wechat(Option):
    def __init__(self):
        super(Wechat,self).__init__()
    def fetchAccessToken(self):
        tokenData=self.getAccessToken()
        print(tokenData)
        if tokenData["access_token"] and tokenData["expires_in"]:
            if self.isValidToken(tokenData):
                return tokenData
            else:
                tokenData=self.updateToken()
                self.saveAccessToken(tokenData)
                return tokenData
        else:
            tokenData=self.updateToken()
            self.saveAccessToken(tokenData)
            return tokenData

    def isValidToken(self,datas):
        nowTime=int(time.time())
        if datas["expires_in"] <= nowTime:
            return False
        else:
            return True
    def updateToken(self):
        nowTime=int(time.time())
        url=Prefix+'token'
        payload={'grant_type': 'client_credential','appid': self.appId,'secret': self.appsecret}
        rsp=requests.get(url, params=payload)
        AccessData=rsp.json()
        AccessData['expires_in']=nowTime+(AccessData['expires_in']-20)*1000
        return AccessData
    def creatMenu(self):
        AccessData=self.fetchAccessToken()
        print(AccessData["access_token"])
        url=Prefix+'menu/create?access_token='+AccessData["access_token"]
        # headers = {'content-type': 'application/json'}
        # if isinstance(menu, str):
        #     menu = menu.encode('utf-8')
        rsp=requests.post(url,data=menu.encode('utf-8'))
        respData=rsp.json()
        print(respData)
        if respData["errcode"]==0:
            return True
        else:
            return False


        
        

        


    
