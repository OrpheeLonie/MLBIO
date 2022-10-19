import kaggle
import json

kaggle.api.authenticate()

kaggle.api.dataset_download_files('surajghuwalewala/ham1000-segmentation-and-classification', path='data/', unzip=True)