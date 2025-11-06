# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 14:49:23 2025

@author: Ashwin
"""

import numpy as np
import matplotlib.pyplot as plt

wt = np.linspace(-3 * np.pi, 3 * np.pi, 500)

sawtooth_wave = np.mod(wt + np.pi, 2 * np.pi) - np.pi

plt.plot(wt, sawtooth_wave, label='Sawtooth Wave')
plt.title('Sawtooth Wave')
plt.xlabel('$\omega t$')
plt.ylabel('$f(\omega t)$')


f_wt = 2 * np.sin(wt)

plt.plot(wt, f_wt, label='Fundamental', color='red', linestyle='--')

f_wt = np.zeros_like(wt)
for n in range(1, 4):
    f_wt += 2 * ((-1)**(n+1) / n) * np.sin(n * wt)
    
plt.plot(wt, f_wt, label='Sum of first 3 harmonics', color='green', linestyle=':')

f_wt = np.zeros_like(wt)
for n in range(1, 11):
    f_wt += 2 * ((-1)**(n+1) / n) * np.sin(n * wt)
    
plt.plot(wt, f_wt, label='Sum of first 10 harmonics', color='purple', linestyle='-.')
plt.legend()

n_values = np.arange(1, 11)
magnitudes = np.abs(2 * ((-1)**(n_values + 1)) / n_values)
phases = np.where((n_values % 2) != 0, 0, np.pi)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.stem(n_values, magnitudes, basefmt=" ")
plt.title('Magnitude of First 10 Harmonics (Log-Log)')
plt.xlabel('n')
plt.ylabel('|A_n|')
plt.xscale('log')
plt.yscale('log')

plt.subplot(2, 1, 2)
plt.stem(n_values, phases, basefmt=" ")
plt.title('Phase of First 10 Harmonics (Semilog-x)')
plt.xlabel('n')
plt.ylabel('Phase (radians)')
plt.xscale('log')