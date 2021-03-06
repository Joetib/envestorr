from django.contrib import admin

from newsletter.models import NewsLeterContact, NewsLetter

# Register your models here.


@admin.register(NewsLeterContact)
class NewsLetterContactAdmin(admin.ModelAdmin):
    
    list_display = ("email",  "active",)
    list_filter = ("active", )
    search_fields = ("email", )

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ("title", "sent", "date_created")
    search_fields = ("title",)
    list_filter = ("is_draft", "sent", "date_created")