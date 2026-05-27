import cmath  # Für komplexe Zahlen
import math   # Für reelle Zahlen

def solve_quadratic(a, b, c):
    """Löst die quadratische Gleichung ax² + bx + c = 0.
    Gibt reelle oder komplexe Lösungen zurück."""
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
    print(f"Lösungen: x1 = {solutions[0]}, x2 = {solutions[1]}")
