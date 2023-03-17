# CINN_cookie

<img src = 'https://i.imgur.com/lg1uNwa.png' width = "200" height = "" >


A minimalist cookiecutter for research and data science projects in the CINN.

## Installation

Run via `cookiecutter gh:N-HEDGER/CINN_cookie`

You will be prompted to give names for your project.

A picture of a brain, instructions for creating a custom environment for the package, as well as instructions for installing the package to your environment will follow.

You should install the package with 

```bash
pip install -e . 
```

With the -e flag indicating the package will be editable. That means that if you change the files, you don’t need to re-install the package for your changes to be picked up by Python.

Putting 

```python
%load_ext autoreload
%autoreload 2
```

In the first cell of your .ipynb files will make the package autoreload. This means that the package will be autoreloaded and update to reflect any changes that you have made. This is excellent for development as it means that you dont have to keep reloading/reinstalling the package to see the changes implemented. 

## Structure

- `data`: Where you put raw data for your project. You usually won’t sync this to source control, unless you use very small, text-based datasets (< 10 MBs).

&nbsp;

- `docs`: Where you put documentation, including Markdown and reStructuredText (reST). Calling it docs makes it easy to publish documentation online through Github pages.

&nbsp;


- `results`: Where you put results, including checkpoints, hdf5 files, pickle files, as well as figures and tables. If these files are heavy, you won’t put these under source control.

&nbsp;


- ` "{{ cookiecutter.package_name }}"`: This contains the package of scripts that drive your analysis. These are the lengthy functions and classes that do all the heavy lifting 'behind the scenes'. We keep these hidden from the 'presentation' end of the project in `notebooks`. 

&nbsp;


- `notebooks`: This contains your annotated .ipynb notebooks that walk people through your analysis in a presentable way. This will import functions from - ` "{{ cookiecutter.package_name }}"` and parameters from `config/config.yml`

&nbsp;

- `config`: Where you will define parameters for your project. This will be in the form of a yaml file with sub-dictionaries `config/config.yml`. No parameters should be hard-coded into scripts or written into notebooks. They should all be loaded in from the yaml file. This will allow you to modify your analysis by simply changing the content of the yaml file. 

&nbsp;


- `tests`: Where you put tests for your code. 

## Pre-populated examples

- ` "{{ cookiecutter.package_name }}"/utils.py` contains the function load_pkg_yaml. This will load in the parameters defined in  `config/config.yml`.



