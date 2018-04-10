from django.contrib import admin
from .models import Complaints
# Register your models here.

class ComplaintsAdmin(admin.ModelAdmin):
	list_display=["user_name","first_name","last_name","issue","locality","desc","photo","resolved"]
	class Meta:
		model = Complaints


admin.site.register(Complaints, ComplaintsAdmin)