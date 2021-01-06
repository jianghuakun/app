#!/usr/bin/python3
import requests
import json
'''终上所述，json与eval区别有两点：

1、json.loads与eval都能将s转成python中的对象，json.loads将json中的字符串转成unicode(types.UnicodeType)，eval转成了str(types.StringType)。

2、json不认单引号，json中的字符串需要用双引号包起来'''
usl1='http://web.xiaoqiu.tv/system/userLogin'
payload1={
            "userName": "1jianghuakun",
            "password": "dd6e5e5918e94d997c686fcebc56922f"
        }
headers1={'content-type':'application/json;charset=utf-8',
          'Accept':'application/json;charset=utf-8'
          }
r=requests.post(usl1,data=json.dumps(payload1),headers=headers1)
dict1=dict(r.json())
jsession2 = dict(r.cookies)['JSESSIONID']
print(r.headers)
print(r.status_code,r.json())
#userId=dict1['data']['userInfo']['id']
headers={'content-type':'application/json;charset=utf-8',
          'Accept':'application/json;charset=utf-8','Cookie':'JSESSIONID=%s'%jsession2}
url='https://9ecd0964-8f09-4608-892e-589c98eeb69c.mock.pstmn.io/game/delete'
headers2={'content-type':'application/json;charset=utf-8',
          'Accept':'application/json;charset=utf-8'

          }
data={
    "id": "1564646464"
}
result=requests.post(url,data=json.dumps(data),headers=headers2)
#print(result.headers)
#print(result.json())


