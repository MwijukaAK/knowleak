from django.contrib import admin

# Register your models here.
from .models import Reading

class ReadingAdmin(admin.ModelAdmin):
    list_display = ("date", "pressure", "flowrate", "timestamp","probability","detection")
    readonly_fields = ["detection", "probability"]

admin.site.register(Reading, ReadingAdmin)

