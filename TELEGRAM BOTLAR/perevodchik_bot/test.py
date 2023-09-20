import requests

url = "https://gcp-translate.p.rapidapi.com/translate"


payload = {text: "botir bugun darga keldi",
src_lang: "uz",
dest_lang: "ru"
}
headers = {
"content-type": "application/json",
"X-RapidAPI-Key": "db68014164msh9c490df0d98ebe1p1da940jsn3ab2eafc0f32",
"X-RapidAPI-Host": "gcp-translate.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())