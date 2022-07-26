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

class Place(models.Model):
    place_1c = models.OneToOneField('Place1C', blank=True, null=True, on_delete=models.SET_NULL)

# Справочник.МестаХранения (Основная) -  dbo._Reference2259
class Place1C(models.Model):
    idrref = models.TextField(_(''), db_column='_IDRRef')  # Ссылка --- _ID
    version = models.TextField(_(''), db_column='_Version')  # ВерсияДанных --- _Version
    marked = models.TextField(_(''), db_column='_Marked')  # ПометкаУдаления --- _Marked
    predefinedid = models.TextField(_(''), db_column='_PredefinedID')  # ИмяПредопределенныхДанных --- _PredefinedID
    parentidrref = models.TextField(_(''), db_column='_ParentIDRRef')  # Родитель --- _ParentID
    folder = models.TextField(_(''), db_column='_Folder')  # ЭтоГруппа --- _Folder
    code = models.CharField(_(''), db_column='_Code', max_length=10)  # Код --- _Code
    description = models.CharField(_(''), db_column='_Description', max_length=150)  # Наименование --- _Description
    fld3015rref = models.TextField(_(''), db_column='_Fld3015RRef', blank=True, null=True)  # МОЛ [Физические лица] --- _Fld3015RRef
    fld3058 = models.TextField(_(''), db_column='_Fld3058', blank=True, null=True)  # СкладТМЦ [Булево] --- _Fld3058
    fld3059 = models.DecimalField(_(''), db_column='_Fld3059', max_digits=3, decimal_places=0, blank=True, null=True)  # Этаж [Число] --- _Fld3059
    fld3060 = models.DecimalField(_(''), db_column='_Fld3060', max_digits=5, decimal_places=0, blank=True, null=True)  # НомерПомещения [Число] --- _Fld3060
    fld3061 = models.DecimalField(_(''), db_column='_Fld3061', max_digits=10, decimal_places=3, blank=True, null=True)  # Площадь [Число] --- _Fld3061
    fld3062 = models.CharField(_(''), db_column='_Fld3062', max_length=5)  # Литера [Строка] --- _Fld3062
    fld3063rref = models.TextField(_(''), db_column='_Fld3063RRef', blank=True, null=True)  # ВидПомещения [Виды помещений] --- _Fld3063RRef
    fld4166 = models.CharField(_(''), db_column='_Fld4166', max_length=100, blank=True, null=True)  # СсылкаВизуализации [Строка] --- _Fld4166
    fld4527 = models.CharField(_(''), db_column='_Fld4527', max_length=15, blank=True, null=True)  # Штрихкод [Строка] --- _Fld4527
    fld4530 = models.CharField(_(''), db_column='_Fld4530', max_length=150, blank=True, null=True)  # Комментарий [Строка] --- _Fld4530
    fld8992 = models.DecimalField(_(''), db_column='_Fld8992', max_digits=15, decimal_places=5, blank=True, null=True)  # СуммаКВтМесяц [Число] --- _Fld8992
    fld10569 = models.CharField(_(''), db_column='_Fld10569', max_length=120, blank=True, null=True)  # НазваниеЛокации [Строка] --- _Fld10569
    fld10576 = models.CharField(_(''), db_column='_Fld10576', max_length=15, blank=True, null=True)  # КодЛокации [Строка] --- _Fld10576
    fld10591 = models.TextField(_(''), db_column='_Fld10591', blank=True, null=True)  # ЭтоЛокация [Булево] --- _Fld10591
    fld190rref = models.TextField(_(''), db_column='_Fld190RRef')  # Проект [Проекты] --- _Fld190RRef
    fld2522rref = models.TextField(_(''), db_column='_Fld2522RRef')  # Автор [Пользователи (настройки)] --- _Fld2522RRef
    fld2973rref = models.TextField(_(''), db_column='_Fld2973RRef')  # АвторСоздания [Пользователи (настройки)] --- _Fld2973RRef

    # class Meta:
        # managed = False
        # db_table = '_Reference2259'
