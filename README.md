# THOR: Time-Varying High-dimensional Ordinal Regression 

THOR is a new autoML tool for temporal tabular datasets and time series. It handles high dimensional datasets with distribution shifts better than other tools. Inspired by the Numerai competiton, THOR has evolved from a specific tool for Numerai competition into a general ML pipeline which has many applications in finance and healthcare. 


## Gradient Boosting Decision Trees

Customised LightGBM-based Gradient Boosting Decision Trees models for temporal tabular datasets.

## Deep Learning Models 

A novel deep learning model for temporal tabular datasets, which complements well with the above GBDT-based models.

## TimeSeries Hybrid 

A new method which combines classical and machine learning techniques for feature engineering and sequence modelling. A hybrid approach which demonstrate robust performances for high dimensional time-series.

## Dynamic Hyperopt 

Apply dynamic hyper-parameter optimisation methods under incremental learning framework for temporal tabular and multi-variate timeseries datasets. 

## Portfolio Optimisation

A new method to combine predictions from machine learning model using well-known theories from finance. Using the best research results from both finance and reinforcement learning, the method can maximise the portfolio return (or minimise the given loss function) within required risk metrics.

## Trend Follower

An enhanced implementation of trend following strategies with improved robustness and lower risks than the standard implementation of moving averages. Offer a better way to replicate trend following strategies and build new strategies that are less correlated to existing ones. 




## Citation
If you are using this package in your scientific work, we would appreciate citations to the following preprint on arxiv.

[Robust machine learning pipelines for trading market-neutral stock portfolios](https://arxiv.org/abs/2301.00790 )

Bibtex entry:
```
@misc{https://doi.org/10.48550/arxiv.2301.00790,
  doi = {10.48550/ARXIV.2301.00790},
  
  url = {https://arxiv.org/abs/2301.00790},
  
  author = {Wong, Thomas and Barahona, Mauricio},
  
  keywords = {Computational Finance (q-fin.CP), Computational Engineering, Finance, and Science (cs.CE), Machine Learning (cs.LG), FOS: Economics and business, FOS: Economics and business, FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {Robust machine learning pipelines for trading market-neutral stock portfolios},
  
  publisher = {arXiv},
  
  year = {2023},
  
  copyright = {Creative Commons Attribution 4.0 International}
}
```




