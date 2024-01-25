# Do students tend to different behaviours when doing their laundry?
(C) 2023-2024 Judith Henkel, Nalin Puvendran, Lenard Rommel and Kevin Weiss.


![Alt text](https://github.com/lenardrommel/washingmachine-analysis/blob/main/plots/averaged_distribution.png)

A group project for [Philipp Hennig's](https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/methoden-des-maschinellen-lernens/personen/philipp-hennig/) lecture "Data Literacy" at the University of Tuebingen.

Full report: https://www.overleaf.com/read/fxhfdfpqspwd#384f75

## Abstract
The objective of this paper is to identify washing machine usage patterns among university students and determine if there are significant differences in those patterns between female and male students. The analysis utilizes a data set gathered from a washing machine booking system of a student dorm.
The initial visualization reveals an expected downward trend in washing machine usage during semester breaks.
An examination of preferred washing time indicates no significant differences between female and male students, both in terms of preferred days and preferred times of the day.
Further analysis of the washing machine utilization rate shows that, while there is no significant difference in the average rate between female and male students, male students exhibit a stronger tendency toward extreme washing rates compared to their female counterparts. A permutation test, yielding a p-value of 0.04, indicates a statistical significance of this difference.

## Installation and Prerequisites
- Clone this repo with `git clone git@github.com:lenardrommel/washingmachine-analysis.git`
  - You may have to [generate SSH keys](https://kinsta.com/blog/generate-ssh-key/): `ssh-keygen -t ed25519 -C "firstname.lastname@student.uni-tuebingen.de"`if you cannot clone the repo
  - Important: Do not enter a passphrase when generating the SSH keys, this will simplify the setup
  - Important: Do not use `sudo` when creating the keys, otherwise the keys will be stored in the root directory (`/root/.ssh/` and not in your home directory `~/.ssh/`)
  - Move to the repo: `cd washingmachine-analysis`
- Create new environment with `conda env create -file=envs\all.yaml`
- Activate the environment with `conda activate washing-machine`

## Project set up
This project has a simple structure. For overview we have a `data` directory with the original anonomized data, 
for the environment we have an `envs` directory. You don't need to access these directory. So please ignore them.
We save every plot in `plots` for obvious reasons. The code for our project you can find in `analysis`.
Here we have two options for you:
- Everything is put together in one jupyter-notebook `main`, easy accessible.
- We also have the original code from each group member.
  - Judith Henkel: `analyse_average_washing_time.py`
  - Lenard Rommel: `firstVisualization.ipynb`
  - Nalin Puvendran & Kevin Weiss: `washing_time_usage.ipynb`

## Enjoy!

