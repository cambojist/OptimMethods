
В модулі реалізовано алгоритми знаходження мінімуму функції, 
які знаходять мінімум, значення функції в точкі мінімуму та кількість ітерацій.

Необхідно:
 - Python 3
 - numpy
 - Annaconda (для тестів)

Модуль містить в собі такі функції:
 Блок 1. Чисельні методи одновимірної мінімізації:
  Методи нульового порядку (прямі):  
   1. Метод дихотомії (dyhotomy)
   2. Метод золотого перерізу (gold)
   3. Метод квадратичної апроксимації (approximation)
  Методи першого:
   1. Метод середньої точки (min_midlle_point)
   2. Метод хорд (horde)
  Метод другого порядку:
   1. Метод Ньютона (newton)
 Блок 2. Стохастичні методи оптимізації
   1. Метод імітації відпалу (annealing)
   2. Метод рою частинок (pso)
   3. Метод кажанів


Як користуватися алгоритмами:
Блок 1. Чисельні методи одновимірної мінімізації пакет one_dim_minimize:
 Методи нульового порядку (прямі): 
  Метод dyhotomy(func, bounds, tol_x=1e-4, d=1e-5) отримує такі аргументи:
   - func - функція
   - bounds - межі функції
   - tol_x - точність обрахування
   - d - додатне число менше за eps

  Метод gold(func, bounds, tol_x=1e-4) отримує такі аргументи:
   - func - функція
   - bounds - межі функції
   - tol_x - точність обрахування

  Метод dyhotomy(func, bounds, h = 0.01, tol_x=1e-4) отримує такі аргументи:
   - func - функція
   - bounds - межі функції
   - h - крок (h > 0)
   - tol_x - точність обрахування

 Методи першого порядку (прямі): 
  Метод min_midlle_point(func, dfunc, bounds, tol_x=1e-4) отримує такі аргументи:
   - func - функція
   - dfunc - перша похідна від функції func
   - bounds - межі функції
   - tol_x - точність обрахування

  Метод horde(func, dfunc, bounds, tol_x=1e-4) отримує такі аргументи:
   - func - функція
   - dfunc - перша похідна від функції func
   - bounds - межі функції
   - tol_x - точність обрахування

 Метод другого порядку:
  Метод newton(func, dfunc, d2func, bounds, tol_x = 1e-4) отримує такі аргументи:
   - func - функція
   - dfunc - перша похідна від функції func
   - d2func - друга похідна від функції func
   - bounds - межі функції
   - tol_x - точність обрахування 

Блок 2. Стохастичні методи оптимізації пакет neuro_minimize:
  Метод annealing(func, x0) отримує такі аргументи:
   - func - функція
   - x0 - початкова точка

  Метод annealing(func, x0) отримує такі аргументи:
   - func - функція
   - d - розмірність
   - s - кількість стартових елементів рою

  Метод bat(func, d, s, maxIter=100) отримує такі аргументи:
   - func - функція
   - d - розмірність
   - s - кількість стартових елементів рою
   - maxIter - максимальна кількість ітерацій
 
