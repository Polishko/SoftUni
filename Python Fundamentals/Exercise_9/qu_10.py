company_employees = {}

while True:
    command = input()

    if command == "End":
        break

    company, employer_id = command.split(" -> ")

    if company not in company_employees:
        company_employees[company] = []

    if employer_id in company_employees[company]: # ya da asagidaki if employee not in dict, boylece continue de gerek yok
        continue

    company_employees[company].append(employer_id)

for company, employees in company_employees.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
