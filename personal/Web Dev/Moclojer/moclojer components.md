https://github.com/moclojer/components

# config

;; TODO

needs a input of a config.edn (extensible data notation) as the one below:

```Clojure
{:webserver/port \#long \#or [\#env PORT 3000]
 :env \#profile {:dev :dev
                :default :dev
                :prod :prod}
 :release "1.0.0"
 :supabase-api-key \#or [\#env SUPABASE_API_KEY ""]
 :supabase-url \#or [\#env SUPABASE_URL "https://"]
 :supabase-jwt-secret \#or [\#env SUPABASE_JWT_SECRET ""]
 :moclojer {:config-path \#profile {:default "resources/moclojer.yml"
                                   :prod "moclojer.yml"}
            :join? \#profile {:default false
                             :dev false
                             :prod true}}
 :storage {:access-key-id \#or [\#env AWS_ACCESS_KEY_ID "foo"]
           :secret-access-key \#or [\#env AWS_SECRET_ACCESS_KEY "bar"]
           :region \#or [\#env AWS_REGION "us-east-1"]
           :protocol \#profile {:dev :http
                               :default :http
                               :prod :https}
           :port \#profile {:dev 4566}
           :host \#profile {:dev "localhost"
                           :default "localhost"
                           :prod "sfo3.digitaloceanspaces.com"}}
 :sentry {:env \#profile {:dev "dev"
                         :prod "prod"
                         :default "prod"}
          :dsn \#or [\#env SENTRY_AUTH_TOKEN "foobar"]}
 :cloud-providers
 {:digital-ocean {:base-url "https://api.digitalocean.com/v2"
                  :token \#or [\#env DO_TOKEN "foobar"]
                  :app-id ""}
  :cloudflare {:base-url "https://api.cloudflare.com/client/v4"
               :token \#or [\#env CF_TOKEN "foobar"]
               :zone-id ""
               :record-content "goldfish-app-zq7eo.ondigitalocean.app"}
  :max-verification-attempts 20
  :verification-timeout-ms 3000}
 :mq {:uri \#or [\#env REDIS_URL "redis://localhost:6379"]}
 :database {:dbtype "postgres"
            :jdbc-url \#or [\#env DATABASE_URL "postgresql://localhost:5432/postgres?user=postgres&password=postgres"]}
 :migration-dir "back/migrations"}
```

this config file sets some basic info of the project

- database type, url and migration dir
- cloudfare info
- digital ocean info
- storage component info
- sentry component info
- supabase (firebase poor edition)

# core

stores all the constructors for the components, making it easier to access and comprehend

# database

# db_utils

# http

# logs

# migrations

# moclojer

# mq

# router

# sentry

# storage

# webserver