# Numero Inteiro binário -> decimal
$x = (d_{k}d_{k-1}...d_{1}d_{0})_{2}$, $d_{k} \in [0,1]$
$A_{k} = d_{k}$
$A_{i} = 2 \times A_{i+1} + d_{i}$ para $i = k-1, ..., 0$
$A_{0}$: número $x$ na base 10

# Decimal -> Binário
$k = 0$
Enquanto $N_{k} \neq 0$
	$N_{K+1}$ = $\lfloor\frac{N_{k}}{2}\rfloor$
$a_{k} = N_{k} - 2 \times N_{k+1}$

# Mantissa Binário -> decimal
$A_{n+1}= 0$
Para $k = n, n-1, ..., 2, 1$:
$A_{k} = \frac{(b_{k}+A_{k+1})}{2}$

# Mantissa Decimal -> Binário
Seja $R_{0}$ um número fracionário positivo na base decimal, e seja $(0.d_{1}d_{2}...)_{2}$ sua representação na base 2. Então:
1. Para j = 1, 2 ,3, ... :
	1. $r_{j} = 2 \times R_{J-1}$
	2. $d_{j} = \lfloor r_{j} \rfloor$ 
	3. $R_{j} = r_{j}-d_{j}$
Esse processo termina quando:
1. $j$ atingir o número de dígitos binários desejados
2. $R_{j} = 0$

# Erro e Aproximações

## truncamento
_absoluto_
$|EAx| = |f_x .10^q+g_x .10^{q-t}-f_x.10^q|$﻿
==$|EAx| < 10^{q-t}$==﻿

_relativo_
$|ERx| = |\frac{EAx}{x}| = \frac{|EAx|}{|x|}$﻿
$|ER_x| < \frac{10^{-t}}{0.1} <{10^{1-t}}$

## arredondamento
_absoluto_
$x = \lbrace\binom{f_x.10^q, se |g_x| <0.5}{f_x.10^q+10^{q-t}, se |g_x| \geq0.5}$﻿
$|EAx| < \frac{1}{2} \times 10^{q-t}$﻿

_relativo_
$|ERx| = \frac{|EAx|}{|x|}<\frac{0.5*10^{q-t}}{f_x*10^q+10^{q-t}}$﻿
==$|ERx| < 0.5*10^{1-t}$==﻿

