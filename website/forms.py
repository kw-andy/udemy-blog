from django import forms
from blog.models import BlogPost


JOBS = (
    ("python", "Développeur Python"),
    ("rust", "Développeur Rust"),
    ("js", "Développeur Javascript"),
    )


class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de $")
        return pseudo

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title",
                  "author",
                  "date",
                  "category",
                  "description"]

