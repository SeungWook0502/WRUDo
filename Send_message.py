import requests
import json

with open("kakao_token.json","r") as fp:
	tokens = json.load(fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + tokens['access_token']
}
data = {
    "template_object" : json.dumps({
        "object_type" : "text",
        "text" : "머하냐",
        "link" : {
        	"web_url" : "https://naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.json())