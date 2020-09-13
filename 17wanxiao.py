import time
import datetime
import json
import requests

# 健康打卡的URL地址
check_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

text = input()
deptId = eval(input())
address = input()
addtext = input()
code = input()
stuNum = input()
userName = input()
phoneNum = input()
userId = input()
emergency = input()
emergencyPhone = input()
sckey = input()


area = {'address': address, 'text': addtext, 'code': code}

areaStr = json.dumps(area, ensure_ascii=False)

# POST提交的json字段，根据自己的修改
jsons = {"businessType": "epmpics", "method": "submitUpInfo",
         "jsonData": {"deptStr": {"deptid": deptId, "text": text},
                      "areaStr": areaStr,
                      "reportdate": round(time.time() * 1000), "customerid": "1999", "deptid": deptId, "source": "app",
                      "templateid": "pneumonia", "stuNo": stuNum, "username": userName, "phonenum": phoneNum,
                      "userid": userId, "updatainfo": [{"propertyname": "bodyzk", "value": "正常温度(小于37.3)"},
                                                          {"propertyname": "istouchcb", "value": "在校（含当日在校内居住）"},
                                                          {"propertyname": "sfwz2", "value": "内地学生"},
                                                          {"propertyname": "symptom", "value": "无"},
                                                          {"propertyname": "homehealth", "value": "无"},
                                                          {"propertyname": "isConfirmed", "value": "无"},
                                                          {"propertyname": "ownbodyzk", "value": "良好"},
                                                          {"propertyname": "ishborwh", "value": "无"},
                                                          {"propertyname": "outdoor", "value": "绿色"},
                                                          {"propertyname": "ownPhone", "value": phoneNum},
                                                          {"propertyname": "emergencyContact", "value": emergency},
                                                          {"propertyname": "mergencyPeoplePhone",
                                                           "value": emergencyPhone}], "gpsType": 0}}
response = requests.post(check_url, json=jsons)
# 以json格式打印json字符串
res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)

SCKEY = sckey

now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

test_day = datetime.datetime.strptime('2020-12-19 00:00:00', '%Y-%m-%d %H:%M:%S')
date = (test_day - bj_time).days
desp = f"""
------
### 现在时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
------
| Text                           | Message |
| :----------------------------------- | ---: |
| 专业/部门                            | {text} |
| 姓名                                 | {userName}  |
| 学号                                 |  {stuNum}    |
| 当前位置                             |   {address}   |
| 今日体温                             |   正常温度(小于37.3)   |
| 自己当日所在位置                     |   在校（含当日在校内居住）   |
| 身份类别                             |   内地学生   |
| 是否出现可以症状                     |   无   |
| 是否存在高危行为                      |    无  |
| 被要求采取医学措施                    |   无   |
| 家庭成员身体状况                      |   良好   |
| 所在小区是否有疫情                   |   无   |
| 居民健康码颜色                       |   绿色   |
| 本人电话                             |  {phoneNum}    |
| 紧急联系人姓名                       |    {emergency}  |
| 紧急联系人电话                       |  {emergencyPhone}    |
------
```
{res}
```
> 关于打卡信息
>
> 1、成功则打卡成功
>
> 2、系统异常则是打卡频繁

### ⚡考研倒计时:
```
{date}天
```

>
> [GitHub项目地址](https://github.com/ReaJason/17wanxiaoCheckin-Actions) 
>
>期待你给项目的star✨
"""

headers = {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

send_url = f"https://sc.ftqq.com/{SCKEY}.send"

params = {
    "text": f"完美校园健康打卡---{bj_time.strftime('%m-%d')}",
    "desp": desp
}

# 发送消息
response = requests.post(send_url, data=params, headers=headers)
if response.json()["errmsg"] == 'success':
    print("Server酱推送服务成功")
else:
    print("Server酱推送服务失败")
