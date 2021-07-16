from django.db import models

# Create your models here.

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  = models.CharField(db.String(128))
    image = models.CharField(db.String(128))
    description  = models.CharField(db.String(128))
    demo_url  = models.CharField(db.String(128))
    programming_language  = models.CharField(db.String(128))
    framework = models.CharField(db.String(128))
    github_link = models.CharField(db.String(128))
    # tags = db.relationship('Tag',backref='project')
    category = models.CharField(db.String(128))
    video_url = models.CharField(db.String(128))
