# Entrevista

- retorno dinamico
- usa o selmer para o render template (similar ao django de python)
- atualiza em runtime diferentes endpoints colocados no template .yml, reiniciando o servidor mock
- da pra alterar o provedor de informacoes pro servidor mock, com a tag `external body` pode ser json ou xlsx (excel), apenas bastando especificar o caminho para este arquivo dentro de onde o mock server possa acessa-lo
- da pra fazer URL requests no exeternal body
- da pra configurar o server no XDG_CONFIG_HOME ($HOME/.config) — default/ ou no MOCLOJER_ENV
- webhook pode ser utilizado pra triggar uma request externa enquanto se usa um endpoint, tipo usar a endpoint task | POST e consultar se ja existe primeiro com task | GET
---
# GIT
## PR
WIP (work in progress)
# Branches
one branch for issue
infinitve verbs alike → EX: doc: adding this and that
or maybe → adds this and that 

---
# Component / Sierra
[https://www.youtube.com/watch?v=13cmHf_kt-Q](https://www.youtube.com/watch?v=13cmHf_kt-Q)

[[Components]]

[[moclojer components]]

# Request lifecycle

pedestal → [https://github.com/pedestal/pedestal](https://github.com/pedestal/pedestal) mais middleware e [https://github.com/metosin/reitit](https://github.com/metosin/reitit) → 4

interceptor (reitit) → → → Handler (from http.in) → response (http.out)

# Error handling
[http://pedestal.io/pedestal/0.6/reference/error-handling.html](http://pedestal.io/pedestal/0.6/reference/error-handling.html)
# CLJ-RQ
redis-queue impl in clj