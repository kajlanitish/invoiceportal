from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import xlrd, datetime

from . import models

# Create your views here.

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        spreadsheet = request.FILES.get('invoice_list')
        wb = xlrd.open_workbook(file_contents=spreadsheet.read())
        sheet = wb.sheet_by_index(0)

        no_of_invoices = sheet.nrows - 1
        no_of_vendors = len(set(sheet.col_values(7))) - 1
        sum_of_invoice_amts = sum(sheet.col_values(6)[1:])
        invalid_invoices = 0

        for i in range(1, sheet.nrows):
            row_values = sheet.row_values(i)

            try:
                vendor = models.Vendor.objects.create(
                    code = row_values[-3],
                    name = row_values[-2],
                    type = row_values[-1],    
                )
            except:
                vendor = models.Vendor.objects.get(code__exact=row_values[-3])

            try:            
                if datetime.datetime(*xlrd.xldate_as_tuple(row_values[4], wb.datemode)) > datetime.datetime.now():
                    raise Exception()

                invoice = models.Invoice.objects.create(
                    invoice_number = int(row_values[0]),
                    doc_number = int(row_values[1]),
                    type = row_values[2],
                    net_due_date = datetime.datetime(*xlrd.xldate_as_tuple(row_values[3], wb.datemode)),
                    doc_date = datetime.datetime(*xlrd.xldate_as_tuple(row_values[4], wb.datemode)),
                    pstng_date = datetime.datetime(*xlrd.xldate_as_tuple(row_values[5], wb.datemode)),
                    amt_in_loc_cur = int(row_values[6]),
                    vendor = vendor,
                )
            except:
                invalid_invoices += 1

        return JsonResponse({'No of Invoices Uploaded': no_of_invoices, 'Sum of Invoice Amounts': sum_of_invoice_amts, 'Number of vendors': no_of_vendors, 'Number of Invalid Invoices': invalid_invoices})
    else:
        return JsonResponse({'Msg':'Error: Only POST requests allowed'})
        # Return that only POST requests are allowed