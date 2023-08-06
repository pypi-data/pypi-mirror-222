# img2fmri

**img2fmri**: a python package for predicting group-level fMRI responses to visual stimuli using deep neural networks

<img src="https://raw.githubusercontent.com/dpmlab/img2fmri/main/model_overview.png" width="700" class="center"/>

Users are encouraged to read the background science information for an overview of the model and its intended uses ([science_overview.pdf](science_overview.pdf)).

## Usage and Documentation
Users are encouraged to view our [ReadTheDocs documentation](https://img2fmri.readthedocs.io/en/latest/) 
for our API documentation, and also review [overview.ipynb](overview.ipynb) notebook which shows the import 
and use of the `img2fmri.predict()` function, as well as its extension to movies using 
`img2fmri.predict(predict_movie=True)`.

**img2fmri** can also be used as a command-line interface, as:

    img2fmri [-h] --input input_dir_or_movie [--output output_dir]
             [--roi_list each roi here] [--sigma sigma_val] [--center_crop true_or_false]
             [--predict_movie true_or_false]

## Installation
To install and use img2fmri, users must work from a coding environment with [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation) and [AFNI](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/main_toc.html) installed, or use our Docker container which comes with those pre-installed. 

### Installation with pip

For users who already have FSL and AFNI installed, img2fmri can be installed and tested with:

    pip install img2fmri
    pytest -s --pyargs img2fmri

### Installation with Docker

For users that intend to use our docker environment to test and use img2fmri, the Dockerfile included in this repo can be used to build an image as follows:

    docker build --no-cache --tag img2fmri --file Dockerfile .

and if successfully built, can be run and tested with:

    docker run -it -p 8888:8888 img2fmri
    pytest -s --pyargs img2fmri

Alternatively, our pre-built image can be pulled and used,though do note that this is a large (~10GB compressed) image.

    docker pull mbennett12/img2fmri
    docker run -it -p 8888:8888 img2fmri
    pytest -s --pyargs img2fmri

### Installation with Conda

Optionally, users can install [Conda](https://docs.conda.io/en/latest/) and create an environment with python 3.9 ready for img2fmri (NOTE: this conda environment still needs access to FSL and AFNI): 

    conda create --name name_of_environment python=3.9
    conda activate name_of_environment
    pip install img2fmri

### Installing Jupyter and running analyses
In order to run the jupyter notebook analyses in [overview.ipynb](overview.ipynb) or 
[model_training.ipynb](model_training/model_training.ipynb), the following commands should be run.

If running the docker container from the command:

    docker run -it -p 8888:8888 img2fmri

users should then run the following command from within the container:

    python3 -m notebook --allow-root --no-browser --ip=0.0.0.0

in order to then access their docker container's jupyter notebook at the following url: `http://localhost:8888`. 
Note that users will need to copy and paste the token shown in the output of the previous command in their
 web browser to access their docker container's directory.

## Support, questions, and how to contribute
Users are encouraged to review [CONTRIBUTING.rst](CONTRIBUTING.rst) with suggestions on Users are encouraged to reiv [Max Bennett](mailto:mbb2176@columbia.edu) with questions or issues.

## License
This package is licensed under an MIT license in `LICENSE.txt`