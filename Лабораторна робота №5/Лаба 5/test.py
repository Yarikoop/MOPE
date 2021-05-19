
import time

st_time = time.time()
for _ in range(100):
    main(15, 6)
print(f'\nСередній час роботи 1 проходження програми: {((time.time() - st_time) / 100)} сек')