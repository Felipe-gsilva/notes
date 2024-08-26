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