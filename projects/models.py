from django.db import models


class NationalFoods(models.Model):
    customer_phone = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    question1_answer = models.CharField(max_length=255, blank=True, null=True)
    question1_no_reason = models.TextField(blank=True, null=True)
    question1_yes_reason = models.TextField(blank=True, null=True)
    question2_answer = models.CharField(max_length=255, blank=True, null=True)
    question2_no_reason = models.CharField(max_length=255, blank=True, null=True)
    question3_answer = models.CharField(max_length=255, blank=True, null=True)
    question3_no_reason = models.CharField(max_length=255, blank=True, null=True)
    question4_answer = models.CharField(max_length=255, blank=True, null=True)
    question5_answer = models.CharField(max_length=255, blank=True, null=True)
    question6_answer = models.CharField(max_length=255, blank=True, null=True)
    captured_by = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)