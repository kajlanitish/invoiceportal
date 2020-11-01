from django.db import models

# Create your models here.

class Vendor(models.Model):
    code = models.CharField(max_length=255, unique=True, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    type = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.code} -- {self.name}'


class Invoice(models.Model):
    invoice_number = models.PositiveIntegerField(unique=True, blank=False)
    doc_number = models.PositiveIntegerField(blank=False)
    type = models.CharField(max_length=255, blank=False, null=False)
    net_due_date = models.DateField(blank=False)
    doc_date = models.DateField(blank=False)
    pstng_date = models.DateField(blank=False)
    amt_in_loc_cur = models.IntegerField(blank=False)
    vendor = models.ForeignKey('upload.Vendor', related_name='invoices', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.invoice_number}'