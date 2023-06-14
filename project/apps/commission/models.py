from django.db import models

# Create your models here.
TYPE_CATEGORY_CHOICES = [('APERTURA DE CUENTAS', 'APERTURA DE CUENTAS'),('GASTOS DE MANTENIMIENTO', 'GASTOS DE MANTENIMIENTO'),('GASTOS DE ADMINISTRACION DE CHEQUES', 'GASTOS DE ADMINISTRACION DE CHEQUES'),('GIROS Y TRANSFERENCIAS', 'GIROS Y TRANSFERENCIAS'),('EMBARGOS Y OFICIOS JUDICIALES', 'EMBARGOS Y OFICIOS JUDICIALES'), ('OTROS GASTOS / COMISIONES ADMINISTRATIVOS Y DE SERVICIOS', 'OTROS GASTOS / COMISIONES ADMINISTRATIVOS Y DE SERVICIOS')]
TYPE_SUBCATEGORY_CHOICES = [('General', 'General'),('Gastos de Apertura Cuenta Corriente', 'Gastos de Apertura Cuenta Corriente'),('Requisitos', 'Requisitos'),('Cajas de Seguridad', 'Cajas de Seguridad'),('Mantenim. de Cuenta Corriente "Operativa"/ Cuenta especial Ley 27260', 'Mantenim. de Cuenta Corriente "Operativa"/ Cuenta especial Ley 27260'), ('Resumen de cuenta impreso - a requerimiento del Cliente', 'Resumen de cuenta impreso - a requerimiento del Cliente'),('Otros gastos', 'Otros gastos'),('Cheques Rechazados de terceros', 'Cheques Rechazados de terceros'),('Cheques Rechazados propios (por cheque)', 'Cheques Rechazados propios (por cheque)'), ('Clearing de Cheques', 'Clearing de Cheques'),('Giros y Transferencias Nacionales', 'Giros y Transferencias Nacionales'),('Giros y Transferencias Internacionales', 'Giros y Transferencias Internacionales'),('Fotocopias','Fotocopias')]
CURRENCY_CHOICES = [('N/A', 'N/A'),('PESOS', 'PESOS'),('DÓLARES', 'DÓLARES')]
FREQUENCY_CHOICES = [('N/A', 'N/A'),('EN SU OPORTUNIDAD', 'EN SU OPORTUNIDAD'),('ANUAL', 'ANUAL'),('SEMESTRAL', 'SEMESTRAL'),('TRIMESTRAL', 'TRIMESTRAL'),('MENSUAL', 'MENSUAL'),('DIARIA', 'DIARIA')]
TYPE_COMMISSION_CHOICES = [('SIN CARGO', 'SIN CARGO'),('SOLO COSTO', 'SOLO COSTO'),('CON CARGO', 'CON CARGO')]
TYPE_COST_CHOICES = [('N/A', 'N/A'),('VARIABLE', 'VARIABLE'),('FIJO', 'FIJO')]


class Commissions_USF(models.Model):
    id_category = models.CharField(max_length=100, choices= TYPE_CATEGORY_CHOICES, default='APERTURA DE CUENTAS')
    id_subcategory = models.CharField(max_length=100, choices= TYPE_SUBCATEGORY_CHOICES , default='General')
    date_of_entry = models.DateField() 
    name_commission = models.CharField(max_length=100, unique = True )
    description = models.CharField(max_length=500,blank=True, null=True)
    type_commission = models.CharField(max_length=100, choices= TYPE_COMMISSION_CHOICES, default='CON BENEFICIO')
    type_cost = models.CharField(max_length=50, choices= TYPE_COST_CHOICES, default='$')
    currency = models.CharField(max_length=50, choices= CURRENCY_CHOICES, default='PESOS')
    frequency = models.CharField(max_length=50, choices= FREQUENCY_CHOICES, default='EN SU OPORTUNIDAD')
    application_base = models.CharField(max_length=100,blank=True, null=True)
    class Meta:
        verbose_name = 'Comisión' 
        verbose_name_plural = 'Comisiones' 
    def __str__(self):
        return self.name_commission 

class Input_Commissions_USF(models.Model):
    idfk_commission = models.ForeignKey(Commissions_USF, on_delete=models.SET_NULL, blank=True, null=True)
    date_of_entry = models.DateField()
    name_employee = models.CharField(max_length=50)
    minimum_amount = models.FloatField(max_length=50,blank=True, null=True)
    fixed_amount = models.FloatField(max_length=50,blank=True, null=True)
    maximum_amount = models.FloatField(max_length=50,blank=True, null=True)
    additional_amount = models.FloatField(max_length=50,blank=True, null=True)
    class Meta:
        verbose_name = 'Valor de comisión' 
        verbose_name_plural = 'Valores de Comisiones' 
    def __str__(self):
        return str(self.idfk_commission)

class Discount_CommissionsBank_USF(models.Model): 
    idfk_commission= models.ForeignKey(Commissions_USF, on_delete=models.SET_NULL, blank=True, null=True)
    name_employee = models.CharField(max_length=50)
    name_client = models.CharField(max_length=50)
    percent_discount = models.IntegerField()
    application_base = models.CharField(max_length=100,blank=True, null=True)
    class Meta:
        verbose_name = 'Descuento de comisión' 
        verbose_name_plural = 'Descuentos de comisiones' 
    def __str__(self):
        return self.name_client
    
   