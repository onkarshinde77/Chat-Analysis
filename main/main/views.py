from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from helper.preprocess import preprocess
from helper.helper import fetch_stats, active_user, create_wordcloud, count_max_word, emoji_list, month_year
import matplotlib.pyplot as plt

def upload_file(request):
    data = None
    file_content = None
    users = []
    selected_user = None

    if request.method == 'POST':
        # Check if file is uploaded
        if request.FILES.get('uploaded_file'):
            uploaded_file = request.FILES['uploaded_file']
            file_content = uploaded_file.read().decode('utf-8')
            data = preprocess(file_content)
            request.session['file_content'] = file_content  # Save to session for later filtering
        else:
            # If no file uploaded, try to get file_content from session
            file_content = request.session.get('file_content')
            if file_content:
                data = preprocess(file_content)

        if data is not None and not data.empty:
            users = data['sender'].unique()
            # Check if user is selected
            selected_user = request.POST.get('selected_user')
            if selected_user:
                # Filter data for selected user
                data = data[data['sender'] == selected_user]
            table = data.to_html(classes='table table-bordered', index=False)
            return render(request, 'upload.html', {
                'file_content': table,
                'users': users,
                'selected_user': selected_user,
                'display' : None,
            })

    return render(request, 'upload.html', {'file_content': file_content})

# def index(request):
#     return render(request,'layout.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):    
    return render(request,'contact.html')