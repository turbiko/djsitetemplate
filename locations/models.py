# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _

class LocationLinks(models.Model):
    location_1c = models.OneToOneField('Location1C', blank=True, null=True, on_delete=models.SET_NULL)

# РегистрСведений.РазмещениеНА (Основная) -  dbo._InfoRg3162
class Location1C(models.Model):
    period = models.DateTimeField(_('Период'), db_column='_Period')  # Период
    recordertref = models.TextField(_('Регистратор T'), db_column='_RecorderTRef')  # Регистратор
    recorderrref = models.TextField(_('Регистратор R'), db_column='_RecorderRRef')  # Регистратор
    lineno = models.DecimalField(_('НомерСтроки'), db_column='_LineNo', max_digits=9, decimal_places=0)  # НомерСтроки
    active = models.TextField(_('Активность'), db_column='_Active')  # Активность --- _Active
    fld3163rref = models.TextField(_('Организация'), db_column='_Fld3163RRef')  # Организация [Организации]
    fld3164rref = models.TextField(_('НА'), db_column='_Fld3164RRef')  # НА [Необоротные активы]
    fld3165rref = models.TextField(_('Проект'), db_column='_Fld3165RRef')  # Проект [Проекты]
    fld3166rref = models.TextField(_('Физлицо'), db_column='_Fld3166RRef')  # Физлицо [Физические лица]
    fld3176rref = models.TextField(_('МестоХранения'), db_column='_Fld3176RRef')  # МестоХранения [Места хранения]

    # class Meta:
        # managed = False
        # db_table = '_InfoRg3162'
