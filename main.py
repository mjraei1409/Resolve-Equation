import sympy as sp

def Equation(*Equations:list, **Responses:list):
    num = len(Equations)
    A = sp.eye(num)
    B = sp.zeros(num,1)

    for eq in Equations:
        for zrb in eq:
            b = zrb
            A[Equations.index(eq), eq.index(zrb)] = b
    
    for re in Responses['res']:
        B[Responses['res'].index(re)] += re

    result_no_clean = (A**-1)*B

    result_clean = []

    nn = 0
    for i in result_no_clean:
        result_clean.append(i)
        nn += 1

    return result_clean

print(Equation([1,-1], [3,1], res=[-1,9]))