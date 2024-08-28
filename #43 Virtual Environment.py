# if you are use new version of packages and python but your friend send any proram or project of old version of packages, so you moust be use same package for run the program in this condition you delete the new version and download old version, so remove this provelam use virtual environment and create deferent version environment.
# useing the virtual environment you are install the version of packages and this is not any relation of python install packages
# you are create the virtual environment moust be install the "venv"

# how to cerate virtual environment?
# stape 1:- select the location.
# stape 2:- opent the cmd in this location.
# stape 3:- run this command "python -m venv 'write the folder name you store the lib' "
#         python -m venv VirEnv_1

# start :- you are also ccreate virtual environment but python also use store environment so start the virtual environment following this staps.
# stape 1:- go to the laction of virtual environment folder. 
#           in my case i go :- D:\UserData\Work\development\programming\python\virtual environment>
# stape 2:- run thic command "'virtual environment folde name'/Scripts/activate.bat"
#           VirEnv_1\Scripts\activate.bat
# after then start your virtual Environment

# stop this use :- deactivate

# install the packages using this :- pip install pandas==1.5

# command
# pip list , all packages show
# pip show module-name, show all detales of Module
# pip freeze,show all pacakge with versions

# create the txt file use this command and you are sent the you project memovers and it is run this file and install all packages automaticly or create Virtual environment.

# command for creat file "pip freeze > file_name.txt" and you are run this command where locatcion create file those location.locals
    
# Go to the place where you have file and run this command and automaticly store all packages in your computer :- "pip install -r file_name.txt"

# program for check the version of module or package 

import turtle as tu
print(tu.__version__)