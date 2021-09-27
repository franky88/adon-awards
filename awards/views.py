from django.shortcuts import render, redirect, get_object_or_404
from .models import Awardee
from .forms import AddAwardeeForm
from django.http import HttpResponse
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime

from awards import forms
# Create your views here.


def render_pdf_view(request, *args, **kwargs):
    award_code = kwargs.get('award_code')
    award = get_object_or_404(Awardee, award_code=award_code)
    template_path = 'award_pdf.html'
    context = {
        'title': 'adon award',
        'instance': award,
        'director1': 'peter baily',
        'director2': 'paul harding',
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=award_' + \
    #     award.name + '.pdf'
    response['Content-Disposition'] = 'filename=adon_award_' + \
        award.name.replace(" ", "_").title()+"_" + str(award.date) + '.pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def export_pdf_by_date(request):
    to_export_awards = Awardee.objects.all()
    query = request.GET.get("q")
    print("query results", query)
    if query:
        to_export_awards = Awardee.objects.filter(
            Q(award_title__title__icontains=query) | Q(name__icontains=query) | Q(date__iexact=query)).distinct()
    print("Data from to export", to_export_awards)
    template_path = 'export_pdf.html'
    context = {
        'title': 'adon awards',
        'director1': 'peter baily',
        'director2': 'paul harding',
        'awards': to_export_awards
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=award_' + \
    #     award.name + '.pdf'
    response['Content-Disposition'] = 'filename=adon_award.pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def adwardList(request):
    to_export_awards = Awardee.objects.all()
    query = request.GET.get("q")
    if query:
        to_export_awards = Awardee.objects.filter(
            Q(award_title__title__icontains=query) | Q(name__icontains=query) | Q(date__iexact=query)).distinct()
    print("Data from to export", to_export_awards)
    awardees = Awardee.objects.all()
    form = AddAwardeeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('awards:list')
    else:
        form = AddAwardeeForm(request.POST or None)
    context = {
        "title": "list of awards",
        "awardees": awardees,
        "form": form,
        "to_export_awards": to_export_awards
    }
    return render(request, "list_awardee.html", context)


def updateAwardee(request, award_code):
    awardee = get_object_or_404(Awardee, award_code=award_code)
    form = AddAwardeeForm(request.POST or None, instance=awardee)
    if form.is_valid():
        awardee = form.save(commit=False)
        awardee.save()
        return redirect('awards:update', award_code=awardee.award_code)
    context = {
        "title": "Update awardee",
        "form": form,
        "instance": awardee
    }
    return render(request, "award_details.html", context)


def deleteAward(request, award_code):
    award = get_object_or_404(Awardee, award_code=award_code)
    award.delete()
    return redirect('awards:list')
