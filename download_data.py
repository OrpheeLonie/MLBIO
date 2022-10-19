import kaggle
import json

kaggle.api.authenticate()

kaggle.api.dataset_download_files('https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification/download?datasetVersionNumber=2', path='data/', unzip=True)
