from django.db import models

# Create your models here.

class SkillCategory(models.Model):
    CATEGORY_CHOICE = (
    ('programming', 'Programming Languages'),
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('database', 'Database'),
    ('deployment', 'Deployment'),
    ('tools', 'Tools'),
)
    
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=50,unique=True)
    
    
    def __str__(self):
        return self.category

class Technology(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='technologies'
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category.get_category_display()} - {self.name}"
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    technologies = models.ManyToManyField(
        Technology,
        related_name='projects'
    )

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table =' Contact Messages'