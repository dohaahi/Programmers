import fractions

def solution(a, b):
    denominator = fractions.Fraction(a, b).denominator

    while denominator % 2 == 0:
        denominator = denominator // 2
    while denominator % 5 == 0:
        denominator = denominator // 5

    return 1 if denominator == 1 else 2