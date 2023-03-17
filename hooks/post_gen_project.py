help = """
Your project has been created!
_____________________________________________________________________________
     _---~~(~~-_.
    _{        )   )
  ,   ) -~~- ( ,-' )_
 (  `-,_..`., )-- '_,)
( ` _)  (  -~( -_ `,  }
(_-  _  ~_-~~~~`,  ,' )
  `~ -^(    __;-,((()))
        ~~~~ {_ -_(())
               `\  }
                 { }      Cookie Cutter created by Nicholas Hedger
_____':::::_____________________________________\__\_________________________

If you have not done so already, create a conda environment for your new 
project with:

cd {{cookiecutter.repo_name}}
conda create --name {{cookiecutter.repo_name}} python=3.8
conda activate {{cookiecutter.repo_name}}
conda env export > environment.yml

Install your new project in your local conda environment with:

pip install -e .

You will need to manually add data to .gitignore to prevent it from syncing to
version control.

Don't forget to sync to GitHub. Have fun!
"""
print(help)
