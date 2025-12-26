import requests
from bs4 import BeautifulSoup as bs
from flask import Flask

resp = requests.get(
        f"https://www.linkedin.com/jobs/search?keywords=frontend%20developer&location=Nepal&geoId=104630404&position=1&pageNum=0"
    )
soup = bs(resp.content, "html.parser")

jobInfoCards = soup.find_all("div", class_="base-card")

for jobInfo in jobInfoCards:
        try:
            title = jobInfo.find("h3").text.strip()
            link = jobInfo.find("a", class_="base-card__full-link")["href"]
            company = jobInfo.find("h4").text.strip().replace(",", "")
            location = (
                jobInfo.find("span", class_="job-search-card__location")
                .text.strip()
                .replace(",", "")
            )
            print(location)
            with open("jobs.csv", "a", encoding="utf-8") as f:
                f.writelines(f"{title},{location},{company},{link}\n")

        except:
            pass
print("added !!")