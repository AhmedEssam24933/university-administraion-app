from django.shortcuts import render, redirect
from .models import Department, Course, Faculty, Student, Enrollment
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def new_data(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        date_of_birth = request.POST['dateofbirth']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['zipcode']
        phone_number = request.POST['phonenumber']
        major = request.POST['major']
        gpa = request.POST['gpa']
        graduation_date = request.POST['graduationdate']
        student = Student(first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, address=address,
         city=city,zip_code=zip_code, phone_number=phone_number, major=major, gpa=gpa, graduation_date= graduation_date)
        student.save()
        student = Student.objects.all()
        return render(request, 'new_data.html', {'student':student})
