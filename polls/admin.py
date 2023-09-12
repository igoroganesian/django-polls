from django.contrib import admin

from .models import Choice, Question

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date",
                    "was_published_recently"]
    #filter; knows it's a DateTimeField, therefore options
    list_filter = ["pub_date"]
    #search box at top of change list - searches question_text
    #uses LIKE query, can add more fields
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)