# Domain Driven Development

## Filosofia e Processo
O DDD funciona através da colaboração intensa entre especialistas de domínio (lógica de negócio) e desenvolvedores. É, em si, uma abstração chamada de **Modelo de Domínio**.


## Estruturas do Design Estratégico
- Linguagem Ubiqua: uma linguagem tem que ser definida para permitar a comunicação entre as partes, evitando jargões técnicos ou falta de profundidade, ou seja, uma mescla dos conceitos das partes.

- Contextos Delimitados (Bounded Context): é uma limitação de restrição seja de código, serviço ou qualquer parte do desenvolvimento. 

- Mapas de Contexto (Context Maps): Documentam as relações entre os dfierentes Bounded Contexts e times (ex: Kernel Compartilhado, Cliente-Fornecedor)

## Estruturas do Desgin Tático (Building BLocks)

- Entities: Objetos definidos por sua identidade (um ID único) e continuidade ao longo do tmepo. Possuem ciclo de vida e estado mutável,  mas com a identidade imutavel (Ex: Cliente).

- Value Objects: Objetos sem identidade conceitual, apenas tem seus valores e atributos. Devem ser imutáveis (Ex: Dinheiro ou Email ao invés de string ou float).

- Aggregates: conjunto dos 2 acima tratados como uma entidade unica (Ex: Pedido com Email, Dinheiro e Cliente)


- Servicos de Dominio: Operações ou lógicas de negócio que não pertencem a uma Entidade ou Objeto de Valor (stateless).

- Repositórios: Abstrações que simulam uma coleção de objetos em memória, mediando o acesso à persintência. Recomenda-se um repositório por Agregado.

- Domain Events: Representam um acontecimento passado no sistema que pode ser registrado tanto em memória principal quanto secundária. (Ex: PedidoConcluido).

- Factories: Criação dos Agregados, entidades e objetos é feita por fábricas é feita aqui.

# Arquitetura Hexagonal conciliada ao DDD

Adiciona adapters que, em suma, são só dependencias injetadas em runtime, separando a regra da implementação em si. Por exemplo, o dominio possui a regra de negocio, por exemplo, precisa receber uma entrada de Cliente, mas não implementa diretamente. O adaptador é quem faz a chamada a API, clausula SQL e qualquer outro processo para preencher a Porta (do dominio).


A estrutura conjunta tem essa aparencia (mas não só) 

- Núcleo (Domain Layer): Entidades, Objetos de Valor, as regras em si. Usa a linguagem ubíqua e é agnostico a tecnologia.

- Service/Application Layer: osquestram o fluxo, como receber comandos e direcioná-los aos agregados corretos.

- Adapters: detalhes técnicos de implementação, cujo código é injetado em tempo de execução. 
