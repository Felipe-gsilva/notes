# Barreiras do Sincronismo

hotspot: variável acessada por vários processos.

## Solução de contador compartilhado

process Worker [i = 1 to N] {
    while (true) {
        $\vdots$
        <arrive++;>
        <await (arrive == N);>
    }
}

gera problema de contenção de memória

## Solução do coordenador e flags de sinalização

```c
process Worker [i = 1 to N] {
    while (true) {
        <arrive[i] = 1;>
        <await (continue[i] == 1);>
        continue[i] = 0;
    }
}
```

```c

process Coordinator {
    while (true) {
        for (j = 1; j <= N; j++) {
            <await (arrive[j] == 1);>
                arrive[j] = 0;
        }

        for (j = 1; j <= N; j++) {
            continue[j] = 1;
        }
    }
}

```

utiliza memória a mais desnecessariamente

# Princípios de Sincronização por Flags
(i) o processo que espera por uma flag de sincronização ser setada é aquele que deve limpar a flag. (ii) a flag n deve ser sinalizada até que se saiba que está limpa.

# Solução para evitar uma criação de outro processo Coordenador
## Solução com barreira de árvore (combining tree barrier)

Cria-se uma estrutura de arvore binaria para rastrear se todos os Workers chegaram na barreira (ou seja, arrive = 1); Ele verifica se o filho a direita e o filho a esquerda tem arrive = 1 (arrive[left(i)] == 1 e arrive[right(i)] == 1);

Precisamos entao, de 3 sub-processos

no folha:
```c
arrive[L] = 1;
<await (continue[L] == 1);>
continue[L] = 0;
```

no raiz:
```c
<await (arrive[L] == 1); >
    arrive[L] = 0;
<await (arrive[R] == 1); >
    arrive[R] = 0;
continue[L] = 1; continue[R] = 1;
```

no interior

```c
// faz o que o raiz faz
<await (arrive[L] == 1); >
    arrive[L] = 0;
<await (arrive[R] == 1); >
    arrive[R] = 0;

// faz o que o folha faz
arrive[I] = 1;
<await (continue[I] == 1);>

// faz o que o raiz faz
continue[I] = 0;
continue[L] = 1; continue[R] = 1;
```

## Symmetric Barriers
Uma barreira simetrica é construida de pares de simples barreiras de 2 processos:

- barreira borboleta; e 
- barreira por disseminação

cada processo avisa outro processo de que chegou na barreira de sincronismo. Eh dividido em estagios. 

No estagio 1, pares adjascentes conversam entre si. (0, 1) (2, 3) (4, 5) (6, 7)

No estagio 2, pares de distancia k + 1 conversam entre si. (0, 2) (1, 3) (4, 6) (5, 7)

No estagio 3, pares de distancia k + 1 conversam entre si. (0, 4) (1, 5) (2, 6) (3, 7)

Tem $log_{2} n$

O trabalho $i$ no estagio $n$ conversa com o trabalhador distante por $2^{s-1} + e -$, utilizando codigo de gray para o flip do i-esimo bit

```c 
for (s=1 to num_estagios) {
    arrive[i] = arrive[i] + 1;
     // determina viznho no estagio (j) ou por
     // j = flip(s) de gray (borboleta) ou por
     // j = i + (2 ^ s) % N (disseminação)
     while(arrive[j] < arrive[i])
        skip;
}

```

solução
```c

for (s=1 to num_estagios) {
    j = para_quem_envia(i, s);
    V(sem[i][s]);
    P(sem[j][s])
}
```
