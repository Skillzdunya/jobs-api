"""Fetch open government jobs for fresh graduates from the SkillzDunya Jobs API."""
import json
import urllib.request

URL = "https://skillzdunya.com/api/v1/jobs?government=1&experience_max=0&status=open&per_page=10"

with urllib.request.urlopen(URL, timeout=30) as resp:
    jobs = json.load(resp)["data"]

for job in jobs:
    print(f'{job["title"]} | last date: {job.get("deadline") or "see ad"} | {job["url"]}')
