# Do students tend to different behaviours when doing their laundry?
(C) 2023-2024 Judith Henkel, Nalin Puvendran, Lenard Rommel and Kevin Weiss.


![Alt text](https://github.com/lenardrommel/washingmachine-analysis/blob/main/plots/averaged_distribution.png)

A group project for [Philipp Hennig's](https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/methoden-des-maschinellen-lernens/personen/philipp-hennig/) lecture "Data Literacy" at the University of Tuebingen.

Full report: https://www.overleaf.com/read/fxhfdfpqspwd#384f75

If you have questions or ideas please contact me via mail [Lenard Rommel](mailto:lenardrommel@icloud.com?subject=[GitHub:Data Literacy]%20Source%20Han%20Sans).

## Abstract
The objective of this paper is to identify washing machine usage patterns among university students and determine if there are significant differences in those patterns between female and male students. The analysis utilizes a data set gathered from a washing machine booking system of a student dorm.
The initial visualization reveals an expected downward trend in washing machine usage during semester breaks.
An examination of preferred washing time indicates no significant differences between female and male students, both in terms of preferred days and preferred times of the day.
Further analysis of the washing machine utilization rate shows that, while there is no significant difference in the average rate between female and male students, male students exhibit a stronger tendency toward extreme washing rates compared to their female counterparts. A permutation test, yielding a p-value of 0.04, indicates a statistical significance of this difference.

## Installation and Prerequisites
I doubt that anyone without sufficient knowledge reads this. 
But since this is a public repository I will explain the following steps in detail so that people with little knowledge have easy access.
Go to your IDE and open a new project. You can call it `washingmachine-analysis`.

Open up a (new) terminal in your IDE and navigate to the new project you ideally called `washingmachine-analysis`.
Then please obey the following steps (you can copy the contents of each box to your terminal). 

### Clone Repository
Clone this repo with:
```bash
git clone git@github.com:lenardrommel/washingmachine-analysis.git
```
### SSH Key Generation
If you encounter issues cloning the repository, consider [generating SSH keys](https://kinsta.com/blog/generate-ssh-key/):
```bash
ssh-keygen -t ed25519 -C "firstname.lastname@student.uni-tuebingen.de"
```
- Important: Do not enter a passphrase when generating the SSH keys, this will simplify the setup
- Important: Do not use `sudo` when creating the keys, otherwise the keys will be stored in the root directory (`/root/.ssh/` and not in your home directory `~/.ssh/`)
- If you are not already there move to the repo: 
```bash
cd washingmachine-analysis
```

### Environment Setup
This project was implemented in Python 3.10. Here is a tutorial of [how to update python](https://ioflood.com/blog/update-python-step-by-step-guide/).

Create a new environment with:
```bash
conda env create -file=envs\all.yaml
```
Activate the environment:
```bash
conda activate washing-machine
```

Now you should be able to run the complete code in your IDE.


## Project Setup
The project structure is straightforward. The `data` directory holds the original anonymized data, 
while `envs` manages the environment. Feel free to ignore these directories.
Plots are stored in `plots`. The primary code resides in the `analysis` directory, offering two convenient options:
- **All-in-One Jupyter Notebook:** `main.ipynb`
- **Individual Code Files:**
  - Judith Henkel: `analyse_average_washing_time.py`
  - Lenard Rommel: `firstVisualization.ipynb`
  - Nalin Puvendran & Kevin Weiss: `washing_time_usage.ipynb`

## Enjoy!
Feel free to explore the project and analyze the washing machine data. If you have any questions or issues, don't hesitate to reach out. Happy analyzing!


![Alt text](https://github.com/lenardrommel/washingmachine-analysis/blob/main/plots/data-for-year.png)

Histogram of the washing data for the whole year with highlighted holidays and moving average.
