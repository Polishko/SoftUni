from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: list = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        output = []
        rooms_copy = self.rooms.copy()

        for room in rooms_copy:
            room_monthly_expenses = room.expenses + room.room_cost

            if room.budget >= room_monthly_expenses:
                room.budget -= room_monthly_expenses
                output.append(f"{room.family_name} paid {room_monthly_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return "\n".join(output)

    def status(self):
        output = [f"Total population: {sum(room.members_count for room in self.rooms)}"]
        for room in self.rooms:
            output.append(f"{room.family_name} with {room.members_count} members. Budget: "
                          f"{room.budget:.2f}$, Expenses: {room.expenses:.2f}$")

            for i in range(len(room.children)):
                output.append(f"--- Child {i + 1} monthly cost: {room.children[i].get_monthly_expense():.2f}$")

            output.append(f"--- Appliances monthly cost: "
                          f"{sum(appl.get_monthly_expense() for appl in room.appliances):.2f}$")

        return "\n".join(output)
