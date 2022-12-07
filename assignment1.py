diner_guest= ["favour","paul","simon","george","marion"]
print(diner_guest)
for guest in diner_guest:
    print(f" Hello {guest} i am inviting you over for a dinner in my home in chicago on sunday at 4pm")

diner_guest[1]= "Rose"
print(diner_guest)
for guest in diner_guest:
    print(f" Hello {guest.upper()} i am inviting you over for a dinner in my home in chicago on sunday at 4pm")

diner_guest.insert(0,"nicoline")
print(diner_guest)

diner_guest.insert(3,"Gabriel")
print(diner_guest)

diner_guest.append("angeline")
print(diner_guest)

for guest in diner_guest:
    print(f" Hello {guest.upper()} i am inviting you over for a dinner in my home in chicago on sunday at 4pm")
