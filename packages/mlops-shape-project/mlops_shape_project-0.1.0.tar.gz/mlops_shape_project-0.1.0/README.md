# **<p align="center" style="color: #DA1B5D;"><strong>Welcome to Shape MLOps Project</strong></p>**

<p align="center">
  <div style="display: inline-block;">
    <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3lyZmtrZXV3azB2czlreWhsczNhbnVucGEwcGphZXVybXdjZm0wcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/BY68rPj9r8oeiu0mmf/giphy.gif" min-width="300px" max-width="100px" width="200px">
  </div>
  <div style="display: inline-block;">
    <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXNvMDliZjNhM28ycGptdjB1MTQ0ZXJlNjJieTh1bjl4ZDBlOTE1eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/9sJOHm62hrvNNTU1g4/giphy.gif" min-width="300px" max-width="100px" width="180px">
  </div>
  <div style="display: inline-block;">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXJqOW5sYjlnbms0b3JlZHp2dnkzdDl2YzN0Y2QxZG05cjIxb3pqNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/KyXBkm9V8df6yD6HVF/giphy.gif" min-width="300px" max-width="100px" width="100px">
  </div>
</p>



## 🌐 **Overview** 
***

This project was initiated as part of Shape's Hard Skill Test for the Machine Learning Engineer role. The core objective was to take an initial script named `job_test_challenge.py` and transform it into a more organized 📐, maintainable 🛠️, and production-ready codebase, all the while preserving its primary functionality. The envisioned transformation entailed the integration of best practices, robust documentation 📄, and a modularized (preferentially object-oriented 📦) design to render the code apt for product release.

### Key Tasks 🔑:

-   Code Modularization and Refactoring: The original script needed an overhaul to reach a modular, and potentially object-oriented, structure 🔄.

-   Documentation: Implementing clear and concise documentation 📚 to ensure smooth navigation and comprehension for fellow developers.

-   Preservation of Output: Despite alterations in the code's structure and logic, the model's predictions (output) ought to remain consistent ✔️.

-   Configuration File Modification: The structure of `artifacts/pipeline.jsonc` was amenable to changes to ensure it meshed seamlessly with the revamped code structure 🔧.

-   Incorporate TODOs: The code housed multiple TODOs that had to be addressed and realized as part of the challenge 📝.

-   Scalability Consideration: The reshaped code was anticipated to cater to hefty data scenarios, suggesting that the supplied sample data file might, in a real-world setting, symbolize a table spanning several gigabytes in a data lake 📊.

### Constraints and Considerations 🚫:

-   The generated code should be portable and capable of executing flawlessly in an alternate Python environment 🐍.

-   The provided "pickle" files were crafted using Python version 3.8.13 and Scikit-learn version 1.0.2. Though other libraries might be pivotal for diverse facets of the project, these particular versions were indispensable for the "pickle" files 📌.

-   Intricate or time-intensive modifications, if not instantly implementable, should be signposted within the code as TODOs. These markers should also sketch out the strategic approach intended for their eventual fulfillment 🕰️.


