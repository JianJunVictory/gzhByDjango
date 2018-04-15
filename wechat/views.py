from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .wechatApi.wechatApi import Wechat

@csrf_exempt
def index(request):
    if request.method=="GET":
        print("good")
        #接收微信服务器get请求发过来的参数
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']
        print(timestamp)
        #服务器配置中的token
        token = 'guangxinxi'
         #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr.encode(encoding='utf-8')).hexdigest()
        print(hashstr)
        
        if hashstr == signature:
          return HttpResponse(echostr)
        else:
          return HttpResponse("field")
    else:
        
        othercontent = autoreply(request)
        return HttpResponse(othercontent)
        return HttpResponse("hello")
    
import xml.etree.ElementTree as ET
def autoreply(request):
    #wechat= Wechat() 后面直接调用wechat对象的方法

    webData = request.body
    xmlData = ET.fromstring(webData)

    msg_type = xmlData.find('MsgType').text
    ToUserName = xmlData.find('ToUserName').text
    FromUserName = xmlData.find('FromUserName').text
    CreateTime = xmlData.find('CreateTime').text
    MsgType = xmlData.find('MsgType').text
    MsgId = xmlData.find('MsgId').text

    toUser = FromUserName
    fromUser = ToUserName

    if msg_type == 'text':
        content = "您好,欢迎关注微信号"
        replyMsg = TextMsg(toUser, fromUser, content)
        print ("返回数据：%s"%replyMsg)
        return replyMsg.send()

    elif msg_type == 'image':
        content = "图片"
        replyMsg = TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    elif msg_type == 'voice':
        content = "语音"
        replyMsg = TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    elif msg_type == 'video':
        content = "视频"
        replyMsg = TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    elif msg_type == 'shortvideo':
        content = "小视频"
        replyMsg = TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    elif msg_type == 'location':
        content = "位置"
        replyMsg = TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    else:
        msg_type == 'link'
        content = "链接"
        replyMsg = TextMsg(toUser, fromUser, content)
        return replyMsg.send()



class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text

import time
class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)