from django import forms
from .models import Commissions_USF,Input_Commissions_USF,Discount_CommissionsBank_USF

TYPE_CATEGORY_CHOICES = [('APERTURA DE CUENTAS', 'APERTURA DE CUENTAS'),('GASTOS DE MANTENIMIENTO', 'GASTOS DE MANTENIMIENTO'),('GASTOS DE ADMINISTRACION DE CHEQUES', 'GASTOS DE ADMINISTRACION DE CHEQUES'),('GIROS Y TRANSFERENCIAS', 'GIROS Y TRANSFERENCIAS'),('EMBARGOS Y OFICIOS JUDICIALES', 'EMBARGOS Y OFICIOS JUDICIALES'), ('OTROS GASTOS / COMISIONES ADMINISTRATIVOS Y DE SERVICIOS', 'OTROS GASTOS / COMISIONES ADMINISTRATIVOS Y DE SERVICIOS')]
TYPE_SUBCATEGORY_CHOICES = [('General', 'General'),('Gastos de Apertura Cuenta Corriente', 'Gastos de Apertura Cuenta Corriente'),('Requisitos', 'Requisitos'),('Cajas de Seguridad', 'Cajas de Seguridad'),('Mantenim. de Cuenta Corriente "Operativa"/ Cuenta especial Ley 27260', 'Mantenim. de Cuenta Corriente "Operativa"/ Cuenta especial Ley 27260'), ('Resumen de cuenta impreso - a requerimiento del Cliente', 'Resumen de cuenta impreso - a requerimiento del Cliente'),('Otros gastos', 'Otros gastos'),('Cheques Rechazados de terceros', 'Cheques Rechazados de terceros'),('Cheques Rechazados propios (por cheque)', 'Cheques Rechazados propios (por cheque)'), ('Clearing de Cheques', 'Clearing de Cheques'),('Giros y Transferencias Nacionales', 'Giros y Transferencias Nacionales'),('Giros y Transferencias Internacionales', 'Giros y Transferencias Internacionales'),('Fotocopias','Fotocopias')]
CURRENCY_CHOICES = [('N/A', 'N/A'),('PESOS', 'PESOS'),('DÓLARES', 'DÓLARES')]
FREQUENCY_CHOICES = [('N/A', 'N/A'),('EN SU OPORTUNIDAD', 'EN SU OPORTUNIDAD'),('ANUAL', 'ANUAL'),('SEMESTRAL', 'SEMESTRAL'),('TRIMESTRAL', 'TRIMESTRAL'),('MENSUAL', 'MENSUAL'),('DIARIA', 'DIARIA')]
TYPE_COMMISSION_CHOICES = [('SIN CARGO', 'SIN CARGO'),('SOLO COSTO', 'SOLO COSTO'),('CON CARGO', 'CON CARGO')]
TYPE_COST_CHOICES = [('N/A', 'N/A'),('%', 'INGRESO VARIABLE'),('$', 'INGRESO FIJO')]

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commissions_USF
        fields = '__all__'

class InputForm(forms.ModelForm):
    class Meta:
        model = Input_Commissions_USF
        fields = '__all__'
        
class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount_CommissionsBank_USF
        fields = '__all__'
