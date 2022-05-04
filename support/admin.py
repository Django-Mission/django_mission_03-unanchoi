from tabnanny import verbose
from django.contrib import admin

from .models import Faq, Inquiry, Answer
# Register your models here.

admin.site.urls(Faq)
admin.site.urls(Inquiry)
admin.site.urls(Answer)