from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.adult import Adult
from project.clients.student import Student


class BankApp:
    LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def find_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan_obj = self.LOAN_TYPES[loan_type]()
        self.loans.append(loan_obj)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client_obj = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client_obj)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client_obj = self.find_client(client_id)

        if loan_type != client_obj.VALID_LOAN:
            raise Exception("Inappropriate loan type!")

        for i in range(len(self.loans)):
            loan = self.loans[i]

            if loan.__class__.__name__ == loan_type:
                client_obj.loans.append(loan)
                self.loans.remove(self.loans[i])

                return f"Successfully granted {loan_type} to {client_obj.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client_obj = self.find_client(client_id)

        if not client_obj:
            raise Exception("No such client!")

        if len(client_obj.loans) != 0:
            raise Exception("The client has loans! Removal is impossible!")

        for i in range(len(self.clients)):
            client = self.clients[i]
            if client.client_id == client_id:
                client_name = client.name
                self.clients.remove(self.clients[i])
                return f"Successfully removed {client_name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        increased_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                increased_loans += 1

        return f"Successfully changed {increased_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        output = []
        total_clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)

        loans_count_granted_to_clients = 0
        granted_sum = 0
        for client in self.clients:
            loans_count_granted_to_clients += len(client.loans)
            granted_sum += sum(loan.amount for loan in client.loans)

        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)

        try:
            average_interest_clients = sum(client.interest for client in self.clients) / len(self.clients)
        except ZeroDivisionError:
            average_interest_clients = 0

        output.append(f"Active Clients: {total_clients_count}")
        output.append(f"Total Income: {total_clients_income:.2f}")
        output.append(f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}")
        output.append(f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}")
        output.append(f"Average Client Interest Rate: {average_interest_clients:.2f}")

        return "\n".join(output)
