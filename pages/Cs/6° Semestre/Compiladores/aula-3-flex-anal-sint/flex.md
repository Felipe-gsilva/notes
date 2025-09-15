aula de flex

# Padrões de expressões regulares
POSIX é o padrão, mas o que mais está sendo utilizado é PCRE.

- Literais -> example 
- Conjuntos [] -> [A-z]
- Grupos () -> (abc)
- Ancoras ^ \$ -> \^example\$ 
- Uniao | -> (let|const)
- Fechamento * (0 ou +) + (positivo) {valor arbitrario} -> (ab)*[c-z]+\[\[:digit:\]\] {1, 3}
- Expansao {NAME} -> a{NAME}b (sendo NAME um valor definido pelo usuario)
- Curinga . -> .
- Escape \ -> \\.\\+\\(

--- 
# Flex 
- char* yytext
    - string contendo o valor do token atual
- int yylen 
    - tamanho da string do token atual
- FILE* yyin 
    - contem o arquivo de leitura. Por padrao, stdin (console).
- void yyrestart(FILE* new_file)
    - injeta um novo arquivo dentro de yyin.
- FILE* yyout 
    - COntem o arquivo que recebera a saide do programa (padrao stdout).
- int yylineno
    - Numero da linha atual (precisa de %option yylineno) no preambulo.
