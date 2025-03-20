# **PARADIGMAS E PILARES DE POO**

Paradigma = modelo/padrao de prog

**abstração**

abstrair problemas reais em um high level absurdo  
definir também os métodos e atributos sem os implementar.  

**objetos**

objetos herdam atributos e métodos das classes as quais pertencem  
--> é uma entidade que guarda informações sobre elementos abstraidos e suas interações com métodos  

classes --> `objetos` --> atributos  
--> métodos  

instanciação --> criação de um objeto baseado em uma classe

## **atributos**

atributos

## **métodos**

funções que podem alterar valores dos atributos, entre outras funcionalidades

## **classe**

Descreve um conjunto de objetos semelhantes em uma abstração e não precisa existir na runtime  
objeto existe na memória durante a execução do programa  

# **Instância**

Um objeto criado a partir de uma classe existente

## **encapsulamento**

o objeto não deve depender das implementações dos códigos, apenas das interfaces  
Ou seja, esconde informaçoes da impl.  

Proteger os métodos é encapsular:  
tipos:  
-public --> qualquer outro objeto pode acessar ele diretamente.  

- private --> pode apenas ser acessado por métodos da mesma classe.
- protected --> só podem ser acessados por objetos de mesma hierarquia ou pacote (herança)

## **getter/setter**

métodos publicos criados para acessar atributos de uma classe

**assinatura**

declarar a função numa interface segregando sua implementação de sua interface.

**herança**

sub-classes  
são criadas contendo métodos e atributos de uma super-classe, evitando  
reescrita de código ou overlap de informações.  

**mensagens**

objetos se comunicam através de requisições (request) e respostas (response)  
seletor e parametros  

**interface**

"end points", ou seja, define os métodos que podem ser acessados, mantendo apenas a assinatura.  
protocolos.  
API 👍  

**polimorfismo**

herança permite que propriedades particulares da subclasse podem ser alterados  
um método pode agir diferentemente em cada objeto, mesmo com assinatura idêntica.  
criar implementações diferentes mesmo com métodos herdados e já implementados em uma hierarquia maior.  

  

# Conceitos e fundamentos de Java

Códigos ão criados em arquivos .java e compilados para bytecode em .class.  
Os arquivos .class são direcionados para a JVM (Java Virtual Machine)  

## portabilidade

a jvm é multiplataforma

## java como plataforma

Java tem 2 componentes, a JVM e Java Application Programming Interface (API)  
A API é agrupada em pacotes.  

# JAVA

## Variáveis e tipos primitivos

## Variáveis de classe

- static, garante que todas as instâncias tenham o mesmo valor de variável.  
    -final, garante que o valor não seja alterado (const em c ou let [sem mut] em rust).  
    

### variáveis locais

existe dentro de um método especifico  
-não precisa de modificador, é assim por padrão  

### main

public static void main(String[] args)  
{  
}  

## padrões para as variáveis

nomes:  
-começar com letra  
-evitar $  
-sem abreviações  
-CAMEL CASE  
-no caso de constantes, snake case com caixa alta  

## TIPOS PRIMITIVOS

byte: 8 bits  
short: 16 bits  
int: 32 bits  
long: 64 bits  
float: 32 bits  
double:64 bits  
boolean: 1 bit  
char: 16 bits  

### objeto String[]

é imutável, com métodos pré-definidos que retornam outras strings  
String[] por default recene null;  

### obs

float deve terminar com f. (ex: 12351f)

## arrays

int[] anArrayOfints;

ou

```Plain
arrayOfInts = new int[10]
```

ou

arrayOfInts[0] = 100;

### n dimensões

int[][][][][][][]..n[]  
cada linha ou coluna pode ter tamanhos diferentes, pois as arrays são tratadas como arrays de arrays  

exemplo  
int[][] matrix = {{1,2,4},{3},{5.9}}  
matrix[j].length; // retorna o tamanho da linha  

### prefixo x pósfixo

a = i++; primeiro atribui depois incrementa a i;

## instanceof

retorna se um objeto é uma instancia de uma classe;  
ex:  
Parent obj1 = new Parent();  
Parent obj2 = new Child();  

obj1 instanceof Parent: true;

## controladores de fluxo

if else  
ternário  
switch  
for  

### exemplo for

int[] numbers = {1093850918591}  
for(int item : numbers) {  
}  

if (....)  
continue (pula para próxima iteração.  
foreach  
while  
do-while  

// e /**/ - comentários

## javadoc

gera um html com a documentação automática do código

# I/O

## [System.in](http://system.in/)

representa fluxo de entrada padrão do sistema  
é do tipo java.io.InputStream  

Scanner // leitura

import java.util.Scanner;

exemplo Scanner sc = new Scanner([System.in](http://system.in/)); // scanner  
int i = sc.nextInt(); //le um inteiro com um método do objeto sc da classe scanner.