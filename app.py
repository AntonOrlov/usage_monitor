import time
import os, sys
import config.local as config
import multiprocessing
from telegram import send_message  
import shutil
import socket

CPU_COUNT = multiprocessing.cpu_count()

def main(args):
  while True:
    warnings = []
    cpu = int(cpu_utilization())
    memory = int(memory_utilization())
    disk = int(disk_utilization())
    if (cpu > config.THRESHOLD["cpu"]):
      warnings.append(["cpu", cpu])
  
    if (memory > config.THRESHOLD["memory"]):
      warnings.append(["memory", memory])
    
    if (disk > config.THRESHOLD["disk"]):
      warnings.append(["disk", disk])

    if (len(warnings) > 0):
      send_message(warnings)

    time.sleep(config.CHECK_INTERVAL)


def memory_utilization():
  with open('/proc/meminfo') as file:
    for line in file:
        if 'MemAvailable' in line:
          available = float(line.split()[1])
        if 'MemTotal' in line:
          total = float(line.split()[1])
  return (total - available) / total * 100


def cpu_utilization():
  loadavg = os.getloadavg()
  return loadavg[1] / CPU_COUNT * 100


def disk_utilization():
  total, used, free = shutil.disk_usage("/")
  return (total - free) / total * 100


if __name__ == "__main__":
  args = sys.argv[1:]
  try:
    main(args)
  except KeyboardInterrupt:
    print('\nInterrupted by keyboard')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
