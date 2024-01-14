import sys
fileNum = int(sys.stdin.readline().rstrip())
extensionDict = {}

for i in range(fileNum):
  fileName = sys.stdin.readline().rstrip().split(".")[1]
  extensionDict[fileName] = extensionDict.get(fileName, 0) +  1

sortedExtension = sorted(extensionDict)
  
for i in range(len(sortedExtension)):
  extension = sortedExtension[i]
  print(extension, extensionDict[extension])