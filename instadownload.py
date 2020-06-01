import requests
from bs4 import BeautifulSoup

def requests_start_url(start_url):
    try:
        response = requests.get(start_url)
        html = response.text
        return html
    except:
        print('Opps! Occurred error')
        return 'Error occurred while requesting given url'

 
 
def find_photo_url(requests_url, 'lxml'):
    try:
        soup = BeautifulSoup(requests_url)
        photo_url = soup.find("meta", property="og:image")
        return photo_url["content"]
    except Exception as e:
        return str(e)

 
# def downloader(photo_url):
#     #extract some character of photo_url in order to name the photo 
#     photo_name = str(randint(1000,9999))
#     print('Photo name is:'+ photo_name)
#     requests_url = requests.get(photo_url)
#     f = open(photo_name + '.jpg', 'ab')
#     f.write(requests_url.content)
#     print('Processing')
#     f.close()
#     print('Download complete')
 
 
def main(url):
    requests_url = requests_start_url(url)
    photo_url = find_photo_url(requests_url)
    return photo_url
    # downloader(photo_url)
