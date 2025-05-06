In this project, I train a set of classical ML models to predict game properties. Then, I use perfomance metrics to decide which of the models is best suited for predicting each of the selected properties. See `ludemes prediction report` for the summary of the findings. 

To run the jupiter notebook, use:

```bash
$ docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/jupyter/datascience-notebook:2024-05-27
```
