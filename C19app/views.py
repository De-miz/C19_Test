from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .C19 import C19_defined_controller, C19_default_controller
from django.template import loader
from .models import Comments
from django.views import View

# Create your views here.

class Index(View): 
    template = loader.get_template('index.html')

    def get(self, request): 
        C19_default_controller()
        data = Comments.objects.all().order_by('date')
        contents = {
        'image_type': 'default', 
        'all_comments': data, 
        'total_comments': len(data)
        }    
        return HttpResponse(self.template.render(contents, request))

    def post(self, request):
        country_name = request.POST['country_name']
        iferror = C19_defined_controller(country_name)
        data = Comments.objects.all().order_by('date')
        contents = {
            'image_type': 'defined', 
            'all_comments': data, 
            'total_comments': len(data), 
            'iferror': iferror
            }
        if iferror == 'error': contents['image_type'] = 'default'; contents['country_name'] = country_name
        return HttpResponse(self.template.render(contents, request))


def comment(request):
    if request.method == 'POST': 
        name = request.POST['name']
        comment = request.POST['comment']
        Comments.objects.create(
            name=name if not name=='' else 'Anonymous', 
            comment=comment
        )       
    return HttpResponseRedirect(reverse('index'))


def about(request): 
    page = loader.get_template('about.html')
    return HttpResponse(page.render({}, request))