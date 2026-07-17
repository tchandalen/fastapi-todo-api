### Setup Project

To run this application

```sh
uvicorn main:app --reload
```

To build image and push to docker repo

```sh
docker build --platform linux/amd64,linux/arm64 -t teangchandalen/tcdl:todo-api --push .
```