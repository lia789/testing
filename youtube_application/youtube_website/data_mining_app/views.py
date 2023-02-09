from django.shortcuts import render, redirect
import csv
from django.http import HttpResponse

from .forms import ChannelSearchKeywordForm
from .utils import get_channel_info




def channels_meta_data(request):
    """
    Handle the request for channel data search.
    If the request method is 'POST', the form data is processed and the `data_preview` view is called.
    Otherwise, a blank form is displayed.

    :param request: the incoming request object
    :return: a response object
    """


    if request.method == "POST":
        # process the form data
        form = ChannelSearchKeywordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data["channel_keyword"]
            data = get_channel_info(my_input=keyword, max_results=5)
            request.session["data"] = data
            return redirect("data_preview_url")
    else:
        # display a blank form
        form = ChannelSearchKeywordForm()
    return render(request, "data_mining_app/home_page.html", {"form": form})



def data_preview(request):
    """
    Handle the request for previewing the channel data.
    If the request method is 'POST', the data is converted to a CSV file and downloaded.
    Otherwise, the data is displayed.

    :param request: the incoming request object
    :return: a response object
    """

    data = request.session.get("data", {})
    if request.method == "POST":
        # convert data to CSV file
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=data.csv"
        writer = csv.writer(response)
        writer.writerow(["Number", "Title", "Description", "Published"])
        for i, item in data.items():
            writer.writerow([i, item["title"], item["description"], item["published"]])
        return response

    return render(request, "data_mining_app/data_preview.html", {"data": data})
