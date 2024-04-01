
from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students_list = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request, 'students.html', {'students': students_list, 'form': form})

def courses(request):
    courses_list = Course.objects.all()
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, 'courses.html', {'courses': courses_list, 'form': form})

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        selected_course_id = request.POST.get('course')
        course = Course.objects.get(id=selected_course_id)
        student.courses.add(course)
    available_courses = Course.objects.exclude(students=student)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})

