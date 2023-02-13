from decimal import Decimal as d
from math import atan


def main(x, z, y):
    term_1 = d(
        d(22) * d(
            d(1) +
            d(55) * d(y) +
            d(d(pow(d(x), d(2))) / d(15)))
        ** (d(7)))

    term_2 = d(d(pow(d(x), d(2))) +
               pow(d(z), d(3))).sqrt() / d(70)
    term_3 = d(d(z)).log10()
    term_4 = d(pow(d(atan(d(90) * d(pow(d(y), d(2))) -
                          d(pow(d(x), d(3))) - d(4))), d(3)))

    return float('%.2e' % + (d(term_1) - d(term_2) + d(term_3) + d(term_4)))


if __name__ == '__main__':
    print(main(0.81, 0.72, -0.08) == -1.06e+05)
    print(main(0.65, 0.74, 0.4) == 7.56e+10)
    print(main(-0.09, 0.99, -0.02) == -2.34e+00)
    print(main(0.57, 0.87, -0.48) == -1.49e+11)
    print(main(-0.46, 0.93, -0.51) == -2.32e+11)
