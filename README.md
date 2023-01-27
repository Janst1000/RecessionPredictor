# Recession Predictor

This project is based on [this repo ](https://github.com/DanlBradley/RecessionPredictor)and this associated [blog post](https://medium.com/mlearning-ai/forecasting-recessions-with-scikit-learn-df58e1ea695f) published in MLearning.ai which goes into more detail on the methodology presented. The main idea for this project is to download a lot of data that we will process and train a model on, which we will then later use to predict future recessions. For that we will use 3 different methods, logistic regression, random forest and XGBoost.

## Navigating this Repo

This project is split up into two parts. The data acquasition and the model creating and prediction part. 

1. Full Potential - this notebook downloads, preprocesses and saves all of the used data in a local csv file which will be read by the other part of the project. In here we download a lot of data from FRED and nasdaqdatalink. To further understand why we chose the follwing indicators for our project, you should take a look at Daniels blog post.
2. Model Tuning - this notebook is where the magic happens and our models are trained and executed. We will also take a closer look at the preformance of the models and compare them which each other. At the end we also try to predict in a monthly basis instead of fiscal quarter basis to try to get a prediction as close as possible to the current date.

## Conda Environment

```bash
conda create -n aoec -f environment.yml
conda activate aoec
```