from django.shortcuts import render

# Create your views here.
from datetime import datetime
from models import taskmodel
def create(request):
	try:
		if request.method=="post":
			title=request.data.get['title']
			description=requst.data.get['descripton',"no description "]
			completion_date=datetime.strptime(request.dat['completion_date'],"%d%m%y %H:%M")
			taskmodel.objects.create(title=title,description=description,\
				completion_date=completion_date,priority=priority)
	except Exception:
	pass
			