rearranjar os buckets caso tenham mais chaves do que o permitido em N. Ou seja, podemos alterar a quantidade de bits necessários para indexação. A profundidade do diretório define a quantidade de bits para indexação

Usando os bits mais significativos, quando estouramos o numero de chaves num bucket, passamos a usar k + 1 bits significativos, sendo assim, temos que o 1001 e 1000 ficariam em um bucket e o 1010 em um n
![[hashing expansivel]]
