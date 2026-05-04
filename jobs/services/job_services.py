# ================= JOB DATA =================

import random

CITIES = ["Bangalore", "Hyderabad", "Mumbai", "Pune", "Chennai"]

COMPANIES = [
    "TCS", "Infosys", "Wipro", "HCL", "Zoho",
    "Freshworks", "Capgemini", "Accenture",
    "StartupX", "TechNova", "CodeLabs",
    "DevWorks", "Cloudify", "NextGenSoft"
]

JOB_TEMPLATES = {
    "backend": [
        "Backend Developer", "Python Developer", "Django Developer", "API Engineer"
    ],
    "frontend": [
        "Frontend Developer", "React Developer", "UI Engineer"
    ],
    "fullstack": [
        "Full Stack Developer", "MERN Developer", "Web Developer"
    ],
    "ml": [
        "Machine Learning Engineer", "Data Scientist", "AI Engineer"
    ]
}


# 🔥 AUTO GENERATE LARGE DATASET
JOBS = []

def generate_jobs():
    for city in CITIES:
        for category, titles in JOB_TEMPLATES.items():
            for _ in range(8):  # 👉 8 per category per city = 30+ jobs/city
                JOBS.append({
                    "title": random.choice(titles),
                    "company": random.choice(COMPANIES),
                    "location": city,
                    "category": category,
                    "url": f"https://www.linkedin.com/jobs/search/?keywords={category}&location={city}"
                })

generate_jobs()


# ================= ROLE MAP =================

ROLE_CATEGORY = {
    "Full Stack Developer": "fullstack",
    "Frontend Developer": "frontend",
    "Backend Developer": "backend",
    "Machine Learning Engineer": "ml",
    "Data Scientist": "ml"
}


# ================= FINAL SMART MATCH =================

def get_jobs(role, city):
    return [
        {
            "title": "Full Stack Developer",
            "company": "TCS",
            "location": city,
            "link": "https://www.tcs.com/careers"
        },
        {
            "title": "MERN Developer",
            "company": "Accenture",
            "location": city,
            "link": "https://www.accenture.com/in-en/careers"
        },
        {
            "title": "Web Developer",
            "company": "Infosys",
            "location": city,
            "link": "https://career.infosys.com/"
        }
    ]