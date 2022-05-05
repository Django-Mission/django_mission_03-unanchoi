from django.db import models



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
    edited_at = models.DateTimeField(verbose_name ="수정시간", auto_now=True)



class Inquiry(models.Model):
    choice_options = [
        ("Django" , "Django"),
        ("Python" , "Python"),
        ("User" , "User"),
        ("Etc" , "Etc")
    ]
    
    email = models.EmailField(verbose_name="email")
    title = models.CharField(verbose_name ="제목", max_length=20)
    writer = models.CharField(verbose_name ="작성자", max_length=20)
    category = models.CharField(verbose_name="종류",
    max_length=20,
    choices=choice_options)
    created_at = models.DateTimeField(verbose_name ="생성시간", auto_now_add=True)
    number = models.TextField(verbose_name="전화번호")

class Answer(models.Model):
    answer = models.TextField()
    inquiry = models.ForeignKey(to=Inquiry, on_delete=models.CASCADE, null=True, blank=True)
