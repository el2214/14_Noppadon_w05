'''
# คำนวณภาษีคนที่ 1

salary_1 = 15000
tax = 0.07
ot_time = 10
ot_rate = 200

gross_pay = salary_1 + (ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay_1 = gross_pay - tax_pay

print(f"จ่ายคนที่ 1 :{net_pay_1}")

# คำนวณภาษีคนที่ 2
salary_2 = 24000
tax = 0.07
ot_time_2 = 4
ot_rate_2 = 200

gross_pay = salary_2 + (ot_time_2 * ot_rate)
tax_pay = gross_pay * tax
net_pay_2 = gross_pay - tax_pay

print(f"จ่ายคนที่ 2 :{net_pay_2}")
'''

def calcurate_salary(salary,ot_time,ot_rate,tax):
    gross_pay = salary + (ot_time * ot_rate)
    tax_pay = gross_pay * tax
    net_pay = gross_pay - tax_pay
    return net_pay, tax_pay, gross_pay

emp_1 = calcurate_salary(15000,10,200,0.07)

print(emp_1)
