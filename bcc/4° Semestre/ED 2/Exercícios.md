![[lista1.pdf]]


# Solução
1 - Um arquivo lógico representa a forma como a linguagem de alto nível representa e enxerga os dados, não necessariamente representa como um arquivo físico está localizado no sistema. Ambos representam conjuntos de bytes, evidentemente, porém, um arquivo físico não tem distinção de suas qualidades internas, ou seja, não difere uma struct de um inteiro ou etc. 

2 - um seeking representa o movimento que a agulha de um disco tem que fazer para achar o cluster onde estão os dados de um arquivo em específico e representa(va) um custo absurdo para o sistema computacional, visto que um movimento cinético é muito mais lento que um elétron em movimento.

3 - conjunto de trilhas verticalmente paralelas. são organizados assim para reduzir o numero de seekings, visto que em um cilindro podem ser feitas várias buscas paralelamente.

4 - são lentos, são mecânicos.

5 - Discos são divididos em:
 - discos
 - superfícies
 - trilhas
 - cilindros 
 - setores;
os discos tentam ao máximo evitar fragmentação, mas a parte de armazenamento dentro deles cabe ao file system, vide ReFS, NTFS, ext4, ext3 ....

6 - São espaços de memória dedicados a transmissão de dados entre dispositivos de entrada e saida e o sistema computacional.

7 - Um cluster representa uma sequência lógica de arquivos, como o arquivo de index que podemos criar.

8 -

9 -

10 -

11- 

12 - 

13 - As limitações são que o caractere utilizado para ser o delimitador deve estar fora do utilizado no campo. O delimitador pode ser uma /, mas / tem direto em texto.

14 - Depende do tamanho. Relative record number guarda o indice 
> Byte offset = RRN * Tamanho do registro.

15 - É importante criar blocos com uma determinada quantidade de structs predefinidas, dessa forma, você diminuirá a quantidade de seekings para buscar um dado, ja que devido ao **principio da localidade**, mais dados podem estar próximos...

16 - (64 * 3) + 10

17 - acesso rápido, memória cheia de merda. cheio de fragmentação.

18 - Relative Record number

19 - 
First Fit is fast and simple to implement, making it the most commonly used algorithm. However, it can suffer from external fragmentation, where small free partitions are left between allocated partitions.

Best Fit reduces external fragmentation by allocating processes to the smallest free partition, but it requires more time to search for the appropriate partition.

Worst Fit reduces external fragmentation by leaving the largest free partition, but it can lead to inefficient use of memory.

20 -  Sim, é vantajoso. A inserção pode ser feita de maneira completamente aleatória, podendo apenas ser sorted no arquivo de index.

21 - você pode marcar para reuso com um bit especial e/ou criar um arquivo com uma Lista de Espaços Disponíveis (LD).

22 - a diferença é que a fragmentação interna ocorre dentro de um registro, ou seja, campos estáticos com espaço inutilizado. A externa acontece fora, entre os structs.

23 -   Para salvar informações uteis para o acesso das informações contidas nele. Tipo o LD ou sla

24 -  
Carla|Guimarães|Rua Riachuelo 123|Jardim America|033|720|.......... Djavan Carlos| Moura|Av D. Pedro I 1234|Vila independência|033|730|

25 -  

26 - burro.

27 - feito  

28 -