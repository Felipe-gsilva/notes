Esses proximos documentos representam meus estudos acerca do Livro - Operational Systems  Three Easy Pieces, de dominio publico.

## 1.1 Introducao aos processos
Um processo, de maneira geral, representa um programa em execucao e seus componentes. O programa armazenado em si, nao representa nada alem de instrucoes e algum tipo de dado estatico, ele so passa a ter algum valor de fato quando eh executado pelo SO.
Neste contexto, cria-se uma problematica. Se um programa so pode ser validado ao ser executado, como podemos executar varios programas em apenas uma maquina fisica, a qual tem apenas uma unidade de processamento?

> podemos utilizar da __virtualizacao__ da CPU. A tecnica para executar varios programas eh conhecida como __Compartilhamento de tempo__ da CPU. Esta tecnica permite executarmos processos de forma concorrente, com apenas uma pequena perda de performance, ja que a CPU estara sendo compartilhada.

Utilizamos _Mecanismos_, que sao metodos e protocolos __low level__ que implementam funcionalidades do sistema. Um exemplo de mecanismo: Context Switcher, que permite a pausa e intercalacao da execucao de programas.

## 1.2 Abstraindo processos

Um processo, evidentemente, eh apenas uma abstracao dada a um programa, o qual acessa e/ou modifica partes do sistema. Para entendermos um processo, precisamos entender primeiramente o que sao os  __Estados de Maquina__: todos os componentes o qual o programa consegue alterar. A exemplo, o estado da memoria. As instrucoes de um programa se compreendem dentro da memoria, assim como todo dado armazenado. Desta forma, o __espaco de endereco__ faz parte da construcao de um _processo_, juntamente aos registrados que participam das operacoes (por exemplo o *program counter* ou o *stack pointer*).

## 1.3 Process API

Uma API de processo deve poder:
- criar: invocado ao se executar qualquer programa
- destruir: matar o processo (_kill_)
- esperar: apenas permitir a execucao do processo e sua finalizacao.
- controle variado: suspensao e resumo do processo, i.e.
- status: devolver info sobre o estado do processo.

## 1.4 Criacao de um processo

.. on going


## Bibliografia 

https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf 
