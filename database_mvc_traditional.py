'''this is a data base which is traditionally used. this is manuall and unstructured data. for new check jason file'''
class Database():
    def __init__(self) :

        self.data = {
            "AC101" : {'paid' : 100 , 'due' : 20},
            "AC102" : {'paid' : 50 , 'due' : 60}
        }
    
    def balance(self , acc_id):
        acc = self.data.get(acc_id)

        if acc :
            return int(acc['paid']) - int(acc ['due'])
        else:
            None


