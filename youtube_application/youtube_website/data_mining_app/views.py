from django.shortcuts import render, redirect

from .forms import ChannelSearchKeywordForm
from .utils import get_channel_info
import csv
from django.http import HttpResponse


def channels_meta_data(request):
    if request.method == "POST":
        keyword = request.POST.get("channel_keyword")
        channel_search_form = ChannelSearchKeywordForm(request.POST)

        if channel_search_form.is_valid():
            keyword = channel_search_form.cleaned_data.get("channel_keyword")
            data = get_channel_info(my_input=keyword, max_results=5)
            request.session["data"] = {}
            request.session["data"] = data

            return redirect("data_preview_url")

    else:
        channel_search_form = ChannelSearchKeywordForm()
        return render(request, "data_mining_app/home_page.html", {"form": channel_search_form})




def data_preview(request):
    data = request.session.get("data", {})

    if request.method == "POST":
        # Convert data to CSV file
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=data.csv"

        writer = csv.writer(response)
        writer.writerow(["Number", "Title", "Description", "Published"])
        for i, item in data.items():
            writer.writerow([i, item["title"], item["description"], item["published"]])



        # Download data after press submit button
        return response


    return render(request, "data_mining_app/data_preview.html", {"data": data})






