from django.shortcuts import render,redirect
from helper.preprocess import preprocess
from helper.helper import fetch_stats, active_user, count_max_word, emoji_list, month_year
from django.core.mail import send_mail
from helper.forms import ContactForm

from helper.charts import active_user_to_img , timeline_chart

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
            file_content = request.session.get('file_content')
            if file_content:
                data = preprocess(file_content)

        if data is not None and not data.empty:
            users = data['sender'].unique()
            selected_user = request.POST.get('selected_user')
            if selected_user and selected_user !='All Users':
                data = data[data['sender'] == selected_user]
            else: selected_user = 'All Users'
            table = data[data['messages'] != '<Media omitted>' ]
            table = table.to_html(classes='table table-bordered', index=False)
            # stat of selected user
            mess_num,words,media, link_count = fetch_stats(selected_user,data)
            # active user
            active_users , per = active_user(data)
            active_users = active_users.head(7)
            chart = active_user_to_img(selected_user,active_users)
            max_user_table = per.to_html(classes='table table-bordered', index=False)
            # most used word
            most_used_words = count_max_word(selected_user,data)
            most_used_words = most_used_words.to_html(classes='table table-bordered', index=False)
            # emoji list
            emoji = emoji_list(selected_user,data)
            emoji = emoji.to_html(classes='table table-bordered', index=False)
            # timeline
            timeline = month_year(selected_user,data)
            timeline = timeline_chart(timeline)
            
            return render(request, 'upload.html', {
                'file_content': table,
                'users': users,
                'selected_user': selected_user,
                'display' : None,
                'mess_num' : mess_num,
                'words' : words,
                'media': media,
                'link_count':link_count,
                'chart': chart,
                'max_user_table': max_user_table,
                'most_used_words':most_used_words,
                'emoji' : emoji,
                'timeline' : timeline,
            })

    return render(request, 'upload.html', {'file_content': file_content,'display': 'block'})

# def index(request):
#     return render(request,'layout.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):    
    return render(request,'contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Us message from {name}"
            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

            send_mail(
                subject,
                full_message,
                email,                # From Email (user's)
                ['shindeonkar704@gmail.com'],  # To Email (your address)
                fail_silently=False,
            )
            return redirect('thank_you')  # Define a success URL in your urls.py
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
