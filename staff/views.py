from django.db.models import CharField, DecimalField, Q
from django.views.generic import ListView

from .models import Boss, Employee

class Home(ListView):
    model = Boss
    template_name = 'staff/index.html'
    context_object_name = 'bosses'


class Staff(ListView):
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
