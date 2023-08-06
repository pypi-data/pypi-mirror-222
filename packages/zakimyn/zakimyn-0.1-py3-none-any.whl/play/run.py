class Select_Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def setting_weapon(self, selec_number:int):
        if selec_number == 1:
            weapon = "도끼"
        elif selec_number == 2:
            weapon = "총"
        else:
            weapon = "기본 무기 손"
        print(weapon,"을(를) 골랐음~")
    
    def print(self):
        print("이름: ",self.name, "나이",self.age)
