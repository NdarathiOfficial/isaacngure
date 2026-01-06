from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'John Doe', 'class': 'form-input'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'john@example.com', 'class': 'form-input'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell me about your project...', 'rows': 5, 'class': 'form-input'})
    )
