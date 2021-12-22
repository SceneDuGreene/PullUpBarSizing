# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:13:26 2021

@author: mike3

Pull Bar Program
Calculate cross section (inches) of beam based on material selection (Yield Tensile Strength, Elastic Modulus) and height (inches) of bar
"""
import numpy as np

def main():

    p = 300 # 1.5x Bodyweight (lbs)... rated for person= 200lbs
    l = 84 # height of bar (inches)
    number_of_posts = 2 # number of posts supporting load
    choices = np.array(['wood','steel','aluminum','cast iron'])
    materialList = np.array([0.3 , 1.6, 30.0, 29.0, 37.0, 10.0, 18.2, 14.5])
    materialChoice = input("Choose your desired material: \n\n"
                           "(1) Wood , Min. Strength: 0.3 ksi , Min Elastic Modulus: 1.6 Mpsi \n"
                           "(2) Steel , Min. Strength: 30 ksi , Min Elastic Modulus: 29.0 Mpsi \n"
                           "(3) Aluminum , Min. Strength: 37 ksi , Min Elastic Modulus: 10 Mpsi \n"
                           "(4) Cast Iron , Min. Strength: 18.2 ksi , Min Elastic Modulus: 14.5 Mpsi \n"
                           "\n Material Choice -->  ")
    
    if str(materialChoice) == 'wood' or int(materialChoice) == 1:
        matStr = materialList[0]; elas = materialList[1]
    elif str(materialChoice) == 'steel' or int(materialChoice) == 2:
        matStr = materialList[2]; elas = materialList[3]
    elif str(materialChoice) == 'aluminum' or int(materialChoice) == 3:    
        matStr = materialList[4]; elas = materialList[5]
    elif str(materialChoice) == 'castiron' or int(materialChoice) == 4:        
        matStr = materialList[6]; elas = materialList[7]
    
    print("\nBased on Strength, Side dimension of {0} needs to be {1} inches".format(choices[int(materialChoice)-1],bending_analysis_1(p,l,matStr*1000,number_of_posts)))
    print("Based on Elasticity (point-load deflection), Side dimension of {0} needs to be {1} inches".format(choices[int(materialChoice)-1],bending_analysis_2(p,l,elas*1000000,number_of_posts)))


def bending_analysis_1(p,l,matStr,number_of_posts):
    side1 = ((6*(p/number_of_posts)*l)/matStr)**(1/float(3))
    round(side1,2)
    return side1

def bending_analysis_2(p,l,elas,number_of_posts):
    side2 = ((8*(p/number_of_posts)*(l**3))/elas)**(1/float(5))
    round(side2,2)
    return side2

if __name__ == '__main__':
    main()
    