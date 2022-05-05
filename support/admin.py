from tabnanny import verbose
from django.contrib import admin

from .models import Faq, Inquiry, Answer
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3
    min_num = 0
    max_num = 5
    verbose_name = '답변'
    verbose_name_plural = '답변'
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'edited_at')

    search_fields = ('id', 'title')
    list_filter = ('category')


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'writer')
    search_fields = ('id', 'title', 'email', 'number')
    list_filter = ('id', 'category')
    inlines = [AnswerInline]



