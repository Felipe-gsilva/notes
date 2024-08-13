# garbage collector

objetos não utilizados são aqueles que não estão sendo referenciados por nenhuma parte do programa  
assim, a memória não utilizada será liberada  

## passo 1: marcação

verificar a referenciação

## passo 2: deleção normal

- alocador de memória possui ponteiros para blocos livres  
    -depois se compacta o heap  
    

## heap na jvm

### young, old and permanent gen

objetos são alternados de geração em geração de acordo com seu tempo de vida  
Minor GC é chamado quando eden é preenchido e são realocados em surviros space.  

# construtor

método construtor q é chamado toda vez em que essa classe é instanciada  
ex:  
private static int contador = 0;  

public __class_name() {  
contador++;  
}  

# java x C++

java n tem destrutor, C++ tem

# Dicas para nivel de acesso

- Use sempre o nivel mais restrito possivel (private).
- Evite campos públicos, exceto para constantes.

## inicializar arrays numa classe antes de instanciar

public static void function(){  
for(int i = 0; i < array.length(); i++)  
array[i] = x;  
}  

## packages

protected e package-private (ausente) são estritamente relacionados a pacotes  
é declarado no inicio do código-fonte da classe