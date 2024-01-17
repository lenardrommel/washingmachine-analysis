# Do students tend to different behaviours when doing their laundry?
(C) 2023-2024 Judith Henkel, Nalin Puvendran, Lenard Rommel and Kevin Weiss.

A group project for [Philipp Hennig's](https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/methoden-des-maschinellen-lernens/personen/philipp-hennig/) lecture "Data Literacy" at the University of Tuebingen.

## Abstract
We aim to analyze a self-gathered dataset of the washing machine usage of Judith's student dormitory.
This dataset encompasses occupant names, floor levels, occupancy times, and the specific washing machines used within the dormitory for the past 365 days. 
Our primary objective is to investigate recurring occupancy patterns and whether males or females use the washing machine more often. Further, we expect a change in occupancy during the semester breaks, but we cannot analyze yearly trends in this data due to insufficient data.

## Installation and Prerequisites
- Clone this repo with `git clone git@github.com:lenardrommel/washingmachine-analysis.git`
  - You may have to [generate SSH keys](https://kinsta.com/blog/generate-ssh-key/): `ssh-keygen -t ed25519 -C "firstname.lastname@student.uni-tuebingen.de"`if you cannot clone the repo
  - Important: Do not enter a passphrase when generating the SSH keys, this will simplify the setup
  - Important: Do not use `sudo` when creating the keys, otherwise the keys will be stored in the root directory (`/root/.ssh/` and not in your home directory `~/.ssh/`)
  - Add them to your GitHub account [here](https://github.com/settings/keys) by following [these steps](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
    - You may have to add github.com to the list of known hosts if you set up a new machine. You can do that by cloning a random repo, such as: `git clone git@github.com:jbeder/yaml-cpp.git`, and accepting the fingerprint (you won't need this repo afterwards).
- Move to the repo: `cd washingmachine-analysis`
- Activate the environment with `conda activate base`

## Analyzing the data
- we put everything in a jupyter notebook
