import requests
from bs4 import BeautifulSoup as bs

resp = requests.get(
    "https://www.linkedin.com/jobs/search?keywords=frontend&location=Nepal"
)
soup = bs(resp.content, "html.parser")

jobInfoCards = soup.find_all("div", class_="base-card")
for jobInfo in jobInfoCards:
    try:
        title = jobInfo.find("h3").text.strip().replace(",", "")
        link = jobInfo.find("a", class_="base-card__full-link")["href"]
        image = jobInfo.find("img")["src"]
        company = jobInfo.find("h4").text.strip().replace(",", "")
        location = (
            jobInfo.find("span", class_="job-search-card__location")
            .text.strip()
            .replace(",", "")
        )
        print(image)
        # with open("jobs.csv", "a", encoding="utf-8") as f:
        # f.writelines(f"{title},{location},{company},{link}\n")
    except:
        pass
# intojson.convert_csv_to_json()
