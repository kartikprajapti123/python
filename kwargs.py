def func(**details):
    print(details['id'])
    print(details['name'])
    print(details['address'])
    print(details.keys())
    print(details.values())
    
    
func(id=10,name="kartik",address="virat nagar")