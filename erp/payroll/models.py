from django.db import models
# from django.conf import settings


class Appraisal(models.Model):
    """Appraisal model schema

    Args:
        models (_type_): appraisal model
    """
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        "auths.Employee",
        on_delete=models.CASCADE,
        related_name="employee_appraisals"
    )
    appraisedBy = models.ForeignKey(
        "auths.Employee",
        on_delete=models.CASCADE,
        related_name="appraised_appraisals"
    )
    appraisalDate = models.DateTimeField()
    score = models.FloatField()
    comments = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Appraisal for {self.employee} on {self.appraisalDate}'


class Payroll(models.Model):
    """Payroll model schema

    Args:
        models (_type_): payroll model
    """
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        "auths.Employee",
        on_delete=models.CASCADE,
        related_name="payrolls"
    )
    appraisal = models.ForeignKey(
        Appraisal,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="payrolls"
    )
    designation = models.CharField(max_length=100, blank=False,)
    pay_start_period = models.DateTimeField()
    pay_end_period = models.DateTimeField() 
    gross_salary = models.FloatField()  # Monthly or pay period gross salary
    deductions = models.FloatField()  # Monthly or pay period deductions
    net_salary = models.FloatField()  # Monthly or pay period net salary
    annual_gross_salary = models.FloatField()  # Annual gross salary
    annual_deductions = models.FloatField()  # Annual deductions
    annual_net_salary = models.FloatField()  # Annual net salary
    allowances = models.FloatField()  # Annual net salary
    pay_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payroll for {self.employee.name} on {self.pay_date}'



# annualSalary BHT FLOAT
# annualSalary FLOAT
# monthlySalary FLOAT
# otherAllowance FLOAT
# totalDeductions FLOAT
# monthlyTaxPayable FLOAT
# staffMonthlyNetPay FLOAT
# refund FLOAT
# specialDeduction FLOAT
# payableForTheMonth FLOAT