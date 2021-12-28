# PullUpBarSizing
Calculate size of pull up bar post based on desired material assuming supports are fixed into the ground.

# Overview
This PYTHON program is used to figure out the minimum cross-sectional dimension needed based on 
1) Weight Capacity of Bar
2) Height of Bar
3) Number of supporting posts
4) Material (wood, metal, composite)

These cross-sectional dimensions are calcualted from using the more conservative value from general Stress Equations from Properties of Materials.

# Background of Eq's Used
>We could use the stress equation that estimates the noraml stress due to bending:

![beam_drawing](https://github.com/SceneDuGreene/PullUpBarSizing/blob/main/bending_diagram.PNG)

<img src="https://latex.codecogs.com/svg.image?\sigma_{normal}&space;=\frac{Mc}{I}" title="\sigma_{normal} =\frac{Mc}{I}" width="150" height="150"/>
In the worst case scenario, the entire load will contribute fully to the bending of the supporting members. This is likely to happen if the user is expecting to do gymnatics movements such as [Giants](https://en.wikipedia.org/wiki/Giant_(gymnastics)) (when a gymnast rotates 360 degrees around an axis while in a fully extended position)

####
 
> We could also use the equation that estimates deflection, y, based on the Geometry, I, as well as Elastic Modulus, E, of the material used: 

<img src="https://latex.codecogs.com/svg.image?y=\frac{Pl^{3}}{3EI} " title="deflection based on desired deflection" width="100" height="100"/>

This equation allows us to include information about the material properties in addition information about the cross-section of the beam used.




