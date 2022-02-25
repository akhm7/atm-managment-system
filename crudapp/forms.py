from django import forms
from .models import Atm, AtmImage, AtmModel, AtmModelFunction, ticket, User, Profile

class AtmForm(forms.ModelForm):
    class Meta:
        model = Atm
        fields = ( 'name', 'serialNumber', 'merchantId', 'atmModelId', 'description', 'terminalId', 'mfo','inBankProcessing', 'RDSCommander','service', 'NFC','workTime', 'lat','long' )


class AtmImageForm(forms.ModelForm):
    class Meta:
        model = AtmImage
        fields = ('title', 'image', 'description', 'atmId')

class AtmModelForm(forms.ModelForm):
    class Meta:
        model = AtmModel
        fields = "__all__"

class AtmModelFunctionForm(forms.ModelForm):
    class Meta:
        model = AtmModelFunction
        fields = "__all__"

class ticketStatusForm(forms.ModelForm):
    def __init__(self,mfo,*args,**kwargs):
        super (ticketStatusForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['atm'].queryset = Atm.objects.filter(mfo=mfo)

    class Meta:
        model = ticket
        fields = ('status','description','broken','atm','user')
 
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ('photo', 'bio')