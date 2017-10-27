def division_without_oprator(nu, de):
    """
    this method is uded to do division of two number without using division oprator
    """
    temp = 1
    quotient = 0
    while de <= nu:
        de <<= 1
        temp <<= 1

    while temp > 1:
        de >>= 1
        temp >>= 1
        if nu >= de:
            nu -= de
            quotient += temp
    return quotient


print division_without_oprator(24, 4)