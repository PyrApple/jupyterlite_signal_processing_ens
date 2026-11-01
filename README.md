# ENS Louis Lumière - Signal processing tutorials

repository: https://github.com/PyrApple/jupyterlite_signal_processing_ens

github page: https://pyrapple.github.io/jupyterlite_signal_processing_ens/lab/index.html

jupyterlite server template copied from https://github.com/jupyterlite/demo


# Misc

- to reset workspace, add at the end of the url: ?reset


# Cleaner Git diff

install
- pip install nbdime

integrate with git
- nbdime config-git --enable --global

use
- git diff ...

# Run local jupyter lite build

## Install

python -m pip install jupyterlab
python -m pip install "jupyterlite-core[serve]"
python -m pip install jupyterlite-pyodide-kernel==0.8.0

## Build / serve

Run these commands from the repository root. The build config selects `content/`
(paths are relative to the project root, not the config file in `repl/`) and excludes
`*_correction.ipynb` notebooks.

rm -Rf ./dist/*
jupyter lite build --config=jupyter_lite_config.json --output-dir=./dist/
jupyter lite serve --config=jupyter_lite_config.json --output-dir=./dist/