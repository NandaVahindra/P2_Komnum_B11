import numpy as np
from scipy import integrate 

#Masukkan Fungsi Integrasi
def f(x):
    return x**2
    
interg = lambda x: f(x)

# Fungsi untuk menghitung integrasi dengan Metode Trapezoidal
def trapezoidal(x, y, n):
    h = (y - x) / n
    s = 0.5 * (f(x) + f(y))
    for i in range(1, n):
        s += f(x + i*h)
    return h * s

# Menghitung nilai integral dengan metode Trapezoidal dan Integrasi Romberg
x = 0
y = 1
n = 4
trapezoidal = trapezoidal(x, y, n)
romberg = integrate.romberg(interg, x, y, show = True) 
print("Hasil perhitungan dengan metode Trapezoidal:", trapezoidal)
print("Hasil perhitungan dengan metode Integrasi Romberg:", romberg)

# Error Relative
result = 0.3333333333333333  
print("Trapezoidal Er :", abs(result - trapezoidal) / abs(result))
print("Romberg Er :", abs(result - romberg) / abs(result))  