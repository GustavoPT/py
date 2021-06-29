from django.shortcuts import render
import threading 
import time 

import requests
import re 
import string 
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
# Create your views here.


class bitcoin:
    pass
class blockchain:
    pass

def index(request):



    return render(request,'index.html',{})


def bitcoin(request):
    


    return render(request,'bi.html',{})
    
def searchengine(request):


    
    if request.method  == 'POST':
        print("here")
        print(request.POST['query'])



    loop thru 

    return render(request, "searchengine.html",{})


def digitrecognizer(request):



    return render(request, "digitrecognizer.html",{})


