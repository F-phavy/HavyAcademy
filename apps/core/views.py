from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.db import IntegrityError

# Make sure this import matches your actual app name
from student_management.models import Student 
from .forms import FacultySignUpForm

class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = FacultySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' 
    success_message = "Faculty account created successfully."

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('username', 'This username is already taken.')
            return self.form_invalid(form)

@login_required
def index(request):
    # This logic gathers the data
    count = Student.objects.count()
    recent = Student.objects.all().order_by('-id')[:5]

    context = {
        'total_students': count,
        'recent_students': recent,
    }
    # Point this to your index file
    return render(request, 'main/index.html', context)

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

@login_required
def profile_view(request):
    # 'request.user' contains all the data for the person currently logged in
    return render(request, 'main/profile.html', {
        'user': request.user
    })