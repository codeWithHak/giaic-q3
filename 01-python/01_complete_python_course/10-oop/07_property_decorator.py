class Grade:
    
    def __init__(self,phy,che,maths):
        self.phy = phy
        self.che = che
        self.maths = maths
        
        # setting percentage in an attribute
        self.percentage =  str((self.phy + self.che + self.maths) / 3) + "%"

    
    # setting percentage by a method
    @property
    def get_percentage(self):
        return f"{(self.phy + self.che + self.maths) / 3:.2f}%"
    
std1 = Grade(40,50,60)
print (std1.percentage) # 50%

# changed the valye of of an attribute
std1.che = 90

# but percentage remained same no changes reflected , That's an issue
print (std1.percentage) # still 0%

print(std1.get_percentage)