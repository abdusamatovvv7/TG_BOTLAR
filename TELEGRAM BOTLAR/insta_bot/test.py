import requests

def video_yuklab_ber(link):
    url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"
    
    querystring = {"url":link}
    
    headers = {
    	"X-RapidAPI-Key": "db68014164msh9c490df0d98ebe1p1da940jsn3ab2eafc0f32",
    	"X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    return response.json()['media']