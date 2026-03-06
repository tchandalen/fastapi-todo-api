### Setup Project

To run this application

```sh
uvicorn main:app --reload
```

To build image and push to docker repo

```sh
docker build -t teangchandalen/tcdl:todo-api --push .
```