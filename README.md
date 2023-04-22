# THOR: Time-Varying High-dimensional Ordinal Regression 

[![Downloads](https://static.pepy.tech/badge/thorml)](https://pepy.tech/project/thorml)

THOR is a new autoML tool for temporal tabular datasets and time series. It handles high dimensional datasets with distribution shifts better than other tools. It makes use of the latest research results from incremental learning to improve robustness of machine learning methods. 


## Gradient Boosting Decision Trees

Customised LightGBM-based Gradient Boosting Decision Trees models for temporal tabular datasets.

## Deep Learning Models 

A novel deep learning model for temporal tabular datasets, which complements well with the above GBDT-based models.

## TimeSeries Hybrid 

A new method which combines classical and machine learning techniques for feature engineering and sequence modelling. A hybrid approach which demonstrate robust performances for high dimensional time-series.

## Dynamic Hyperopt 

Apply dynamic hyper-parameter optimisation methods under incremental learning framework for temporal tabular and multi-variate timeseries datasets. 





## How to get THOR running on my computers 


### Docker 

As this packages used various machine learning and CUDA libaries for GPU support, we recommend to use docker to manage the dependencies. 

The image is now uploaded on [Docker Hub](https://hub.docker.com/repository/docker/thomaswong2023/thor-public/general).

The following Docker images contains all the dependencies used in this tool. 

```bash
docker pull thomaswong2023/thor-public:deps
docker run --gpus device=all -it -d --rm --name thor-public-example thomaswong2023/thor:public:deps bash

```


### PyPI 

This project is also on [PyPI](https://pypi.org/project/thorml/).

Install the package with the following command. Dependencies are not installed with the package 

```bash
pip install thorml -r requirements.txt

```






