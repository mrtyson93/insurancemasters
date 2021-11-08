# How to install/set up your conda environment?

In this folder, you will find the exported conda environment file. You can run the following command to create your clone of the environment.

```bash
$ conda env create --name insurancemasters --file projenv-spec-file.txt
```

or run if on windows

```bash
$ conda env create -f environment.yml
```

Activate the insurancemasters environment using the ouput from the environment command

After running the above command, you should have a new environment created called "insurancemasters". You can output your list of conda environment using the following command.

```bash
$ conda env list
```

You should see a new entry like the following.

```bash
# conda environments:
#
base                     /Users/bingyue/opt/anaconda3/
insurancemasters      *  /Users/bingyue/opt/anaconda3/envs/insurancemasters
```
