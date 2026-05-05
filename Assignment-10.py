from tempurature.celcius import c_to_f , c_to_k
from tempurature.farhenit import f_to_c
from tempurature.kelvin import k_to_c


print("Tempurature conversion options")
print("1. Celcius to farhenit")
print("2. Farhenit to Celcius")
print("3. Celcius to Kelvin")
    
choice = int(input("Enter your choice (1/2/3) : "))
    
if choice == 1 :
    celcius = float(input("Enter the tempurature in celcius : "))
    print(f"{celcius}C = {c_to_f(celcius)}F")
        
elif choice == 2 :
    farhenit = float(input("Enter the tempurature in farhenit : "))
    print(f"{farhenit}F = {f_to_c(farhenit)}C")    
        
elif choice == 3 :
    kelvin = float(input("Enter the tempurature in celcius : "))
    print(f"{kelvin}C = {c_to_k(kelvin)}K")   
            
else:
    print("Invalid Option")        