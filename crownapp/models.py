from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Family(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="families")
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Family'
        verbose_name_plural = 'Families'
        ordering = ['last_name']
    
    def __str__(self):
        return f"{self.last_name} Family"
