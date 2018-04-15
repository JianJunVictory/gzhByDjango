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

    #处理access_token的api
    def fetchAccessToken(self):
        tokenData=self.getAccessToken()
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

    #创建，删除，获取菜单api，个性化菜单此处省略
    def creatMenu(self,menu=menu):
        AccessData=self.fetchAccessToken()
        url=Prefix+'menu/create?access_token='+AccessData["access_token"]
        rsp=requests.post(url,data=menu.encode('utf-8'))
        respData=rsp.json()
        if respData["errcode"]==0:
            return True
        else:
            return False
    
    def deteleMenu(self):
        AccessData=self.fetchAccessToken()
        url=Prefix+'menu/delete?access_token='+AccessData["access_token"]
        rsp=requests.get(url)
        respData=rsp.json()
        if respData["errcode"]==0:
            return True
        else:
            return False

    def getMenu(self):
        AccessData=self.fetchAccessToken()
        url=Prefix+'menu/get?access_token='+AccessData["access_token"]
        rsp=requests.get(url)
        respData=rsp.json()
        return respData

    #素材管理接口

        
        

        


    
