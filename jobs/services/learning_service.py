import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")


def get_courses(skills):

    results = []

    for skill in skills:

        results.append({
            "skill": skill,
            "title": f"Best {skill} Courses",
            "platform": "Search",
            "link": f"https://www.coursera.org/search?query={skill}"
        })

        results.append({
            "skill": skill,
            "title": f"{skill} Full Course",
            "platform": "YouTube",
            "link": f"https://www.youtube.com/results?search_query={skill}+full+course"
        })

    return results