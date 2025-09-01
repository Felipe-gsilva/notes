# Remote Procedure Call (RPC)
É um mecanismo de comunicação entre processos em ambientes distribuidos, no qual processos requisitam a execução de serviços por parte de um módulo remoto. Na prática, esse mecanismo implementa fielmente o conceito de cliente-servidor.

O módulo remoto, responsável por atender as requisições, é composto por procedimentos e processos tanto internos quanto exportados (visíveis remotamente). 
## Sintaxe
```
module mname
    headers de operações exportadas 

body
- declaracoes de variaveis
- codigo de inicialização 
- procedimentos das ops exportadas
- procedimentos e processos locais

end mname 
```

Os headers são da forma 
> op opname (formals) \[return result\]

Os procedimentos são da forma:
> proc opname (format identifiers) returns res. identifier 
>   declaracao variaveis locais 
>   comandos

Esses procedimentos são chamados remotamente por:
> call mname.opname(arguments)

## Lógica de execução

| processo que chama | servidor |
|--------------------|----------|
| call mname.op | executa op |
| `estado de espera` | termina de executar op |
| volta a executar | |


## Exemplo - Servidor de relógio 

