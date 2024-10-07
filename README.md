# Data
**The data and problem statement is on [Kaggle](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri?select=Testing)**

# To Run DVC Pipeline
**1. Initialization:** `dvc init`
<br>**2. Run the pipeline:** `dvc repro`
<br>**3. See the result:**`dvc dag`

# ModuleNotFoundError
**If you got this error for a reason, put your working dir in the PYTHONPATH variable env like the following command:** `export PYTHONPATH=/home/sagemaker-user/Brain-Tumor-Classification-MRI:$PYTHONPATH`

# How to run the application
### 1. Clone the repository
### 2. Create a conda environment
### 3. Install the requirements: `$ pip install -r requirements.txt`
### 4. Run the following command: `$ python app.py`

# AWS CI-CD Deployment with Github Actions
### 1. Login to AWS console
### 2. Create IAM user for deployment with specific access
1) EC2: For the virtual machine
2) ECR: Elastic Container registry to save your docker image in AWS Docker Hub
<br> **Policies:** _AmazonEC2ContainerRegistryFullAccess_ and _AmazonEC2FullAccess_
### 3. Create ECR Repo to store the docker image
**Save the URI like thils:** `962265167812.dkr.ecr.us-east-1.amazonaws.com/brain-tumor-classification`
### 4. Create EC2 machine (Ubuntu)
### 5. Connect to the EC2 Instance you created and run the following commands
**Optional**
<br> `sudo apt-get update -y`
<br> `sudo apt-get upgrade`
<br>**Required**
<br> `curl -fsSL https://get.docker.com -o get-docker.sh`
<br> `sudo sh get-docker.sh`
<br> `sudo usermod -aG docker ubuntu`
<br> `newgrp docker`
### 6. Configure EC2 as a self-hosted runner
**Open the project repo on GitHub and go to:** _Settings_ **>** _Actions_ **>** _Runners_ **>** _New self-hosted runner_ **>** _choose the OS_ **>** _run commands one by one_
### 7. Setup the GitHub secrets
**Go to** _Settings_ **>** _Secrets and variables_ **>** _Actions_ **>** _New repository secret_
<br> AWS_ACCESS_KEY_ID =
<br> AWS_SECRET_ACCESS_KEY =
<br> AWS_REGION = *us-east-1*
<br> AWS_ECR_LOGIN_URI = *962265167812.dkr.ecr.us-east-1.amazonaws.com*
<br> ECR_REPOSITORY_NAME = *brain-tumor-classification*
