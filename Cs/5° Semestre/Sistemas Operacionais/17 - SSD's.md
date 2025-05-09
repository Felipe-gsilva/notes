Discos padrão são em torno de 100.000x mais lentos que o desempenho acumulado entre cache e CPU. Portanto usar um SSD hoje é quase indispensável.

## Operações em memória flash
Leitura, escrita (programação da página), apagamento de bloco.

Quando é necessária uma escrita de página, todos os bits de uma página em um SSD tem que ser igual a 1. Ou seja, toda escrita gera um *overhead* de sobrescrita, onde colocamos todos os bits pra 1 e a partir dai ocorre a escrita. Esta operação também não pode ser paginada, tem que ser feita de forma blocada, ou seja, x blocos.

A organização dos circuitos de uma memória flash pode ser feita de 3 formas diferentes.
- Single Level Cell: considerar cada bit como um elemento do circuito, com threshold de x volts para valor 0 e y volts para valor 1.
- Multi level cell: 2 bits armazenado em um transistor apenas. O threshold muda, divididos em 4 faixas. (aumenta a densidade, mas gera lentidão)
- Triple level cell: 3 bits armazenados (000-111). (ainda mais denso, mais lento).

O apagamento por blocos gera um desgaste físico no SSD's, o que limita a quantidade de escritas possíveis por SSD.

# Gerenciamento
Devemos evitar o mapeamento direto, já que ele colocará mais desgaste físico. Usaremos uma técnica chamada de `Mapeamento Logaritmico`. Tenta-se usar qualquer bloco com menos páginas escritas, assim, evita-se sobrescrita desnecessária. No entanto, escrever em outro bloco faz necessário criar um *garbage collector* nas páginas não mais usadas e ainda escritas.

|                       | Aleatório |     | Sequencial |     |
| --------------------- | --------- | --- | ---------- | --- |
|                       | R         | W   | R          | W   |
| Samsung 840 Pro       | 103       | 287 | 421        | 384 |
| Seagate 600           | 84        | 252 | 424        | 374 |
| Intel SSD 335         | 39        | 222 | 344        | 354 |
| Seagate Savvia 15Krpm | 2         | 2   | 223        | 223 |
Tudo em MB/s.

A leitura é mais lenta aleatoriamente pois não sabe-se exatamente onde estão as páginas contíguas, é necessário chavear até achar o que se busca.
Na escrita, apenas escreve em um bloco apenas, todas as páginas solicitadas (se couber).

Como o acesso é aleatório, não se tem custo ao buscar qualquer endereço inicial, apenas alterar o registrador de endereço. Ou seja, apenas usa-se FIFO para todas as requisições.
