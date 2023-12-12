import requests
from bs4 import BeautifulSoup

# URL của trang web bạn muốn crawl
url = 'https://example.com'

# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không (status code 200)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích HTML của trang web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ví dụ: Trích xuất tiêu đề của trang web
    title = soup.title.text
    print(f'Tiêu đề trang web: {title}')

    # Ví dụ: Trích xuất tất cả các liên kết trong trang
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

else:
    print(f'Yêu cầu không thành công, mã lỗi: {response.status_code}')
