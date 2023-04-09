import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from matplotlib.patches import Rectangle


def fun(x):
    return np.exp(2 * (x + 1))


def tau_left(i):
    return 3 * i / n


def tau_middle(i):
    return (tau_right(i) + tau_left(i)) / 2


def tau_right(i):
    return 3 * (i + 1) / n


true_sum = np.exp(2) / 2 * (np.exp(6) - 1)
print("Истина: ", true_sum)

n = int(input("N ?\n> "))
equipment = {"l": tau_left, "m": tau_middle, "r": tau_right}
e = input("l | m | r ?\n> ")
eq = equipment[e]

assert n != 0

integral_sum = 0

x = np.linspace(0, 3)
y = fun(x)

fig = plt.figure()

ax = fig.add_subplot(111)

plt.plot(x, y)

for i in tqdm(range(0, n)):
    integral_sum += 3 / n * fun(eq(i))
    rect1 = Rectangle((3 * i / n, 0), 3 / n, fun(eq(i)), color='blue', fc='none', lw=2)
    ax.add_patch(rect1)

plt.text(0, 3000, f"N: {n}")
plt.text(0, 2900, f"Оснащение: {e}")
plt.text(0, 2800, f"Интегральная сумма: {integral_sum}")
plt.show()

print(f"Сумма: {integral_sum}")
print(f"Погрешность: {abs(true_sum - integral_sum)}")
