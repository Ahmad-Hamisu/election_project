# views.py

from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import AnnouncedPuResult, LGA
from .forms import AnnouncedPuResultForm


def polling_unit_result(request, polling_unit_uniqueid):
    results = AnnouncedPuResult.objects.filter(
        polling_unit__id=polling_unit_uniqueid)
    return render(request, 'polling_unit_result.html', {'results': results})


def index(request):
    return render(request, 'index.html')


def success_page(request):
    return render(request, 'success_page.html')


def lga_summed_result(request):
    lgas = LGA.objects.all()
    selected_lga_id = request.GET.get('lga_id', None)

    if selected_lga_id:
        polling_units = AnnouncedPuResult.objects.filter(
            polling_unit__ward__lga__id=selected_lga_id)
        total_results = polling_units.values(
            'party').annotate(total_score=Sum('party_score'))
    else:
        total_results = None

    return render(request, 'lga_summed_result.html', {'lgas': lgas, 'total_results': total_results})


def store_polling_unit_result(request):
    if request.method == 'POST':
        form = AnnouncedPuResultForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other page
            return redirect('success_page')
    else:
        form = AnnouncedPuResultForm()

    return render(request, 'store_polling_unit_result.html', {'form': form})
