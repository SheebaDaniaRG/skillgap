# 🔥 STATIC JOB DATA

JOBS = [
    {"title": "Full Stack Developer", "company": "Infosys", "location": "Bangalore", "address": "Electronic City Phase 1"},
    {"title": "Backend Developer", "company": "TCS", "location": "Chennai", "address": "OMR Road"},
    {"title": "Frontend Developer", "company": "Wipro", "location": "Hyderabad", "address": "Hitech City"},
    {"title": "Full Stack Developer", "company": "Accenture", "location": "Pune", "address": "Hinjewadi Phase 2"},
    {"title": "Backend Developer", "company": "Capgemini", "location": "Mumbai", "address": "Airoli"},
    {"title": "Frontend Developer", "company": "HCL", "location": "Bangalore", "address": "Whitefield"},
]


# 🔥 SMART JOB MATCHING + RANKING
def get_jobs(role, city):
    role = role.lower()
    city = city.lower()

    scored_jobs = []

    for job in JOBS:
        job_role = job["title"].lower()
        job_city = job["location"].lower()

        if job_city != city:
            continue

        score = 0

        # 🔥 EXACT MATCH → highest priority
        if role == job_role:
            score += 3

        # 🔥 PARTIAL MATCH
        elif role in job_role or job_role in role:
            score += 2

        # 🔥 KEYWORD MATCH
        elif any(word in job_role for word in role.split()):
            score += 1

        if score > 0:
            scored_jobs.append((score, job))

    # 🔥 SORT BY BEST MATCH
    scored_jobs.sort(reverse=True, key=lambda x: x[0])

    # return only jobs (remove scores)
    return [job for _, job in scored_jobs]