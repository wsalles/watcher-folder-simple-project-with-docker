
#!/bin/bash

# ARGUMENTO OBRIGATORIO PARA DETERMINAR A TAG DA IMAGEM DOCKER

if [ "$1" = "" ]; then
        echo "#######################################"
	echo "#   ATENÇÃO - ARGUMENTO OBRIGATORIO   #"
        echo "#######################################"
        echo ""
	echo "É necessário informatar a TAG para a imagem Docker!"
	echo "Utilize um dos exemplos abaixo:"
	echo "sh start.sh 2.0"
	exit 1
else
        echo "Iniciando o script para o Compose"
fi

stack="watcher"
folder=("file-copy")
prefix="spla"
images=(file-copy)
TAG=$1

installDocker() {
        echo "#####################"
	echo "# 1) INSTALL DOCKER #"
        echo "#####################"
	echo ""
        mkdir /etc/docker/ >/dev/null 2>&1
	if [ $? -eq 0 ]; then
          echo "Instalando o Docker...!"
	  curl -fsSL https://get.docker.com | sh
	  docker swarm init
	else
          echo "O Docker ja esta instalado!"
	  sleep 1;
        fi
}

dockerImages() {
        echo ""
	echo "##########################################"
	echo "## 2) CRIANDO AS IMAGENS DOS CONTAINERS ##"
	echo "##########################################"
	echo ""
	for x in "${images[@]}"
	do
	  docker images | grep -E "$prefix/$x.*$TAG" >/dev/null 2>&1
	  if [ $? -eq 0 ]; then
	    printf "A imagem: $prefix/$x:$TAG ja existe!\n"
	  else
	    docker build -t $prefix/$x:$TAG ./$x/.
	    docker push $prefix/$x:$TAG
	    printf "A imagem: $prefix/$x:$TAG foi criada!\n"
	  fi
        echo ""
	done
}


deploy() {
	export TAG=$TAG
	docker stack deploy -c docker-compose.yml watcher
}

installDocker;
dockerImages;
deploy;
