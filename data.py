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
obj1 = Create("kaviya",987654321987,9632581470)
obj2 = Create("ramya",876543219876,7412583690)
obj3 = Create("jeni",765432198765,8523691470)

arr = [obj1.create_dict(),obj2.create_dict(),obj3.create_dict()]
