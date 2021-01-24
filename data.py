import os ,itertools
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
v_id_counting = itertools.count(start=9874561230)
a_id_coutning = itertools.count(start= 987456123010)
arr = [Create(file.split('.')[0],v_id_counting,a_id_counting).create_dict() for _,_,files in os.walk(image_dir) for file in files]

    
    
            



