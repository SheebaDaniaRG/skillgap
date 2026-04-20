from django.db import models
from .utils import extract_skills
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.ManyToManyField(Skill, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        extracted = extract_skills(self.description)

        self.skills.clear()

        for skill_name in extracted:
            skill_obj, _ = Skill.objects.get_or_create(name=skill_name)
            self.skills.add(skill_obj)

    def __str__(self):
        return self.title
    
    # models.py

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)