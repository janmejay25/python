def dic_print(**kwargs):
    
    for key,value in kwargs.items():
        
        print(f"{key} : {value}")
dic_print(name='john',age=25,city='newyork')
