- A entrada na "fita" do scanner (AFD) é feita por um programa anterior (leitor de arquivo) que usa de separadores da linguagem de programação.
	- O scanner (analisador léxico) então verifica se o token enviado é válido.
- O analisar léxico analisa somente se os tokens são BEM FORMADOS.
# Exemplo de erros léxicos
- Uso de caracteres fora do alfabeto da linguagem;
- Erros de grafia.

# Token: padrões e lexemas
- Dada LP possui um conjunto de tokens que definem as sequências de caracteres válidos para a linguagem.
- Cada sequência de caractere em um programa fonte tem significado próprio na LP.
- Por exemplo, a sequência "if" pode significar um identificador ou o nome de uma estrutura de controle (dependendo da linguagem).
- Um **token** é uma classe de sequência de caracteres, que juntos têm um significado específico em uma linguagem fonte.
- Sequências diferentes podem estar associadas ao mesmo token. Ex: 10 e 234
- A sequência de caracteres que forma um token é chamada **lexema**
	- Ex: pi = 3,1416; 
	- pi é um lexema pra o token identificador.
- O padrão de um token é a regra de formação (ex: nome de variável em c).
	- Ex: token CONSTANTE_INTEIRA tem o padrão sequência de um ou mais dígitos

# Maneira de implementar um Analisador Léxico
1) Construir um simulador de um AF.
2) Implementar as transições de estado no código (chumbado).
3) Usar um gerador de analisador léxico.
