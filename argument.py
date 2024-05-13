def persondetails(Name, **data):
    print(Name, data)
    for i, j in data.items():
        print(Name, i, j)
    

persondetails(Name='Keerthi', age=35, Location='Bangalore', Mobile=9798354548)