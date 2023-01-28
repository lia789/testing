Python virtual environment setup:

*   $ python -m venv env\_name
*   $ env\\Scripts\\activate (Windows CMD)
*   $ "C:\\Users\\path\\env\\Scripts\\activate.bat" (Windows with text)
*   $ source /director\_path/env/bin/activate (Linux CMD)

Python package management:

*   $ pip install package\_name
*   $ pip install -r requirements.txt (requirements.txt)
*   $ pip install git+github\_repo\_url.git (install package from Github)
*   $ pip install git+github\_repo\_url.git@commit\_hash (install package from Github with specific commit id)
*   $ pip install package\_name==1.5.2 (specific version)
*   $ pip list (list of package name)
*   $ pip uninstall package\_name -y (uninstall)

Jupyter lab environment setup:

*   activate env\_name and run these commands:
*   $ pip install ipykernel
*   $ python -m ipykernel install --user --name=env\_name
*   uninstall a kernel: $ jupyter kernelspec uninstall env\_name
*   list of kernel: $ jupyter kernelspec list

Python code format library list:

*   Linting: flake8, pylint, mypy, autopep8, isort, pydocstyle, black

VS Code extensions for Python environment:

*   Python
*   Better Comments
*   Code Spell Checker
*   Code Runner
*   Error Lens
*   Excel Viewer
*   JSON formatter
*   Jupyter
*   Pylance
*   Python Docstring Generator
*   Test Explorer UI
*   Python Test Explorer for Visual Studio Code
*   autoDocstring - Python Docstring Generator
*   Django
*   HTMLHint
*   IntelliSense for CSS class names in HTML
*   Live Server
*   Prettier - Code formatter

VS Code setup json file:

*   { "files.autoSave": "onFocusChange", "explorer.confirmDragAndDrop": false, "explorer.confirmDelete": false, "python.linting.enabled": true, "python.linting.lintOnSave": true, "python.linting.flake8Enabled": true, "python.linting.pylintEnabled": true, "python.linting.mypyEnabled": true, "python.formatting.provider": "autopep8", "python.languageServer": "Pylance", "python.showStartPage": false, "autoDocstring.generateDocstringOnEnter": true, "autoDocstring.docstringFormat": "numpy", "autoDocstring.startOnNewLine": true }
*   use Match Brackets to never
