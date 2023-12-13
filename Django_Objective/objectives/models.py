from django.db import models

# Create your models here.
class Objective(models.Model):
    objective_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    descibtion = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
