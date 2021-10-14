import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.

new = f"{base_url}/search_by_date?tags=story"
n_result = requests.get(new)


# This URL gets the most popular stories

popular = f"{base_url}/search?tags=story"
p_result = requests.get(popular)

 
# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api

def make_detail_url(id):
  return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  #메인페이지는 popular로 설정.
  order_by = request.args.get("order_by", "popular")
  #popular 데이터가 fakeDB에 없을경우.
  if order_by not in db:
    print("Requesting thd data...Wait a minutes..")
    #/?order_by = popular인 경우
    if order_by == "popular":
      news = p_result
    #/?order_by = new인 경우  
    elif order_by == "new":
      news = n_result
    #api문서 'hits'부분 추출  
    results = news.json()['hits']
    #추출한 results 데이터를 fakeDB에 넣는다.
    db[order_by] = results
  else:
    #fakeDB에 데이터가 있는경우, DB 안에서 가져온다. = 좀 더 빠른 스크래핑을 위함  
    results = db[order_by]
  #index.html에 반영  
  return render_template("index.html", order_by = order_by, results = results)    

@app.route("/<id>")
def detail(id):
  #id에 따른 api호출
  d_request = requests.get(make_detail_url(id))
  result = d_request.json()
  #detail.html에 반영
  return render_template("detail.html", result = result) 

app.run(host="0.0.0.0")