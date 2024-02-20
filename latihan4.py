class shark:
    def __init__(self,name):
        self.name=name
    def swim(self):
        print(self.name+" is swimming. ")
    def be_awezome(self):
        print(self.name+" is being awezome. ")
        
def main():
    sammy=shark("Sammy")
    sammy.swim()
    sammy.be_awezome()

if __name__=="__main__":
    main()