# Question 2

# all values are in US dollars $

Gross_Income=input("Please enter gross income:")
Gross_Income=float(Gross_Income)

Standard_Deduction=10000

Dependents=input("Enter the number of dependents:")
Dependents=int(Dependents)

#  For each dependent, a taxpayer is allowed an additional $3,000 deduction.
Dependent_Deduction=3000

Taxable_Income=Gross_Income-Standard_Deduction-(Dependent_Deduction*Dependents)
# tax rate=20%
Tax=(Taxable_Income*20)/100
print("Tax:",Tax)