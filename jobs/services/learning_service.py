# 🔥 COURSE DATABASE (YOUTUBE + COURSERA)

COURSES = {
    "Docker": [
        {
            "title": "Docker Full Course for Beginners",
            "platform": "YouTube",
            "link": "https://youtu.be/3c-iBn73dDE"
        }
    ],
    "AWS": [
        {
            "title": "AWS Cloud Practitioner Essentials",
            "platform": "Coursera",
            "link": "https://www.coursera.org/learn/aws-cloud-practitioner-essentials"
        }
    ],
    "React": [
        {
            "title": "React JS Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/bMknfKXIFA8"
        }
    ],
    "Django": [
        {
            "title": "Django Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/F5mRW0jo-U4"
        }
    ],
    "Python": [
        {
            "title": "Python for Beginners",
            "platform": "YouTube",
            "link": "https://youtu.be/_uQrJ0TkZlc"
        }
    ],
    "SQL": [
        {
            "title": "SQL Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/HXV3zeQKqGY"
        }
    ],
    "Git": [
        {
            "title": "Git & GitHub Crash Course",
            "platform": "YouTube",
            "link": "https://youtu.be/RGOj5yH7evk"
        }
    ],
    "APIs": [
        {
            "title": "REST API Tutorial",
            "platform": "YouTube",
            "link": "https://youtu.be/7YcW25PHnAA"
        }
    ],
    "HTML": [
        {
            "title": "HTML Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/qz0aGYrrlhU"
        }
    ],
    "CSS": [
        {
            "title": "CSS Full Course",
            "platform": "YouTube",
            "link": "https://youtu.be/1Rs2ND1ryYc"
        }
    ]
}


# 🔥 NORMALIZE SKILL NAME (IMPORTANT FIX)
def normalize(skill):
    skill = skill.strip().lower()
    mapping = {
        "api": "APIs",
        "apis": "APIs",
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "git": "Git",
    }
    return mapping.get(skill, skill.title())


# 🔥 MAIN FUNCTION
def get_courses(missing_skills):
    results = []

    for skill in missing_skills:
        key = normalize(skill)

        if key in COURSES:
            results.extend(COURSES[key])

    # fallback if nothing found
    if not results:
        return get_generic_courses()

    return results


# 🔥 FALLBACK
def get_generic_courses():
    return [
        {
            "title": "Full Stack Developer Roadmap",
            "platform": "YouTube",
            "link": "https://youtu.be/nu_pCVPKzTk"
        }
    ]


# 🔥 COURSE DATABASE

COURSES = {
    "python": [
        {"title": "Python Full Course", "platform": "YouTube", "link": "https://youtu.be/_uQrJ0TkZlc"}
    ],
    "sql": [
        {"title": "SQL Full Course", "platform": "YouTube", "link": "https://youtu.be/HXV3zeQKqGY"}
    ],
    "react": [
        {"title": "React Full Course", "platform": "YouTube", "link": "https://youtu.be/bMknfKXIFA8"}
    ],
    "django": [
        {"title": "Django Full Course", "platform": "YouTube", "link": "https://youtu.be/F5mRW0jo-U4"}
    ],
    "docker": [
        {"title": "Docker Course", "platform": "YouTube", "link": "https://youtu.be/3c-iBn73dDE"}
    ],
    "aws": [
        {"title": "AWS Course", "platform": "Coursera", "link": "https://www.coursera.org/learn/aws-cloud-practitioner-essentials"}
    ],
    "javascript": [
        {"title": "JavaScript Full Course", "platform": "YouTube", "link": "https://youtu.be/hdI2bqOjy3c"}
    ],
    "html": [
        {"title": "HTML Course", "platform": "YouTube", "link": "https://youtu.be/qz0aGYrrlhU"}
    ],
    "css": [
        {"title": "CSS Course", "platform": "YouTube", "link": "https://youtu.be/1Rs2ND1ryYc"}
    ],
    "apis": [
        {"title": "REST API Tutorial", "platform": "YouTube", "link": "https://youtu.be/7YcW25PHnAA"}
    ],
    "git": [
        {"title": "Git & GitHub", "platform": "YouTube", "link": "https://youtu.be/RGOj5yH7evk"}
    ]
}


# 🔥 NORMALIZE SKILLS
def normalize(skill):
    skill = skill.strip().lower()

    mapping = {
        "api": "apis",
        "rest api": "apis",
        "rest apis": "apis",
        "js": "javascript"
    }

    return mapping.get(skill, skill)


# 🔥 SMART COURSE RECOMMENDER
def get_courses(missing_skills):
    results = []
    added = set()

    for skill in missing_skills:
        key = normalize(skill)

        if key in COURSES and key not in added:
            results.extend(COURSES[key])
            added.add(key)

    # 🔥 fallback if nothing matched
    if not results:
        return [{
            "title": "Full Stack Developer Roadmap",
            "platform": "YouTube",
            "link": "https://youtu.be/nu_pCVPKzTk"
        }]

    return results