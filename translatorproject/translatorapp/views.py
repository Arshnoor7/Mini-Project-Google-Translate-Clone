from django.shortcuts import render


import requests

import environ
# Initialise environment variables
env = environ.Env()

# Create your views here.
def index(request):
    if(request.method =='POST'):

        txt=request.POST["txt"]
      
        target_lang=request.POST['target_lang']
        source_lang=request.POST['source_lang']

        try:
        
            url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
            payload = {
            	"q": txt,
            	"target": target_lang,
            	"source": source_lang
            }
            headers = {
            	"content-type": "application/x-www-form-urlencoded",
            	"Accept-Encoding": "application/gzip",
            	"X-RapidAPI-Key": env('apikey'),
            	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
            }
            response = requests.post(url, data=payload, headers=headers)
            response=response.json()
            print(response)
            context={
                "result":response["data"]["translations"][0]["translatedText"]
            }
            return render(request,"result.html",context)
        
        except:
            url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
            payload = {
            	"q": txt,
            	"target": target_lang,
            	"source": source_lang
            }
            headers = {
            	"content-type": "application/x-www-form-urlencoded",
            	"Accept-Encoding": "application/gzip",
            	"X-RapidAPI-Key":  env('apikey'),
            	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
            }
            response = requests.post(url, data=payload, headers=headers)
            response=response.json()
            print(response)
            context={
                "result":response["error"]["message"]
            }
            return render(request,"result.html",context)


    return render(request,"index.html")
        
