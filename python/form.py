import requests
import smtplib #smtp服务器
from email.mime.text import MIMEText #邮件文本
import pymysql

cookies = {
    "SESSION": "MTBjMTg3OWYtMGYwNC00ZWM1LThmOTYtNjUxYzJhMGI1ZWRl",#填写你抓包得到的SEESION
    "path": "/",
}

headers = {
    "Host": "student.wozaixiaoyuan.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/4G Language/zh_CN",
    "Referer": "https://servicewechat.com/wxce6d08f781975d91/147/page-frame.html",
    "token": "",#填写token
    "Content-Length": "340",
}

# data = {
#   "answers": '["0","36.5","36.4","36.1"]',#这是提交的每个选项 0无异常
#   "latitude": "29.83321252",
#   "longitude": "115.21385372",
#   "country": "中国",#国家
#   "city": "黄石市",#黄石市
#   "district": "阳新县",#下陆区
#   "province": "湖北省",#湖北省
#   "township": "五马坊",#团城山街道
#   "street": "",#团城山
#   "areacode": ""
# }
data = {
  "answers": '["0","36.5","36.4","36.1"]',
  "latitude": "",
  "longitude": "",
  "country": "",
  "city": "",
  "district": "",
  "province": "",
  "township": "",
  "street": "",
  "areacode": ""
}

# 邮件发送函数
def sendemail(receiver,content):
    subject = "我不在校园"#邮件标题
    sender = "jarry599@163.com"#发送方
    recver = receiver #接收方
    password = "ARZADNKQAKCEDWII"
    message = MIMEText(content,"plain","utf-8")
    #content 发送内容     "plain"文本格式   utf-8 编码格式
    message['Subject'] = subject #邮件标题
    message['To'] = recver #收件人
    message['From'] = sender #发件人
    smtp = smtplib.SMTP_SSL("smtp.163.com",994) #实例化smtp服务器
    smtp.login(sender,password)#发件人登录
    smtp.sendmail(sender,[recver],message.as_string()) #as_string 对 message 的消息进行了封装
    smtp.close()

# 定义一个数组存储所有用户
infoDict = {
    'user_id':[],
    'name':[],
    'token':[],
    'email':[]
}
# 获取用户信息存到infoDict中
def getInfo():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "jia599599", "book")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "select user_id,name,token,email from stu_info"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            infoDict['user_id'].append(row[0])
            infoDict['name'].append(row[1])
            infoDict['token'].append(row[2])
            infoDict['email'].append(row[3])
            # print(row)
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
getInfo()

infoPosition = {
  "latitude": "",
  "longitude": "",
  "country": "",#国家
  "city": "",#黄石市
  "district": "",#下陆区
  "province": "",#湖北省
  "township": "",#团城山街道
  "street": "",#团城山
}
def getPosition(email):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "jia599599", "book")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "select * from stu_position where email='"+email+"'"
    # sql = "select * from stu_position where email='1197780293@qq.com'"
    
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            infoPosition['latitude'] = row[2]
            infoPosition['longitude'] = row[3]
            infoPosition['country'] = row[4]
            infoPosition['city'] = row[5]
            infoPosition['district'] = row[6]
            infoPosition['province'] = row[7]
            infoPosition['township'] = row[8]
            infoPosition['street'] = row[9]
            
            return row
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()


def autoForm():
    #response = requests.post('https://student.wozaixiaoyuan.com/health/save.json', headers=headers, cookies=cookies, data=data).json()
    response = requests.post('https://student.wozaixiaoyuan.com/health/save.json', headers=headers,data=data).json()
    r=response['code']
    return response
    # if(r==0):
    #     requests.get(
    #         "http://miaotixing.com/trigger",
    #         {
    #             "id": "t5yTeP0",
    #             "text": "用户token:" + str(headers["token"]) + '\n' + "打开成功",
    #             "type": "json"
    #         }
    #     )
    #     print("打卡成功")
    #     return r
    # else:
    #     requests.get(
    #         "http://miaotixing.com/trigger",
    #         {
    #             "id": "t5yTeP0",
    #             "text": "用户token:" + str(headers["token"]) + '\n' + "打开失败 请更换token",
    #             "type": "json"
    #         }
    #     )
    #     print("打卡失败")
    #     return -1


# 获取每日妙语
def getWitticism():
    response = requests.get('http://api.tianapi.com/txapi/sentence/index?key=75f59f3f6f98a4a4e3c0c869cb303614').json()
    #print(response)
    if(response['code'] == 200):
        #print(response['newslist'][0]['content'])
        content = response['newslist'][0]['content']
        return content
        
def main():
    i=0
    count = 1
    for val in infoDict['token']:
        headers['token'] = val
        #根据邮箱获取到位置信息
        getPosition(infoDict['email'][i])
        #更新data
        data['latitude'] = infoPosition['latitude']
        data['longitude'] = infoPosition['longitude']
        data['country'] = infoPosition['country']
        data['city'] = infoPosition['city']
        data['district'] = infoPosition['district']
        data['province'] = infoPosition['province']
        data['township'] = infoPosition['township']
        data['street'] = infoPosition['street']
        
        print(data)
       
        # 执行签到
        response = autoForm()
        
        # print(state)
        if(response['code']==0):
            text = "姓名:"+infoDict['name'][i]+"\ntoken:"+val+"\n打卡成功啦！奥里给~\n"+getWitticism();
            sendemail(infoDict['email'][i],text)
            print("第"+str(count)+"个")
            print("打卡成功")
        elif(response['code']==1):
            m=response['message']
            text = "姓名:"+infoDict['name'][i]+"\ntoken:"+val+"\n今日打卡已结束 明天依旧光芒万丈噢 晚安宝贝儿~\n"+"message:"+m+"\n"+getWitticism();
            sendemail(infoDict['email'][i],text)
            print(m)
            print("第"+str(count)+"个")
        else:
            m=response['message']
            text = "姓名:"+infoDict['name'][i]+"\ntoken:"+val+"\n打卡失败，请更新token或检查信息是否填写正确\n"+"message:\n"+"将姓名与token发送至邮箱：jarry599@163.com\n我看到了就会更新";
            sendemail(infoDict['email'][i],text)
            print(m)
            print("打卡失败")
            print("第"+str(count)+"个")
        # print(val)
        # print(infoDict['name'][i])
        # print(infoDict['email'][i])
        i=i+1
        count=count+1

if __name__ == '__main__':
    main()