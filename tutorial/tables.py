import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
    id = tables.Column(attrs={"th": {"style": "background-color:lightgray"}})
    first_name = tables.Column(attrs={"th": {"style": "background-color:lightgray"}})
    last_name = tables.Column(attrs={"th": {"style": "background-color:lightgray"}})
    user = tables.Column(attrs={"th": {"style": "background-color:lightgray"}})
    birth_date = tables.Column(attrs={"th": {"style": "background-color:lightgray"}})

    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': "table table-striped"}
        order_by = '-birth_date'
        #fields = ("id","first_name","last_name","user","birth_date")



