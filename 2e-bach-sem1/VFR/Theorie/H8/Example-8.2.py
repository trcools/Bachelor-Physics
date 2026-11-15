import numpy as np
import matplotlib.pyplot as plt

# Definieer een kleine enumeratie van rationale getallen in [0, 1] voor q_1, q_2, q_3
q_n = [0.5, 0.25, 0.75]


def compute_fN(x, N):
    # Initialiseer nulvector
    y = np.zeros_like(x)

    for n in range(1, N + 1):
        q = q_n[n - 1]

        # Bereken |x - q_n|^{-1/2} en voorkom runtime errors door singulariteiten op x=q
        with np.errstate(divide="ignore"):
            term = np.abs(x - q) ** (-0.5)

        # Limiteer de amplitude op N via min(|x - q_n|^{-1/2}, N)
        term = np.minimum(term, N)

        # Tel term op vermenigvuldigd met de convergentiefactor 2^{-n}
        y += (2**-n) * term

    return y


# Discretiseer het domein [0, 1] met hoge resolutie om de asymptoten te vangen
x = np.linspace(0, 1, 10000)

plt.figure(figsize=(9, 5))

# Bereken en plot opeenvolgende iteraties van de sequence
for N in [1, 2, 3]:
    plt.plot(x, compute_fN(x, N), label=f"N={N}", alpha=0.8)

plt.title(r"Constructie van de Cauchy sequence $f_N(x)$")
plt.xlabel("$x$")
plt.ylabel(r"$f_N(x)$")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()


# =======================================================================================
# Genereer een Farey-achtige sequence van rationale getallen in [0, 1]
# Deze enumeratie simuleert de dichtheid van Q in R voor de eerste N_max termen
# =======================================================================================
def generate_q_sequence(N_max):
    q_list = [0.0, 1.0]
    denominator = 2
    while len(q_list) < N_max:
        for numerator in range(1, denominator):
            q = numerator / denominator
            if q not in q_list:
                q_list.append(q)
                if len(q_list) == N_max:
                    break
        denominator += 1
    return np.array(q_list)


# Parameters voor de benadering met hoge resolutie om aliasing te minimaliseren
N_max = 30
q_n = generate_q_sequence(N_max)
x = np.linspace(0, 1, 100000)
y = np.zeros_like(x)

# Sommatie van de reeks tot N_max om de pointwise limit f(x) te benaderen
for n in range(1, N_max + 1):
    q = q_n[n - 1]

    # Bereken pool en negeer DivideByZero waarschuwingen op x = q
    with np.errstate(divide="ignore"):
        term = np.abs(x - q) ** (-0.5)

    # We verwijderen de limiet min(..., N) uit f_N(x) om direct f(x) te simuleren
    y += (2**-n) * term

# Plot de fractaal-achtige structuur
plt.figure(figsize=(12, 6))
plt.plot(x, y, color="red", linewidth=0.3)
plt.title(
    rf"Numerieke benadering van $f(x)$ met $N_{{max}}={N_max}$ rationale asymptoten"
)
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
# Beperk de y-as om de basisstructuur zichtbaar te houden in plaats van enkel uitschieters
plt.ylim(0, 15)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
