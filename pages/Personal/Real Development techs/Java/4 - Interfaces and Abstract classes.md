# Interfaces

são um tipo especial de referencia, porém não podem ser instanciadas, diferentemente das classes.

- Implicitamente, os atributos são constantes (final, public e static).
- os métodos são definidos somente pela sua assinatura (public e abstract).

ex:  
public interface Interface{  
int metodo(parametros){  
}  

ex. de uso:

public class Classe implements interface {  
}  

uma interface pode herdar (extends) várias interfaces.

- interfaces podem ser usadas como qualquer outro tipo em java e elas representam qualquer objetos que a implemente.

uma interface pode receber métodos abstratos com as tags  
-default  
-static  
e implementá-las.  

classes que implementam interfaces precisam implementar TODOS os métodos abstratos contidos nela (menos os que possuem default).

Métodos de superclasses tem precedência sobre métodos default de interfaces.

## Classes Abstratas

Classes abstratas são classes que representam um objeto de maneira genérica mas não possuem instãncias (abstract).  
Não precisam de implementação.  

ex:  
abstract class AbstractClass{  
int metodo(parametros){  
}  

ex. de uso:

public class Classe extends AbstractClass{  
// int método é puxado ai  
}