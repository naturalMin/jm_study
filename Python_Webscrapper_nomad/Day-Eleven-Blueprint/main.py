import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

# 레딧 스크래핑

def get_post(html, subreddit):
  # 투표수 추출
  votes = html.find("div",{"class":"_1rZYMD_4xY3gRcSS3p8ODO"})
  if votes:
    votes = votes.string
    #k를 1000으로 변환
    if "k" in votes:
      votes = votes.replace("k","")
      votes = float(votes)*1000
  title = html.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"})
  #제목 추출
  if title:
    title = title.string
  #게시글 주소 추출  
  link = html.find("a",{"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})
  if link:
    link = link['href']
  #추출한 투표수, 제목, 주소 값 반환 (광고데이터 제외) 
  if votes and title and link:
    return {      
      'votes' : int(votes),
      'title' : title,
      'link' : link,
      'subreddit' : subreddit
      }
  
def get_subreddit(subreddit):
  #subreddit 사이트 주소 html태그 추출
  all_list = []
  
  url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
  request = requests.get(url, headers = headers)
  soup = BeautifulSoup(request.text, "html.parser")
  container = soup.find("div",{"class":"rpBJOHq2PR60pnwJlUyP0"})
  if container:
    posts = container.find_all("div",{"class":None},recursive=False)
    # recursive=False 해당 태그의 직계 자식으로 제한 find,find_all만 가능
    for post in posts:
      #추출한 html을 포스트 추출하는 함수로 보냄.
      extracted_post = get_post(post, subreddit)
      if extracted_post:
        all_list.append(extracted_post)
 
  return all_list

def aggregated(subreddit):
  aggre_list = []
  for subreddit in subreddits:
    posts = get_subreddit(subreddit)
    aggre_list = aggre_list + posts
  return aggre_list        
"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""
# 플라스크


subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]
  
app = Flask("DayEleven")

@app.route("/")
def home():
  return render_template("home.html", subreddits = subreddits) 

@app.route("/read")
def read():
  #선택된 sureddits item을 리스화
  s_list = []
  #subreddits 리스트에서 추출작업
  for subreddit in subreddits:
    if subreddit in request.args:
      #추출 후 s_list에 추가
      s_list.append(subreddit)
  #해당되는 args들에 맞게 선택된 값에 해당되는 값 추출    
  posts = aggregated(s_list) 
  #투표가 높은 순으로 정렬-내림차순
  posts.sort(key=lambda post: post['votes'], reverse=True)  
        
  return render_template("read.html",s_list = s_list, posts = posts) 
app.run(host="0.0.0.0")