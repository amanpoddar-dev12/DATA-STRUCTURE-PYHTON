#algorithm 1st
# def gdc(num1,num2):
#  fn=[i for i in range (1,num1+1) if (num1%i)==0 ]  #first number
#  ln=[j for j in range (1,num2+1) if (num2%j)==0 ]  #last number
#  cf=[f for f in fn if f in ln]                     #common factor
#  return (cf[-1])
# result=gdc(12,24)
# print(result)

#algo 2nd
# def gdc(num1,num2):
#  fn=[]  #first number
#  for i in range (1,num1+1):
#   if (num1%i)==0: 
#     fn.append(i)
#  ln=[]  #last number
#  for j in range (1,num2+1):
#      if (num2%j)==0:
#         ln.append(j)
#  cf=[]      #common factor
#  for f in fn:
#   if f in ln:
#     cf.append(f)
#  return (cf[-1])
# # num1=int(input('enter first number='))
# # num2=int(input('enter second number='))
# result=gdc(12,24)
# print(result)

#algo 3rd
num1=int(input('enter first number='))
num2=int(input('enter second number='))
list1=[]
for i in range(1,num1+1):
    if num1%i==0:
     list1.append(i)

list2=[]
for i in range(1,num2+1):
    if num2%i==0:
     list2.append(i)
list3=[]
for f in list1:
    if f in list2:
      list3.append(f)
print(list3[-1])


#forth algoritm

# def gcd(num1,num2):
#     cf=[]
#     for i in range(1,min(num1,num2)+1):
#      if (num1%i)==0 and (num2%i)==0:
#         cf.append(i)
#     return (cf[-1])
# result=gcd(12,24)
# print(result)
