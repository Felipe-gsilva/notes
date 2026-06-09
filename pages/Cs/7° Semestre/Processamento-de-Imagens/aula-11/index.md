# Fourier

Séries de Fourier: 
- qualquer função periódica pode ser expressa como a soma de senos e cossenos.
- qualquer função não periódica é a integral de senos e cossenos multiplicada por uma função de ponderação.

Revisão matemática ensino médio: 
- periódo é inversamente proporcional à frequência
- Período: $f(t) = f(t + T_0)$, sendo $T_0$ o periodo e $t$ o tempo
- Frequência Angular/Fundamental: $\omega_0 \frac{2\pi}{T}$, dado em rad/s.
- $2\pi$ = ciclo completo

frequência fundamental: ideia de quantos radianos são percorridos por unidade de tempo 
- É a onda mais longa 
- Tem a menor frequência

Podemos modelar essa série (infinitos harmônicos) com $n$ harmônicos = $n\omega_0$

## Definição 

Dado uma função periódica $f(t)$ de frequência $\omega_0$ pode ser representado por:

$$
\tilde f(t) = a_0 + \sum\limits_{n=1}^{\inf}a_n cos(n\omega_0t) + b_n sin(n\omega_0t)
$$

para $n = 1$, temos a frequência fundamental.


Fator exponencial complexo: $e_{iθ}, e_{-i\tetha}, e_{j\theta} ou e_{-j\theta}$ 


Transformada de Fourier 1D:
$F(\omega) = \int f(t).e^{j\omega t} dt$

Transformada inversa 1D: 
$F(\omega) = \frac{1}{2\pi} \int f(t).e^{j\omega t} dt$

Transformada Discreta 1D:


