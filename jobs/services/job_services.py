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
    role = role.strip()
    city = city.strip().lower()

    category = ROLE_CATEGORY.get(role)

    if not category:
        return []

    # 🔥 STRICT FILTER FIRST
    exact = [
        job for job in JOBS
        if job["category"] == category and job["location"].lower() == city
    ]

    # 🔥 RELAX FILTER (same category anywhere)
    relaxed = [
        job for job in JOBS
        if job["category"] == category
    ]

    # 🔥 FINAL FALLBACK (same city any role)
    city_only = [
        job for job in JOBS
        if job["location"].lower() == city
    ]

    results = exact if exact else relaxed if relaxed else city_only

    return results[:12]  # 🔥 always show 10+ jobs