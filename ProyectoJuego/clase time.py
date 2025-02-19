import time
start_time  = time.time()
time.sleep(2)
elapsed_time = time.time() -start_time
print("tiempo trsnscurrido:", elapsed_time "segundos")
import time

#obtener el tiempo actual
start_time = time.time()

# hacer algo que  tome tiempo
time.sleep(2)

#calcular el tiempo  transcurrido
elapsed_time = time.time() -start_time
print("Tiempo trasncurrido :", elapsed_time, "segundos")
