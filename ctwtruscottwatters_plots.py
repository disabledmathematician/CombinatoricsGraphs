# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plot2d(f1, f2, f3, f4):
    x1, x2, x3, x4 = [], [], [], []
    y1, y2, y3, y4 = [], [], [], []
    for x in range(-20, 21, 1):
        x1.append(x)
        x2.append(x)
        x3.append(x)
        x4.append(x)
        y1.append(f1(x))
        y2.append(f2(x))
        y3.append(f3(x))
        y4.append(f4(x))
    plt.figure(0, dpi=700, figsize=[10, 7])
    plt.title("I love you Dad Mark William Watters. Sons Tai and Charles")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x1, y1, color='gold', label='$2^x$')
    plt.plot(x2, y2, color='green', label='$x^2$')
    plt.plot(x3, y3, color='crimson', label='$x^3$')
    plt.plot(x4, y4, color='pink', label='$x + 0.1955$')
    plt.legend()
    plt.xlim(-15, 15)
    plt.ylim(-1000, 1000)
    plt.savefig('2.png')
    
def plot3d():
    pass
plot2d(lambda x: 2 ** x, lambda x: x ** 2, lambda x: x ** 3, lambda x: x + 0.1955)


    
    
