import http.client
import json
import urllib.parse

# 🔗 Create connection
conn = http.client.HTTPSConnection("jobs-api14.p.rapidapi.com")

# 🔐 Headers
headers = {
    "x-rapidapi-key": "19fde17561msh28e9f2774405f0bp1a75cajsnb56852b9b776",
    "x-rapidapi-host": "jobs-api14.p.rapidapi.com"
}

# 🔍 Encode query
query = urllib.parse.quote("python developer")

# 📍 Location (IMPORTANT)
location = urllib.parse.quote("India")

# 📡 Request
conn.request(
    "GET",
    f"/v2/bing/search?query={query}&location={location}",
    headers=headers
)

# 📥 Response
res = conn.getresponse()
data = res.read()

# 📊 Convert JSON
jobs = json.loads(data.decode("utf-8"))

# ==============================
# 🔥 NEW PART (THIS IS WHAT I ASKED)
# ==============================

job_list = jobs.get("data", [])

print("\n🚀 TOP JOBS:\n")

for job in job_list[:5]:
    print("TITLE:", job.get("job_title"))
    print("COMPANY:", job.get("employer_name"))
    print("LOCATION:", job.get("job_location"))
    print("-" * 40)