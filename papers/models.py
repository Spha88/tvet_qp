from datetime import datetime
from django.db import models


exam_period_choices = [
        ('supplementary Exam', 'Supplementary Exam'),
        ('May/June', 'May/June'),
        ('Nov/Dec', 'Nov/Dec'),
    ]

class Subject(models.Model):
    level_choices = [
        ('2', 'Level 2'),
        ('3', 'Level 3'),
        ('4', 'Level 4'),
        ('N4', 'N4'),
        ('N5', 'N5'),
        ('N6', 'N6'),
    ]
    program_choices = [
        ('NCV', 'NCV'),
        ('Report 191', 'Report 191 (Nated)')
    ]
    fundamental_or_vocational_choices = [
        ('vocational', 'Vocational'),
        ('fundamental', 'Fundamental'),
    ]

    name = models.CharField(max_length=150)
    level = models.CharField(max_length=150, choices=level_choices)
    ncv_or_report191 = models.CharField(max_length=150, choices=program_choices)
    fundamental_or_vocational = models.CharField(max_length=150, choices=fundamental_or_vocational_choices, blank=True)

    def __str__(self):
        return f"{self.name} {self.level}"

class QuestionPaper(models.Model):
    
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    year = models.CharField(max_length=4)
    exam_period = models.CharField(max_length=150, choices=exam_period_choices)
    question_paper = models.FileField(upload_to='question_papers/%Y/%m/%d/', blank=False)
    marking_guideline = models.FileField(upload_to='marking_guidelines/%Y/%m/%d/', blank=False, null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.subject} {self.year}"