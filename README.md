# The Office



## Overview



## Architecture Diagram
![Architecture Diagram](https://raw.githubusercontent.com/nehaprabhavalkar/The-Office/master/images/office_diagram.jpg)

## Tech Stack

#### Python Libraries

- requests
- pandas
- sklearn
- plotly

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
│  ├─ imdb_scraping.py
│  └─ utils.py
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
    


## Setup


## License
MIT

