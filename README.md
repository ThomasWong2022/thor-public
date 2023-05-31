# THOR: Time-Varying High-dimensional Ordinal Regression 

[![Downloads](https://static.pepy.tech/badge/thorml)](https://pepy.tech/project/thorml)

THOR is a new autoML tool for temporal tabular datasets and time series. It handles high dimensional datasets with distribution shifts better than other tools. It makes use of the latest research results from incremental learning to improve robustness of machine learning methods. 


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



## Citation
If you are using this package in your scientific work, we would appreciate citations to the following preprint on arxiv.

[Dynamic Feature Projection and model selection methods for temporal tabular datasets with regime changes](https://arxiv.org/abs/2301.00790)

Bibtex entry:
```
@misc{wong2023dynamic,
      title={Dynamic Feature Engineering and model selection methods for temporal tabular datasets with regime changes}, 
      author={Thomas Wong and Mauricio Barahona},
      year={2023},
      eprint={2301.00790},
      archivePrefix={arXiv},
      primaryClass={q-fin.CP}
}
```










