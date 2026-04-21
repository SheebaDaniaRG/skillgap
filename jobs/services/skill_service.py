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
    ],
    "Machine Learning Engineer": [
        "Python", "Machine Learning", "TensorFlow", "Pandas", "SQL"
    ]
}


# 🔥 NORMALIZATION ENGINE (UPGRADED)
def normalize(skill):
    skill = skill.strip().lower()

    mapping = {
        # APIs
        "api": "apis",
        "rest api": "apis",
        "rest apis": "apis",

        # JS
        "js": "javascript",

        # ML
        "ml": "machine learning",
        "ai": "machine learning",

        # variations
        "django basics": "django",
        "python basics": "python",
    }

    return mapping.get(skill, skill)


# 🔥 DISPLAY FORMAT
def format_skill(skill):
    return skill.upper() if len(skill) <= 3 else skill.title()


# 🔥 MAIN LOGIC
def analyze_skill_gap(user_skills, role):

    # normalize input
    user_skills = [normalize(skill) for skill in user_skills]

    required = [normalize(s) for s in ROLE_SKILLS.get(role, [])]

    user_set = set(user_skills)
    required_set = set(required)

    matched = list(user_set & required_set)
    missing = list(required_set - user_set)

    # format output
    matched_formatted = [format_skill(s) for s in matched]
    missing_formatted = [format_skill(s) for s in missing]

    # score
    score = int((len(matched) / len(required_set)) * 100) if required_set else 0

    return {
        "matched": matched_formatted,
        "missing": missing_formatted,
        "score": score
    }


# 🔥 OPTIONAL
def get_all_roles():
    return list(ROLE_SKILLS.keys())