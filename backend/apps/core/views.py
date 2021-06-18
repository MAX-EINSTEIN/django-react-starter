from django.shortcuts import redirect, render
from django.urls import reverse


def home_page(request):
    status = request.user.is_authenticated
    # status = True
    if status:
        return redirect(reverse('blog:home'))
    return render(request=request, template_name='home.html')
