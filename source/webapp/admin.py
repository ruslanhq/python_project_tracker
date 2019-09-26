from django.contrib import admin

# Register your models here.


from webapp.models import Task, Status, Type


# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'author', 'created_at']
#     list_filter = ['author']
#     search_fields = ['title', 'text']
#     fields = ['title', 'author', 'text', 'created_at', 'updated_at']
#     readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Type)

