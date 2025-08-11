# await

comando que de fato não faz nada, atua como uma flag de sincronismo. Em sua forma mais simples temos

> <S;> => indica que S é executado de modo exclusivo

temos também a forma que indica sincronismo simples:

> <await(B);>=> indica que o próximo comando será executado quando B for válido

temos finalmente, a combinação, dada por:

> <await(B) S;> - representa uma ação atômica condicional, ou seja, atrasa a execução até que B seja verdadeiro e então executa S.

Await pode ser implementado dentro de uma região crítica, sendo a ação atômica condicional descrita por um while loop, neste formato:

```c
\\ demilitador entrada da região critica
while (!B) {
    \\ delimitador saida da região críticaa
    delay;
    \\ demilitador entrada da região critica
}
S;
\\ delimitador saida da região crítica
```

este código evalua B dentro da região critica, tornando a execução atomica. Percebe-se que, ao sair da região critica dentro do while, outra thread pode executá-la também, mantendo a ideia de atomicidade.

---

## Aplicando o await - problemas do multiplos leitores/escritores


como await é uma abstração de uma ação condicional atômica, podemos implementá-los de diversas formas, desde que consigamos garantir a atomicidade e que a condição seja respeitada. 

```c
int nr = 0; // numero de leitores ativos
sem rw = 1; // semaforo de escritores

process Writer[j=1 to N] {
	while (true) {
		...
		P(rw);
		escreve;
		V(rw);
	}
}

process Reader [i=1 to M] {
	while (true) {
		
		<	nr = nr + 1; if (nr == 1) P(rw); > // quando há um leitor, paramos as escritas
		leitura;
		<   nr = nr - 1;  if (nr == 0) V(rw); > // quando há 0 leitores, voltamos a escrever
	}
}
```


Vamos usar 2 formas, os semáforos e os monitores, vistos anteriormente:

### semaforos 
```c
int nr = 0; // numero de leitores ativos
sem rw = 1; // semaforo de escritores
sem mutex = 1; 

process Writer[j=1 to N] {
	while (true) {
		...
		P(rw);
		escreve;
		V(rw);
	}
}

process Reader [i=1 to M] {
	while (true) {
		...
		P(mutex);
		nr = nr + 1;
		if (nr == 1) P(rw);
		V(mutex);
		
		leitura;
		
		P(mutex)
		nr = nr - 1;
		if (nr == 0) V(rw);
		V(mutex);
	}
}
```

não se pode utilizar apenas um mutex no reader (como foi feito anteriormente), pois precisa-se ter um mutex para entrada de leitores e outro para saída de leitores, pois se usasse o mesmo, caso ficasse um leitor esperando pois houve solicitação de escrita, não seria possível liberar os leitores que já estavam lendo, pois o mutex estaria com o leitor que foi bloqueado na entrada.

Como mencionado, precisamos atrasar a ação atômica condicional para permitir sincronismo.

logo, a solução é esta:

```c
int nr = 0, nw = 0, dr = 0, dw = 0;

// dr = delayed reader || dw = delayed writer

sem e = 1, r = 0, w = 0;

process Writer[j=1 to N] {
	while(true) {
		P(e);
		if (nr > 0 or nw > 0) {
			dw = dw + 1;
			V(e);
			P(e);
		}
		nw = nw + 1;
		V(e);

		escreve;

		P(e);
		nw = nw - 1;
		if (dr > 0) {
			dr = dr - 1;
			V(r);
		}
		else if (dw > 0) {
			dw = dw - 1;
			V(w);
		}
		else
			V(e);
	}
}

process Reader[i=1 to M] {
	while (true) {
		P(e);
		if (nw > 0) {
			dr = dr + 1;
			V(e);
			P(r);
		}
		nr = nr + 1;
		if (dr > 0) {
			dr = dr - 1;
			V(r);
		}
		else {
			V(e);
		}

		leitura;

		P(e);
		nr = nr - 1;
		if (nr == 0 and dw > 0) {
			dw = dw - 1;
			V(w);
		}
		else {
			V(e);
		}
	}
}
```

### Monitores
```c
monitor RW_Controller{
	int nr = 0, nw = 0;
	cond OK to read, OK to write;
	
	procedure request_read() {
			while (nw > 0)
				wait(OK to read);
			nr = nr + 1;
	}
	
	procedure release_read() {
		nr = nr - 1;
		if (nr == 0) signal(OK to write);	
	}
	
	procedure request_write() {
		while (nr > 0 || nw > 0)
			wait(OK to write);
		nw = nw + 1;	
	}

	procedure release_write() {
		nw = nw - 1;
		signal(OK to write);
		signal_all(OK to read);
	}
}
```

ainda causa starvation, no entanto, a abstração é consideravelmente mais simples.