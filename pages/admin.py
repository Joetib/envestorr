from django.contrib import admin
from configuration.admin import ImageAdmin
from pages.models import InvestmentOpportunity, TeamMember

# Register your models here.
@admin.register(InvestmentOpportunity)
class InvestOpportunityAdmin(ImageAdmin):
    image_fields = ['picture',]

    list_display = ("title", "date_created", "last_modified")


@admin.register(TeamMember)
class TeamMemberAdmin(ImageAdmin):
    image_fields = ('picture',)
    list_display = ("name", "position")
