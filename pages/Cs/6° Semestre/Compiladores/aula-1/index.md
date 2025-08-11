# Introdução
Compilador: programa que recebe entradas de texto em uma determinada linguagem fonte e a "traduz" sem percas para uma outra determinada linguagem, atraves do seguinte fluxo de dados: (i) analise; e (ii) sintese.

1. Analise: subdividida em:
    - analisador lexico: responsável por tokenizar (ler e agrupar) o input de texto recebido pelo compilador (arquivo(s)).
    - analisador sintatico: responsavel por fazer uma analise hierarquica dos tokens, agrupando-os em colecoes com significados coletivos.
    - analisador semantico: assegura que os componentes agrupados tem algum sentido (como int = 5 e nao int = 2.0)

2. Sintese:
    - gerador de código intermediario (opcional): tem como objetivo quebrar o codigo fonte em instrucoes mais simples e, consequentemente, mais proximas do codigo alvo.
    - otimizador de códigos: tenta melhorar o codigo (se houver, intermediario) de forma a obter um codigo alvo menos custoso em execucao.
    - gerador de códigos: fase final de geração de código o qual culmina na criação de um "executável".

3. subetapas (acontecem em paralelo às demais):
    - tratador de erros
    - gerenciador da tabela de simbolos

--- 
## Extra
O livro [compiladores](https://github.com/Felipe-gsilva/cs-common-private-files/blob/main/Books/Compiladores_%20Princ%C3%ADpios%2C%20T%C3%A9cnicas%20e%20Ferramentas%20--%20ALFRED%20V_%20AHO%2C%20Ravi%20Sethi%2C%20monica%20S_%20Lam.pdf) mostra outra estrutura um pouco mais robusta (com uma tabela de simbolos externa):

string -> **analisador lexico** -> fluxo de tokens -> **analisador sintatico** -> arvore de sintaxe -> **analisador semantico** ->  arvore de sintaxe -> **gerador de codigo intermediario** -> representacao intermediaria -> **gerador de codigo dependente da maquina** -> representacao intermediaria -> **gerador de codigo** -> codigo da maquina alvo -> **otimizador independente de maquina** -> codigo final 

## Analisador Lexico

todo lexema (valido) escaneado pelo analisador lexico tem uma entrada na tabela de simbolos dada por <id, 1> onde id é um simbolo abstrato e 1 é a posição na tabela. Se for um operador a entrada se dá por <*>, descartando os espaços.

i.e:
a = b + c * 60
$\vdots$
<id, 1> <=> <id, 2> <+> <id, 3> <*> <60>

## Analisador sintatico
Utiliza uma forma intermediaria de representacao tipo arvore, atraves dos tokens recebidos pela analise lexica, demonstrando a estrutura gramatical da sequencia de tokens. Uma representacao tipica é uma árvore sintática em que cada nó é um operador e os filhos representam seus operandos.

## Analisador semantico
Também utiliza a mesma representacao de árvore mas ajusta alguns "problemas" (ou ao menos os detecta). Por exemplo, uma multiplicação de int's não pode ter um operando do tipo float, então será chamado a função floattoint() para corrigir o problema. Em outras palavras, o analisador semantico utiliza da árvore sintática e das entradas da tabela de simbolos para verificar a consistencia semântica do programa com a definição da linguagem.

Certas técnicas são empregadas, como a supracitada verificação de tipos. Esses ajustes de tipo são chamados de **coerções** de acordo com o tipo preferido.

## Geração de código intermediario, otimização e geração de codigo
Não vou me estender, é bem direto o que eu já escrevi antes. Será visto melhor no capitulo 6.