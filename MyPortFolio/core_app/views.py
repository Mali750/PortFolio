from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import json
from django.core import serializers
from .models import Query_Details
from .forms import login_form
from django.utils.timezone import now

# Create your views here.
def home_page(request):
    context = {'home':'active'}
    return render(request, 'core_app/home.html', context)

#saving the submission query data 
def contact_function(request):
    if request.method == "POST":
        name = request.POST.get('inputName')
        email = request.POST.get('inputEmail')
        subject = request.POST.get('inputSubject')
        message = request.POST.get('inputTextarea')

        if name and email and message:  # Basic validation
            # Check if a submission with the same name & email already exists
            existing_query = Query_Details.objects.filter(name=name, email=email).first()

            if existing_query:
                return render(request, "core_app/Contact.html", {
                    "error": "A submission with this name and email already exists."
                })

            # Save new query
            Query_Details.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
                submitted_at=now()
            )
            return redirect('submission')  # Redirect to success page

    return render(request, "core_app/Contact.html")

def Submission(request):
    return render(request, 'core_app/thank_you.html')

#getting data from database
def form_view(request):
    submissions = Query_Details.objects.all().order_by('-submitted_at')
    submissions_json = serializers.serialize('json', submissions)
    context = {
        'submissions': submissions,
        'submissions_json': json.loads(submissions_json)
    }
    return render(request, 'core_app/form_data.html', context)

#saving data in database
def login_view(request):
    if request.method == 'POST':
        fm = login_form(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('delete')
        else:
            fm.add_error(None, "Invalid username or password")
    else:
        fm = login_form()
    return render(request, 'core_app/login.html', {'form': fm}) 

def delete_dashboard(request):
    obj = Query_Details.objects.all()

    return render(request, 'core_app/operations.html', {'obj': obj})

def delete_view(request, pk):
    # Get the specific object to delete
    obj = get_object_or_404(Query_Details, pk=pk)
    
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('delete_dashboard'))  # Redirect back to the form data list
    
    # Optional: Add a confirmation page
    return render(request, 'core_app/confirm_delete.html', {'obj': obj})