import requests

url = "https://dapi.kakao.com/v2/search/image"
headers = {
	"Authorization" : "KakaoAK a8cb3627761dffc8aa80a5c461e1b64e"
}
data = {
	"query" : "펭수"
}

reponse = requests.get(url, headers=headers, data=data)

print(reponse.json())