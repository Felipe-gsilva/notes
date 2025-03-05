# Components explained
On this file, we are adding a brief explanation about our component structure. To simplify even more, you can watch [Stuart's Sierra](TODO) explanation. With the background built, you can later come here and complete your journey with our own component explanation.


## core
The core component is the one responsible for defining all of the constructors our component system needs, but, as you can see, we are not yet declaring the component dependencies. This is set on fly.

## config
The config component is responsible for granting our entire api config is correctly built, being by the default configuration or any passed into it. It encapsulates any state we can use in our application, for default the dev environment.

needs a input of a config.edn (extensible data notation) as the one below:

```Clojure
{:webserver/port \#long \#or [\#env PORT 3000]
 :env \#profile {:dev :dev
                :default :dev
                :prod :prod}
 :release "1.0.0"
 {...}
```

## database
The database component is capable of connecting our database, wherever it is located, to the application. It means this component states changes depending on how your infrastructure is desgined. -- TODO

## db-utils
To guarantee specific input and to parse our raw passed argument from database component, db-utils comes in handy. It's now used to fix some input differences and building the correct URI either for the database either for each query the dabase will receive.

## http
The http component handle http requests TODO

## migrations
Migration componets are responsible for confing and stablishing the database migration, preventing the programmer to change the database directly aand promoting a automatic config. This component API is capable of building the database config based on a config path and have some essential basic db functions.

to make a migration, you can use some of the pre selected words (create up down migrate-until-just-before init migrate rollback pending-list) and using a config.edn. This example below works on some of our repos:


```sh

clj -M:migratus back/config.edn "create" 

```

## mq
Responsible for wrapping our clj-rq repo into our application. To understand clj-rq better, read our offical [docs](http://github.com/moclojer/clj-rq/README.md)

## router

## sentry

## storage

## webserver

