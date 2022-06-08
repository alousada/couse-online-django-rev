from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Choice, Question

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline]
    list_display = ['question_text','course']

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

