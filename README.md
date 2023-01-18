# Building a Flask app on Image Classification of Dog or Cat Dataset

[Play with the App]()

A simple Flask App that can classify an image as Dog or Cat using a convolutional neural network model.

I

<p align="center">

<img src='static/img/home.png'>

</p>

<p align="center">

<img src='static/img/predict.png'>

</p>

<p align="center">

<img src='static/img/prediction.png'>

</p>

## Tools Used:

* Tensorflow
* Keras
* Inception
* h5py
* Flask
* Bootstrap
* Heroku

## INTRODUCTION

### 1. The Dog vs. Cat Dataset

**Dogs vs. Cats** [dataset](https://www.kaggle.com/c/dogs-vs-cats/data) provided by  Microsoft Research contains 25,000 images of dogs and cats with the labels

* 1 = dog
* 0 = cat

### 2. Project goals

- Building a **deep neural network** using **TensorFlow** to classify dogs and cats images.
- Making a **Flask application** so user can upload their photos and receive the prediction.

### 3. Project plan

During this project, we need to answer these following questions:

**A. Build the model**

- How to import the data
- How to preprocess the images
- How to create a model
- How to train the model with the data
- How to export the model
- How to import the model

**B. Build the Flask app**

**Front end**

- HTML
  - How to connect frontend to backend
  - How to draw a number on HTML
  - How to make UI looks good

**Back end**

- Flask
  - How to set up Flask
  - How to handle backend error
  - How to make real-time prediction
  - Combine the model with the app

## SETUP ENVIRONMENT

* In order to run our model on a Flask application locally, you need to clone this repository and then set up the environment by these following commands:

```shell
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install pipenv
# Install dependencies
pipenv install --dev
# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

* On the Terminal, use these commands:

```
# enter the environment
pipevn shell
pipenv graph
set FLASK_APP=app.py
set FLASK_ENV=development
export FLASK_DEBUG=1
flask run
```

* If you have error `ModuleNotFoundError: No module named 'tensorflow'` then use

```
pipenv install tensorflow==2.0.0beta-1
```

* If  `* Debug mode: off` then use

```
export FLASK_DEBUG=1
```

* Run the model by

```shell
pipenv run flask run
```

* If you want to exit `pipenv shell`, use `exit`

## HOW IT WORK: CONVOLUTIONAL NEURAL NETWORK (CNN)

This is the project that we finished after studying ** “Convolutional Neural Networks in TensorFlow” course.**
This course is part of the highly sought-after “DeepLearning.AI TensorFlow Developer Professional Certificate” program on Coursera.

<p align="center">
  <img width="760" height="400" src="https://miro.medium.com/max/1838/1*oB3S5yHHhvougJkPXuc8og.gif">
</p>
You can find details in the [article](https://medium.com/@betul.gurbuz.dev/convnets-cnn-74aa18f2d543)

### Next Steps

* Deploy with Docker
* More models
  * VGG-16
  * ResNet50
  * MobileNet V3

