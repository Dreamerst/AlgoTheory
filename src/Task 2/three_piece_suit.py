class ThreePieceSuit:
    def __init__(self, size: int, coat_buttons: int, jacket_buttons: int, belt: bool):
        if (size >= 38) and (size <= 64):
            self.size = size
        else:
            raise ValueError(f"Use russian clothing size: 38 - 64, not {size}")
        if coat_buttons >= 0:
            self.coat_buttons = coat_buttons
        else:
            raise ValueError("Coat buttons can not be less than zero")
        if jacket_buttons >= 0:
            self.jacket_buttons = jacket_buttons
        else:
            raise ValueError("Jacket buttons can not be less than zero")
        self.belt = belt

    def info(self):
        description = f"Костюм-тройка {self.size} размера: "
        if self.coat_buttons == 0:
            description += "пиджак без пуговиц "
        else:
            description += f"пиджак с {self.coat_buttons} пуговиц "
        if self.jacket_buttons == 0:
            description += "жилет без пуговиц "
        else:
            description += f"жилет с {self.jacket_buttons} пуговиц "
        if not self.belt:
            description += "брюки без ремня"
        else:
            description += "брюки с ремнём"
        return description

    def fabric_calculation(self) -> float:
        min_fabric = 6
        fabric = min_fabric + int((self.size - 38) / 3) / 2
        return fabric

    def cost_calculation(self) -> int:
        fabric = self.fabric_calculation()
        if self.belt:
            cost = int(fabric * 1000) + self.coat_buttons * 150 + self.jacket_buttons * 130 + 200
        else:
            cost = int(fabric * 1000) + self.coat_buttons * 150 + self.jacket_buttons * 130
        return cost
