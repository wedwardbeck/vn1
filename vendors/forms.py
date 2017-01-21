from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name1', 'name2', 'address1', 'address2', 'city', 'state', 'vn_ent',
                  'vnstatus', 'vntaxnum', 'added_by')