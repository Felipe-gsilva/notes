subclasses (classe mais especifica) herdam suas superclasses (classe mais generica)

```Java
public class Carlos extends Pessoa {
[..]
}
```

importante para reuso de software  
construtores são capazes de serem chamados pela subclasse com 'super'  

- é possivel declar um campo na subclasse com o mesmo nome de um campo da superclasse  
    -um metodo protected pode ser reescrevido como private na subclasse  
    

## polimorfismo

existem várias instancias, ou seja, cada objeto pode responder diferentemente para cada mensagem, de acordo com a sobreposição ou não de métodos

o primeiro método a ser chamado pela JVM tende a ser o mais especializado, sempre que houver  
essa alteração ocorre quando os métodos tem assinaturas identicas com mesmo tipo ou subtipo de retorno  

notação @Override serve para anotar quais métodos são polimorfismos de superclasses  
só serve para acusar erro em caso da não existência do método pai.  

se a superclasse não tem um construtor vazio, a subclasse não consegue utilizar-se de um construtor vazio genérico

### final com herança

métodos final não podem ser sobrescritos e nem herdados  
é recomendado que métodos inseridos dentro de um construtor devem ser final  

### casting implicito

uma classe pai pode receber uma instancia de uma classe filho, mas o inverso não é válido, apenas com casting explícito

### implicito:

ex: Pessoa pessoa = new Carlos();

### explicito

ex: Carlos carlos = new Carlos();  
Pessoa pessoa = new Pessoa();  
carlos = (Carlos)pessoa;