from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from ckeditor.widgets import CKEditorWidget

class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm

# Unregister default FlatPage admin
admin.site.unregister(FlatPage)

# Register our customized FlatPage admin
admin.site.register(FlatPage, FlatPageAdmin)