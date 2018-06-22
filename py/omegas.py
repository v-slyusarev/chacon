import legendre
import random

def omega_0(x, p):
    if x >= 0 and x < p - 1:
        return x
    else:
        return 0
# all symmetric


def square_omega_1(x, p):
    assert x < p
    return x * (p - x - 1) if 0 <= x < p - 1 else 0
# symmetric only for p=3


def square_omega_2(x, p):
    assert x < p
    return x * (p - x) if 0 <= x < p - 1 else 0
# symmetric only for p=3


def square_omega_3(x, p):
    assert x < p
    return x**2 if 0 <= x < p - 1 else 0
# symmetric only for p=3


def linear_omega_1(x, p):
    return 41 * omega_0(x, p)
# all symmetric


def linear_omega_2(x, p):
    return omega_0(x, p) + 41
# all symmetric


def step_omega(x, p):
    if p % 2 == 1:
        return 0 if x < (p - 1) / 2 else 1
    if p % 2 == 0:
        if x < p / 2 - 1:
            return 0
        else:
            if x == p / 2 - 1:
                return 1
            else:
                return 2
# all symmetric


def legendre_omega(x, p):
    return legendre.calculateLegendre(x + 1, p) + 1
# symmetric unless p is pythagorean prime
# for pythagorean primes symmetric unless m=3


#def generate_correct_omega(p, list):
#    return lambda x: (list[x] if x < (p - 1) // 2 else 1 - list[p-2-x])

def generate_binary_omega(p):
    list = [random.randint(0,1) for j in range((p-1)//2 + (p-1)%2)]
    return lambda x, p: (list[x] if x < (p - 1) // 2 else 1 - list[p-2-x])

def generate_basic_omega(p):
    values = random.shuffle([i for i in range((p-1)//2 + (p-1)%2)])
    return lambda x, p: (list[x] if x < (p - 1) // 2 else p-2 - list[p-2-x])

def generate_omega_for_th2(p):
    zeta = random.randint(1,p-2)
    list = [random.randint(0, zeta) for j in range((p - 1) // 2 + (p - 1) % 2)]
    return lambda x, p: (list[x] if x < (p - 1) // 2 else  zeta - list[p-2-x])

def generate_omega_for_l4(p):
    omega = generate_omega_for_th2(p)
    a = random.randint(1, 1000)
    b = random.randint(0, 1000)
    return lambda x, p: a * omega(x, p) + b

def generate_bad_omega(p):
    omega = generate_omega_for_th2(p)
    print("I used to be ",[omega(x, p) for x in range(p - 1)])
    return lambda x, p: omega(x, p) if x!= 0 else 800

def generate_good_and_bad_omega(p):
    omega = generate_omega_for_th2(p)
    print("I used to be ",[omega(x, p) for x in range(p - 1)])
    return (omega, lambda x, p: omega(x, p) if x!= 0 else 800)