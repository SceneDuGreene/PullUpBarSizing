# PullUpBarSizing
Calculate cross-sectional side diemsneion of pull up bar support post based on material specification. Supports are assumed to be fixed into the ground and square in cross-section.

# Overview
This PYTHON program is used to figure out the minimum cross-sectional side dimension needed based on 
1) Weight Capacity of Bar
2) Height of Bar
3) Number of supporting posts
4) Material (wood, metal, composite)

These cross-sectional dimensions are calcualted from using the more conservative value from general Stress Equations from Properties of Materials.

# Background of Equations Used

![beam_drawing](https://github.com/SceneDuGreene/PullUpBarSizing/blob/main/pullup_supports_FBDs.png)

> We could use the stress equation that estimates the normal stress due to bending as seen in Case B:
<img src="https://latex.codecogs.com/svg.image?\sigma_{normal}&space;=\frac{Mc}{I}" title="normal stress due to bending" width="150" height="150"/>
In the worst case scenario (B1), the entire load will contribute fully to the bending of the supporting members. This is likely to happen if the user is expecting to do gymnatics movements such as Giants (when a gymnast rotates 360 degrees around an axis while in a fully extended position).

####
Here we can calculate the side, s of the beam to be: <img src="https://latex.codecogs.com/svg.image?s&space;=&space;\sqrt[3]{\frac{6Pl}{\sigma&space;_{yield}*NumberOfPosts}}" title="SOLVED normal stress due to bending" />

####
 
> We could also use the equation that estimates deflection, y, based on the Geometry, I, as well as Elastic Modulus, E, of the material used: 

<img src="https://latex.codecogs.com/svg.image?y=\frac{Pl^{3}}{3EI} " title="deflection based on desired deflection" width="100" height="100"/>

This equation allows us to include information about the material properties in addition information about the cross-section of the beam used. Generally, we want to limit deflection to less than one half of the cross-sectional side dimension.

Here we can calculate the side, s of the beam to be:
<img src="https://latex.codecogs.com/svg.image?s&space;=&space;\sqrt[5]{\frac{8Pl^{3}}{E*NumberOfPosts}}" title="SOLVED deflection based on desired deflection" />

## Getting Started
Start by figuring out the 4 pieces of information that you will need to assign to these variables.
- p = 1.5x Bodyweight (lbs)
- l = Height of Bar (inches)
- number_of_posts = number of posts
- materialChoice = Wood, Steel, Aluminum, Cast Iron

Once the variables **p**, **l**, and **number_of_posts**  have been assigned, run the program. By default, p is rated for a person weighing 200 lbs (with a safety factor), l is set to 84 inches (7 ft), and number_of_posts is set to be 2. Remember that the program is looking for the height of the pull up bar to be in *inches*.

The program will then ask you to select your choice of material and will output the minimum reccomended side dimensions.

***Take note that these supports are assumed to be fixed into the ground and that support members are assumed to be square in cross-section as indicated in the drawing above.***

## Input
- p = 300 # 1.5x Bodyweight (lbs)... rated for person= 200lbs
- l = 84 # height of bar (inches)
- number_of_posts = 2 # number of posts supporting load

## Interactive User Input
1) Wood , Min. Strength: 0.3 ksi , Min Elastic Modulus: 1.6 Mpsi 
2) Steel , Min. Strength: 30 ksi , Min Elastic Modulus: 29.0 Mpsi 
3) Aluminum , Min. Strength: 37 ksi , Min Elastic Modulus: 10 Mpsi 
4) Cast Iron , Min. Strength: 18.2 ksi , Min Elastic Modulus: 14.5 Mpsi 

 Material Choice -->  ***USER INPUT 1,2,3 OR 4 HERE***

## Output
**Based on Strength, Side dimension of wood needs to be 6.316359597656378 inches
Based on Elasticity (point-load deflection), Side dimension of wood needs to be 3.3851648625016493 inches**

## Interpretation of Output
In this example, the side dimensions for wood were calculated to be 6.32in (Bending Stress Theory) and 3.38in (Point-Load Deflection Theory). I would reccomend using the larger of the values, 2 wooden 6.32in x 6.32in x 84in posts. In this case, the bending stress equation gave us the more conservative value. 
