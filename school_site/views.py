from django.shortcuts import render

# Create your views here.
# def render(request, htm_file, context=None)
def home(request):
    context = {
        "school_name":  "Milestone College",
        "user_name" : "Sajjad Mahmud",
        "subjects" : ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Bangla', 'Enginsh'],
        # 'registration_open': False,
        'registration_open': True

    }
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        # print(request.POST)

        context.update({"user_name" : f"{first_name} {last_name}",})
        context.update({"email" : email,})
        return render(request, 'homepage.html', context=context)
    
    return render(request, 'homepage.html', context=context)


def about(request):
    context = {}
    return render(request, 'about.html', context=context)
