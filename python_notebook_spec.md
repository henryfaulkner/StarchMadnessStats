# Specification for Starch Madness Data Analysis's Python Notebook

## Base technical flow

- Recursively read all JSON files from the /recipes directory, calculating the score for each recipe based on this formula (tournament_score = (won_round_one * 20) + (won_round_two * 30) + (won_round_three * 40) + (won_round_four * 50) + (won_round_five * 60)), store score in in-memory object, and add each in-memory object a single in-memory array
- Create charts based on data

## Required Data Charts

### Scores per recipe 

- Bar chart (descending order by scores)

### Scores per ingredient type

- Bar chart (descending order by scores)

### Number of times an ingredient appreared in dataset

- Pie Chart

### How each ingredient scored over time (per round in ascending order, "won_round_one" then "won_round_two", etc.)

- Line Chart

### Scores per recipe's ethnic origin

- Bar chart (descending order by scores)

### Number of times a particular ethnic origin appreared in dataset

- Pie Chart