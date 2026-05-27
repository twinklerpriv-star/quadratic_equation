import cmath  # Für komplexe Zahlen
import math   # Für reelle Zahlen

def solve_quadratic(a, b, c):
    """Löst die quadratische Gleichung ax² + bx + c = 0.
    Fängt lineare Fälle (a = 0) ab. Gibt reelle oder komplexe Lösungen zurück."""
    if a == 0:
        if b != 0:
            # Lineare Gleichung: bx + c = 0 -> x = -c/b
            return (-c / b,)
        else:
            if c == 0:
                # 0 = 0: Unendlich viele Lösungen
                return "Unendlich viele Lösungen"
            else:
                # c = 0 (mit c != 0): Keine Lösung
                return "Keine Lösung"

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant >= 0:  # Reelle Lösungen
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    else:  # Komplexe Lösungen
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

if __name__ == "__main__":
    print("Quadratische Gleichung lösen: ax² + bx + c = 0")
    a = float(input("Gib a ein: "))
    b = float(input("Gib b ein: "))
    c = float(input("Gib c ein: "))

    solutions = solve_quadratic(a, b, c)
    
    if isinstance(solutions, str):
        print(f"Ergebnis: {solutions}")
    elif len(solutions) == 1:
        print(f"Lineare Gleichung, eine Lösung: x = {solutions[0]}")
    else:
        print(f"Lösungen: x1 = {solutions[0]}, x2 = {solutions[1]}")
