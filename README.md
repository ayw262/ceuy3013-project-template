Reinforced Concrete Beam Design:
-------------
-------------

This is a program for reinforced concrete beam design.
The user inputs the compressive strength and yield strength of the concrete and steel,
along with the intended dead and live loads and load factors.
This program will return the beam dimensions (width, height, effective depth)
and the size and number of reinforcing steel bars required.

Note: This program can only be used for point loads loaded at the same point of the beam and distributed loads across the entire length of the beam.

Some things to be noted before running the program:

- All inputs are required.
- All values must be inputted without commas.
- Permitted values for compressive strength in psi:
  3000, 4000, and 5000 (5000 only works with a yield strength of 60000)
- Permitted values for yield strength in psi:
  40000 and 60000


Inputs:
------

- compressive strength of concrete (psi)
- yield stress of steel (psi)
- point dead load (kips)
- point live load (kips)
- distance from the left end of the beam to the point loads (feet)
- length of entire beam (feet)
- distributed dead load (kips/ft)
- distributed live load (kips/ft)
- load combination factors


Example:
-----
