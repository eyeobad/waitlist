from django import forms
from .models import WaitlistEntry

class WaitlistForm(forms.ModelForm):
    """Form for handling waitlist signups with .edu validation."""
    class Meta:
        model = WaitlistEntry
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'id': 'email-input',
                'required': True,
                'class': (
                    'w-full h-14 pl-4 pr-32 py-2 text-lg '
                    'text-white placeholder-black '        # white text + light placeholder
                    'bg-white bg-opacity-20 '                  # translucent white background
                    'border-2 border-gray-300 rounded-lg '
                    'focus:ring-2 focus:ring-indigo-500 '
                    'focus:border-indigo-500 '
                    'transition-all duration-300'
                ),
                'placeholder': 'Enter your .edu email...',
            })
        }

    def clean_email(self):
        """Custom validator to ensure the email is a .edu address and is unique."""
        email = self.cleaned_data.get('email', '').lower()
        if not email.endswith('.edu'):
            raise forms.ValidationError("A valid .edu email address is required.")
        
        if WaitlistEntry.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already on the waitlist.")
            
        return email
