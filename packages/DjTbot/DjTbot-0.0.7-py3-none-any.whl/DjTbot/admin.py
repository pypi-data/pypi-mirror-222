from django.contrib import admin
from DjTbot.models import TBotUser, TBotGroup


class TBotUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', ]
    search_fields = []

    @staticmethod
    def group_names(obj):
        return ''


class TBotGroupAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(TBotUser)
admin.site.register(TBotGroup)
