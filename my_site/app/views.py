from django.shortcuts import render, redirect
from .forms import UserInputForm

import csv
from django.http import HttpResponse
from django.views import View
from .models import QuotesText

from scrapyd_api import ScrapydAPI



scrapyd = ScrapydAPI('http://localhost:6800')





def home_page(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input_keyword = form.cleaned_data["quotes_keyword"]
            print(f"====== {user_input_keyword} ========")

            # scrapyd.schedule('quotesbot', 'toscrape-xpath')


            global project_id
            project_id = scrapyd.schedule('quotesbot', 'toscrape-xpath')

        return redirect("export_quotes")

    
    else:
        form = UserInputForm()
        return render(request, "app/home_page.html", context={"form": form})





def export_quotes_view(request):
    if request.method == "POST":
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="quotes.csv"'

        writer = csv.writer(response)
        writer.writerow(['Title', 'Author'])

        quotes = QuotesText.objects.all().values_list('title', 'author')
        for quote in quotes:
            writer.writerow(quote)

        return response

    return render(request, 'app/thank_you_page.html')





import requests

# def run_spider(request):

#     """
#     # Working code
#     status_url = "http://localhost:6800/daemonstatus.json"
#     job_status = requests.get(status_url).text
#     """

#     status_url = "http://localhost:6800/daemonstatus.json"
#     response = requests.get(status_url)
#     if response.status_code == 200:

#         while True:
#             job_status = requests.get(status_url).json()['running']
#             if job_status == 0:
#                 print("==========Spider Finish ===========")
#                 break  
#             print("++++ 1 ++++")
#             return render(request, "app/status.html", context={"status": job_status})
#     return render(request, "app/status.html", context={"status": "No Spider"})
                

def run_spider(request):
    # status_url = "http://localhost:6800/daemonstatus.json"
    # response = requests.get(status_url)
    # if response.status_code == 200:
    #     job_status = requests.get(status_url).json()['running']
    #     return render(request, "app/status.html", context={"status": job_status})


    return render(request, "app/status.html")

