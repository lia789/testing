from django.shortcuts import render, redirect
from scrapyd_api import ScrapydAPI
from django.http import JsonResponse


from .forms import TagForm

def home_page(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data['tag_name']
            scrapyd = ScrapydAPI('http://localhost:6800')
            # scrapyd.schedule('good_reader_project', 'love', tag=tag_name)
            scrapyd.schedule('good_reader_project', 'love')
            return redirect('result_page')
    else:
        form = TagForm()
    return render(request, 'tags_app/home_page.html', {'form': form})




def result_page(request):
    return render(request, 'tags_app/result_page.html')





def spider_status(request):
    scrapyd = ScrapydAPI('http://localhost:6800')
    status = scrapyd.list_jobs('good_reader_project')['running']
    return JsonResponse({'status': status})
