'''
Módulo que calcula el factorial
'''

def factorial(n):
    '''
    Función que calcula el factorial de un número.

    Parameters
    ----------
    x : Int
        Número para generar su factorial. 

    Returns
    -------
    Factorial de x.
    '''
    f = 1
    # range hasta n+1 para que considere el propio número 
    for i in range(1, n+1):
        f = f * i

    return f