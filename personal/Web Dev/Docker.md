```YAML
services:
  front:
    build: front
    ports:
      - "5173:5173"

  app:
    build: app
    ports:
      - "8000:8000"
```

  

```Docker
FROM docker.io/clojure:temurin-21-tools-deps-alpine

WORKDIR /app/

COPY . .

EXPOSE 8000

CMD [ "clojure", "-M:dev", "-m", "dev.core"]
```