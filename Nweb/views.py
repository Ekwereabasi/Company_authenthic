from django.shortcuts import render, redirect
from .forms import ProjectInquiryForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm  # Import your PostForm


def project_inquiry(request):
    if request.method == 'POST':
        form = ProjectInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_success')
    else:
        form = ProjectInquiryForm()

    return render(request, 'Nweb/index.html', {'form': form})

def inquiry_success(request):
    return render(request, 'Nweb/inquiry_success.html')


def Maintenance(request):
    return render(request, 'Nweb/Maintenance.html')


# New views for additional pages
def about(request):
    form = ProjectInquiryForm()# Your form instance
    return render(request, 'Nweb/about.html', {'form': form})

def services(request):
    form = ProjectInquiryForm()# Your form instance
    return render(request, 'Nweb/services.html', {'form': form})


def book(request):
    form = ProjectInquiryForm()# Your form instance
    return render(request, 'Nweb/book.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'Nweb/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'Nweb/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm  # Use the custom form
    template_name = 'Nweb/post_form.html'
    success_url = reverse_lazy('post_list')

    # Optionally override form_valid if custom processing is needed
    def form_valid(self, form):
        return super().form_valid(form)