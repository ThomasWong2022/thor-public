FROM gcr.io/kaggle-gpu-images/python:latest
#### Install Signatory, needs to update when newer supporting torch1.11.0
RUN pip install signatory==1.2.6.1.9.0 --no-deps
#### Additional NN models 
RUN pip install pytorch-lightning
RUN pip install pytorch-tabnet --no-deps
RUN pip install numerapi==2.12.9
#### Build THOR package
WORKDIR /
COPY src/pythor/ src/pythor/
COPY setup.py setup.py
COPY README.md README.md
RUN pip install .
WORKDIR /workspace 
