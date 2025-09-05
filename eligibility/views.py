from django.shortcuts import render
from django import forms

# Form for collecting user input
class EligibilityForm(forms.Form):
    age = forms.IntegerField(label="Age")
    income = forms.IntegerField(label="Monthly Income")
    category = forms.ChoiceField(choices=[
        ("general", "General"),
        ("sc", "SC"),
        ("st", "ST"),
        ("obc", "OBC"),
        ("ews", "EWS"),
        ("minority", "Minority"),
        ("women", "Women"),
        ("pwd", "Disabled / PwD"),
    ])

# View function
def home(request):
    result = None
    schemes = []

    if request.method == "POST":
        form = EligibilityForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data["age"]
            income = form.cleaned_data["income"]
            category = form.cleaned_data["category"]

            # ---------- RULE ENGINE (15+ conditions) ----------
            
            # Low income / general rules
            if age > 60 and income < 20000:
                schemes.append({"name": "Senior Citizen Pension Scheme",
                                "details": "Monthly pension for senior citizens with low income."})

            if income < 15000:
                schemes.append({"name": "General Health Insurance Scheme",
                                "details": "Affordable health insurance for low and middle income groups."})

            if age < 18:
                schemes.append({"name": "Child Education Support",
                                "details": "Financial aid for school students under 18."})

            if 18 <= age <= 25 and income < 30000:
                schemes.append({"name": "Youth Employment Scheme",
                                "details": "Employment support program for youth aged 18–25."})

            if age > 40 and income < 40000:
                schemes.append({"name": "Mid-Career Upskilling Program",
                                "details": "Government sponsored training for professionals above 40."})

            if age > 65:
                schemes.append({"name": "Senior Healthcare Scheme",
                                "details": "Free medical checkups and discounted medicines for 65+ citizens."})

            if income < 10000:
                schemes.append({"name": "Low-Income Housing Aid",
                                "details": "Housing support for families earning below 10k/month."})

            # Category based rules
            if category == "sc" and income < 25000:
                schemes.append({"name": "SC Educational Scholarship",
                                "details": "Scholarship for students from SC category with family income <25k."})

            if category == "st" and income < 20000:
                schemes.append({"name": "ST Development Grant",
                                "details": "Financial aid for Scheduled Tribe families with income below 20k."})

            if category == "obc" and income < 20000:
                schemes.append({"name": "OBC Skill Development Program",
                                "details": "Free skill training for OBC youth with income <20k."})

            if category == "ews" and income < 30000:
                schemes.append({"name": "EWS Subsidy Scheme",
                                "details": "Government subsidy for EWS households earning under 30k."})

            if category == "minority" and income < 25000:
                schemes.append({"name": "Minority Education Support",
                                "details": "Scholarship program for minority students from low-income families."})

            if category == "women" and age >= 21 and income < 20000:
                schemes.append({"name": "Women Empowerment Scheme",
                                "details": "Skill training and financial aid for women above 21 years old."})

            if category == "pwd" and income < 40000:
                schemes.append({"name": "Disability Pension Scheme",
                                "details": "Monthly pension for persons with disabilities (PwD)."})

            # Higher income rules (to cover middle/high earners too)
            if 50000 <= income <= 100000:
                schemes.append({"name": "Middle-Class Housing Loan Subsidy",
                                "details": "Special home loan interest subsidy for middle-class families (₹50k–₹1L income)."})

            if income > 100000 and age < 40:
                schemes.append({"name": "Young Professional Investment Scheme",
                                "details": "Tax-saving investment options for professionals under 40 earning above ₹1L."})

            if income > 100000 and age >= 40:
                schemes.append({"name": "Wealth Management Pension Plan",
                                "details": "Retirement-focused scheme for high earners above 40 years old."})

            # Default if no matches
            if not schemes:
                result = "No eligible schemes found. Please try different inputs."
    else:
        form = EligibilityForm()

    return render(request, "home.html", {"form": form, "result": result, "schemes": schemes})
