"""class BmiCalculator:
    def __init__(self):
        self.height=0
        self.weight=0
       # self.bmi=0.00
        
    def bmi(self,height,weight):
        self.height=height
        self.weight=weight
        bmi=float(self.weight/(self.height)**2)

        return bmi

    def bmi_description(self,bmi):
        
        print("bmi from function",bmi)
        if bmi < 18.00:
            return "UnderWeight"
        elif bmi>=18.5 and bmi<=24.9:
            return "Normal Weight"
        elif bmi>=25 and bmi<=29.9:
            return "Over Weight "
        else:
            return "Obsesity- BMI of 30 or greater"""



class BmiCalculator:
    def bmi(self,height,weight):
        height_meter=int(height)/100
        return round(float(weight)/(height_meter**2),2)

    def bmi_description(self,bmi):
        bmi=float(bmi)
        if bmi < 18.00:
            return "UnderWeight"
        elif bmi>=18.5 and bmi<=24.9:
            return "Normal Weight"
        elif bmi>=25 and bmi<=29.9:
            return "Over Weight "
        else:
            return "Obese"



                   
    