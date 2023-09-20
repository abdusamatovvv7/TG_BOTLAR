import requests

url = "https://tiktok-download-without-watermark.p.rapidapi.com/analysis"

querystring = {"query":"interview preparation"}

headers = {
	"X-RapidAPI-Key": "db68014164msh9c490df0d98ebe1p1da940jsn3ab2eafc0f32",
	"X-RapidAPI-Host": "tiktok-download-without-watermark.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())