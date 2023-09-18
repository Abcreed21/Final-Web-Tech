from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(label='Category Name', max_length=100)

    
class FreelancerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    profile_picture = forms.ImageField()
    phone_number = forms.CharField(max_length=15)
    email_address = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    language = forms.CharField(max_length=50)
    level = forms.ChoiceField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
