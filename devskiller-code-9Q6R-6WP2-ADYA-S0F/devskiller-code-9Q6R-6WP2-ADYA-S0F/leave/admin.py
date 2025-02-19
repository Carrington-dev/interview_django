import logging
from leave.models import User
from django.contrib import admin

logger = logging.getLogger(__name__)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''

    list_display = ('username', 'email', 'manager', 'language', 'is_admin', 'date_joined' )
    list_filter = ('date_joined',)
    readonly_fields = ('date_joined',)
    search_fields = ('username', 'email',)
    date_hierarchy = 'date_joined'
    ordering = ('-pk',)