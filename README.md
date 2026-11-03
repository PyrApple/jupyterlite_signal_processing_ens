# User readme

# Content description 

This repository holds signal processing courses and tutorials designed for ENS Louis Lumière students by David Poirier-Q.

## Useful links

Github repository: https://github.com/PyrApple/jupyterlite_signal_processing_ens  
Jupyter notebook: https://pyrapple.github.io/jupyterlite_signal_processing_ens/lab/index.html

## Course and tutorials organisation 

The list below is a (strong) suggestion of the order in which courses / tutorials should be followed.
Tutorials marked as (opt) are not directly attached to the course above (they still require to complete the courses above in the hierarchy to be undertaken).

- courses/1_numerisation
    - tutorials/1_sines

- courses/2_fft_introduction
    - tutorials/2_fft
    - tutorials/2b_resampling
    - (opt) tutorials/2c_spectrogram

- courses/3_convolution_introduction
    - tutorials/3_convolution
    - (opt) tutorials/3b_delaydetect

- courses/4_fft_development
    - tutorials/4_fft_2

- courses/4b_fft_case_studies

- courses/5b_iir_introduction
    - (opt) tutorials/4c_deconvolution

- courses/6_iir_development


## Reset Jupyter workspace

- To reset workspace and kep files added by user (if no overlap), add at the end of the url: ?reset
- To reset workspace and remove files added by user, View/Activate Command Palette/Clear Browser Data


# Developer Readme

## Useful links

Jupyterlite server template copied from https://github.com/jupyterlite/demo

## Cleaner Git diff

```bash
# install
pip install nbdime
# integrate with git
nbdime config-git --enable --global
# use
git diff ...
```

## Run local jupyter lite build

### Install

```python
python -m pip install jupyterlab
python -m pip install "jupyterlite-core[serve]"
python -m pip install jupyterlite-pyodide-kernel==0.8.0
```

### Build / serve

Run from repository root

```bash
rm -Rf ./dist/*
jupyter lite build --config=jupyter_lite_config.json --output-dir=./dist/
jupyter lite serve --config=jupyter_lite_config.json --output-dir=./dist/
```

## Hidden tutorial corrections

To toggle hide corrections, comment `extra_ignore_contents` line in jupyter_lite_config.json.