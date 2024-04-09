"""
The bug was in 'else' case, the code didn't check the case when both parameters were entered!
Below is the corrected code.
"""


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "phone_number",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]

    def clean(self):
        _clean_data = super().clean()

        if not bool(self.cleaned_data["email"]) and not bool(self.cleaned_data["phone_number"]):
            raise ValidationError("Insert email or phone number. At least one of them should be set.")

        elif not bool(self.cleaned_data["email"]):
            if get_user_model().objects.filter(phone_number=_clean_data["phone_number"]).exists():
                raise ValidationError("User with phone number already exists!!!")

        elif not bool(self.cleaned_data["phone_number"]):
            if get_user_model().objects.filter(email=_clean_data["email"]).exists():
                raise ValidationError("User with email already exists!!!")

        else:
            email_exists = get_user_model().objects.filter(email=_clean_data["email"]).exists()
            phone_number_exists = get_user_model().objects.filter(phone_number=_clean_data["phone_number"]).exists()
            if email_exists and phone_number_exists:
                raise ValidationError("User with these email and phone number already exists!!!")
            elif email_exists:
                raise ValidationError("User with this email already exists!!!")
            elif phone_number_exists:
                raise ValidationError("User with this phone number already exists!!!")

        return _clean_data
