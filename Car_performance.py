import math
def main():
    air_density = 1.225
    gravity = 9.81
    average_values = {"Mass": 1600 ,"Engine Power":120000,"Wheel Radius":0.32,"Drag Coefficient":0.25,"Frontal Area":2.2,"Drivetrain Efficiency":0.85}
    
    def get_mass():
        while True:
            mass = input('Mass in Kgs...')
            if not mass.isdigit():
                continue
            mass = int(mass)
            if 360 > mass and mass > 0:
                print('Error... Mass is too small...')
                continue
            elif mass > 5100:
                print('Error... Mass is too large...')
                continue
            elif mass <= 0:
                print('Error... Mass cannot be less than 0...')
                continue
            else:
                average_values['Mass'] = mass
                break

    def get_power():
        while True:
            engine_power = input('Engine Power in kW...')
            if not engine_power.isdigit():
                continue
            engine_power = int(engine_power) * 1000
            if 50000 > engine_power and engine_power > 0:
                print('Error... Power value is too small...')
                continue
            elif engine_power > 1500000:
                print('Error... Power value is too large...')
                continue
            elif engine_power <= 0:
                print('Error... Power cannot be less than 0...')
                continue
            else:
                average_values['Engine Power'] = engine_power
                break
        
    def get_wheel():
        while True:
            wheel_radius = input('Wheel radius in inches...')
            if not wheel_radius.isdigit():
                continue
            wheel_radius = round(wheel_radius,1)*0.0254
            if wheel_radius > 0 and wheel_radius < 0.28:
                print('Error... Wheel radius is too small...')
                continue
            elif wheel_radius > 0.45:
                print('Error... Wheel radius is too large...')
                continue
            elif wheel_radius < 0:
                print('Error... Wheel radius cannot be less than 0...')
                continue
            else:
                average_values['Wheel Radius'] = wheel_radius
                break
    
    def get_drag():
        while True:
            drag = input('Drag Coefficient...')
            if not drag.isdigit():
                continue
            drag = round(drag,2)
            if drag < 0.19 and drag > 0:
                print('Error... Drag coefficient is too small...')
                continue
            elif drag > 0.5:
                print('Error... Drag coefficient is too large')
                continue
            elif drag <= 0:
                print('Error... Drag coefficient cannot be less than 0...')
                continue
            else:
                average_values['Drag Coefficient'] = drag
                break
    
    def get_area():
        while True:
            area = input('Frontal area in m²...')
            if not area.isdigit():
                continue
            area = int(area)
            if area < 1.5 and area > 0:
                print('Error... Area is too small...')  
                continue
            elif area > 4:
                print('Error... Area is too big...')
                continue
            elif area <= 0:
                print('Error... Area cannot be less than 0...')
                continue
            else:
                average_values['Frontal Area'] = area
                break

    def get_efficiency():
        while True:
            efficiency = input('Drivetrain efficiency as a percentage...')
            if not efficiency.isdigit():
                continue
            efficiency = int(efficiency)/100
            if efficiency < 0.6 and efficiency > 0:
                print('Error... Drivetrain efficiency is too small...')
                continue
            elif efficiency > 1:
                print('Error... Drivetrain efficiency is too large...')
                continue
            elif efficiency < 0:
                print('Drivetrain efficiency cannot be less than 0...')
                continue
            else:
                average_values['Drivetrain Efficiency'] = efficiency
                break
    def calculate_time:
        
    def menu_display():
            print(f'------------------------\n|{'Part':<20}|{'Value':<4}|\n--------------------|----|')
            for part, value in average_values.items:
                print(f'|{part:<20}|{value:<4}|')
            print('------------------------')
            while True:
                menu_choice = input('Would you like to...\n(1) calculate 0-60mph?\n(2) change the mass?\n(3) change the engine power?\n(4) change the wheel radius?\n(5) change the drag coefficient\n(6) change the area?\n(7) change the drivetrain efficiency?\n(8) end the program?\n\nChoose an option...')    
                if not menu_choice.isdigit():
                    continue
                menu_choice = int(menu_choice)
                if menu_choice == 1:
                    calculate_time()
                elif menu_choice == 2:
                    get_mass()
                elif menu_choice == 3:
                    get_power()
                elif menu_choice == 4:
                    get_wheel()
                elif menu_choice == 5:
                    get_drag()
                elif menu_choice == 6:
                    get_area()
                elif menu_choice == 7:
                    get_efficiency()
                elif menu_choice == 8:
                    exit()

main()    