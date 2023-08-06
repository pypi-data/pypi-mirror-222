# Blacklight  

[![test](https://github.com/BlackLightLabs/blacklight/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/BlackLightLabs/blacklight/actions/workflows/test.yml) [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/449f7ff90fcb4340a4c90884d15f700a)](https://www.codacy.com/gh/BlackLightLabs/blacklight/dashboard?utm_source=github.com&utm_medium=referral&utm_content=BlackLightLabs/blacklight&utm_campaign=Badge_Coverage) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/449f7ff90fcb4340a4c90884d15f700a)](https://www.codacy.com/gh/BlackLightLabs/blacklight/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BlackLightLabs/blacklight&amp;utm_campaign=Badge_Grade)![PyPI - Downloads](https://img.shields.io/pypi/dm/blacklight?color=lime&label=Downloads%20from%20PyPi&logoColor=blue)

## Genetic algorithms in autoML. 
This project aims to use Genetic Algorithms to optimize the topologies of Deep Neural Networks (DNNs) and explore new possibilities that traditional optimization techniques might overlook. The fitness function of the algorithm is the accuracy of the model, and the genes represent the individual topologies.

## Installation 

Make sure you have Python 3.9 or higher installed (not greater than 3.11). 
### Windows, Linux

1. Create new virtual environment:
   - ```pip install -m virtualenv```
   - ```python -m venv your_virtual_env_name```
   - ```your_virtual_env_name\Scripts\activate```
2. Install Tensorflow:
   - ```pip install tensorflow```
2. Install the package:
   - ```pip install blacklight```

### MacOS (Intel)

1. Create new virtual environment:
   - ```pip install -m virtualenv```
   - ```python -m venv your_virtual_env_name```
   - ```your_virtual_env_name\Scripts\activate```
2. Install Tensorflow:
   - ```pip install tensorflow-macos```
   - ```pip install tensorflow-metal```
2. Install the package:
   - ```pip install blacklight```

### MacOS (Apple Silicon)
1. Download Miniconda from: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
2. Install Miniconda:
   - Navigate to downloads folder ```cd ~/Downloads```
   - ```bash Miniconda3-latest-MacOSX-arm64.sh -b -p $HOME/miniconda```
3. Activate Miniconda:
   - ```source ~/miniconda/bin/activate```
4. Install TensorFlow dependencies: 
    - ```conda install -c apple tensorflow-deps```
5. Install TensorFlow:
    - ```pip install tensorflow-macos``` 
    - ```pip install tensorflow-metal```
6. Install the package:
   - ```pip install blacklight```
    
## Hypothesis

The hypothesis of this project is that DNN topologies will converge to either a local maximum or an absolute maximum over the evolution process, offering better performance than a DNN with randomly selected topology. For this experiment, the project will use equivalent activation functions (ReLU) and SGD for back-propagation, holding everything except the topology constant. Updated documentation coming soon.

## Methodology

The project utilizes a genetic algorithm to evolve the topology of the DNN. The algorithm starts with a randomly generated population of DNN topologies and evaluates their fitness using the accuracy of the model. The fittest individuals are selected for reproduction, while the weaker ones are discarded. The offspring of the selected individuals are then created through crossover and mutation. This process is repeated for a specified number of generations, and the best-performing topology is chosen as the final output.

## Documentation 
Documentation can be found at https://blacklightlabs.github.io/blacklight/html/index.html
