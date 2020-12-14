import math
import pandas as pd
# from google.colab import drive
# Creating a dataframe for each Excel sheet
#drive.mount('/content/drive')

def beamdesign():

    df = pd.ExcelFile('PythonProjectTables.xlsx')
    df1 = pd.read_excel(df, 'TableA2')
    df2 = pd.read_excel(df, 'TableA5')
    df3 = pd.read_excel(df, 'TableA7')
    df4 = pd.read_excel(df, 'TableA8')
    df5 = pd.read_excel(df, 'TableA9')
    df6 = pd.read_excel(df, 'TableA10')
    df7 = pd.read_excel(df, 'TableA11')

    # Loads needed to be supported
    print("Enter compressive strength and yield strength in psi (do not include commas)")
    cstrength1 = float(input("Enter f'c:"))
    yieldstrength1 = float(input("Enter fy:"))
    print("Enter loads in kips and lengths in feet")
    pointDL  = float(input("Enter point dead load:"))
    pointLL  = float(input("Enter point live load:"))
    left = float(input("Enter distance from left end of the beam to the point load:"))
    length = float(input("Enter beam length:"))
    right = length - left
    distDL  = float(input("Enter distributed dead load:"))
    distLL  = float(input("Enter distributed live load:"))
    deadfactor = float(input("Enter the dead load combination factor:"))
    livefactor = float(input("Enter the live load combination factor:"))

    # Choosing which table to use according to user input
    if (cstrength1 == 3000) & (yieldstrength1 == 40000):
      table = df3
    elif (cstrength1 == 3000) & (yieldstrength1 == 60000):
      table = df4
    elif (cstrength1 == 4000) & (yieldstrength1 == 40000):
      table = df5
    elif (cstrength1 == 4000) & (yieldstrength1 == 60000):
      table = df6
    else:
      table = df7

    # Calculating ultimate moment
    ultpointload = (deadfactor * pointDL) + (livefactor * pointLL)
    ultdistload = (deadfactor * distDL) + (livefactor * distLL)
    ultmoment = ((ultpointload * left * right)/length) + ((ultdistload * (length ** 2))/8)

    # Creating initial dimensions for the beam
    cstrength = df2["fc"]
    yieldstrength = df2["fy"]
    kbar = df2["k"]
    min = df2["min"]

    rows = len(df2)

    for i in range(0, rows):
      if (yieldstrength1 == yieldstrength[i]) & (cstrength1 == cstrength[i]):
        kbar1 = kbar[i]
        min1 = min[i]

    effdepth = ((24 * ultmoment) / (0.9 * kbar1)) ** (1/3)
    effdepth = (math.ceil(effdepth/2)) * 2 #rounds to largest whole, even number
    width = str(effdepth/2)
    height = str(effdepth + 3)
    effdepth1 = str(effdepth)

    # Recalulating ultimate moment with self weight of the beam
    selfweight = (width * height / 144) * 0.150
    selfmoment = (deadfactor * selfweight * length**2) / 8
    ultmoment1 = ultmoment + selfmoment

    # Finding area required  for steel bars
    kbar2 = (ultmoment1 * 12) / (0.9 * width * effdepth**2)
    k = table["k"]
    rho1 = table["R"]

    n = 0
    while kbar2 > k[n]:
      n = n + 1

    rho = rho1[n]
    areabar = rho * width * effdepth

    # Finding minimum area required for bars
    areamin = min1 * width * effdepth

    if areamin < areabar:
      areaneeded = areabar
    else:
      areaneeded = areamin

    index = 0
    lists = df1.values.tolist()
    # Changing table into one long list without the first column
    giantlist = []
    for sublist in lists:
      for item in range(len(sublist)):
        if item != 0:
          giantlist.append(sublist[item])

    # Finds smallest area of steel that is larger than required
    while areaneeded > giantlist[index]:
      index = index + 1
    # Determines number of bars needed (by which row in the table the value is)
    bararea = giantlist[index]
    numberofbars = str(math.ceil(index/9))
    # Determines size of the bar by what column the selected value is in
    while index > 9:
      index = index - 9
    size = str(index + 3)

    print("Use a width of " + width + " feet, height of " + height + " feet, and effective depth of " +effdepth1 + " feet with " + numberofbars + " #" + size + " bars")
