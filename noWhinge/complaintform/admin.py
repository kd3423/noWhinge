from django.contrib import admin
from .models import Complaints
# Register your models here.

class ComplaintsAdmin(admin.ModelAdmin):
	list_display=["first_name","last_name","issue","locality","desc","photo"]
	class Meta:
		model = Complaints


admin.site.register(Complaints, ComplaintsAdmin)