from django.db import models

# Create your models here.

class Faq(models.Model):

    choice_options = [
        ("Django" , "Django"),
        ("Python" , "Python"),
        ("User" , "User"),
        ("Etc" , "Etc")
    ]


    title = models.CharField(verbose_name ="작성자", max_length=20)
    category = models.CharField(verbose_name="종류", 
    max_length=20, 
    default = "Python",
    choices=choice_options
)
    content = models.TextField(verbose_name="내용")
    edited_at = models.DateTimeField(auto_add = True)
    
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE, null=True, blank=True)



class Answer(models.Model):
    answer = models.TextField()
class Inquiry(models.Model):
    choice_options = [
        ("Django" , "Django"),
        ("Python" , "Python"),
        ("User" , "User"),
        ("Etc" , "Etc")
    ]
 
    title = models.CharField(verbose_name ="작성자", max_length=20)
    writer = models.CharField(verbose_name ="작성자", max_length=20)
    category = models.CharField(verbose_name="종류",
    max_length=20,
    choices=choice_options)
    created_at = models.DateTimeField(created_at)