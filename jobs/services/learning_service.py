# ================= NORMALIZER =================
def normalize_skill(skill):
    return skill.strip().lower()


# ================= COURSE DATABASE =================
COURSES = {
    "python": [
        {
            "title": "Python for Beginners",
            "platform": "YouTube",
            "link": "https://youtu.be/_uQrJ0TkZlc"
        }
    ],
    "sql": [
        {
            "title": "SQL Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/HXV3zeQKqGY"
        }
    ],
    "docker": [
        {
            "title": "Docker Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/3c-iBn73dDE"
        }
    ],
    "react": [
        {
            "title": "React Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/bMknfKXIFA8"
        }
    ],
    "django": [
        {
            "title": "Django Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/F5mRW0jo-U4"
        }
    ],
    "html": [
        {
            "title": "HTML Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/qz0aGYrrlhU"
        }
    ],
    "css": [
        {
            "title": "CSS Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/1Rs2ND1ryYc"
        }
    ],
    "javascript": [
        {
            "title": "JavaScript Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/W6NZfCO5SIk"
        }
    ],
    "git": [
        {
            "title": "Git & GitHub Crash Course",
            "platform": "YouTube",
            "link": "https://youtu.be/RGOj5yH7evk"
        }
    ],
    "apis": [
        {
            "title": "REST API Tutorial",
            "platform": "YouTube",
            "link": "https://youtu.be/7YcW25PHnAA"
        }
    ],
    "aws": [
        {
            "title": "AWS Cloud Practitioner",
            "platform": "Coursera",
            "link": "https://www.coursera.org/learn/aws-cloud-practitioner-essentials"
        }
    ]
}


# ================= MAIN FUNCTION =================
def get_courses(missing_skills):
    results = []
    seen = set()

    # 🔥 normalize all skills
    normalized_skills = [normalize_skill(s) for s in missing_skills]

    for skill in normalized_skills:
        if skill in COURSES:
            for course in COURSES[skill]:
                if course["title"] not in seen:
                    results.append(course)
                    seen.add(course["title"])

    # 🔥 fallback if nothing found
    if not results:
        return get_generic_courses()

    return results


# ================= FALLBACK =================
def get_generic_courses():
    return [
        {
            "title": "Full Stack Developer Roadmap",
            "platform": "YouTube",
            "link": "https://youtu.be/nu_pCVPKzTk"
        }
    ]