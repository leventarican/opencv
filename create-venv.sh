#!/bin/bash

# create virtual environment
cvVersion="4.1.0"
cwd=$(pwd)
python3 -m venv OpenCV-"$cvVersion"-py3
echo "# Virtual Environment Wrapper" >> ~/.bashrc
echo "alias workoncv-$cvVersion=\"source $cwd/OpenCV-$cvVersion-py3/bin/activate\"" >> ~/.bashrc
source "$cwd"/OpenCV-"$cvVersion"-py3/bin/activate

# now install python libraries within this virtual environment
pip install wheel numpy scipy matplotlib scikit-image scikit-learn ipython dlib

# quit virtual environment
deactivate
######################################