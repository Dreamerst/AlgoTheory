class Trousers:
    def __init__(self, size: int, belt: bool):
        if (size >= 38) and (size <= 64):
            self.size = size
        else:
            raise ValueError(f"Use russian clothing size: 38 - 64, not {size}")
        self.belt = belt

    def info(self):
        if not self.belt:
            return f"Брюки без ремня {self.size} размера"
        else:
            return f"Брюки с ремнём {self.size} размера"

    def fabric_calculation(self) -> float:
        min_fabric = 1.2
        fabric = min_fabric + int((self.size - 38) / 3) / 20
        return fabric

    def cost_calculation(self) -> int:
        fabric = self.fabric_calculation()
        if self.belt:
            cost = int(fabric * 900) + 200
        else:
            cost = int(fabric * 900)
        return cost
