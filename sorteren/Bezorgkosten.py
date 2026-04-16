
# David Biratu, 1922540
def basis_bezorgkosten(afstandKM):
    if afstandKM <= 10:
        return 4.50
    elif afstandKM <= 30:
        return 4.50 + 0.25 * (afstandKM - 10)
    else:
        return -1


def definitieve_bezorgkosten(klanttype, spoed, afstandKM):
    if basis_bezorgkosten(afstandKM) == -1:
        return -1
    else:
        if klanttype == "premium":
            return 0.8 * basis_bezorgkosten(afstandKM)
        elif klanttype == "zakelijk":
            return 0.9 * basis_bezorgkosten(afstandKM)
        else:
            return basis_bezorgkosten(afstandKM) + 3 if spoed else basis_bezorgkosten(afstandKM)

def test_bezorg_functies():
    test_n = [10, 11, 30, 31]
    test_s = ["normaal", "premium", "zakelijk"]
    for n in test_n:
        for s in test_s:
            print(f"afstand: {n} km, basis_bezorgkosten: €{basis_bezorgkosten(n)}, definitieve_bezorgkosten: €{definitieve_bezorgkosten(s, False, n)}, {s}\n")

test_bezorg_functies()
