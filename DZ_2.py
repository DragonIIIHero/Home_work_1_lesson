class ZeroDivisior:
    def __init__(self, divi, denom):
        self.divider = divi
        self.denominator = denom

    @staticmethod
    def divide_by_zero(divi, denom):
        try:
            return (divi / denom)
        except:
            return (f"Делить на ноль нельзя")


div = ZeroDivisior(2, 6)
print(ZeroDivisior.divide_by_zero(15, 0))
print(ZeroDivisior.divide_by_zero(6, 22))
