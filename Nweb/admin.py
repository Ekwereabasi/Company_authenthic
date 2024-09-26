from django.contrib import admin
from .models import ProjectInquiry, Post

@admin.register(ProjectInquiry)
class ProjectInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'budget_size', 'requires_nda', 'created_at')
    list_filter = ('requires_nda', 'created_at')
    search_fields = ('name', 'email', 'referral_source')

    readonly_fields = ('name', 'email', 'budget_size', 'description', 'referral_source', 'requires_nda')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'budget_size', 'description', 'referral_source', 'requires_nda')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Display fields in the list view
    search_fields = ('title', 'content')  # Searchable fields
    list_filter = ('created_at',)  # Filter by creation date
    ordering = ('-created_at',)  # Order posts by creation date descending
