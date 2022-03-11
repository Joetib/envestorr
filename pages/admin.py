from django.contrib import admin

from pages.models import InvestmentOpportunity, TeamMember

# Register your models here.
@admin.register(InvestmentOpportunity)
class InvestOpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "last_modified")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
