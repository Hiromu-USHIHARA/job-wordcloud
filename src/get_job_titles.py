import requests
from bs4 import BeautifulSoup

def get_job_titles(city: str, max_pages: int = 1):
    job_titles = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(1, max_pages + 1):
        url = f"https://jp.stanby.com/search?l={city}&p={page}"
        res = requests.get(url, headers=headers)

        if res.status_code != 200:
            print("取得失敗:", res.status_code)
            continue

        soup = BeautifulSoup(res.text, "html.parser")
        job_elems = soup.select("h2.title.default")

        for job in job_elems:
            text = job.get_text(strip=True)
            text = text.split("/")[0].split("／")[0].strip()
            job_titles.append(text)

    return job_titles

print(get_job_titles("渋谷", 5))
