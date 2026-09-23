from abc import ABC, abstractmethod

# 1. ABSTRACTION
class FamilyMember(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def perform_role(self) -> str:
        """Abstract method; details are hidden, implementation required by subclasses."""
        pass



# 2. ENCAPSULATION


class Parent(FamilyMember):
    def __init__(self, name: str, age: int, savings: float):
        super().__init__(name, age)
        self.__savings = savings  

    def get_savings(self) -> float:
        return self.__savings

    def contribute_savings(self, amount: float):
        if amount > 0:
            self.__savings += amount

    def perform_role(self) -> str:
        return f"{self.name} manages the household finances."


# 3. INHERITANCE
class Child(Parent):
    def __init__(self, name: str, age: int, savings: float, school: str):
        super().__init__(name, age, savings)
        self.school = school  # Unique attribute for Child

    # 4. POLYMORPHISM (Method Overriding)
    def perform_role(self) -> str:
        return f"{self.name} goes to {self.school} and focuses on studying."



# 5. (Execution)
if __name__ == "__main__":
    father = Parent(name="John", age=45, savings=50000.0)
    daughter = Child(name="Emily", age=16, savings=500.0, school="Pinecrest High")

    print(f"Initial family savings: ${father.get_savings()}")
    father.contribute_savings(1500.0)
    print(f"Updated family savings: ${father.get_savings()}\n")

    family: list[FamilyMember] = [father, daughter]
    
    for member in family:
        print(f"Member: {member.name}")
        print(f"Role: {member.perform_role()}\n")
