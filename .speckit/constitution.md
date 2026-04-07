# StarchMadnessStats Constitution

## Project Overview

- **Project Name:** StarchMadnessStats
- **Type:** Post-mortem data analysis project
- **Core Functionality:** Analyze tournament results from a food-based tournament ("Starch Madness") to compile data, gain insights, and tell data stories
- **Target Users:** Tournament organizers and participants interested in understanding tournament outcomes

## Core Principles

1. **Data-First Approach:** All analysis is grounded in the actual tournament data from recipe JSON files
2. **Reproducible Analysis:** Python notebook should be able to regenerate all insights from raw data
3. **Clear Visualization:** Charts and visualizations should tell compelling stories about the tournament
4. **Inclusive Storytelling:** Celebrate all participants and cuisines represented in the tournament

## Technical Standards

- Python-based data analysis using Jupyter/IPython notebook format
- JSON file format for recipe data storage
- Matplotlib or similar for data visualization
- Score calculation formula:
  - `tournament_score = (won_round_one * 20) + (won_round_two * 30) + (won_round_three * 40) + (won_round_four * 50) + (won_round_five * 60)`

## Data Schema

Recipe JSON files must contain:
- `title`: Recipe name
- `ethnic_origin`: Cultural/regional origin of the dish
- `ingredients`: List of ingredients
- `won_round_one` through `won_round_five`: Binary (0/1) indicating tournament round wins
- `is_celebrity_author`: Boolean indicating if the recipe was written by a celebrity
- `round_votes`: Array of vote counts for each round (votes in round_one, round_two, etc.)
- `cooked_url`: Link to recipe on cooked.wiki (optional)
- `source_url`: Original recipe source URL (optional)

## Feature List

1. **Tournament Score Calculation** - Calculate scores for each recipe based on round wins
2. **Score per Recipe Chart** - Bar chart showing recipes ranked by tournament score
3. **Ingredient Performance Analysis** - Analyze how different ingredients perform
4. **Ethnic Origin Analysis** - Performance breakdown by cuisine type
5. **Round-by-Round Progression** - Track how recipes advance through tournament rounds
6. **Round Voting Patterns** - Analyze vote counts per round to understand voting trends
7. **Celebrity Author Analysis** - Compare performance of celebrity-authored recipes vs others
8. **Data Storytelling** - Generate insights and narratives from the tournament data
