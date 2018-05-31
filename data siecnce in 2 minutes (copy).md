Title: Keras:Neural Networks in Python
Date: 2017-12-27 22:00
Category: Deep Learning
Tags: Data science
Slug: keras deep Learning
Author: Mohcine madkour
Illustration: datasciencejpg.jpg


# Keras : Neural Networks in Python
Keras is an easy-to-use and powerful library for Theano and TensorFlow that provides a high-level neural networks API to develop and evaluate deep learning models. I created a handy code reference for those who need an extra push to get started

In no time, this Keras code will make you familiar with how you can load datasets from the library itself, preprocess the data, build up a model architecture, and compile, train, and evaluate it. As there is a considerable amount of freedom in how you build up your models, you'll see that the codes use some of the simple key code examples of the Keras library that you need to know to get started with building your own neural networks in Python.

Furthermore, you'll also see some examples of how to inspect your model, and how you can save and reload it. Lastly, you’ll also find examples of how you can predict values for test data and how you can fine tune your models by adjusting the optimization parameters and early stopping.

In short, you'll see that this cheat sheet not only presents you with the six steps that you can go through to make neural networks in Python with the Keras library.

Before I get started, this a  quick presentation for those who are curious to know about deep learning in python

# Hands on deep learning in python

Two of the top numerical platforms in Python that provide the basis for Deep Learning research and development are Theano and TensorFlow.

In this section, you will discover the Keras Python library that provides a clean and convenient way to create a range of deep learning models on top of Theano or TensorFlow.

## What is Keras?

Keras is a minimalist Python library for deep learning that can run on top of Theano or TensorFlow.

It was developed to make implementing deep learning models as fast and easy as possible for research and development.

It runs on Python 2.7 or 3.5 and can seamlessly execute on GPUs and CPUs given the underlying frameworks. It is released under the permissive MIT license.

Keras was developed and maintained by François Chollet, a Google engineer using four guiding principles:

- Modularity: A model can be understood as a sequence or a graph alone. All the concerns of a deep learning model are discrete components that can be combined in arbitrary ways.
- Minimalism: The library provides just enough to achieve an outcome, no frills and maximizing readability.
- Extensibility: New components are intentionally easy to add and use within the framework, intended for researchers to trial and explore new ideas.
- Python: No separate model files with custom file formats. Everything is native Python.


##How to Install Keras

Keras is relatively straightforward to install if you already have a working Python and SciPy environment.

You must also have an installation of Theano or TensorFlow on your system already.

    sudo pip install keras


**Alternatively: install Keras from the Github source**

First, clone Keras using git:

    git clone https://github.com/keras-team/keras.git

Then, cd to the Keras folder and run the install command:

    cd keras
    sudo python setup.py install

**Configure Backends**

By default Keras use tensor flow, type the command : >$ gedit ~/.keras/keras.json in terinal to Sswitch from TensorFlow to CNTK or Theano

Switching from TensorFlow to CNTK or Theano

{
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "image_data_format": "channels_last", 
    "backend": "tensorflow"
}


We can summarize the construction of deep learning models in Keras as follows:

1. Define your model. Create a sequence and add layers.
1. Compile your model. Specify loss functions and optimizers.
1. Fit your model. Execute the model using data.
1. Make predictions. Use the model to generate predictions on new data.


You can see installation instructions for both platforms here:

###Installation instructions for Theano

    conda install numpy scipy mkl nose sphinx pydot-ng
    pip install parameterized
    conda install theano pygpu

Install and configure the GPU drivers for Linux GPU

Install CUDA drivers

Follow [this link](https://developer.nvidia.com/cuda-downloads) to install the CUDA driver and the CUDA Toolkit. You must reboot the computer after the driver installation. Test that it was loaded correctly after the reboot, executing the command nvidia-smi from the command line.

Note: Sanity check: The bin subfolder should contain an nvcc program. This folder is called the cuda root directory.

Fix ‘lib’ path : Add the CUDA ‘lib’ subdirectory (and/or ‘lib64’ subdirectory if you have a 64-bit OS) to your $LD_LIBRARY_PATH environment variable. Example: /usr/local/cuda/lib64



###Installation instructions for TensorFlow

Python 2.7 Ubuntu CPU onlu

    pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.0-cp27-none-linux_x86_64.whl

GPU support

    pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp27-none-linux_x86_64.whl

Run a short TensorFlow program

Invoke python from your shell as follows:

$ python

Enter the following short program inside the python interactive shell:


    import tensorflow as tf
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))

If the system outputs the following, then you are ready to begin writing TensorFlow programs:

    Hello, TensorFlow!

example 1: https://machinelearningmastery.com/time-series-forecasting-long-short-term-memory-network-python/

Kaggle : https://github.com/tdpetrou/kaggle

Kaggle Heart proejct: 
https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/discussion/46257
https://github.com/yehiahesham/Movie_Sentiment_Analysis
https://www.kaggle.com/c/second-annual-data-science-bowl/discussion/18548
http://danmalter.github.io/
https://github.com/jocicmarko/kaggle-dsb2-keras/
https://www.datacamp.com/community/blog/keras-cheat-sheet

fine tune models: https://flyyufelix.github.io/2016/10/03/fine-tuning-in-keras-part1.html
