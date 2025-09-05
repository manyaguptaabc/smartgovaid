from django import forms

class EligibilityForm(forms.Form):
    age = forms.IntegerField(label="Age")
    income = forms.IntegerField(label="Monthly Income")
    category = forms.ChoiceField(
        choices=[
            ("general", "General"),
            ("obc", "OBC"),
            ("sc", "SC"),
            ("st", "ST"),
        ],
        label="Category"
    )
