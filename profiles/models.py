# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='defaultuser.jpg', upload_to='profile_images')
    full_name = models.CharField(max_length=150)
    connected_1c_profile = models.OneToOneField('Person1C', blank=True, null=True, on_delete=models.SET_NULL)


# Справочник.ФизическиеЛица (Основная) -  dbo._Reference44
class Person1C(models.Model):
    idrref = models.TextField(db_column='_IDRRef')  # Ссылка --- _ID
    version = models.TextField(db_column='_Version')  # ВерсияДанных --- _Version
    marked = models.TextField(db_column='_Marked')  # ПометкаУдаления --- _Marked
    predefinedid = models.TextField(db_column='_PredefinedID')  # ИмяПредопределенныхДанных --- _PredefinedID
    parentidrref = models.TextField(db_column='_ParentIDRRef')  # Родитель --- _ParentID
    folder = models.TextField(db_column='_Folder')  # ЭтоГруппа --- _Folder
    code = models.CharField(db_column='_Code', max_length=9)  # Код --- _Code
    description = models.CharField(db_column='_Description', max_length=100)  # Наименование --- _Description
    fld433 = models.CharField(db_column='_Fld433', max_length=50, blank=True, null=True)  # Фамилия [Строка] --- _Fld433
    fld434 = models.CharField(db_column='_Fld434', max_length=50, blank=True, null=True)  # Имя [Строка] --- _Fld434
    fld435 = models.CharField(db_column='_Fld435', max_length=50, blank=True, null=True)  # Отчество [Строка] --- _Fld435
    fld436rref = models.TextField(db_column='_Fld436RRef', blank=True, null=True)  # Пол [Пол] --- _Fld436RRef
    fld437 = models.CharField(db_column='_Fld437', max_length=12, blank=True, null=True)  # ИНН [Строка] --- _Fld437
    fld438 = models.CharField(db_column='_Fld438', max_length=100, blank=True, null=True)  # EMail [Строка] --- _Fld438
    fld439 = models.DateTimeField(db_column='_Fld439', blank=True, null=True)  # ДатаРождения [Дата] --- _Fld439
    fld440 = models.CharField(db_column='_Fld440', max_length=250, blank=True, null=True)  # МестоРождения [Строка] --- _Fld440
    fld441 = models.CharField(db_column='_Fld441', max_length=100, blank=True, null=True)  # АдресПрописки [Строка] --- _Fld441
    fld442 = models.CharField(db_column='_Fld442', max_length=100, blank=True, null=True)  # АдресПроживания [Строка] --- _Fld442
    fld443 = models.CharField(db_column='_Fld443', max_length=50, blank=True, null=True)  # ТелефонМоб [Строка] --- _Fld443
    fld444 = models.CharField(db_column='_Fld444', max_length=13, blank=True, null=True)  # ТелефонВнутр [Строка] --- _Fld444
    fld445rref = models.TextField(db_column='_Fld445RRef', blank=True, null=True)  # Фото [Хранилище файлов] --- _Fld445RRef
    fld1219 = models.TextField(db_column='_Fld1219', blank=True, null=True)  # Комментарий [Строка] --- _Fld1219
    fld1220 = models.CharField(db_column='_Fld1220', max_length=14, blank=True, null=True)  # ПаспортСерия [Строка] --- _Fld1220
    fld1221 = models.CharField(db_column='_Fld1221', max_length=14, blank=True, null=True)  # ПаспортНомер [Строка] --- _Fld1221
    fld1222 = models.DateTimeField(db_column='_Fld1222', blank=True, null=True)  # ПаспортДатаВыдачи [Дата] --- _Fld1222
    fld1223 = models.TextField(db_column='_Fld1223', blank=True, null=True)  # ПаспортКемВыдан [Строка] --- _Fld1223
    fld2786rref = models.TextField(db_column='_Fld2786RRef', blank=True, null=True)  # ВидДокумента [Тип документа] --- _Fld2786RRef
    fld2787 = models.TextField(db_column='_Fld2787', blank=True, null=True)  # НеИспользуетсяИНН [Булево] --- _Fld2787
    fld2793 = models.TextField(db_column='_Fld2793', blank=True, null=True)  # НеЯвляетсяНалоговымРезидентом [Булево] --- _Fld2793
    fld3107 = models.CharField(db_column='_Fld3107', max_length=150, blank=True, null=True)  # ФИОнаРусском [Строка] --- _Fld3107
    fld3108 = models.CharField(db_column='_Fld3108', max_length=40, blank=True, null=True)  # Гражданство [Строка] --- _Fld3108
    fld3694 = models.CharField(db_column='_Fld3694', max_length=100, blank=True, null=True)  # ИдентификаторЗУП [Строка] --- _Fld3694
    fld3699 = models.CharField(db_column='_Fld3699', max_length=100, blank=True, null=True)  # ИдентификаторЗУП_Сотрудник [Строка] --- _Fld3699
    fld8581 = models.TextField(db_column='_Fld8581', blank=True, null=True)  # БанковскиеРеквизиты [Строка] --- _Fld8581
    fld2522rref = models.TextField(db_column='_Fld2522RRef')  # Автор [Пользователи (настройки)] --- _Fld2522RRef
    fld2973rref = models.TextField(db_column='_Fld2973RRef')  # АвторСоздания [Пользователи (настройки)] --- _Fld2973RRef
    fld7296 = models.DateTimeField(db_column='_Fld7296')  # ДатаСоздания [Дата] --- _Fld7296
    fld7297 = models.DateTimeField(db_column='_Fld7297')  # ДатаИзменения [Дата] --- _Fld7297

    # class Meta:
        # managed = False
        # db_table = '_Reference44'
