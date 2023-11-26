from datetime import datetime

class Employee:
    def __init__(self, start_date, end_date, name, hours, rate, tax_rate):
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.hours = hours
        self.rate = rate
        self.tax_rate = tax_rate

    @staticmethod
    def get_date_range():
        start_date = input("Enter the 'From' date (mm/dd/yyyy): ")
        end_date = input("Enter the 'To' date (mm/dd/yyyy): ")
        return start_date, end_date

    @staticmethod
    def get_employee_name():
        return input("Enter employee name: ")

    @staticmethod
    def get_total_hours():
        return float(input("Enter total hours: "))

    @staticmethod
    def get_hourly_rate():
        return float(input("Enter hourly rate: "))

    @staticmethod
    def get_income_tax_rate():
        return float(input("Enter income tax rate: "))

    def calculate_pay(self):
        gross_pay = self.hours * self.rate
        income_tax = gross_pay * (self.tax_rate / 100)
        net_pay = gross_pay - income_tax
        return {"gross_pay": gross_pay, "income_tax" : income_tax, "net_pay": net_pay}

    def create_employee_data(self):
        pay = self.calculate_pay()
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "employee_name": self.name,
            "hours" : self.hours,
            "rate" : self.rate,
            "gross_pay" : pay["gross_pay"],
            "tax_rate" : self.tax_rate,
            "income_tax" : pay["income_tax"],
            "net_pay": pay["net_pay"]
            }

def calculate_totals(records):
    totals = {
        "employees": len(records),
        "hours": sum(record['hours'] for record in records),
        "gross_pay": sum(record['gross_pay'] for record in records),
        "tax": sum(record['income_tax'] for record in records),
        "net_pay": sum(record['net_pay'] for record in records)
    }
    return totals

def display_employee_data(employee_data):
    print("\nEmployee Information")
    print(f"From Date: {employee_data['start_date']}")
    print(f"To Date: {employee_data['end_date']}")
    print(f"Employee Name: {employee_data['employee_name']}")
    print(f"Total Hours: {employee_data['hours']}")
    print(f"Hourly Rate: {employee_data['rate']}")
    print(f"Gross Pay: {employee_data['gross_pay']}")
    print(f"Income Tax Rate: {employee_data['tax_rate']}")
    print(f"Income Tax: {employee_data['income_tax']}")
    print(f"Net Pay: {employee_data['net_pay']}")

def display_summary(totals):
    print("\nSummary")
    print(f"Total Employees: {totals['employees']}")
    print(f"Total Hours: {totals['hours']}")
    print(f"Total Gross Pay: {totals['gross_pay']}")
    print(f"Total Tax: {totals['tax']}")
    print(f"Total Net Pay: {totals['net_pay']}")

def main():
    records = []

    while True:
        start_date, end_date = Employee.get_date_range()
        name = Employee.get_employee_name()
        if name.lower() == "end":
            break

        hours = Employee.get_total_hours()
        rate = Employee.get_hourly_rate()
        tax_rate = Employee.get_income_tax_rate()

        employee = Employee(start_date, end_date, name, hours, rate, tax_rate)
        employee_data = employee.create_employee_data()
        records.append(employee_data)
        display_employee_data(employee_data)

    totals = calculate_totals(records)
    display_summary(totals)

if __name__ == "__main__":
    main()