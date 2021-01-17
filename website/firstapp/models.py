from django.db import models

# Create your models here.

class Uniinf(models.Model):
    Rank = models.CharField(max_length=100)
    Name_of_University = models.CharField(max_length=100)
    Name_of_Course = models.CharField(max_length=100)
    Link_to_the_program_highlights = models.CharField(max_length=200)
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    def __str__(self):
        return self.Rank


class Program_Highlights(models.Model):
    Rank = models.CharField(max_length=100)
    Start_Month = models.CharField(max_length=10)
    Class_Size = models.CharField(max_length=10)
    Avg_Work_Experience = models.CharField(max_length=10)
    Avg_Student_Age = models.CharField(max_length=10)
    Women_Students = models.CharField(max_length=10)
    Avg_Salary = models.CharField(max_length=10)
    Scholarship = models.CharField(max_length=10)
    Accreditations = models.CharField(max_length=10)

    def __str__(self):
        return self.Start_Month




    