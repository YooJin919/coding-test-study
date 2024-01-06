fileNum = int(input())
extensionDict = {}

for i in range(fileNum):
  fileName = input().split(".")[1]
  extensionDict[fileName] = extensionDict.get(fileName, 0) +  1

sortedExtension = sorted(extensionDict)
  
for i in range(len(sortedExtension)):
  extension = sortedExtension[i]
  print(extension, extensionDict[extension])