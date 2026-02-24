import math
def main():
    air_density = 1.225
    gravity = 9.81
    rolling_resistance_coefficient = 0.015
    target_speed = 26.8
    time_step = 0.01
    average_values = {'Mass(Kg)': 1600 ,'Engine Power(W)':120000,"Drag Coefficient":0.25,"Frontal Area(m²)":2.2,"Drivetrain Efficiency":0.85}
    
    def get_mass():
        while True:
            mass = input('\nMass in Kgs...')
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
            engine_power = input('\nEngine Power in kW...')
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
    
    def get_drag():
        while True:
            drag = input('\nDrag Coefficient...')
            if not drag.isdigit():
                continue
            drag = round(float(drag),2)
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
            area = input('\nFrontal area in m²...')
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
            efficiency = input('\nDrivetrain efficiency as a percentage...')
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

    def calculate_time():
        velocity = 0.00000001 
        time = 0
        while velocity < target_speed:
            engine_force = (average_values['Engine Power(W)'] * average_values["Drivetrain Efficiency"]) / velocity
            drag_force = 0.5 * air_density * average_values["Drag Coefficient"] * average_values["Frontal Area(m²)"] * velocity**2
            rolling_force = rolling_resistance_coefficient * average_values['Mass(Kg)'] * gravity
            net_force = engine_force - drag_force - rolling_force
            acceleration = net_force / average_values['Mass(Kg)']
            velocity += acceleration * time_step
            time += time_step
        print(f'\nThis car will travel 0-60mph in {round(time,2)} seconds...')

    def table():
        print(f" _____________________________\n|{'Aspect':<22}|{'Value':<6}|\n|----------------------|------|")
        for part, value in average_values.items():
            print(f'|{part:<22}|{value:<6}|')
        print(' -----------------------------')

    def menu_display():
            print(f" _____________________________\n|{'Aspect':<22}|{'Value':<6}|\n|----------------------|------|")
            for part, value in average_values.items():
                print(f'|{part:<22}|{value:<6}|')
            print(' -----------------------------')
            while True:
                menu_choice = input('\nWould you like to...\n\n(1) calculate 0-60mph?\n(2) change the mass?\n(3) change the engine power?\n(4) change the drag coefficient\n(5) change the area?\n(6) change the drivetrain efficiency?\n(7) display table of values?\n(8) end the program?\n\nChoose an option...')    
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
                    get_drag()
                elif menu_choice == 5:
                    get_area()
                elif menu_choice == 6:
                    get_efficiency()
                elif menu_choice == 7:
                    table()
                elif menu_choice == 8:
                    exit()
    menu_display()
main()    