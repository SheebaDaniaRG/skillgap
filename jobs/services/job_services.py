# ================= LIVE JOB SERVICE =================

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")


ROLE_CATEGORY = {
    "Full Stack Developer": "full stack developer",
    "Frontend Developer": "frontend developer",
    "Backend Developer": "backend developer",
    "Machine Learning Engineer": "machine learning engineer",
    "Data Scientist": "data scientist",
}


def generate_jobs(role="software developer", city="India"):

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": f"{role} jobs in {city}, India",
        "page": "1",
        "num_pages": "1"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )

        result = response.json()

        print("========== API RESPONSE ==========")
        print(result)

        jobs = []

        for job in result.get("data", []):

            jobs.append({
                "title": job.get("job_title"),
                "company": job.get("employer_name"),
                "location": job.get("job_location"),
                "link": job.get("job_apply_link"),
                "salary": job.get("job_salary_string"),
                "posted": job.get("job_posted_at")
            })

        return jobs

    except Exception as e:

        print("Job fetch error:", e)

        return []


def get_jobs(role, city):

    search_role = ROLE_CATEGORY.get(role, role)

    return generate_jobs(
        role=search_role,
        city=city
    )