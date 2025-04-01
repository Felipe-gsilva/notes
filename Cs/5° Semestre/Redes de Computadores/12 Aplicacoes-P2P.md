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
No início da distribuição, apenas o “servidor” tem o arquivo F.
- Para levar este arquivo à rede de pares, o servidor deve enviar cada bit do arquivo pelo menos uma vez através seu link de dados (usando sua banda máxima us ).

Assim, o tempo de mínimo distribuição, é pelo menos:

tempo minimo = $\frac{f}{\micro_s}$


Assim como no modelo CS, o par com menor banda não pode obter todos os F bits do arquivo em menos do que $\frac{F}{d_{min}}$.

Tempo mínimo = NF / (us + u1 + u2 + u3 + ... + uN) -> $\micro_s + \sum\limits_{i=1}^{N}\micro_{i} \micro_i$

### Resumo

- Servidor - Melhor caso:  $\frac{F}{\micro_s}$

- No - Melhor caso: cada cliente faz o download de uma cópia.
    - Tempo de download do cliente mais lento: $\frac{F}{d_{min}}$
    - Todos os nós: download agregado de NF bits

- Taxa maxima de upload do sistema: $\micro_s + \sum\limits_{i=1}^{N}\micro_{i}$

Assim o tempo mínimo real de distribuição P2P é:

$$D_{p2p} = max \lbrace \frac{F}{\micro_s}, \frac{F}{d_{min}}, \frac{NF}{\micro_s + \sum\limits_{i=1}^{N}\micro_{i}}  \rbrace$$
