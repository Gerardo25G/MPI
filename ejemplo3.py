from mpi4py import MPI

comm = MPI.COMM_WORLD
hostname = MPI.Get_processor_name()

print("Hola desde la pc", hostname)
