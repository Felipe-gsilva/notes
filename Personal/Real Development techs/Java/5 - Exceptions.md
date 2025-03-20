serve para tratar os runtime errors, ao se tratar erros com exceções  
EX:  
extrapolar um vetor, dividir por 0, casting explicito errado, arquivo inexistente, tentar gravar um disco cheio...  

A execução para no ponto de erro e grava a exceção no objeto. O compilador tenta encontrar a tratativa do erro, se não o encontrar, exit();  
caso o método atual não tenha um handler de erro, ele procura o tratamento de erro no método que o chamou até chegar na main.  

## throws

public void x() throws exceção1, exceção2 {}

## filhos de throwable

### exception e (checked)

são erros que podem ser contornados, como abertura de um arquivo incorreto, por exemplo

### error (unchecked)

erros externos a aplicação, que não necessariamente conseguem ser tratados pelo programa

### runtimeexception (unchecked)

pode ser capturada pelo programador, mas o erro majoritariamente está no código (skill issue)

### try-catch

try {  
[..]  
} catch (exception e | sqlexception e) {  
[..]  
}  

## histórico de execução

é possível obter cada elemento de execução ocorrido até o ponto de falha.  
pode-se chamar o método e.printstacktrace(); para printar o que fora supracitado.