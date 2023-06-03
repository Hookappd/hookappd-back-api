## Compose for hookappd-back-api

## Deploy with docker compose

```shell
docker-compose up -d --build
```
## Expected result

Listing containers must show one container running and the port mapping as below:
```
CONTAINER ID   IMAGE                                 COMMAND       CREATED         STATUS         PORTS                            NAMES
39bd15c72789   hookappd-back-api-hookappd-back-api   "/start.sh"   4 seconds ago   Up 3 seconds   80/tcp, 0.0.0.0:8000->8000/tcp   hookappd-back-api
```

After the application starts, navigate to `http://localhost:8000` in your web browser and you should see the following json response:
```
{
"message": "OK"
}
```

Stop and remove the containers
```
$ docker compose down
```

---
Url: http://127.0.0.1:8000/manufactures <br />
Description: Show available hooka manufactores

How to add new manufacture:
```
curl -d '{"name":"Darkside"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/manufactures
```
