from django import forms

class BioForm(forms.Form):
    full_name = forms.CharField(
        label= "Full Name",
        max_length=50,
        required=True, # (by default required will be true. so no need to define unless you want to set False)
        widget=forms.TextInput(
        attrs={"class": "form-control"}
        ))
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
        attrs={"class": "form-control"}
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
        attrs={"class": "form-control"}
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
        attrs={"class": "form-control"}
        )
    )
    