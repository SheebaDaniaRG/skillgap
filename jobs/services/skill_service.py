# 🔥 ROLE → REQUIRED SKILLS MAP
ROLE_SKILLS = {
    "Full Stack Developer": [
        "HTML", "CSS", "JavaScript", "React",
        "Python", "Django", "SQL", "APIs",
        "Git", "Docker"
    ],
    "Frontend Developer": [
        "HTML", "CSS", "JavaScript", "React", "TypeScript"
    ],
    "Backend Developer": [
        "Python", "Django", "SQL", "APIs", "Docker"
    ]
}


# 🔥 NORMALIZE SKILLS (IMPORTANT)
def normalize(skill):
    skill = skill.strip().lower()
    mapping = {
        "api": "apis",
        "rest api": "apis",
        "rest apis": "apis",
        "sql": "sql",
        "html": "html",
        "css": "css",
        "js": "javascript",
    }
    return mapping.get(skill, skill)


# 🔥 FORMAT OUTPUT (CLEAN DISPLAY)
def format_skill(skill):
    return skill.upper() if len(skill) <= 3 else skill.title()


# 🔥 MAIN FUNCTION
def analyze_skill_gap(user_skills, role):

    # normalize user input
    user_skills = [normalize(skill) for skill in user_skills]

    # normalize required skills
    required = [normalize(s) for s in ROLE_SKILLS.get(role, [])]

    required_set = set(required)
    user_set = set(user_skills)

    missing = list(required_set - user_set)
    matched = list(required_set & user_set)

    # format for display
    missing = [format_skill(s) for s in missing]
    matched = [format_skill(s) for s in matched]

    # score
    score = int((len(matched) / len(required_set)) * 100) if required_set else 0

    return {
        "missing": missing,
        "matched": matched,
        "score": score
    }


# 🔥 OPTIONAL
def get_all_roles():
    return list(ROLE_SKILLS.keys())