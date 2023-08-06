![PyPI - Package Version](https://img.shields.io/pypi/v/nlp-models?logo=pypi&style=flat&color=blue)
<a href="https://github.com/minggnim/nlp-models/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue" alt="MIT License"></a>
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/nlp-models.svg)](https://pypi.python.org/pypi/nlp-models/)
[![Python package](https://github.com/minggnim/nlp-classification-model/actions/workflows/python-package.yml/badge.svg)](https://github.com/minggnim/nlp-classification-model/actions/workflows/python-package.yml)
[![Dependency Review](https://github.com/minggnim/nlp-classification-model/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/minggnim/nlp-classification-model/actions/workflows/dependency-review.yml)

# NLP Models

A repository for building transformer based nlp models

## Run Llama2 Chat UI on CPU
```
cd pipelines/nlp_models/
streamlit run app.py
```

## Models

1. bert_classifier
   A wrapper package around BERT-based classification models

   - [Training example](https://github.com/minggnim/nlp-models/blob/master/notebooks/01_bert-classification-finetuning/01_a_classification_model_training_example.ipynb)
   - [Inference example](https://github.com/minggnim/nlp-models/blob/master/notebooks/01_bert-classification-finetuning/01_b_classification_inference_example.ipynb)
2. multi_task_model
   An implementation of multi-tasking model built on encoder models

   - [Zero-shot multi-task model](https://github.com/minggnim/nlp-models/blob/master/notebooks/02_multi-task-model/02_a_multitask_model_zeroshot_learning.ipynb)
   - [Training example](https://github.com/minggnim/nlp-models/blob/master/notebooks/02_multi-task-model/02_b_multitask_model_training_example.ipynb)
   - [Inference example](https://github.com/minggnim/nlp-models/blob/master/notebooks/02_multi-task-model/02_c_multitask_model_inference_example.ipynb)
   - [Qqrant Vector DB](https://github.com/minggnim/nlp-models/blob/master/notebooks/02_multi-task-model/02_d_qdrant_vector_db.ipynb)

## Other Example Notebooks

- [Training GPT-2 model](https://github.com/minggnim/nlp-models/blob/master/notebooks/03_gpt-2-training/gpt-2-training/03_gpt2_training.ipynb)
- [Running Falcon 4b model](https://github.com/minggnim/nlp-models/blob/master/notebooks/04_llms/05_falcon_4b.ipynb)
- [Run Llama2 chat on cpu](https://github.com/minggnim/nlp-models/blob/master/notebooks/04_llms/06_llama2_langchain_gglm_inference.ipynb)

## Installation

### Install from PyPi

```
pip install nlp-models
```

### Install from source

```
git clone git@github.com:minggnim/nlp-models.git
pip install -r requirements
```
