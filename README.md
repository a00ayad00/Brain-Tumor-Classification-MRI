# Data
**The data and problem statement on [Kaggle](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri?select=Testing)**

# To Run DVC Pipeline
**1. Initialization:** `dvc init`
<br>**2. Run the pipeline:** `dvc repro`
<br>**3. See the result:**`dvc dag`

# ModuleNotFoundError
**If you got this error for a reason, put your working dir in the PYTHONPATH variable env like the following command:** `export PYTHONPATH=/home/sagemaker-user/Brain-Tumor-Classification-MRI:$PYTHONPATH`