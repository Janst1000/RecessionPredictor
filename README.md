# Recession Predictor - Phase 3 Project


## Navigating this Repo
The project is broken up into three main notebooks, in chronological order:

1. Data cleaning: This notebook makes the necessary API calls to the Nasdaq Datalink and imports local data. It then performs the necessary joins and saves the prepared DataFrame as a .csv file to be used in the model tuning notebook.

2. Model tuning: This notebook focuses on testing the different models against each other and determining a winner. It also creates visualizations to better understand model performance and

3. Simulation: This notebook takes the probability outputs of recession from 1963-2022 and uses it to simulate a basic portfolio strategy. The simulation takes that probability and "purchases" Dow Jones shares according to the probability that there will not be a recession, and purchases gold according to the probability that there will be a recession. This portfolio is updated quartely, as that is when new economic leading indicators come in to update the next model.



## Overview


## Business Problem


## Methods


![](/figures/StockSim.png)

## Conclusion
