#!/usr/bin/env bash

../../build/ibpm -Re 75 -nx 2700 -ny 800 -ngrid 2 -length 54 -xoffset -2 -yoffset -8 -xshift 0.75 -nsteps 100000 -restart 100 -tecplot 100 -geom cylinder.geom -dt .02 -ubf 0 -tecplotallgrids 0
