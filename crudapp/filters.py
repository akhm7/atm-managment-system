import django_filters
from .models import Atm
 
CHOICES =[
        ["name", "по алфавиту"],
        ["price", "дешевые сверху"],
        ["-price", "дорогие сверху"]
]
 
 
class AtmFilter(django_filters.FilterSet):
    class Meta:
        model = Atm
        #exclude = [field.name for field in Atm._meta.fields]
        #order_by_field = 'name'
        fields = ('atmModelId','mfo', 'atmModelId__functions')