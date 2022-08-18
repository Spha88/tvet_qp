from django.contrib import admin
from papers.models import QuestionPaper, Subject

class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'year', 'exam_period', )
    list_display_links = ('id', 'subject')
    ordering = ('subject', 'year',)
    list_filter = ('subject', 'year', 'exam_period',)
    list_per_page = 10
    search_fields = ('subject', )

admin.site.register(QuestionPaper, QuestionPaperAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'ncv_or_report191', 'fundamental_or_vocational', )
    ordering = ('name', 'level')
    list_per_page = 10
    list_display_links = ('id', 'name',)
    list_filter = ('level', 'name', 'ncv_or_report191', 'fundamental_or_vocational')
    search_fields = ('name', 'level', 'ncv_or_report191')

admin.site.register(Subject, SubjectAdmin)