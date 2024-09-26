from django import forms
from .models import ProjectInquiry, Post

class ProjectInquiryForm(forms.ModelForm):
    class Meta:
        model = ProjectInquiry
        fields = ['name', 'email', 'budget_size', 'description', 'referral_source', 'requires_nda']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'budget_size': 'Budget Size',
            'description': 'Project Description',
            'referral_source': 'How did you hear about us?',
            'requires_nda': 'This Project requires an NDA',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
