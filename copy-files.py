from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import os

def generateFiles(root, file, path):
    os.system('dd if={} of={}  count=1024000 bs=1024'.format(os.path.join(root, file), os.path.join(path, file)))


pathFrom = '/amartirosyan/Desktop/folder-1/'
pathTo = '/amartirosyan/Desktop/folder-2/'

# Copy files using processes
executor = ProcessPoolExecutor(max_workers=8)
for root, directories, files in os.walk(pathFrom):
    for file in files:
        executor.submit(generateFiles(root, file, pathTo))

# Copy files using threads
executor = ThreadPoolExecutor(max_workers=8)
for root, directories, files in os.walk(pathFrom):
    for file in files:
        executor.submit(generateFiles(root, file, pathTo))

# Copy files without using threads
for root, directories, files in os.walk(pathFrom):
    for file in files:
        generateFiles(root, file, pathTo)

# Time: real 0m12.