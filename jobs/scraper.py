import requests
from bs4 import BeautifulSoup

from .models import Job, Skill
from .utils import extract_skills


def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"

    print("🚀 Scraping jobs...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    count = 0

    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p", class_="location").text.strip()

        content_div = job.find("div", class_="content")
        description = content_div.get_text(separator=" ").strip()

        # ✅ Create job
        job_obj, created = Job.objects.get_or_create(
            title=title,
            company=company,
            defaults={
                "location": location,
                "description": description
            }
        )

        # 🔥 STEP 1: Base extraction
        combined_text = f"{title} {company} {description}"
        extracted_skills = extract_skills(combined_text)

        title_lower = title.lower()

        # 🔥 STEP 2: STRONG ROLE-BASED ENRICHMENT (ALWAYS APPLIES)

        role_map = {
            "developer": ["python", "django", "sql", "git"],
            "engineer": ["c", "linux", "problem solving", "algorithms"],
            "data": ["python", "sql", "excel", "machine learning"],
            "analyst": ["python", "sql", "excel", "statistics"],
            "manager": ["management", "communication", "leadership"],
            "designer": ["ui/ux", "figma", "creativity"],
            "executive": ["communication", "management"],
            "officer": ["communication", "management"],
            "health": ["risk management", "compliance"],
            "safety": ["risk management", "compliance"],
            "programmer": ["python", "algorithms", "data structures"],
        }

        for key, skills in role_map.items():
            if key in title_lower:
                extracted_skills.extend(skills)

        # 🔥 STEP 3: FORCE MINIMUM QUALITY (IMPORTANT)
        if len(extracted_skills) < 3:
            extracted_skills.extend(["communication", "teamwork"])

        # 🔥 STEP 4: CLEANUP
        extracted_skills = list(set([s.lower().strip() for s in extracted_skills]))

        # ✅ Save skills
        for skill_name in extracted_skills:
            skill_obj, _ = Skill.objects.get_or_create(name=skill_name)
            job_obj.skills.add(skill_obj)

        # 🧠 Debug (for demo)
        print("📌", title)
        print("👉 Skills:", extracted_skills)
        print("------")

        if created:
            count += 1

    print(f"\n✅ Added {count} jobs WITH skills")