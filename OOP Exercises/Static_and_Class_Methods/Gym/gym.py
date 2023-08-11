from typing import List
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        current_customer = [c for c in self.customers if current_subscription.customer_id == c.id][0]
        current_trainer = [t for t in self.trainers if current_subscription.trainer_id == t.id][0]
        current_plan = [p for p in self.plans if current_subscription.exercise_id == p.id][0]
        current_equipment = [e for e in self.equipment if current_plan.equipment_id == e.id][0]

        return f"{current_subscription}\n{current_customer}\n{current_trainer}\n{current_equipment}\n{current_plan}"
