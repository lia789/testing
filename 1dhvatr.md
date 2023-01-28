Python Environment Setup Cheat Sheet
====================================

Virtual Environment Setup
-------------------------

shell

```shell
$ python -m venv env_name
$ env\Scripts\activate  # activate on Windows CMD
$ "C:\Users\path\env\Scripts\activate.bat"  # activate on Windows with text
$ source /director_path/env/bin/activate  # activate on Linux CMD
```

Python Package Management
-------------------------

ruby

```ruby
$ pip install package_name					
$ pip install -r requirements.txt				# requirements.txt
$ pip install git+github_repo_url.git				# install package from Github
$ pip install git+github_repo_url.git@commit_hash		# install package from Github with specific commit id
$ pip install package_name==1.5.2				# specific version
$ pip list							# list of package name
$ pip uninstall package_name -y					# uninstall
```

Jupyter Lab Environment Setup
-----------------------------

ruby

```ruby
* activate env_name and run this command
    $ pip install ipykernel
    $ python -m ipykernel install --user --name=env_name
* uninstall a kernel
    $ jupyter kernelspec uninstall env_name
* list of kernel
    $ jupyter kernelspec list
```

Python Code Format Library List
-------------------------------

python

```python
# Linting
flake8
pylint
mypy
autopep8
isort
pydocstyle
black
```

VS Code Extensions for Python Environment
-----------------------------------------

diff

```diff
- Python
- Better Comments
- Code Spell Checker
- Code Runner
- Error Lens
- Excel Viewer
- JSON formatter
- Jupyter
- Pylance
- Python Docstring Generator
- Test Explorer UI
- Python Test Explorer for Visual Studio Code
- autoDocstring - Python Docstring Generator
- Django
- HTMLHint
- IntelliSense for CSS class names in HTML
- Live Server
- Prettier - Code formatter
```

VS Code Setup JSON File
-----------------------

json

```json
{
    // Editor settings
    "files.autoSave": "onFocusChange",
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    
    // Python Linting settings
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "autopep8",
    // Python Execution settings
    "python.languageServer": "Pylance",
    "python.showStartPage": false,
    
    // Python Docstring settings
    "autoDocstring.generateDocstringOnEnter": true,
    "autoDocstring.docstringFormat": "numpy",
    "autoDocstring.startOnNewLine": true
}
```

*   Use Match Brackets to never.
