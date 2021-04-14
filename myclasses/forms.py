from django import forms
from .models import AllClasses


class AllClassesForm(forms.ModelForm):
    class Meta:
        model = AllClasses
        fields = ['class_name',
                  'class_join_code',
                  'class_subject',
                  'class_university',
                  'class_collage',
                  'class_department',
                  'class_level',
                  'class_division',
                  'class_year']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'class_name': 'Title',
            'class_join_code': 'Join code',
            'class_subject': 'Subject',
            'class_university': 'University',
            'class_collage': 'Collage',
            'class_department': 'Department',
            'class_level': 'Level',
            'class_division': 'Division',
            'class_year': 'Year',
        }

        self.fields['class_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control f-input'
            self.fields[field].label = False