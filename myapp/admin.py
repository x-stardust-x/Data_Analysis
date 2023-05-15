from django.contrib import admin
from myapp.models import task

# Register your models here.


class taskAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'email', 'type', 'name',
                    'token', 'overview', 'cover')


class taskAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'email', 'type', 'name',
                    'token', 'overview', 'cover')
    ordering = ('uuid',)


admin.site.register(task, taskAdmin)
