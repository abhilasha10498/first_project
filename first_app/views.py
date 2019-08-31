from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from first_app.models import Topic,AccessRecord,Webpage
def index(request):
    Webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':Webpage_list}
    return render(request,'first_app/index.html',context=date_dict)
=======
def index(request):
    my_dict={'insert_me':"hello everyone"}
    return render(request,'first_app/index.html',context=my_dict)
>>>>>>> f7c3cecd5e84d40cb8201c40f12c405777c84e64

# Create your views here.
