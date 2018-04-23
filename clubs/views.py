from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.views import View
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
import datetime
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from QuickRegister.models import Profile
from django.contrib import messages

from django.views.generic.edit import FormView
from .forms import ClubForm

class CreateView(LoginRequiredMixin, FormView):
    template_name = 'clubs/create.html'
    form_class = ClubForm
    success_url = '/clubs'

    def form_valid(self, form):
        club = form.save(commit=False)
        # club.refresh_from_db()
        name = form.cleaned_data.get('name')
        if not Club.objects.filter(name=name):
            club.name = name
            club.description = form.cleaned_data.get('description')
            club.save()
            messages.success(self.request, 'Successfully created ' + club.name)
        else:
            messages.error(self.request, 'Club with the same name already exists')
        return super().form_valid(form)

class HomeView(TemplateView):
    template_name = 'clubs/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['clubs'] = Club.objects.all()
        return context


class ClubView(TemplateView):
    template_name = 'clubs/club.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['club'] = get_object_or_404(Club, pk=kwargs['pk'])
        return context

def export_csv(request, **kwargs):
    if request.method == 'GET':
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        fields = Profile._meta.get_fields()
        club = get_object_or_404(Club, pk=kwargs['pk'])
        # Write headers
        writer.writerow([
            smart_str(field.name) for field in fields
        ])

        # Write content
        writer.writerow([
            smart_str(getattr(x.user.profile, field.name)) for x in Membership.objects.filter(club=club) for field in fields 
        ])
        return response


class JoinView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        club = get_object_or_404(Club, pk=kwargs['pk'])
        if not Membership.objects.filter(user=self.request.user, club=club):
            membership = Membership(
                user=self.request.user,
                club=club,
                date_joined=datetime.datetime.now())
            membership.save()
            return HttpResponse("Successfully joined {}".format(club))
        return HttpResponse("You are already part of {}".format(club))

class MembersView(LoginRequiredMixin, TemplateView):
    template_name = 'clubs/members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club = get_object_or_404(Club, pk=kwargs['pk'])
        context['members'] = [x.user for x in Membership.objects.filter(club=club)]
        return context

class QrView(TemplateView):
    template_name = 'clubs/qr.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = get_object_or_404(Club, pk=kwargs['pk'])
        return context

class LeaveView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        club = get_object_or_404(Club, pk=kwargs['pk'])
        membership = Membership.objects.filter(user=self.request.user, club=club)
        if membership:
            membership.delete()
        return HttpResponseRedirect(reverse('clubs:home'))
# for future reference..
# def export_csv(modeladmin, request, queryset):
#     import csv
#     from django.utils.encoding import smart_str
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
#     writer = csv.writer(response, csv.excel)
#     response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
#     fields = Club._meta.get_fields()
#     writer.writerow([
#         smart_str(field.name) for field in fields
#     ])
#     for obj in queryset:
#         writer.writerow([
#             smart_str(obj._meta.get_field(field.name)) for field in fields
#         ])
#     return response
# export_csv.short_description = u"Export CSV"

# def export_xls(modeladmin, request, queryset):
#     import xlwt
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet("MyModel")
    
#     row_num = 0
    
#     columns = [
#         (u"ID", 2000),
#         (u"Title", 6000),
#         (u"Description", 8000),
#     ]

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     for col_num in xrange(len(columns)):
#         ws.write(row_num, col_num, columns[col_num][0], font_style)
#         # set column width
#         ws.col(col_num).width = columns[col_num][1]

#     font_style = xlwt.XFStyle()
#     font_style.alignment.wrap = 1
    
#     for obj in queryset:
#         row_num += 1
#         row = [
#             obj.pk,
#             obj.title,
#             obj.description,
#         ]
#         for col_num in xrange(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
            
#     wb.save(response)
#     return response
    
# export_xls.short_description = u"Export XLS"

# def export_xlsx(modeladmin, request, queryset):
#     import openpyxl
#     from openpyxl.cell import get_column_letter
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename=mymodel.xlsx'
#     wb = openpyxl.Workbook()
#     ws = wb.get_active_sheet()
#     ws.title = "MyModel"

#     row_num = 0

#     columns = [
#         (u"ID", 15),
#         (u"Title", 70),
#         (u"Description", 70),
#     ]

#     for col_num in xrange(len(columns)):
#         c = ws.cell(row=row_num + 1, column=col_num + 1)
#         c.value = columns[col_num][0]
#         c.style.font.bold = True
#         # set column width
#         ws.column_dimensions[get_column_letter(col_num+1)].width = columns[col_num][1]

#     for obj in queryset:
#         row_num += 1
#         row = [
#             obj.pk,
#             obj.title,
#             obj.description,
#         ]
#         for col_num in xrange(len(row)):
#             c = ws.cell(row=row_num + 1, column=col_num + 1)
#             c.value = row[col_num]
#             c.style.alignment.wrap_text = True

#     wb.save(response)
#     return response

# export_xlsx.short_description = u"Export XLSX"
