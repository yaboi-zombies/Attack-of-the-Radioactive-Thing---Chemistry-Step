#Imports
import PySimpleGUI as sg
import os

#Setup
sg.theme('DarkBlue')
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Main
display_layout = [[sg.Text(text="The 'Menno Bot' Bot", font=('bold', 20))], [sg.Button(button_text="Show Instructions", key="show")], [sg.Column([[sg.Text(text="Color Determination", font="bold")], [sg.Image(filename="images\\m.png"), sg.Text(text="M #"), sg.InputText(size=(3, None), enable_events=True, key="m")], [sg.Image(filename="images\\less.png"), sg.Text(text="<#"), sg.InputText(size=(3, None), enable_events=True, key="less")], [sg.Text(text="Color:"), sg.Text(key="color")], [sg.Image(filename="images\\acet_left.png"), sg.Text(text="Left Acetaldehyde # (while using correct color)"), sg.InputText(size=(2, None), enable_events=True, key="acet")], [sg.Text(text="Circle (Color # / M) = ", key="circle_text", visible=False), sg.InputText(size=(2, None), enable_events=True, key="circle", visible=False)]]), sg.Column([[sg.Text(text="Final Chemical", font="bold")], [sg.Checkbox("1,3,5-Tetra-Nitra-Phenol", enable_events=True, key="phenol")], [sg.Checkbox("Octa-Hydro-2, 5-Nitro-3, 4,7-Para-Zocine", enable_events=True, key="zocine")], [sg.Checkbox("3-Methyl-2, 4-Di Nitrobenzene", enable_events=True, key="benzene")], [sg.Checkbox("3,4-Di-Nitroxy-Methyl-Propane", enable_events=True, key="propane")]])], [sg.Button(button_text="Calculate Mixtures", key="mix")], [sg.Column([[sg.Text(font="bold")], [sg.Text(text="Mixture 1", font="bold")], [sg.Text(text="Mixture 2", font="bold")], [sg.Text(text="Mixture 3", font="bold")], [sg.Text(text="Mixture 4", font="bold", key="mix4")]], key="mixtures", visible=False), sg.Column([[sg.Text(text="Ingredients", font="bold")], [sg.Text(font="bold", key="in1")], [sg.Text(font="bold", key="in2")], [sg.Text(font="bold", key="in3")], [sg.Text(font="bold", key="in4")]], key="ingredients", visible=False), sg.Column([[sg.Text(text="Number", font="bold")], [sg.Text(font="bold", key="num1")], [sg.Text(font="bold", key="num2")], [sg.Text(font="bold", key="num3")], [sg.Text(font="bold", key="num4")]], key="numbers", visible=False, element_justification="center")], [sg.Text(text="Instructions:", key="ins1", visible=False)], [sg.Text(text="1) Enter M and <#s to determine circle value. If you get a bad M value you may have to determine the circle value manually using the colors", key="ins2", visible=False)], [sg.Text(text="2) Change to the correct color and enter the left value of the Acetaldehyde diamond from outside the TV station", key="ins3", visible=False)], [sg.Text(text="3) Check the box of the correct final chemical and hit Calculate Mixtures. Follow the mixture instructions to create the bomb's chemical!", key="ins4", visible=False)]]
window = sg.Window('Attack of the Radioactive Thing: Chemistry Step', display_layout)#, location = (-1275, 200))
while True:
    event, values = window.read()
    if event == 'show':
        if window['show'].get_text() == 'Show Instructions':
            window['ins1'].Update(visible = True)
            window['ins2'].Update(visible = True)
            window['ins3'].Update(visible = True)
            window['ins4'].Update(visible = True)
            window['show'].Update('Hide Instructions')
        elif window['show'].get_text() == 'Hide Instructions':
            window['ins1'].Update(visible = False)
            window['ins2'].Update(visible = False)
            window['ins3'].Update(visible = False)
            window['ins4'].Update(visible = False)
            window['show'].Update('Show Instructions')
    if event == 'm' or event == 'less':
        if values['m'] != "" and values['less'] != "":
            if (int(values['less']) - 1) % int(values['m']) == 0:
                circle = int((int(values['less']) - 1) / int(values['m']))
                window['color'].Update("Top")
            elif (int(values['less']) + 1) % int(values['m']) == 0:
                circle = int((int(values['less']) + 1) / int(values['m']))
                window['color'].Update("Middle")
            elif (int(values['less']) + 3) % int(values['m']) == 0:
                circle = int((int(values['less']) + 3) / int(values['m']))
                window['color'].Update("Bottom")
            else:
                window['color'].Update("Double check M and < values")
                if 'circle' in locals():
                    del circle
            matches = 0
            if (int(values['less']) - 1) % int(values['m']) == 0:
                matches += 1
            if (int(values['less']) + 1) % int(values['m']) == 0:
                matches += 1
            if (int(values['less']) + 3) % int(values['m']) == 0:
                matches += 1
            if matches > 1:
                window['color'].Update("Multiple Options, manually determine circle value")
                if 'circle' in locals():
                    del circle
                window['circle_text'].Update(visible = True)
                window['circle'].Update(visible = True)
            else:
                window['circle'].Update(visible = False)
                window['circle_text'].Update(visible = False)
        else:
            window['color'].Update("")
    if event == 'circle':
        circle = int(values['circle'])
    if event == 'acet':
        if values['acet'].isnumeric():
            acet_left = int(values['acet'])
        else:
            if 'acet_left' in locals():
                del acet_left
    if event == 'mix':
        count = 0
        if values['phenol'] == True:
            count += 1
        if values['propane'] == True:
            count += 1
        if values['zocine'] == True:
            count += 1
        if values['benzene'] == True:
            count += 1
        if 'circle' not in locals() or 'acet_left' not in locals() or count != 1:
            if 'circle' not in locals():
                sg.Popup('Circle value has not been determined')
            if 'acet_left' not in locals():
                sg.Popup('Left Acetaldehyde number has not been specified')
            if values['phenol'] == False and values['propane'] == False and values['zocine'] == False and values['benzene'] == False:
                sg.Popup('Please choose a final chemical')
            if count > 1:
                sg.Popup('Multiple final chemicals selected')
        else:
            window['mix'].Update("Re-Calculate Mixtures")
            if acet_left in [1, 4, 5, 6, 7, 9]:
                if acet_left == 1:
                    #TV Station 
                    acetaldehyde = 1 + 8
                    glycerol = 2 + 7
                    methylbenzene = 9 + 3
                    nitrated_glycerol_solution = 6 + 7
                    mixed_acid = 3 + 5
                    #Spawn
                    racing_fuel = 9 + 7
                    insect_repellent = 1 + 2
                    vodka = 9 + 2
                    baking_soda = 4 + 4
                    detergent = 7 + 2
                    food_coloring = 7 + 6
                    #Shop
                    drain_opener = 7 + 6
                    quarters = 6 + 2
                    glass_cleaner = 1 + 6
                    nail_polish_remover = 3 + 4
                    pennies = 9 + 5
                    pool_cleaner = 8 + 8
                    #Campers
                    plant_food = 7 + 9
                    paint = 5 + 3
                    vinegar = 9 + 2
                    ice = 5 + 8
                    bleach = 4 + 6
                    powdered_milk = 1 + 9
                    #Garage
                    hexamine = 5 + 3
                    phenolsulfonic_acid = 6 + 3
                    phenol = 3 + 4
                    aldehyde_sludge = 5 + 7
                    formaldehyde = 2 + 9
                    dinitro = 5 + 7
                    #Beach
                    fat = 3 + 2
                    motor_oil = 6 + 2
                    wheel_cleaner = 7 + 3
                    table_salt = 5 + 2
                if acet_left == 4:
                    #TV Station 
                    acetaldehyde = 4 + 8
                    glycerol = 4 + 9
                    methylbenzene = 1 + 6
                    nitrated_glycerol_solution = 8 + 1
                    mixed_acid = 3 + 2
                    #Spawn
                    racing_fuel = 7 + 7
                    insect_repellent = 6 + 9 
                    vodka = 2 + 9
                    baking_soda = 6 + 7 
                    detergent = 1 + 7
                    food_coloring = 8 + 3
                    #Shop
                    drain_opener = 3 + 5
                    quarters = 1 + 4
                    glass_cleaner = 3 + 7
                    nail_polish_remover = 3 + 2 
                    pennies = 8 + 3
                    pool_cleaner = 9 + 6
                    #Campers
                    plant_food = 2 + 9
                    paint = 2 + 5
                    vinegar = 4 + 1
                    ice = 3 + 7
                    bleach = 5 + 5
                    powdered_milk = 9 + 6
                    #Garage
                    hexamine = 9 + 5
                    phenolsulfonic_acid = 9 + 8
                    phenol = 2 + 6
                    aldehyde_sludge = 2 + 9
                    formaldehyde = 4 + 9
                    dinitro = 9 + 6
                    #Beach
                    fat = 9 + 7
                    motor_oil = 7 + 8 
                    wheel_cleaner = 1 + 5
                    table_salt = 1 + 6
                if acet_left == 5:
                    #TV Station 
                    acetaldehyde = 5 + 4
                    glycerol = 3 + 8
                    methylbenzene = 9 + 2
                    nitrated_glycerol_solution = 5 + 7
                    mixed_acid = 7 + 5
                    #Spawn
                    racing_fuel = 1 + 5 
                    insect_repellent = 7 + 9
                    vodka = 4 + 7
                    baking_soda = 5 + 9 
                    detergent = 9 + 4
                    food_coloring = 9 + 8
                    #Shop
                    drain_opener = 6 + 9
                    quarters = 5 + 7
                    glass_cleaner = 9 + 1 
                    nail_polish_remover = 4 + 5 
                    pennies = 4 + 1
                    pool_cleaner = 9 + 8
                    #Campers
                    plant_food = 7 + 6
                    paint = 4 + 4
                    vinegar = 1 + 9
                    ice = 1 + 2
                    bleach = 3 + 2
                    powdered_milk = 6 + 6
                    #Garage
                    hexamine = 3 + 3
                    phenolsulfonic_acid = 1 + 3
                    phenol = 4 + 3
                    aldehyde_sludge = 8 + 7
                    formaldehyde = 7 + 6
                    dinitro = 6 + 7
                    #Beach
                    fat = 8 + 4
                    motor_oil = 8 + 6
                    wheel_cleaner = 5 + 8
                    table_salt = 8 + 8
                if acet_left == 6:
                    #TV Station 
                    acetaldehyde = 6 + 6
                    glycerol = 8 + 4
                    methylbenzene = 2 + 8
                    nitrated_glycerol_solution = 5 + 8
                    mixed_acid = 8 + 7
                    #Spawn
                    racing_fuel = 7 + 1
                    insect_repellent = 4 + 8
                    vodka = 5 + 1
                    baking_soda = 4 + 6 
                    detergent = 9 + 4
                    food_coloring = 4 + 7
                    #Shop
                    drain_opener = 6 + 5
                    quarters = 5 + 8
                    glass_cleaner = 9 + 9
                    nail_polish_remover = 8 + 3 
                    pennies = 3 + 8
                    pool_cleaner = 9 + 7
                    #Campers
                    plant_food = 8 + 9
                    paint = 7 + 3
                    vinegar = 2 + 4
                    ice = 9 + 4
                    bleach = 3 + 8
                    powdered_milk = 1 + 7
                    #Garage
                    hexamine = 3 + 2
                    phenolsulfonic_acid = 5 + 3
                    phenol = 5 + 8
                    aldehyde_sludge = 8 + 3
                    formaldehyde = 7 + 5
                    dinitro = 2 + 7
                    #Beach
                    fat = 9 + 5
                    motor_oil = 6 + 3
                    wheel_cleaner = 5 + 5
                    table_salt = 5 + 3
                if acet_left == 7:
                    #TV Station 
                    acetaldehyde = 7 + 1
                    glycerol = 7 + 2 
                    methylbenzene = 2 + 6
                    nitrated_glycerol_solution = 5 + 9
                    mixed_acid = 2 + 6
                    #Spawn
                    racing_fuel = 6 + 8 
                    insect_repellent = 5 + 1
                    vodka = 8 + 8
                    baking_soda = 9 + 2 
                    detergent = 3 + 3
                    food_coloring = 5 + 1
                    #Shop
                    drain_opener = 9 + 7
                    quarters = 5 + 7
                    glass_cleaner = 9 + 7
                    nail_polish_remover = 6 + 3
                    pennies = 6 + 1
                    pool_cleaner = 2 + 8
                    #Campers
                    plant_food = 2 + 5
                    paint = 2 + 3
                    vinegar = 4 + 2
                    ice = 6 + 4
                    bleach = 2 + 5
                    powdered_milk = 1 + 6
                    #Garage
                    hexamine = 4 + 4
                    phenolsulfonic_acid = 9 + 4
                    phenol = 5 + 5
                    aldehyde_sludge = 3 + 4
                    formaldehyde = 6 + 8
                    dinitro = 3 + 4
                    #Beach
                    fat = 3 + 7
                    motor_oil = 2 + 7 
                    wheel_cleaner = 9 + 4
                    table_salt = 7 + 8
                if acet_left == 9:
                    #TV Station 
                    acetaldehyde = 9 + 3
                    glycerol = 9 + 9
                    methylbenzene = 4 + 8
                    nitrated_glycerol_solution = 2 + 8
                    mixed_acid = 9 + 7
                    #Spawn
                    racing_fuel = 8 + 3
                    insect_repellent = 3 + 4
                    vodka = 7 + 9
                    baking_soda = 2 + 4 
                    detergent = 7 + 9
                    food_coloring = 8 + 4
                    #Shop
                    drain_opener = 5 + 2
                    quarters = 6 + 3
                    glass_cleaner = 5 + 3
                    nail_polish_remover = 9 + 8
                    pennies = 7 + 7
                    pool_cleaner = 9 + 7
                    #Campers
                    plant_food = 7 + 6
                    paint = 7 + 8
                    vinegar = 2 + 9
                    ice = 1 + 1
                    bleach = 1 + 5
                    powdered_milk = 1 + 1
                    #Garage
                    hexamine = 3 + 8
                    phenolsulfonic_acid = 1 + 9
                    phenol = 9 + 2
                    aldehyde_sludge = 1 + 7
                    formaldehyde = 9 + 4
                    dinitro = 1 + 8
                    #Beach
                    fat = 3 + 9
                    motor_oil = 5 + 4 
                    wheel_cleaner = 4 + 9
                    table_salt = 3 + 5
                if values['phenol'] == True:
                    window['mixtures'].Update(visible = True)
                    window['ingredients'].Update(visible = True)
                    window['numbers'].Update(visible = True)
                    window['in1'].Update("Motor Oil (Next to Bomb) + Wheel Cleaner (Shop) + Insect Repellent (Spawn by Board)")
                    window['in2'].Update("Phenol + Drain Opener (RV Bathroom Toilet)")
                    window['in3'].Update("Phenol Sulfonic Acid + Detergent (Shop)")
                    window['mix4'].Update(visible = False)
                    window['num1'].Update(motor_oil + wheel_cleaner + insect_repellent - circle)
                    window['num2'].Update(phenol + drain_opener - circle)
                    window['num3'].Update(phenolsulfonic_acid + detergent - circle)
                if values['propane'] == True:
                    window['mixtures'].Update(visible = True)
                    window['ingredients'].Update(visible = True)
                    window['numbers'].Update(visible = True)
                    window['in1'].Update("Racing Fuel (Garage Exit) + Quarters (Payphone)")
                    window['in2'].Update("Vodka (Shop) + Pennies (Register)")
                    window['in3'].Update("Formaldehyde + Acetaldehyde + Detergent (Shop)")
                    window['in4'].Update("Aldehyde Sludge + Nail Polish Remover (Hotel Desk)")
                    window['num1'].Update(racing_fuel + quarters - circle)
                    window['num2'].Update(vodka + pennies - circle)
                    window['num3'].Update(formaldehyde + acetaldehyde + detergent - circle)
                    window['num4'].Update(aldehyde_sludge + nail_polish_remover - circle)           
                if values['zocine'] == True:
                    window['mixtures'].Update(visible = True)
                    window['ingredients'].Update(visible = True)
                    window['numbers'].Update(visible = True)
                    window['in1'].Update("Racing Fuel (Right of Garage Door) + Quarters (Payphone)")
                    window['in2'].Update("Formaldehyde + Glass Cleaner (Shop)")
                    window['in3'].Update("Hexamine + Vinegar (Shop Backroom) + Detergent (Shop) + Plant Food (Quickies)")
                    window['mix4'].Update(visible = False)    
                    window['num1'].Update(racing_fuel + quarters - circle)
                    window['num2'].Update(formaldehyde + glass_cleaner - circle)
                    window['num3'].Update(hexamine + vinegar + detergent + plant_food - circle)
                if values['benzene'] == True:
                    window['mixtures'].Update(visible = True)
                    window['ingredients'].Update(visible = True)
                    window['numbers'].Update(visible = True)
                    window['in1'].Update("Paint (Racing Stripes) + Drain Opener (RV Bathrooms on Toilet) + Detergent (Shop)")
                    window['in2'].Update("Methylbenzene + Vinegar (Shop Backroom) + Detergent (Shop) + Baking Soda (Shop)")
                    window['in3'].Update("Dinitro + Racing Fuel (Garage Door)")
                    window['mix4'].Update(visible = False)
                    window['num1'].Update(paint + drain_opener + detergent - circle)
                    window['num2'].Update(methylbenzene + vinegar + detergent + baking_soda - circle)
                    window['num3'].Update(dinitro + racing_fuel - circle)
            else:
                sg.Popup('Incorrect value for Acetaldehyde Left #')
    if event == sg.WIN_CLOSED:
        break
window.close()