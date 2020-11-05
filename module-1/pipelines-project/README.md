![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Data Pipeline

## Overview

The goal of this project is for you to practice what you have learned so far on this program. For this project, you will start with a data set of your choice. You will need to import it, use your newly-acquired skills to build a data pipeline that processes the data and produces a result. You should demonstrate your proficiency with the tools we covered (functions, classes, list comprehensions, string operations, pandas, and error handling, etc.) in your pipeline.

**You will be working individually for this project**, but we'll be guiding you along the process and helping you as you go. Show us what you've got!

### What is a pipeline?
A data pipeline is a series of data processes in which the output of each one is the input of the next, forming a chain. 

---

## Technical Requirements

The technical requirements for this project are as follows:

* You must construct a data pipeline with the majority of your code wrapped in functions.
* The following data pipeline stages should be covered: acquisition, wrangling, analysis, and reporting.
* You must demonstrate all the topics we covered in the chapter (functions, list comprehensions, string operations, and error handling) in your processing of the data.
* There should be some data set that gets imported and some result that gets exported.
* Your code should be saved in a Python executable file (.py), your data should be saved in a folder named data, and your results should be saved in a folder named output.
* You should also include a README.md file that describes the steps you took and your thought process as you built your data pipeline.

## TO DO's

- A) Find a dataset to start you work! A great place to start looking would be [Awesome Public Data Sets](https://github.com/awesomedata/awesome-public-datasets) and [Kaggle Data Sets](https://www.kaggle.com/datasets).
  
- B) Clean and wrangle your dataset, prepare the data for your needs and intentions.

- C) Enrich the dataset with external data, you have to choose at least one of the following:
  - Get data from an API.
    - _Note:_ The API you use may require authentication via token or oAuth.
  - Do web scraping with python `requests` module.
    - _Note:_ Some dynamic pages with lots of javascript code may not be scraped with requests. A more advanced tool such as `selenium` might be needed.

- D) The data you bring in to enrich the dataset must be related to it and complement it! Figure out how it fits together and how you prepare the data of both sources for your report.
  
- E) Create some reports containing valuable data from the dataset + enrichment. Some of the things you may do are:
  - Simply sumarize the data and do some basic statistics \(`mean`, `max`, `min`, `std`, etc.).
  - Do domain based statistics or data aggregations using `groupby()` .
  - `LOTS AND LOTS` of plots, of all types and colors.
  - Go nuts with the investigation. 

- F) The finished report must be a `very pretty` jupyter notebook, with text, clean code, meaningful outputs, plots and charts. Try telling a story with your data, that is, conduct us (the readers) through your findings and lead us into your conclusions.
  - _Note:_ The report jupyter **must** be separate from the code for cleaning, acquiring, processing data, etc. These may be in other jupyters or in `.py` modules. _Be not afraid to modulate 🎶_



## Super Ultra Mega Blaster Tips

* **Examine the data**.

* **Break the project down into different steps** - A hundred simple tasks are better than a single complicated one

* **Use the tools in your tool kit** - your knowledge of intermediate Python as well as some of the things you've learned in the bootcamp. This is a great way to start tying everything you've learned together!

* **Work through the lessons in class** & ask questions when you need to! 

* Think about adding relevant code to your project each day, instead of, you know... _procrastinating_.

* **Commit early, commit often**, don’t be afraid of doing something incorrectly because you can always roll back to a previous version. Name your commits well.

* **Consult documentation and resources provided** to better understand the tools you are using and how to accomplish what you want. GIYF.

* **Have fun! Never give up! Be proud of your work!**

## Useful Resources

* [Python Functional Programming How To Documentation](https://docs.python.org/3.7/howto/functional.html)
* [Python List Comprehensions Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Python Errors and Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
* [StackOverflow String Operation Questions](https://stackoverflow.com/questions/tagged/string+python)
