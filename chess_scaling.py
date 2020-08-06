import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(4, 4 / 1.5))
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.text(2000, 2400, 'PC programs', color='blue')
time, elo = np.loadtxt('data_chess_year_elo.csv', unpack=True)
ax1.scatter(time, elo, color='blue', s=5)

ax1.text(2012, 2900, 'Carlsen', color='gray')
time, elo = np.loadtxt('data_chess_player_carlsen.csv', unpack=True)
ax1.plot(time, elo, color='gray')

ax1.text(1991, 2900, 'Kasparov', color='gray')
time, elo = np.loadtxt('data_chess_player_kasparov.csv', unpack=True)
ax1.plot(time, elo, color='gray')

ax1.text(2005, 3100, 'SF8', color='red', ha='center')
time, elo = np.loadtxt('data_chess_SF8.csv', unpack=True)
ax2.plot(time, elo, color='red')

ax1.text(2005, 3400, 'LC0', color='orange', ha='center')
time, elo = np.loadtxt('data_chess_LC0.csv', unpack=True)
ax2.plot(time, elo, color='orange')

ax1.text(1997, 2900, 'Deep Blue', color='darkblue')
ax1.scatter(1997, 2850, color='darkblue')

ax1.set_xlabel(r'Year', color='blue')
ax1.set_ylabel('ELO')
ax2.set_xlabel(r'MIPS', color='red')
ax1.tick_params(axis='x', colors='blue')
ax2.tick_params(axis='x', colors='red')
ax2.set_xscale('log')
ax1.set_ylim(2000, 3600)
ax1.set_xlim(1990, 2020)
ax2.set_xlim(27, 500000)
plt.savefig('chess_scaling.pdf', bbox_inches='tight')
