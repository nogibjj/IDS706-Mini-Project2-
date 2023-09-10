# IDS 706 Data Engineering Mini Project 2

### Overview
This repository is created using my Mini Project 1 template. It uses a couple of Pandass functions and returns descriptive statistics for a given dataframe, which is about camera models' wide range of features. 

Dataset used: [1000 Cameras Dataset](https://www.kaggle.com/datasets/crawford/1000-cameras-dataset)


### Key components in the repository are:
- `camera.csv`
- `Makefile`
- `requirements.txt`
- `Dockerfile`
- `.devcontainer`
- `main.py`
- `test_main.py`
- `GitHub Actions`

### Result
- `make lint`
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/7ef2e6df-7288-4837-83c3-7a5be4c30dc6)

- `make test` : It passed tests on all the functions I defined.
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/af54efae-d3d7-40ca-818b-e49683829a8f)

- `make format`
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/01f3ea79-060d-46e6-94e1-032b914c409c)

### Output from test_main.py
This shows top five columns of dataframe with head function, summary statistics of a price column, and a scatter plot. 
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/431a09f2-2984-4f97-9f4b-6da936e8cbaf)

### Data Visualization (Storage vs. Weights of cameras) 
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/44cff96e-5eef-469f-8fa9-e6d4da628446)
