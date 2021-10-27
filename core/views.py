from django.shortcuts import render, redirect

import requests
import re


URL_EXPRESSION = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


def index(request):
	context = {}
	if request.method == "POST":
		try:
		 	response = requests.get(request.POST["url"]).text
		 	urls = re.findall(URL_EXPRESSION, response)

		 	context["urls"] = []

		 	for i in range(len(urls)):
		 		if len(urls[i]) > 75:
		 			context["urls"].append({"summary": urls[i][:80] + "...", "url": urls[i], "id": i})
		 		else:
		 			context["urls"].append({"summary": urls[i][:80], "url": urls[i], "id": i})

		 	context["n"] = len(urls)
		except:
			context["error"] = "Error"

	return render(request, "index.html", context)