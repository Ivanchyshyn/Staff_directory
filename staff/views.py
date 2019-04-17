from django.db.models import CharField, DecimalField, Q
from django.views.generic import ListView, FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Boss, Employee
from .forms import UserForm, UserProfileForm

class HomeView(ListView):
    model = Boss
    template_name = 'staff/index.html'
    context_object_name = 'bosses'


class StaffView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'staff/staff.html'
    context_object_name = 'staff'
    fields = [f for f in Employee._meta.fields if (isinstance(f, CharField) or isinstance(f, DecimalField))]

    def get(self, request):
        search_query = request.GET.get('search_box', None)
        if search_query is not None:
            queries = [Q(**{f'{f.name}__icontains': search_query}) for f in self.fields]
            qs = Q()
            for query in queries:
                qs = qs | query
            result = Employee.objects.filter(qs)
            self.queryset = result
        return super().get(request)


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            return HttpResponseRedirect('/login/')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(
                  request,
                  'register/register.html',
                  {'user_form': user_form,
                  'profile_form': profile_form}
                )
