def details(name:'Gayathri', age=34):
    print(name)
    print(age)

details('Keerthi', 35)

def persondetails(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(name, i, j)
        print(i,j)


persondetails('Gayathri', age=34, Location='Bangalore', No=9844595571)