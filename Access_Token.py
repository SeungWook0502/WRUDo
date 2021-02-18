import requests
import json

#https://kauth.kakao.com/oauth/authorize?client_id=a8cb3627761dffc8aa80a5c461e1b64e&response_type=code&redirect_uri=https://localhost.com&scope=talk_message

url = "https://kauth.kakao.com/oauth/token"

data = {
	
	"grant_type" : "authorization_code",
	"client_id" : "a8cb3627761dffc8aa80a5c461e1b64e",
	"redirect_url" : "https://localhost.com",
	"code" : "Wmnrr2LkQupZu0mVxNQsF1Py-CX_X2kT06qlpSPGgNIMmcnXhxN_TF_cIoVQzWscjf6MBgo9c5oAAAF3pYMTBQ"
}

response = requests.post(url,data=data)

tokens= response.json()

with open("kakao_token.json","w") as fp:
	json.dump(tokens,fp)

print(tokens)