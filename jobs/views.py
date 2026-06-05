from django.http import JsonResponse
from django.shortcuts import render
from .models import Job

# SERVICES
from .services.job_services import get_jobs
from .services.skill_service import analyze_skill_gap
from .services.learning_service import get_courses

# UTILS
from .utils import extract_skills, extract_text_from_pdf

# CHART
import base64
from io import BytesIO
import matplotlib.pyplot as plt


# ================= CHART =================
def generate_chart(skills):
    if not skills:
        return None

    top_skills = skills[:5]
    labels = top_skills
    values = list(range(len(top_skills), 0, -1))

    plt.figure()
    plt.barh(labels, values)
    plt.title("Top Missing Skills")

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    image_png = buffer.getvalue()
    buffer.close()

    return base64.b64encode(image_png).decode("utf-8")


# ================= ROADMAP =================
def build_roadmap(missing_skills):
    roadmap = []

    for skill in missing_skills[:6]:
        roadmap.append({
            "skill": skill,
            "course": f"Learn {skill}",
            "link": f"https://www.youtube.com/results?search_query=learn+{skill}"
        })

    return roadmap


# ================= MAIN VIEW =================
def skill_gap_view(request):
    score = None
    missing_skills = []
    matched_skills = []
    chart = None
    roadmap = []
    courses = []
    jobs = []

    role = "Full Stack Developer"
    city = "Bangalore"

    if request.method == "POST":

        # Handles BOTH manual + resume mode
        role = request.POST.get("role") or request.POST.get("role_resume") or role
        city = request.POST.get("city") or request.POST.get("city_resume") or city

        # ===== INPUT =====
        if request.FILES.get("resume_file"):
            file = request.FILES["resume_file"]

            try:
                text = extract_text_from_pdf(file)

                # DEBUG RESUME TEXT
                print("========== RESUME TEXT ==========")
                print(text[:3000])
                print("=================================")

                user_skills_list = extract_skills(text)

                # DEBUG SKILLS FOUND
                print("========== SKILLS FOUND ==========")
                print(user_skills_list)
                print("==================================")

            except Exception as e:
                print("Resume parsing error:", str(e))
                text = ""
                user_skills_list = []

        else:
            user_skills = request.POST.get("skills", "")
            user_skills_list = [
                s.strip()
                for s in user_skills.split(",")
                if s.strip()
            ]

        # ===== SKILL GAP =====
        result = analyze_skill_gap(user_skills_list, role)

        missing_skills = sorted(result["missing"])
        matched_skills = result["matched"]
        score = result["score"]

        # ===== COURSES =====
        courses = get_courses(missing_skills)

        # ===== JOBS =====
        jobs = get_jobs(role, city)

        # DEBUG JOBS
        print("========== DEBUG ==========")
        print("ROLE:", role)
        print("CITY:", city)
        print("JOBS RETURNED:", jobs)
        print("===========================")

        # ===== CHART =====
        chart = generate_chart(missing_skills)

        # ===== ROADMAP =====
        roadmap = build_roadmap(missing_skills)

        # ===== SAVE USER HISTORY =====
        if request.user.is_authenticated:
            try:
                from users.models import SkillGapHistory

                SkillGapHistory.objects.create(
                    user=request.user,
                    resume_text=", ".join(user_skills_list),
                    missing_skills=", ".join(missing_skills),
                    recommended_courses=", ".join(
                        [course["title"] for course in courses]
                    )
                )
            except Exception as e:
                print("History save error:", str(e))

    return render(request, "dashboard.html", {
        "score": score,
        "missing_skills": missing_skills,
        "matched_skills": matched_skills,
        "chart": chart,
        "roadmap": roadmap,
        "courses": courses,
        "jobs": jobs,
        "role": role,
        "city": city,
    })


# ================= API =================
def job_search(request):
    location = request.GET.get("location")
    query = request.GET.get("query")

    jobs = get_jobs(query, location)

    return JsonResponse(jobs, safe=False)


# ================= EXTRA PAGES =================
def trending_skills(request):

    jobs = get_jobs("python developer", "India")

    skill_keywords = [
        "python", "django", "flask", "sql",
        "mysql", "postgresql", "mongodb",
        "aws", "docker", "git", "linux",
        "react", "javascript", "typescript",
        "redis", "kubernetes"
    ]

    skill_count = {}

    for job in jobs:

        text = " ".join([
            str(job.get("title", "")),
            str(job.get("company", "")),
        ]).lower()

        for skill in skill_keywords:

            if skill.lower() in text:
                skill_count[skill] = skill_count.get(skill, 0) + 1

    total = sum(skill_count.values()) or 1

    data = []

    for skill, count in sorted(
        skill_count.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        percentage = round((count / total) * 100)
        data.append((skill.upper(), percentage))

    return render(
        request,
        "trending.html",
        {"data": data}
    )


def role_explorer(request):

    roles = [
        {
            "name": "Python Developer",
            "skills": ["Python", "Django", "SQL"]
        }
    ]

    return render(
        request,
        "roles.html",
        {"roles": roles}
    )


def city_demand(request):
    cities = [
        ("Bangalore", 4800),
        ("Hyderabad", 2300),
        ("Pune", 2000),
        ("Mumbai", 1700),
        ("Chennai", 1200),
    ]
    return render(request, "city.html", {"cities": cities})


def courses_page(request):
    courses = get_courses(["Python", "SQL", "Docker"])
    return render(request, "courses.html", {"courses": courses})