# Synthetic-Data-Generation-Of-Cheque-Leaf

Cheque leaf are very confidential data which can't be found easily in the Internet, but to train machine learning models regarding cheque leaf we need its dataset.

The Synthetic Data Generation of Cheque Leaf project aims to develop a system for generating realistic and accurate synthetic cheque dataset for use in training machine learning models. The system will use a combination of computer vision techniques and deep learning algorithms to train Synthetic data generation algorithm using cheque images to generate dataset with a high degree of variability in terms of features.

The system will be designed to generate synthetic cheque dataset that closely mimic real-world cheques, while also being customizable to meet the needs of specific training tasks. The synthetic data will be validated and tested to ensure that it accurately represents the range of variability present in real-world cheque images.

Also, the dataset of cheque is processed with statistical data visualization to validated and summarize the huge data to the user easily.

**EXISTING SYSTEM**

In Existing system, the datasets are not found in Internet or in any other medium as Cheque leaf are very confidential data, only few images of specimen cheque leaf are found through Kaggle but with that we can't train any machine learning models directly.

**Disadvantages** :

**Missing Dataset**.

As datasets are not found in Internet or in any other medium as Cheque leaf are very confidential data.

**Only 100s of Data (image)**.

Only few images of specimen cheque leaf are available with which the dataset creation is not possible.

![Picture1](https://github.com/kheshore/Synthetic-Data-Generation-Of-Cheque-Leaf/assets/43311731/be328fdb-d393-4bdf-b9dc-6c833b426017) 

FIG 1 Existing System – Specimen Cheque Leaf in IMG Format

**Can't train the ML models directly**.

As specimen cheques leaf are only available in Image format, which has to be converted into dataset using Computer vision and then Train the Machine Learning models, which is a huge process and Time consuming.

**.**

**PROPOSED SYSTEM**

In proposed system, Using computer vision and machine learning technologies a machine learning algorithm is trained which can be used to generate synthetic dataset. The User Experience (UX) is very human-centric and understandable as it contains a Graphical User Interference (GUI) so it is easy to analyse any dataset in a single execution with multiple graphs and charts, even multiple datasets can be analysed together, also it is cross-platform such that all the package requirements are predefined and installed along with the script which makes it a platform independent script.

**Advantages** :

**GUI Based – Better UX**.

GUI (Graphical User Interface) plays a significant role in creating a better user experience (UX) for digital products. A well-designed GUI can make it easier for users to interact with a product, understand how it works, and accomplish their goals more efficiently.

**Platform Independent Script.**

A platform-independent script is a script that can run on multiple platforms or operating systems without requiring any modifications or adjustments. This means that the script can be written once and then deployed on any platform that supports the required scripting environment.

**Large dataset can be created in very less time.**

Processing large datasets can be a time-consuming task, especially if the data needs to be processed in real-time through various methods and techniques like RNN, Faker, Random can help to process large datasets quickly

**Can train ML models directly.**

As dataset of cheques leaf are available in csv format, which can be directly used to train the Machine Learning models in less time.

**SOFTWARE SPECIFICATION**

| **COMPONENTS** | **REQUIREMENTS** |
| --- | --- |
| OPERATING SYSTEM | Windows 8 and Above |
| FRONT END | Python (TKinter) |
| BACK END | Python (Seaborn) |

**HARDWARE SPECIFICATION**

| **COMPONENTS** | **REQUIREMENTS** |
| --- | --- |
| CPU | x86 64-bit CPU (Intel / AMD architecture) |
| RAM | 2GB Minimum |
| STORAGE | 5GB Minimum disk space |
| PERIPHERALS | Common Peripherals (Mouse, Keyboard,..) |

**MODULE DESCRIPTION**

**Module – 1 (Dataset Creation)**

**Machine Learning – Data Set**

A dataset in machine learning is, quite simply, a collection of data pieces that can be treated by a computer as a single unit for analytic and prediction purposes. This means that the data collected should be made uniform and understandable for a machine that doesn't see data the same way as humans do. For this, after collecting the data, it's important to pre-process it by cleaning and completing it, as well as annotate the data by adding meaningful tags readable by a computer.

A tabular dataset can be understood as a database table or matrix, where each column corresponds to a particular variable, and each row corresponds to the fields of the dataset. The most supported file type for a tabular dataset is "Comma Separated File," or CSV. But to store a "tree-like data," we can use the JSON file more efficiently.

The dataset in CSV format contains the following parameters.

  - Cheque Number,
  - Date,
  - Payee Name,
  - Account Number,
  - Amount,
  - Bank Name - ['SBI', 'HDFC', 'ICICI', 'KOTAK', 'HSBC', 'KVB'],
  - Cheque Type - ['bearer', 'order', 'crossed', 'open', 'self', 'traveller'].

**Faker**

Faker is a Python library that generates fake data. Fake data is often used for testing or filling databases with some random data, which can be trained and infused with ML models.

**Random**

Random is a Python library that generates random data with given list or by generation. Random data is often used for testing or filling databases with some random data.

**Module – 1 (Statistical Data Visualization)**

**Seaborn**

Seaborn is a library for making statistical graphics in Python. It builds on top of matplotlib and integrates closely with pandas data structures.

Seaborn helps to explore and understand the data. Its plotting functions operate on data frames and arrays containing whole datasets and internally perform the necessary semantic mapping and statistical aggregation to produce informative plots. Its dataset-oriented, declarative API lets you focus on what the different elements of your plots mean, rather than on the details of how to draw them.

Following are the Statistical Data Visualization for cheque leaf dataset

  - Heatmap of the cheque leaf data,
  - Bar chart of average amounts per bank,
  - Average amount per bank,

**Tkinter**

Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

The tkinter package ("Tk interface") is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

The UI contains following buttons.

- Module 1
  - Select Save Location – Used to select the directory of created dataset.
  - Generate – Used to start the Model and create the dataset.
- Module 2


  - Select CSV File – Used to Select the directory of the dataset.
