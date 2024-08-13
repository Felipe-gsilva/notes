---

๏ Generics

๏ Classes e métodos genéricos

๏ Genéricos restritos

๏ Herança de classes genéricas

๏ Wildcards

๏ Collections

๏ Interfaces e classes de coleções

๏ Algoritmos sobre genéricos

๏ Iteradores

---

# **VAI CAIR NA PROVA**

?  
não identifica o tipo que será enviado, portanto não pode ser reusado dentro de um método, ou seja, não será posível adicionar a uma possível lista qualquer objeto do tipo desconhecido  

**Usando Wildcard ou Generics< T >**

- Usar coringa apenas para flexibilizar parametros completamente sem relação
- Usar < T > quando há uma relação entre os parâmetros

**Apagamento de Tipos (Erasure) - O compilador muda os tipos de generico para concreto**

o erasure funciona como um casting durante a passagem de parâmetros, substituindo os tipos genéricos por tipos concretos

`Restrições:`

- não é possível passar generics com tipos primitivos
- não é possível criar instâncias de valores genéricos
- não é possível criar campos estáticos de tipos genéricos
- não é possível criar vetores com tipos genéricos
- não é possível criar objetos de exceção com gererics

---

# **Generics**

- servem como templates e permitem que tipos sejam parametros na definição de classes, interfaces e métodos
- evita o uso de casting explicito

um Tipo Generico é uma classe parametrizada sobre tipos

Parametro é incluido entre colchetes angulares <>  
logo após o nome da classe, assim sendo, o tipo T pode ser de qualquer  
tipo  

ex:  
  
`public class Box<T> { private T t; public void set(T t) {this.t = t} }`

**Convenções**

- E(Element)
- K(Key)
- T(Type)
- V(Value)
- N(Number)

**Construção**

durante a construção de um objeto com parametro generico, deve-se colocar em sua criação o tipo escolhido  
ex:  
  
`Box<Integer> integerBox = new Box<Integer>;`

`Box<Integer> = new Box<>();`

**Métodos**

isso poder ser utilizado em métodos, apenas, estáticos e não estáticos, construtores..  
--> deve aparecer antes do ipo do retorn  

`public static <K, V> boolean compare(Pair<K, V> p1, Pair<K, V> p2);`

**Restrições**

é possível restringir o que é recebido dentro de uma genérico, por exemplo, alguma que implementa X ou estenda Y

`<T extends x>`

pode, também, estender diversas classe diferentes

`<T extends x && y && z>`

## **Wildcards**

podemos usar o wildcard (coringa hehehehe) para não permitir a inserção de qualquer tipo de uma classe em uma outra.

> basta usar o ?

`public void boxTest(Box<?> n)`

pode-se restringir superiormente o tipo do wildcard com extends, provavelmente é a impl ideal

`public void boxTest(Box<? extends Carlos> n)`

restrição inferior, quer dizer que a classe recebida deve ser pai de uma outra classe

`public void boxTest(Box<? super Carlos> n)`

---

# **Collections**

é um objeto que agrupa de diferentes formas vários elementos

JAVA oferece:

- interfaces com definições das colections
- implementações
- algoritmos em métodos prontos

**Tipos de collections principais**

- Set: não permite repetir termos e representa conjuntos Matemática
- SortedSet: set mas sorted
- List: Coleção ordenada de elementos
- Queue: fila FiFo (funções -> add, offer, remove, pool)
- Deque: fila mas com inserção e remoção no começo e no fim
- Map: função matemática basicamente
- SortedMap: sortido 😂

> Existem diversas classes concretas que implementam essas interfaces

**Collections.methods()**

- sort: usa mergeSort = O(nLogn)
- shuffle: embaralha
- reverse, fill, copy, swap(elements), addAll
- binarySearch(list, key): O(logn)

> por prática, deve-se utilizar a interface que se implementa o TAD para referenciar o tipo

---

## **Iterator**

Métodos genéricos para acesso

- hasNext() -- while(tem)

> for(Iterator it = list.iterator(); it.hasNext(); ) -- it.next()

  

TODA COLLECTION PADRÃO TEM UM ITERATOR NELA, ENTÃO VC PODE PERCORRE-LA COM ELE

  

๏ boolean hasNext()

- Retorna true se há elementos a serem lidos no iterador

๏ E next()

- Retorna o próximo elemento do iterador.

๏ void remove()

- Remove o último elemento obtido pela chamada de next()
- Só é possível chamar uma vez para cada chamada de next()
- Se essa regra for desrespeitada, uma exceção é lançada.