## 🚀 **Run the project**
***
The provided configuration appears to be from a `pyproject.toml` file, which is a configuration file for the [Poetry](https://python-poetry.org/) dependency management and packaging tool in Python. To install and execute this project, follow the steps below:

### 1️⃣ Install Poetry:
If you haven't installed Poetry yet, you can do so with the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or you can use other installation methods detailed in the [official documentation](https://python-poetry.org/docs/#installation).

### 2️⃣ Clone the project (if you haven't already):
Assuming the project is hosted on a Git repository, clone it:

```bash
git clone https://github.com/JuniorTorresMTJ/mlops_shape_project.git
cd mlops-shape-project
```

### 3️⃣ Install project dependencies:
Navigate to the project directory and install the dependencies using Poetry:

```bash
poetry install
```

This command installs both the main dependencies and the dev dependencies of the project.

### 4️⃣ Activate the virtual environment:
Poetry creates a virtual environment for your project. Activate it with:

```bash
poetry shell
```

### 5️⃣ Run the project:
The exact command to run the project depends on its structure. Typically, there's a main Python script or module you'd execute to start the project. If there's a clear entry point, you can run:


```bash
python mlops_shape_project\app.py
```


### 6️⃣ Additional tasks:
The provided configuration also contains some tasks defined with `taskipy`. You can run these tasks using the `poetry run task` command. For example:

- To run the lint task: 

```bash
  poetry run task lint
```

- To serve the documentation:

```bash
  poetry run task doc
```

### 7️⃣ Expected Model Results:
When evaluating the performance and predictions of our model, we often look at two key components:

#### ✅ Expected Class Labels:

Class labels serve as numerical representations of the expected predictions or classifications from the model. In this context, the class labels can either be -1 or 1. These values might represent two distinct classes or categories in a binary classification scenario.

![Array-output](assets\img\Output.png)


#### ✅ Model Prediction DataFrame:

Beyond the direct class labels, there is also a DataFrame compiled with the model's predictions. Specifically, this DataFrame contains a column named svm_predict, which displays the predicted class labels for each data instance.

![Dataframe-output](assets\img\Output2.png)

## 📖 **Documentation**:

The documentation of this project is an essential component for understanding its structure, functionalities, and usage guides. We strongly believe that comprehensive documentation can speed up the adoption, contribution, and debugging processes of the project. The documentation was crafted using [MkDocs](https://www.mkdocs.org/), a swift and straightforward tool for creating documentation websites from markdown files. It allows us to concentrate on the content while automating the process of converting Markdown into a structured and styled website.

⚠️[Documentation Link](https://mlops-shape-project.readthedocs.io/en/latest/)⚠️


## 📑 **Overview of Project Technologies**
***

This section offers a comprehensive understanding of the technologies incorporated into our project, shedding light on each tool in detail. Grasping these technologies is pivotal for any developer or stakeholder aiming to become acquainted with the infrastructure and the project code.

* * * * *

-   [Python](https://www.python.org/) 3.8.10 🐍
    -   Description: Language used for application development.

* * * * *

-   [Poetry](https://python-poetry.org/) 📦
    -   Description: A tool for dependency management and packaging in Python. Poetry provides a streamlined and consistent approach to handle Python projects and their dependencies, ensuring transparency and reproducibility throughout the process.

* * * * *

-   [Scikit-learn](https://scikit-learn.org/stable/) 1.0.2 📊
    -   Description: A machine learning library in Python. Scikit-learn, together with Pandas, stands as an essential tool for data processing, analysis, and the deployment of machine learning models. Both libraries bring forth a vast set of features and are widely recognized in the community.

* * * * *

-   [Pandas](https://pandas.pydata.org/docs/index.html) ^2.0.3 🐼
    -   Description: Used for data reading and transformations.

* * * * *

-   [Blue](https://pypi.org/project/blue/) ^0.9.1 🔵
    -   Description: Coding standard adopted for the project.

* * * * *

-   [isort](https://pycqa.github.io/isort/) ^5.12.0 📑
    -   Description: A coding utility to organize imports in a consistent format.

* * * * *

-   [taskipy](https://pypi.org/project/taskipy/1.0.0/) ^1.11.0 🛠️
    -   Description: Facilitates development by creating tasks.

* * * * *

-   [pyarrow](https://arrow.apache.org/docs/python/index.html) ^12.0.1 🏹
    -   Description: Enables reading of .parquet data files.

* * * * *

-   [Docker](https://hub.docker.com/) 🐳
    -   Description: Docker is a platform designed to develop, ship, and run applications within containers. It ensures our application and its dependencies are packaged into an isolated container, which enhances portability and ease of deployment across varied environments.

* * * * *

Grasping the intricate details of these technologies will significantly augment the efficiency and effectiveness of engagement with the project. 🚀🌟


##  📝 **Next Steps**
***

Here are some next steps that can be implemented in the future:

### 1️⃣ API Creation using FastAPI

Development of an API using [FastAPI](https://fastapi.tiangolo.com/), a modern and fast framework for creating Python APIs. This will facilitate integration with other platforms and allow remote access to the project's resources.

### 2️⃣ Validation with Stakeholders

We plan to conduct several feedback sessions with our stakeholders to ensure the project aligns with the expectations and needs of the end users.

### 3️⃣ Monitoring Setup

Monitoring the performance and functionality of the system is crucial to ensure its reliability and efficiency. It's important to implement tools and processes for keeping an eye on the system.

### 4️⃣ Alert Setup for Slack or Email

To ensure a swift response to any issues that may arise, we'll implement alerts that will send notifications to Slack or predetermined emails in case of system failures.

### 5️⃣ Refactoring of the `dataframe_checker.py` class

Currently, the `dataframe_checker.py` class is responsible for validating input data. Initially, it wasn't built with PySpark, but ideally, its internal logic should be replaced with [PySpark](https://spark.apache.org/docs/latest/api/python/index.html) to optimize validation and preparation of data on large datasets.

### 6️⃣ Scheduling with Airflow

To automate and orchestrate our workflows, we will use [Airflow](https://airflow.apache.org/). It will assist us in defining, scheduling, and monitoring workflows programmatically.

### 7️⃣ Model Registration in MLflow

Lastly, to track and manage our machine learning model iterations, we will use [MLflow](https://mlflow.org/) to register, version, and share models.


## 💻 **CONTACT ME** 💻
***


 <p align="center">
<a  href="https://www.linkedin.com/in/marivaldotorres/">
    <img align="center"alt="Junior Torres | Linkedin" target="_blank" width="24px" src="assets\linkedin.png" />
  </a>

  <a href="https://www.instagram.com/mlenginner.py/">
    <img align="center" alt="Junior Torres | Instagram" target="_blank" width="24px" src="assets\instagram.png" />
  </a>
  <a href="mailto:juniortorres.mtj@gmail.com">
    <img align="center" alt="Junior Torres | Gmail" target="_blank" width="26px" src="assets\gmail.png" />
  </a>
  <a href="https://github.com/JuniorTorresMTJ">
    <img align="center" alt="Junior Torres | Github" target="_blank" width="26px" src="assets\github.svg" />
  </a>
 </p>