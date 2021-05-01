import os,sys
bl = '\033[1;96m'
y = '\033[1;93m'
red = '\033[1;31m'
green = '\033[1;92m'
cya='\033[1;035m'
cy='\033[1;095m'
nld = "NLD"
e = "USDP"
NLD_V = 299999
USDP_V = 299999
def add(x, y):
  return x + y
os.system("clear")
print(bl)
print ("NLD = 299999,USDP = 299999")
print ("What you gonna vote?")
print ("NLD or USDP")
print ("Write NLD or USDP that you gonna vote")
print ("This is The last vote!")
vote = input("Enter your vote:"+y+" ")
if vote == nld:
  print (cya)
  os.system("bash load.sh")
  print(".")
  print (NLD_V,"+",1,"=",add(NLD_V, 1))
  print ("You are best people")
  print ("We win!!!!")
elif vote == e:
  print(red)
  os.system("bash load.sh")
  print(".")
  print (USDP_V,"+",1,"=",add(USDP_V, 1))
  print ("I hate you so much go away from Myanmar")
  print ("That because you we lose!")
else:
  print(red)
  print ("Wrong Vote!!!")
  print("")
  print("")
  os.system("python d.py")