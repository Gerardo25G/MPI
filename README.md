# MPI
Comunicacion entre dos máquinas median mpiexec
## Tabla de contenidos:
---

- [Badges o escudos](#badges-o-escudos)
- [Descripción y contexto](#descripción-y-contexto)
- [Ejemplo de python](#ejemplo-de-python)

## Empezamos
Para la comunicación entre las maquinas deben tener un mismo usuario

<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/84022712-563d-4641-9bef-244832fa31d1"/></p> 





## Configuración maquina Master
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

## Configuracion maquinas Clientes
- Creamos una carpeta
```
$ mkdir MPI
```
- Montamos la carpeta MPI de nuestra maquina master
```
$ sudo mount master:/home/mpi/MPI /home/mpi/MPI
```

## Pruebas 
Ejecutamos la siguiente línea de código para ver si tenemos comunicación entre nuestras maquinas
```
$ mpiexec -hostfile hosts python ejemplo.py
```

<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/60c059b1-fe96-4ee7-bbf6-17e3ec4c3c02"/></p> 
<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/a710d3b8-f231-4aba-9044-3be0819d1338"/></p> 


## Ejemplo de Python
<p align="center"><img src="https://github.com/Gerardo25G/MPI/assets/49174524/3ea1644d-d2f8-4948-91e8-6dbfeaeb5d4c"/></p> 


