import requests
import json

url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

querystring = {"url":"https://www.tiktok.com/@tiktok/video/7106658991907802411","hd":"1"}

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

bir = response.json()
with open('new.json', 'w+') as file:
    json.dump(bir, file)


# import requests
# def audio_yukla_ber(video_id):
# 	url = "https://youtube-mp36.p.rapidapi.com/dl"

# 	querystring = {"id":video_id}

# 	headers = {
# 		"X-RapidAPI-Key": "",
# 		"X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
# 	}

# 	response = requests.get(url, headers=headers, params=querystring)
# 	return response.json()['link']


# import requests

# def video_yuklab_ber(link):
# 	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

# 	querystring = {"url": link}

# 	headers = {
# 		"X-RapidAPI-Key": "",
# 		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
# 	}

# 	response = requests.get(url, headers=headers, params=querystring)
# 	return response.json()['media']










# print(video_yuklab_ber("https://www.instagram.com/reel/CsTqWJCoEAt/"))


# import requests

# url = "https://instagram-scraper-2022.p.rapidapi.com/ig/user_id/"

# querystring = {"user":"cr7cristianoronaldo"}

# headers = {
# 	"X-RapidAPI-Key": "",
# 	"X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
