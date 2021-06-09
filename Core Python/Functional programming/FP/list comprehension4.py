#square of even nos and cube of odd nos
lst=[i*i if i%2==0 else i*i*i for i in range(1,51)]
print(lst)