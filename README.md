# MPI
Comunicación entre dos máquinas median mpiexec
## Tabla de contenidos:
---
- [Empezamos](#empezamos)
- [Instalaciones necesarias](#instalaciones-necesarias)
- [Para ejecutar codigo python y mpiexec](#para-ejecutar-codigo-python-y-mpiexec)
- [Configuraciones Generales y clave ssh](#configuraciones-generales-y-clave-ssh) 
- [Configuración máquina Master](#configuración-maquina-master)
- [Configuración máquina Clientes](#configuración-maquinas-clientes)
- [Pruebas](#pruebas)
- [Ejemplo de python](#ejemplo-de-python)

## Empezamos
Para la comunicación entre las máquinas deben tener un mismo usuario

<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/84022712-563d-4641-9bef-244832fa31d1"/></p> 

- Opcional
Si deseamos cambiar el nombre de nuestro host lo podemos hacer y una vez cambiado debemos reiniciar nuestra máquina
```
$hostnamectl set-hostname master
``` 

## Instalaciones necesarias 
En cada máquina que vamos a ocupar necesitamos tener instalado lo siguiente 
```
$ sudo apt-get update
$ sudo apt install net-tools openmpi-bin openmpi-common libopenmpi-dev openssh-client openssh-server nfs-kernel-server
```
## Para ejecutar codigo python y mpiexec 
Tenemos que tener instalado lo siguiente
```
$ sudo apt-get install python-pip
$ pip install mpi4py
```
## Configuraciones Generales y clave ssh
- En todas la maquinas necesitamos editar el archivo host y agregar una maquina Master y los Clientes que sean necesarios
```
$ sudo nano /etc/hosts
```
Agregamos las ip de nuestras máquinas como se muestra en la siguiente imagen
<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/14f95487-8517-4284-97cc-9523f6aad8f3"/></p> 

- Crear directorio oculto para crear llaves de ssh
```
$ mkdir ~/.ssh
```
- Generar llave
```
$ ssh-keygen -t rsa
```
- Copia de respaldo
```
$ cp id_rsa.pub authorized_keys
```
<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/0cc28332-abf8-4f1a-9d3f-1a273fb3f474"/></p> 

- Pasar llave a los clientes(contraseña de máquina client) 
```
$ ssh-copy-id client1
$ ssh-copy-id client2
```
- Tener configura el siguiente archivo en los clientes
```
$ sudo nano /etc/ssh/sshd_config
```
La configuración debe estar el PubKeyAuthentication y RSAAuthentication en yes
<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/aa04f70f-bf2b-4d37-8f5a-c521e9493c69"/></p> 

- Reiniciar ssh
```
$ sudo service ssh restart
```

## Configuración máquina Master
- Creamos una carpeta
```
$ mkdir MPI
```
- Damos los permisos de escritura a la carpeta
```
$ sudo nano /etc/exports
```
Adicionamos la siguiente linea al archivo /home/mpi/MPI client1(rw,sync,no_subtree_check) client2(rw,sync,subtree_check)

<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/7541632e-e2c8-45f5-b6a1-827b1cfb5abf"/></p> 

- Reiniciamos el server y lo volvemos habilitar 
```
$ sudo systemctl restart nfs-kernel-server
$ sudo systemctl enable nfs-kernel-server
```

## Configuración máquinas Clientes
- Creamos una carpeta
```
$ mkdir MPI
```
- Montamos la carpeta MPI de nuestra máquina master
```
$ sudo mount master:/home/mpi/MPI /home/mpi/MPI
```

## Pruebas 
Ejecutamos la siguiente línea de código para ver si tenemos comunicación entre nuestras máquinas
```
$ mpiexec -hostfile hosts python ejemplo.py
```

<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/60c059b1-fe96-4ee7-bbf6-17e3ec4c3c02"/></p> 
<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/a710d3b8-f231-4aba-9044-3be0819d1338"/></p> 


## Ejemplo de Python
<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/3ea1644d-d2f8-4948-91e8-6dbfeaeb5d4c"/></p> 


