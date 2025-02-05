from django import forms
from App_build.models import CsvUpload

class CsvForm(forms.ModelForm):
    class Meta:
        model = CsvUpload
        fields = ['csv_file']