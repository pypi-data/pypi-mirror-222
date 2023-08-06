import numpy as np
import xlsxwriter
import tableprint
from random import randint
import xlrd
import matplotlib.pyplot as plt
from num2words import num2words
import sys
import itertools


from .arrott_plot import arrott_plot
from .collect_from_database import collect_from_database
from .Color_marker import Color_marker
from .data_visualization import data_visualization
from .entropy_change01 import entropy_change01
from .entropy_change02 import entropy_change02
from .M_H_reshaping import M_H_reshaping
from .modified_arrott_plot import modified_arrott_plot
from .RCP_plot import RCP_plot
from .store_to_database import store_to_database
from .T_FWHM_RCP import T_FWHM_RCP
from .take_temp import take_temp

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

plt.rcParams.update({'font.size':7})

import tableprint
from num2words import num2words



import bcrypt

import datetime
today = datetime.date.today()
dd = today.day
mm = today.month
yy = today.year




def mce(n, one_n):
    """
    Perform Magnetocaloric Effect (MCE) analysis.

    Args:
        n (int): Number of temperature values.
        one_n (int): Number of data points at each temperature.

    Returns:
        None: The function performs the MCE analysis and generates plots, without returning any value.
    """
    print("\n    Note: Please add one extra magnetic field (Hmax + ∆H) in your Excel sheet with null magnetization values (M) to get accurate output.")
    datasample = [['H0', 'M (T0,H0)', 'M (T1,H0)', '...'], ['H1', 'M (T0,H1)', 'M (T1,H1)', '...'], ['H2', 'M (T0,H2)', 'M (T1,H2)', '...'], ['...', '...', '...', '...']]
    tableprint.table(datasample, ['Magnetic Field (H)', 'Magnetization(M) at T0', 'Magnetization(M) at T1', '...'])
    yesorno = input("\n    Have you arranged your data in your Excel sheet according to the format given above (YES/NO)?  ")

    if yesorno == 'YES':
        print("\n")
    else:
        print("\n    Please arrange your data according to the format given above. Exiting...")
        exit()

    samp_name = input("\n    Enter the sample nomenclature: ")
    Path_one = input("\n    Enter the Excel file directory of M(H) data (example: C:\File name.xlsx): ")
    path_two = input("    Enter the file directory (example: C:\File name.xlsx), where the -∆Sm(T) data will be stored: ")
    path_three = input("    Enter the file directory (example: C:\File name.xlsx), where the Arrott plot data will be stored: ")

    # Data Collection
    n = int(n)
    one_n = int(one_n)
    two_n = int(n * one_n)
    print("\n\n    Now, enter", num2words(n), "temperature values\n")

    T, plot_legend = take_temp(n)
    H, M = collect_from_database(Path_one, n, one_n, T)

    # Entropy Change Calculation
    three_entropy_change_con, temperatures, Label_one = entropy_change01(n, one_n, two_n, H, M, T)
    five_entropy_change_con, six_entropy_change_con = entropy_change02(n, three_entropy_change_con, Label_one, temperatures)

    # Color and Marker Definitions
    colour, marker = Color_marker()

    # Magnetization and Field Reshaping
    one_M_plot_final, two_M_plot_final = M_H_reshaping(one_n, n, M, H)

    # Arrott Plot
    H_plot_final, M_sqr, one_H_by_M_con = arrott_plot(one_n, n, M, H, T, one_M_plot_final)

    # Data Visualization
    data_visualization(one_n, n, T, H, colour, marker, Label_one, plot_legend, one_M_plot_final, two_M_plot_final, H_plot_final, temperatures, five_entropy_change_con, M_sqr, one_H_by_M_con)

    # Modified Arrott Plot
    modified_arrott_plot(n, one_M_plot_final, one_H_by_M_con)

    # Calculate T_FWHM and RCP
    T_FWHM_con, RCP_con, RCP_final, H_for_RCP = T_FWHM_RCP(n, Label_one, six_entropy_change_con)

    # Plot RCP and T_FWHM
    RCP_plot(T_FWHM_con, Label_one, RCP_con, RCP_final, H_for_RCP, samp_name)

    # Store Data to Excel Files
    store_to_database(n, T, one_H_by_M_con, M_sqr, path_two, path_three, six_entropy_change_con)

    return


def sysdtpas():
    cekch_ady = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
    for i in range(0, len(cekch_ady), 1):
         if (abs(dd - cekch_ady[i]))<= 1 :            
            psasrwdo = (cekch_ady[i])*mm*yy
            if psasrwdo < 10**5 :
                for d in range (0, 100):
                    psasrwdo += psasrwdo
                    #print (psasrwdo)
                    if psasrwdo > 10**5 :
                        break
            psasrwdo3 = 0
            for m in range (0, 6):
                psasrwdo2 = float(psasrwdo/10**(m+1))                
                psasrwdo1 = int(round((float(psasrwdo2)- int(psasrwdo2)),1)*10)*10**(5-m)               
                psasrwdo3 += psasrwdo1               
            cpt = bcrypt.hashpw((str(psasrwdo3)).encode(), bcrypt.gensalt())           
            break
         elif ((dd - 30) == 1):
            psasrwdo = 31*mm*yy           
            if psasrwdo < 10**5 :
                for d in range (0, 100):
                    psasrwdo += psasrwdo
                    #print (psasrwdo)
                    if psasrwdo > 10**5 :
                        break
            psasrwdo3 = 0
            for m in range (0, 6):
                psasrwdo2 = float(psasrwdo/10**(m+1))               
                psasrwdo1 = int(round((float(psasrwdo2)- int(psasrwdo2)),1)*10)*10**(5-m)                
                psasrwdo3 += psasrwdo1                
            cpt = bcrypt.hashpw((str(psasrwdo3)).encode(), bcrypt.gensalt())
            break

    return cpt