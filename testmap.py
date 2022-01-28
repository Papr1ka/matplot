from random import randint
from matplotlib import pyplot as plt
from os import path

p = path.abspath("D://documents//python//plot//style.mplstyle")


plt.style.use(p)
figure = plt.figure(1, (5, 5), 200)
ax = figure.add_subplot(1, 1, 1)

time = [i for i in range(1, 25)]
commands = [randint(0, 100) for i in range(1, 25)]

ax.plot(time, commands, color='gray', linestyle="--", label="Команды в час")
ax.set_title("commands per hour", fontsize=20)
ax.legend(loc='lower left')
ax.set_xlabel("Время")
ax.set_ylabel("Команды")
ax.set_xticks(range(0, 25, 1))
ax.set_yticks(range(0, 101, 5))
ax.grid(color='red', linestyle='-', alpha=0.3)

plt.show()