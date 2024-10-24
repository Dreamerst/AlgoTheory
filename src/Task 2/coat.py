class Coat:
    def __init__(self, size: int, buttons: int):
        if (size >= 38) and (size <= 64):
            self.size = size
        else:
            raise ValueError(f"Use russian clothing size: 38 - 64, not {size}")
        if buttons >= 0:
            self.buttons = buttons
        else:
            raise ValueError("Buttons can not be less than zero")

    def info(self):
        if self.buttons == 0:
            return f"Пиджак без пуговиц {self.size} размера"
        else:
            return f"Пиджак с {self.buttons} пуговиц {self.size} размера"

    def fabric_calculation(self) -> float:
        min_fabric = 2
        fabric = min_fabric + int((self.size - 38) / 3) / 10
        return fabric

    def cost_calculation(self) -> int:
        fabric = self.fabric_calculation()
        cost = int(fabric * 800) + self.buttons * 150
        return cost
