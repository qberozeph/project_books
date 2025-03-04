### Обновления docker на сервере
```sh
  git pull origin main
  docker build -t my_image .
  docker stop my_container
  docker rm my_container
  docker run -d --name=my_container -p 80:8000 my_image
```
