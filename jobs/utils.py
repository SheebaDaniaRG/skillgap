import re
from collections import Counter
from pypdf import PdfReader

from .skills_list import SKILLS


# ================= NORMALIZATION =================
def normalize_skill(skill):
    return skill.strip().lower()


SKILL_ALIASES = {
    "ml": "machine learning",
    "ai": "machine learning",
    "js": "javascript",
    "py": "python",
}


def normalize_skills(skills):
    normalized = []

    for skill in skills:
        skill = normalize_skill(skill)

        if skill in SKILL_ALIASES:
            normalized.append(SKILL_ALIASES[skill])
        else:
            normalized.append(skill)

    return list(set(normalized))


# ================= PDF TEXT EXTRACTION =================
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# ================= SKILL EXTRACTION =================
def extract_skills(text):
    text = text.lower()
    found = set()

    for skill in SKILLS:
        skill_lower = skill.lower()

        # Strong word boundary matching
        pattern = r'\b' + re.escape(skill_lower) + r'\b'

        if re.search(pattern, text):
            found.add(skill_lower)

    return list(found)


# ================= DEMAND ANALYSIS =================
def get_skill_demand(jobs):
    counter = Counter()

    for job in jobs:
        # ⚠️ defensive check (avoid crash if no skills field)
        if hasattr(job, "skills"):
            for skill in job.skills.all():
                name = normalize_skill(skill.name)
                counter[name] += 1

    return counter


# ================= SKILL GAP =================
def get_skill_gap(user_skills, jobs):
    user_skills = normalize_skills(user_skills)
    demand = get_skill_demand(jobs)

    gap = {}

    for skill, count in demand.items():
        if skill not in user_skills:
            gap[skill] = count

    return sorted(gap.items(), key=lambda x: x[1], reverse=True)


# ================= SCORE =================
def calculate_score(user_skills, jobs):
    user_skills = normalize_skills(user_skills)
    demand = get_skill_demand(jobs)

    total_weight = sum(demand.values())
    matched_weight = 0

    for skill, weight in demand.items():
        if skill in user_skills:
            matched_weight += weight

    if total_weight == 0:
        return 0

    return int((matched_weight / total_weight) * 100)


# ================= RESOURCES =================
SKILL_RESOURCES = {
    "python": "https://roadmap.sh/python",
    "django": "https://roadmap.sh/django",
    "java": "https://roadmap.sh/java",
    "aws": "https://roadmap.sh/aws",
    "docker": "https://roadmap.sh/docker",
    "sql": "https://roadmap.sh/sql",
    "react": "https://roadmap.sh/react",
}


# ================= RECOMMENDATIONS =================
def get_recommendations(missing_skills):
    recommendations = []

    for skill, demand in missing_skills:
        resource = SKILL_RESOURCES.get(
            skill,
            f"https://www.google.com/search?q=learn+{skill}"
        )

        recommendations.append({
            "skill": skill,
            "demand": demand,
            "resource": resource
        })

    return recommendations


# ================= ROADMAP =================
def generate_roadmap(missing_skills):
    roadmap = []

    for i, (skill, demand) in enumerate(missing_skills[:5], start=1):
        roadmap.append({
            "step": i,
            "skill": skill,
            "demand": demand,
            "action": f"Learn {skill}"
        })

    return roadmap