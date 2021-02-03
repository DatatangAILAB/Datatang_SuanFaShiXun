## PyTorch solution of rhythm prediction task Using BiLSTM-CRF model.

This repo contains a PyTorch implementation of a BiLSTM-CRF model for rhythm prediction task.

## Structure of the code

At the root of the project, you will see:

```text
├── pyner
|  └── callback
|  |  └── lrscheduler.py　　
|  |  └── trainingmonitor.py　
|  |  └── ...
|  └── config
|  |  └── basic_config.py #a configuration file for storing model parameters
|  └── dataset　　　
|  └── io　　　　
|  |  └── data_loader.py　　
|  |  └── data_transformer.py　　
|  └── model
|  |  └── embedding
|  |  └── layers
|  |  └── nn
|  └── output #save the ouput of model
|  └── preprocessing #text preprocessing 
|  └── train #used for training a model
|  |  └── trainer.py 
|  |  └── ...
|  └── utils # a set of utility functions
|  └── test
├── test_predict.py
├── train_bilstm_crf.py
├── train_word2vec.py
```

## Dependencies

- csv
- tqdm
- numpy
- pickle
- scikit-learn
- PyTorch 1.0
- matplotlib

## How to use the code

2. Modify configuration information in `pyner/config/basic_config.py`(the path of data,...).
3. run `python train_bilstm_crf.py` ．
4. run `python test_predict.py` ．

