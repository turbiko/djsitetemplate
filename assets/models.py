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

class AssetItem(models.Model):
    item_1c = models.OneToOneField('AssetItem1C', blank=True, null=True, on_delete=models.SET_NULL)


# Справочник.ОсновныеСредства (Основная) -  dbo._Reference1087
class AssetItem1C(models.Model):
    idrref = models.TextField(_('Ссылка'), db_column='_IDRRef')  # Ссылка
    version = models.TextField(_('ВерсияДанных'), db_column='_Version')  # ВерсияДанных
    marked = models.TextField(_('ПометкаУдаления'), db_column='_Marked')  # ПометкаУдаления
    predefinedid = models.TextField(_('ИмяПредопределенныхДанных'), db_column='_PredefinedID')  # ИмяПредопределенныхДанных
    owneridrref = models.TextField(_('Владелец'), db_column='_OwnerIDRRef')  # Владелец
    parentidrref = models.TextField(_('Родитель'), db_column='_ParentIDRRef')  # Родитель
    folder = models.TextField(_('ЭтоГруппа'), db_column='_Folder')  # ЭтоГруппа
    code = models.CharField(_('Код'), db_column='_Code', max_length=7)  # Код
    description = models.CharField(_('Наименование'), db_column='_Description', max_length=150)  # Наименование
    fld1138 = models.CharField(_('НаименованиеПолное'), db_column='_Fld1138', max_length=300, blank=True, null=True)  # НаименованиеПолное [Строка]
    fld1139 = models.TextField(_('Изготовитель'), db_column='_Fld1139', blank=True, null=True)  # Изготовитель [Строка]
    fld1140 = models.TextField(_('НомерПаспорта'), db_column='_Fld1140', blank=True, null=True)  # НомерПаспорта [Строка]
    fld1141 = models.CharField(_('ЗаводскойНомер'), db_column='_Fld1141', max_length=70, blank=True, null=True)  # ЗаводскойНомер [Строка]
    fld1142 = models.DateTimeField(_('ДатаВыпуска'), db_column='_Fld1142', blank=True, null=True)  # ДатаВыпуска [Дата]
    fld1143 = models.TextField(_('Комментарий'), db_column='_Fld1143', blank=True, null=True)  # Комментарий [Строка]
    fld1144 = models.TextField(_('Автотранспорт'), db_column='_Fld1144', blank=True, null=True)  # Автотранспорт [Булево]
    fld1145 = models.TextField(_('Модель'), db_column='_Fld1145', blank=True, null=True)  # Модель [Строка]
    fld2797rref = models.TextField(_('СчетУчета'), db_column='_Fld2797RRef', blank=True, null=True)  # СчетУчета [План счетов бухгалтерского учета]
    fld2799rref = models.TextField(_('СчетАмортизации'), db_column='_Fld2799RRef', blank=True, null=True)  # СчетАмортизации [План счетов бухгалтерского учета]
    fld2800 = models.DateTimeField(_('ДатаВвода'),db_column='_Fld2800', blank=True, null=True)  # ДатаВвода [Дата]
    fld2801 = models.DecimalField(_('СрокИспользования'), db_column='_Fld2801', max_digits=5, decimal_places=1, blank=True, null=True)  # СрокИспользования [Число]
    fld2802rref = models.TextField(_('ВидАмортизации'), db_column='_Fld2802RRef', blank=True, null=True)  # ВидАмортизации [Виды амортизации]
    fld2803 = models.DecimalField(_('ПроцентАмортизации'), db_column='_Fld2803', max_digits=5, decimal_places=2, blank=True, null=True)  # ПроцентАмортизации [Число]
    fld2804rref = models.TextField(_('СтатьяЗатратАмортизации'), db_column='_Fld2804RRef', blank=True, null=True)  # СтатьяЗатратАмортизации [Статьи доходов/затрат (бух.)]
    fld2805rref = models.TextField(_('СчетИнвестиций'), db_column='_Fld2805RRef', blank=True, null=True)  # СчетИнвестиций [План счетов бухгалтерского учета]
    fld3129rref = models.TextField(_('МестоХранения'), db_column='_Fld3129RRef', blank=True, null=True)  # МестоХранения [Места хранения]
    fld3144rref = models.TextField(_('НалоговаяГруппа'), db_column='_Fld3144RRef', blank=True, null=True)  # НалоговаяГруппа [Налоговые группы необоротных активов]
    fld3145 = models.TextField(_('МНМА'), db_column='_Fld3145', blank=True, null=True)  # МНМА [Булево]
    fld3170rref = models.TextField(_('СчетЗатрат'), db_column='_Fld3170RRef', blank=True, null=True)  # СчетЗатрат [План счетов бухгалтерского учета]
    fld3175 = models.DateTimeField(_('ДатаЛиквидации'), db_column='_Fld3175', blank=True, null=True)  # ДатаЛиквидации [Дата]
    fld3239rref = models.TextField(_('ВидАктива'), db_column='_Fld3239RRef', blank=True, null=True)  # ВидАктива [Виды необоротных активов]
    fld3263 = models.DecimalField(_('ЛиквидационнаяСтоимость'), db_column='_Fld3263', max_digits=15, decimal_places=2, blank=True, null=True)  # ЛиквидационнаяСтоимость [Число]
    fld3698rref = models.TextField(_('КодУКТВЭД'), db_column='_Fld3698RRef', blank=True, null=True)  # КодУКТВЭД [Классификатор кодов для НН]
    fld3898rref = models.TextField(_('СтавкаНДС'), db_column='_Fld3898RRef', blank=True, null=True)  # СтавкаНДС [Налоги] --- _Fld3898RRef
    fld4512 = models.CharField(_('СтарыйИнвНомер'), db_column='_Fld4512', max_length=15, blank=True, null=True)  # СтарыйИнвНомер [Строка]
    fld4513 = models.DecimalField(_('СуммаФиксАмортизации'), db_column='_Fld4513', max_digits=15, decimal_places=2, blank=True, null=True)  # СуммаФиксАмортизации [Число]
    fld4516 = models.CharField(_('Штрихкод'), db_column='_Fld4516', max_length=15, blank=True, null=True)  # Штрихкод [Строка]
    fld4735rref = models.TextField(_('ГруппаМСФО'), db_column='_Fld4735RRef', blank=True, null=True)  # ГруппаМСФО [Группы НА МСФО]
    fld4990 = models.DecimalField(_('СтоимостьПриобретенияБезНДС'), db_column='_Fld4990', max_digits=15, decimal_places=2, blank=True, null=True)  #  СтоимостьПриобретенияБезНДС [Число]
    fld4991 = models.DecimalField(_('ПриобретениеНДС'), db_column='_Fld4991', max_digits=15, decimal_places=2, blank=True, null=True)  # ПриобретениеНДС [Число]
    fld6075rref = models.TextField(_('ВидДеятельностиАмортизации'), db_column='_Fld6075RRef', blank=True, null=True)  # ВидДеятельностиАмортизации [Виды деятельности]
    fld6127 = models.TextField(_('АмортизацияВСчетДохода'), db_column='_Fld6127', blank=True, null=True)  # АмортизацияВСчетДохода [Булево]
    fld6128rref = models.TextField(_('АмДоходСчетУчета'), db_column='_Fld6128RRef', blank=True, null=True)  # АмДоходСчетУчета [План счетов бухгалтерского учета]
    fld6129rref = models.TextField(_('АмДоходСчетДохода'), db_column='_Fld6129RRef', blank=True, null=True)  # АмДоходСчетДохода [План счетов бухгалтерского учета]
    fld6130rref = models.TextField(_('АмДоходСтатьяДохода'), db_column='_Fld6130RRef', blank=True, null=True)  # АмДоходСтатьяДохода [Статьи доходов/затрат (бух.)]
    fld9601 = models.DecimalField(_('АмортизацияУУ'), db_column='_Fld9601', max_digits=1, decimal_places=0, blank=True, null=True)  # АмортизацияУУ [Число]
    fld10200 = models.TextField(_('ТелепрограммаЗакупная'), db_column='_Fld10200', blank=True, null=True)  # ТелепрограммаЗакупная [Булево]
    fld10201 = models.TextField(_('ТелепрограммаСобственная'), db_column='_Fld10201', blank=True, null=True)  # ТелепрограммаСобственная [Булево]
    fld10202 = models.TextField(_('Спонсорская'), db_column='_Fld10202', blank=True, null=True)  # Спонсорская [Булево]
    fld10203 = models.TextField(_('МузыкальнаяСправкаНаличие'), db_column='_Fld10203', blank=True, null=True)  # МузыкальнаяСправкаНаличие [Булево]
    fld10204 = models.TextField(_('ПрограммаНаРесурсе'), db_column='_Fld10204', blank=True, null=True)  # ПрограммаНаРесурсе [Булево]
    fld10205 = models.CharField(_('ОписаниеУкр'), db_column='_Fld10205', max_length=1000, blank=True, null=True)  # ОписаниеУкр [Строка]
    fld10206 = models.CharField(_('ОписаниеРус'), db_column='_Fld10206', max_length=1000, blank=True, null=True)  # ОписаниеРус [Строка]
    fld10207 = models.TextField(_('ПрокатноеСвидетельствоНаличие'), db_column='_Fld10207', blank=True, null=True)  # ПрокатноеСвидетельствоНаличие [Булево]
    fld10208 = models.CharField(_('СканСсылкаМузСправка'), db_column='_Fld10208', max_length=300, blank=True, null=True)  # СканСсылкаМузСправка [Строка]
    fld10209 = models.CharField(_('СканСсылкаПрокат'), db_column='_Fld10209', max_length=300, blank=True, null=True)  # СканСсылкаПрокат [Строка]
    fld10220rref = models.TextField(_('ПроизводствоПрограмм'), db_column='_Fld10220RRef', blank=True, null=True)  # ПроизводствоПрограмм [Производство программ]
    fld10256 = models.DecimalField(_('Хронометраж'), db_column='_Fld10256', max_digits=5, decimal_places=0, blank=True, null=True)  # Хронометраж [Число]
    fld10257 = models.DateTimeField(_('НачалоПериодаПоказа'), db_column='_Fld10257', blank=True, null=True)  # НачалоПериодаПоказа [Дата]
    fld10258 = models.DateTimeField(_('ОкончаниеПериодаПоказа'), db_column='_Fld10258', blank=True, null=True)  # ОкончаниеПериодаПоказа [Дата]
    fld10259rref = models.TextField(_('ЯзыкВедущего'), db_column='_Fld10259RRef', blank=True, null=True)  # ЯзыкВедущего [Языки]
    fld10260rref = models.TextField(_('ЯзыкВКадре'), db_column='_Fld10260RRef', blank=True, null=True)  # ЯзыкВКадре [Языки]
    fld10261rref = models.TextField(_('ЯзыкАдаптации'), db_column='_Fld10261RRef', blank=True, null=True)  # ЯзыкАдаптации [Языки]
    fld10445 = models.DecimalField(_('СуммаФиксАмортизацииНУ'), db_column='_Fld10445', max_digits=15, decimal_places=2, blank=True, null=True)  # СуммаФиксАмортизацииНУ [Число]
    fld10483 = models.DateTimeField(_('НачалоПрав'), db_column='_Fld10483', blank=True, null=True)  # НачалоПрав [Дата]
    fld10484 = models.DateTimeField(_('ОкончаниеПрав'), db_column='_Fld10484', blank=True, null=True)  # ОкончаниеПрав [Дата]
    fld10485 = models.CharField(_('ХронометражЗакуп'), db_column='_Fld10485', max_length=10, blank=True, null=True)  # ХронометражЗакуп [Строка]
    fld10549 = models.TextField(_('ПереносноеУстройство'), db_column='_Fld10549', blank=True, null=True)  # ПереносноеУстройство [Булево]
    fld10577 = models.DecimalField(_('СрокИспользованияУУ'), db_column='_Fld10577', max_digits=5, decimal_places=1, blank=True, null=True)  # СрокИспользованияУУ [Число]
    fld10742 = models.TextField(_('ТехникаИтОтдела'), db_column='_Fld10742', blank=True, null=True)  # ТехникаИтОтдела [Булево]
    fld3817 = models.TextField(_('НеХозДеятельность'), db_column='_Fld3817')  # НеХозДеятельность [Булево]

    # class Meta:
        # managed = False
        # db_table = '_Reference1087'
