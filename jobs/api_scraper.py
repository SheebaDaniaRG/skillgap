import http.client
import json
import urllib.parse

from .models import Job, Skill
from .utils import extract_skills


def fetch_jobs_from_api():
    print("🚀 Fetching jobs from API...")

    conn = http.client.HTTPSConnection("jobs-api14.p.rapidapi.com")

    headers = {
        "x-rapidapi-key": "YOUR_API_KEY_HERE",
        "x-rapidapi-host": "jobs-api14.p.rapidapi.com"
    }

    query = urllib.parse.quote("python developer")
    location = urllib.parse.quote("India")

    conn.request(
        "GET",
        f"/v2/bing/search?query={query}&location={location}",
        headers=headers
    )

    res = conn.getresponse()
    data = res.read()

    jobs_json = json.loads(data.decode("utf-8"))

    print("🔍 DEBUG RESPONSE:")
    print(jobs_json)

    job_list = jobs_json.get("data")

    if isinstance(job_list, dict):
        job_list = job_list.get("jobs", [])

    if not job_list:
        job_list = jobs_json.get("jobs", [])

    if not job_list:
        print("❌ No jobs found")
        return

    count = 0

    for job in job_list:
        title = job.get("title") or job.get("job_title") or "No Title"
        company = job.get("company") or job.get("employer_name") or "Unknown"
        description = job.get("description") or job.get("job_description") or ""

        if not description:
            continue

        job_obj, created = Job.objects.get_or_create(
            title=title,
            company=company,
            defaults={"description": description}
        )

        skills = extract_skills(description)

        for skill_name in skills:
            skill_obj, _ = Skill.objects.get_or_create(name=skill_name)
            job_obj.skills.add(skill_obj)

        if created:
            count += 1

    print(f"✅ Added {count} API jobs with skills")