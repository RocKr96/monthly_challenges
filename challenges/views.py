from django.http import response
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {"january": "Eat Healthy", "february": "Fit Yourself",
                      "march": "Get Fit", "april": "Fit Yourself",
                      "may": "Get Fit", "june": "Fit Yourself",
                      "july": "Get Fit", "august": "Fit Yourself",
                      "september": "Get Fit", "october": "Fit Yourself",
                      "november": "Get Fit", "december": None}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "month_list" : months
        })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"""
    #     <ul>
    #         <h1>
    #             {list_items}
    #         </h1>
    #     </ul>
    # """
    # return HttpResponse(response_data)

def monthly_challenge_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        raise Http404()
        # return HttpResponseNotFound(render_to_string("404.html"))
        # return HttpResponseNotFound("<h1>Invalid Month</h1>")
    forward_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_challenge(request, month):
    if month.lower() in monthly_challenges:
        challenge_text = monthly_challenges.get(month.lower())
        return render(request, "challenges/challenge.html", { 
            "month" : month,
            "text" : challenge_text
            })
    raise Http404()
    # return HttpResponseNotFound(render_to_string("404.html"))