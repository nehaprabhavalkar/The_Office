# The Office

## Overview

- Automated data collection of episode ratings and transcripts
- Automated data quality checks to ensure correctness of the data
- Infographics about the TV series
- Content-based recommendation system to recommend similar episodes 


## Architecture Diagram
![Architecture Diagram](https://raw.githubusercontent.com/nehaprabhavalkar/The_Office/master/images/office_diagram.jpg)

## Tech Stack

#### Python Libraries

- requests
- pandas
- Beautiful Soup
- sklearn
- nltk
- plotly

#### Deployment
- AWS EC2

## Project Directory Structure

```
The-Office
├─ .github
│  └─ ISSUE_TEMPLATE
│     ├─ story-template.md
│     └─ task-template.md
├─ .gitignore
├─ code
│  ├─ dialogues_scraping.py
│  ├─ episode_recommendation.py
│  ├─ graphs.py
│  ├─ helper.py
│  └─ imdb_scraping.py
├─ conf
│  └─ config.yml
├─ images
│  └─ office_diagram.jpg
├─ LICENSE
└─ README.md

```

## Files Description 
1. **config.yml** - configuration file
2. **data_cleaning.py** -  performs the following functions:-
    - removal of extra white spaces
    - removal of irrelevant punctuations
    - converts date into proper format
3. **dialogues_scraping.py** -  scrapes data from officequotes website 
    and stores into a csv file
4. **imdb_scraping.py** - scrapes data from IMDb website and stores
    into a csv file
5. **data_quality_check.py** - performs the following checks:-
    - row count check
    - null values check
6. **episode_recommendation.py** -  content based recommender module which
    recommends based on similar episode description
7. **graphs.py** - plots graph using plotly
8. **helper.py** - contains helper functions used frequently in other modueles
    


## Setup
#### For Deployment 

1. Clone the repository using 
   git clone https://github.com/nehaprabhavalkar/The_Office.git 

2. While launching your EC2 instance, go to Advanced Details and in User Data field add file setup.sh

3. Using any FTP application (eg. FileZilla) transfer the entire repository into your VM

4. Navigate into the folder and install the requirements using 
   pip install -r requirements.txt

5. Run using python3 imdb_scraping.py


## License
MIT