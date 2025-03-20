person= {
    "name":"sunita",
    "phone":"212-515-5555",
    "address":["123 Main st","Sydney"]
}
print(person['address'][1])


nums=[1,2,3,4,5]
sum = 0
for num in nums:
    sum+=num
print(sum)


myfile=open('myfile.txt', 'wt')
write('hello',file=myfile,)