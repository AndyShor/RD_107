[![License: GPL](https://img.shields.io/badge/License-GPL-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

# RD107 - legendary rocket engine
This repository contains model case for CFD simulation of [RD107](https://en.wikipedia.org/wiki/RD-107) rocket engine using free and open source CFD package OpenFOAM.
Together with the model case there are some auxiliary materials that are used to define case input such as scripts generating the nozzle geometry,
scripts calculating combustion products properties required for the model.
I wrote a [longread article](https://andrey-shornikov.medium.com/taming-of-the-fire-tribute-to-the-unsung-hero-of-space-exploration-96ccb9964b00) describing technical side of this simulation and a bit of history - why I am so excited specifically about RD107.
I also wrote another [short(-er) article](https://medium.com/@andrey-shornikov/become-a-rocket-scientist-for-0-99-with-a-capstone-project-100bf3944c02) about my experience of running this case on AWS trying to implement best cloud CFD practices (spot instances, persistent storage of intermediate results etc).

Here is an example of the model results. This is a temperature distribution in the RD107 exhaust plume in the first 25 ms after ignition at the sea level.
Enjoy propagating shock waves, colliding shock waves ([Mach diamonds](https://en.wikipedia.org/wiki/Shock_diamond)) and imagine the roar it creates.

Overexpanded flow and Mach diamonds for the flow whe starting at sea level
![flow](/figures/T_ambient_p=100kPa.gif)

Almost matched flow in the mid-air where ambient pressure is a third of sea level pressure
![flow](/figures/T_ambient_p=30kPa.gif)

# Repo structure
This repository has the following structure

* data - thermodynamic data of jet engine combustion products, retrieved form [JANAF](https://janaf.nist.gov/) database and cleaned
* figures - containes images with the run results as well as nozzle drawing, and a few others
* model - is the OpenFOAM case folder, can be run 'as is' (see below), configured for sea level launch, 'as is' will take ~24h on an average laptop
* notebooks - contains some Jupyter notebooks used to generate OpenFOAM geometry and gas settings from JANAF data
* src - auxiliary python code to work with Cantera ( 3-d party chemical code, used to better understand fuel-rich combustion) and working with JANAF data

# Run the model yourself

Model case in the /model folder is ready to go, geometry is based on the original drawing of RD107 nozzle

![geom](/figures/RD107.jpg)

With proper OpeFOAM (tested on OpenFOAM v8 on Ubuntu 20.04 (AWS) and 18.04 (WSL) ) the case can be run by just


```console
foo@bar:~$ blockMesh
foo@bar:~$ setFields
foo@bar:~$ rhoCentralFoam

```

Beware case takes long time to solve, temperature distribution below took 24h to solve.
Solved cases are visualized with Paraview applying needed symmetries ( to load into Paraview select rd107.foam file)

# Modify the case

If you want to use the case as a startinng point use provided notebooks to change geometry.
If your case runs on other oxidizer-fuel pair than RP-1/LOX  (Methane/LOX, Hydrogen/LOX, N???O???/UDMH)
you can use provided notebooks, JANAF database and other references (for fuel to oxidizer ratio)
to calculate combustion product composition, mean molecular mass, and heat capacity 
(and replace data in /model/constant/thermophysicalProperties)

heat capacity for this RP-1/LOX case

![Cp](/figures/Combustion_product_Cp.png)

# Run on AWS

Take advantage of affordable cloud computing and run the case on AWS (my [article](https://medium.com/@andrey-shornikov/become-a-rocket-scientist-for-0-99-with-a-capstone-project-100bf3944c02) on how to do it)
With a properly selected instances and organized storage a single run costs about $1

![AWS](/figures/openFOAM_AWS.jpg)




