class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(c):
        if not ConversorTemperatura.__validar(c):
            raise ValueError("O valor deve ser numérico.")
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_para_celsius(f):
        if not ConversorTemperatura.__validar(f):
            raise ValueError("O valor deve ser numérico.")
        return (f - 32) * 5/9

    @staticmethod
    def __validar(valor):
        return isinstance(valor, (int, float))