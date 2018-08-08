class clock:
    def __init__(self, hour,minute):
        self.hour=hour
        self.minute=minute
    
    def representation(self):
        total=self.hour*60 + self.minute
        minuto=total%60
        total=total-minuto
        hora=int(total/60)%24 
        return str(hora).zfill(2),str(minuto).zfill(2)
    
    def set_minute(self,minute):
        self.minute+=minute

if __name__ == "__main__":
    print("ingrese la hora")
    hour=int(input())
    print("ingrese los minutos ")
    minute=int(input())
    my_clock=clock(hour,minute)
    h=my_clock.representation()[0]
    m=my_clock.representation()[1]
    print("La hora es:"+h+":"+m)
    while(1):
        print("si desea cambiar la hora indique los minutos")
        minutes=int(input())
        my_clock.set_minute(minutes)
        h=my_clock.representation()[0]
        m=my_clock.representation()[1]
        print("La nueva hora es:"+h+":"+m)
        
       
    