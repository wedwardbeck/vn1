from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Vendor
from .forms import VendorForm


# Create your views here.

def vendor_list(request):
    vendors = Vendor.objects.filter(added_dt__lte=timezone.now()).order_by('name1')
    return render(request, 'vendors/vendor_list.html', {'vendors': vendors})


def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'vendors/vendor_detail.html', {'vendor': vendor})


def vendor_new(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.added_by = request.user
            vendor.added_dt = timezone.now()
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm()
    return render(request, 'vendors/vendor_edit.html', {'form': form})


def vendor_edit(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.added_by = request.user
            vendor.published_date = timezone.now()
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendors/vendor_edit.html', {'form': form})
