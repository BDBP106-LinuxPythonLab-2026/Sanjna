#!/bin/bash

awk ' $4=="PHE" ' prot.pdb | awk '{print $2}' > PHE_atoms.xyz
