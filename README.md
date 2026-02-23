# Knowledge-Bot
I making my first Knowledge bot.

## Python project setup

This repository is now initialized as a minimal Python project. The following steps were performed:

1. A virtual environment created at `.venv/`.
2. A `pyproject.toml` declaring the project name and `ipykernel` dependency.
3. A Jupyter kernel `Python (knowledge-bot)` registered using the venv.
4. Workspace settings configured in `.vscode/settings.json` to point VS Code at the venv.

To replicate or extend the setup manually you can run:

```powershell
python -m venv .venv                    # create venv
.venv\Scripts\activate                # activate it
python -m pip install --upgrade pip     # upgrade pip
python -m pip install ipykernel         # install kernel support
python -m ipykernel install --user --name knowledge-bot --display-name "Python (knowledge-bot)"
```

After this, any notebook or Python file opened in VS Code will use the `knowledge-bot` interpreter and kernel.

Feel free to add additional dependencies to `pyproject.toml` and install them via the venv.

### 📁 Git ignores

The project git configuration should exclude sensitive or large local artefacts. Add a `.gitignore` at the repository root containing at least:

```
.env
.venv/
venv-1/
```

This will keep environment directories and secrets out of version control.

