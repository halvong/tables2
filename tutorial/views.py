from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from .models import Person
from .tables import PersonTable

class PersonList(SingleTableView):
    def get(self,request):
        table = PersonTable(Person.objects.all())
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=6)
        return render(request, "person_list.html", { "table": table })

