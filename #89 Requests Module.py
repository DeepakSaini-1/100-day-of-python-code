import requests
from bs4 import BeautifulSoup

# response=requests.get("https://imagej.net/images/AuPbSn40.jpg")
# print(response.text)

"""url="https://jsonplaceholder.typicode.com/posts"

data={
    "title": "foo",
    "body": "bar",
    "userId": 1,
}

headers={
    'Content-type':'application/json; charset=UTF.8',
}

response=requests.post(url, headers=headers, json=data)

print(response.text)"""

# find the h,a,p in any web page

url=input("Enter the url: ")
find=input("Find any thing on web page: ")

r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")

for heading in soup.find_all(find):
    print(heading.txt)