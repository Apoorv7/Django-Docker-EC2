# Django-docker

## This Django project consists of:
-  `docker-compose` file 
-  `Userservice` microservice folder 
-  `Todo` microservice folder

## Docker-compose file consists of two services:
### Services:
- `Userservice` 
- `Todo`

### Networks:
- `django-docker`


> Before running docker compose you need to add docker_user and docker_pass in environment variable. For more info you can view `views.py` file in `todo_app` folder.


## Ways for building images and Running Container
With Docker Compose file we can directly run the below command:

 ```
 docker-compose up --build -d
 ```

This command will firstly build the images with respect to the services mentioned in the docker-compose.yml file and then will start the contatiner for each service and join them with the django-docker network for bridge connection.

For stopping the containers we can run the below command:

```
docker-compose stop
```

Without Docker Compose file we need to manually run commands for building each image with docker file and then run the docker run command for starting container.

For building the image we can run the below command:

```
docker build -t [tagname] [path of folder]
```

Also need to create a new network if not using default one:

```
docker network create [network-name]
```

For starting the container with image run the below command:

```
docker run --name [container-name] -p [port address] --network [network name] [image name] 
```

## Deployment to ec2 instance

For this firstly we need to create a new isntance in ec2. I have created using type t2.micro and have added some security groups to it with some inbound rule so anyone can access it.

Now we need to do ssh connection from terminal to connect to ec2 isntance.

For this we need to create a new key pair from network and security and download the .pem file which has the rsa key from ec2 in our local system.

Now open the terminal and cd to the folder where .pem file present.

```
cd [path of folder]
```

After this we need to run the `ssh` command with some parameters:

```
ssh -i [pem file path] [ec2-user]@[Public IPv4 address]
```

Once connected we can copy all the folder contents using `scp` command to the ec2 isntance.

```
ssh -i [pem file path] -r [local folder directory] [ec2-user]@[Public IPv4 address]:[path in ec2 instance]
```

After the files are copied we need to install docker in the ec2 instance and run the following commands: 

```
sudo yum update
sudo yum install docker
```

Now you can run the docker compose command

```
docker-compose up --build -d
```

To check the containers running you can run:

```
docker ps
```

Now you can test the connection with the curl command:

```
curl http://[Public IPv4 address:[port]/]
```