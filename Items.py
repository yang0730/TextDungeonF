Items=[]

file = open('Item.md','r')
lines = file.readlines()
for line in lines:
  line = line.strip("\n")
  line = line.split(",")
  line[0] = int(line[0])
  line[1] = line[1].strip("\'")
  line[2] = int(line[2])
  line[3] = int(line[3])
  line[4] = int(line[4])
  line[5] = int(line[5])
  line[6] = int(line[6])
  line[7] = line[7].strip("\'")
  line[8] = line[8].strip("\'")
  line[9] = int(line[9])
  Items.append(line)


def findItem(i):
  for item in Items:
    if item[0] == i:
      return item

