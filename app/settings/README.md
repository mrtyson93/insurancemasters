How to install/set up your conda environment?

In this folder, you will find the exported conda environment file. You can run the following command to create your clone of the environment.
$ conda env create --name insurancemasters --file projenv-spec-file.txt

After running the above command, you should have a new environment created called "insurancemasters". You can output your list of conda environment using the following command.
$ conda env list

You should see a new entry like the following.
# conda environments:
#
base                     /Users/bingyue/opt/anaconda3/
insurancemasters      *  /Users/bingyue/opt/anaconda3/envs/insurancemasters



