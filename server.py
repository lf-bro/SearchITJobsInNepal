import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify, render_template, redirect, url_for
import json
import scrap
# import intojson
import jsonread

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("searchjob.html")


@app.route("/search")
def search():
    return render_template("jobresult.html")


@app.route("/jobs")
def jobs():
    with open("jobs.json", "r", encoding="utf-8") as f:
        return jsonify(json.loads(f.read()))


@app.route("/scrape/<topic>")
def scrape(topic):
    resp = requests.get(
        f"https://www.linkedin.com/jobs/search?keywords={topic}&location=Nepal&geoId=104630404&position=1&pageNum=0"
    )
    soup = bs(resp.content, "html.parser")

    jobInfoCards = soup.find_all("div", class_="base-card")

    for jobInfo in jobInfoCards:
        try:
            title = jobInfo.find("h3").text.strip().replace(",", "")
            link = jobInfo.find("a", class_="base-card__full-link")["href"]
            company = jobInfo.find("h4").text.strip().replace(",", "")
            location = (
                jobInfo.find("span", class_="job-search-card__location")
                .text.strip()
                .replace(",", "")
            )
            # image = jobInfo.find("img", class_="artdeco-entity-image")["src"]
            with open("jobs.csv", "a", encoding="utf-8") as f:
                f.writelines(f"{title},{location},{company},{link}\n")
        except:
            pass
    # intojson.convert_csv_to_json()
    # scrap.scrap(topic)
    jsonread.readjson()
    return redirect(url_for("search"))


app.run(debug=True)
