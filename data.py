import os
class Create:
    def __init__(self,name,voter,aadhar):
        self.name = name
        self.voter = voter
        self.aadhar = aadhar
    def create_dict(self):
        return (
            {
                "name":self.name,
                 "voter":self.voter,
                 "adh":self.aadhar,
            }
        )
base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir,"images")
names= [file.split('.')[0] for _,_,files in os.walk(image_dir) for file in files]
arr = []
for name in range(len(names)):
    names[name] = Create(names[name],987456123+name,123456+name)
    arr.append(names[name].create_dict())
    
    
            



