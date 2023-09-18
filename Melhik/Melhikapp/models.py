from django.db import models
from django.contrib.auth.models import User
from admin_dashboard.models import *

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)


class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.TextField()
    portfolio = models.URLField()


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    contact_information = models.TextField()
    job_postings = models.ManyToManyField('Job', related_name='employers')


class Job(models.Model):
    PRICE_TYPE_CHOICES = [
        (1, 'Fixed Budget Price'),
        (2, 'Hourly Pricing'),
        (3, 'Biding Price'),
    ]
    PERIOD_TYPE_CHOICES = [
        ('period', 'Start immediately after the candidate is selected'),
        ('job', 'Job will Start On'),
    ]

    title = models.CharField(max_length=200)
    price_type = models.IntegerField(choices=PRICE_TYPE_CHOICES)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    period_type = models.CharField(max_length=10, choices=PERIOD_TYPE_CHOICES)
    start_date = models.DateField()
    to_date = models.DateField()
    reference_links = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField()


class Forum(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField()


class Resource(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources/')