Este documento representa meus estudos acerca do livro Redes de Computadores e a Internet - uma abordagem top down

---

# Comparilhamento de arquivos - Aplicacao P2P

O mais usado na Internet.
Ele nao utiliza do potencial de computacao distribuida proveniente na Rede.

Eh uma classe de aplicacoes que aproveita dos recursos na borda da rede, diretamente entre os sistemas.

- Armazenamento
- Processamento
- Largura de Banda

Quando um client procura por um arquivo em um seeder na rede e comeca a fazer o download, ele mesmo passa a ser um seeder, como um servidor, e disponibiliza o arquivo.

## Definicao
Sistema distribuido, sem controle centralizado ou organizacao hierarquica.
- o software peer to peer tem funcionalidades equivalentes entre as maquinas.
- pontos sao autonomos.
- pontos e conexoes n precisam ser constantes.

- rede de overlay: os pares foram uma rede sobreposta a rede IP

## Escalabilidade

### Modelo Classico
- Transmitir uma cópia do arquivo para cada um dos N pares.
    - Transmitir um total de (N x F ) bits.
    - Tempo para distribuição do arquivo deve ser pelo menos NF/us.
- $d_{min}$: menor capacidade de download de um par.
    - Par com menor taxa não pode obter todos os F bits do arquivo em menos tempo do
que F/dmin.

$$D_{cs} = max \lbrace \frac{NF}{\micro_{s}} \, \frac{F}{d_{min}} \rbrace$$



### E se tivessemos mais seeders?

