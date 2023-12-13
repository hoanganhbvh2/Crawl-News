import requests
from bs4 import BeautifulSoup
# URL của trang web bạn muốn crawl
url = 'https://dantri.com.vn/tin-moi-nhat.htm'
# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không (status code 200)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích HTML của trang web
    soup = BeautifulSoup(response.text, 'html.parser')
    content_page = soup.find_all('div', class_='article-content')
    # context1_content = soup.find_all('div', class_='article-excerpt')
else:
    print(f'Yêu cầu không thành công, mã lỗi: {response.status_code}')
#Hiển thị nội dung ở trang chính
time=0
print( 'TỔNG HỢP : Tin hot của Dân trí ngày tức thì')
print("\033[1m************************* Tin hot của Dân trí :***********************\033[0m")
for article in content_page:
    time+=1
    print("\033[1m---------------------------TIN NỔI BẬT SỐ:%s----------------------------\033[0m"%time)
    print("\033[1mTiêu Đề :\033[0m")
    print(article.contents[0].text)
    print("\033[1m Nội dung :\033[0m")
    print(article.contents[1].text)
    if(time==3):
        break
