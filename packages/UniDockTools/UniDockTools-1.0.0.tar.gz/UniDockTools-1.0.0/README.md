# Introduction
Comparing with the origin Uni-Dock software, here are two new features:
- ligands prepare  
  
  support origin SDF formats  
  
- gnina CNNscores
  
  support using gnina CNNscores to rescore docking posing which sampled by vina scoring function

# Installation

## 1. install unidock
   
We recommend users to install unidock in a new conda virtual environment to avoid potential configuration conflict issues.

  
    conda create -n unidock -c https://conda.mlops.dp.tech:443/caic unidock
  
## 2. install gnina
If you also want to use gnina CNNscores to rescore docking pose, you should install gnina.
- binary   
install gnina by download binary file from [gnina's realeses website](https://github.com/gnina/gnina/releases)
- source code  
install gnina from source code according to [gnina installation document](https://github.com/gnina/gnina#installation)
