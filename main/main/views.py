from django.http import HttpResponse
from django.shortcuts import render

import numpy as np
from helper.preprocess import preprocess
from helper.helper import fetch_stats , active_user , create_wordcloud,count_max_word , emoji_list,month_year
import matplotlib.pyplot as plt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt  # If you use CSRF token in JS, you can remove this decorator
def upload_files(request):
    uploaded_files = request.FILES.getlist('files')
    saved_files = []
    for file in uploaded_files:
        # Save each file as needed
        with open(f'/tmp/{file.name}', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        saved_files.append(file.name)
    return JsonResponse({'status': 'success', 'files': saved_files})


def index(request):
    return render(request,'layout.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):    
    return render(request,'contact.html')
