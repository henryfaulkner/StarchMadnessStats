# StarchMadnessStats Specification

## Project Overview

- **Project Name:** StarchMadnessStats
- **Type:** Post-mortem data analysis project
- **Core Functionality:** Analyze tournament results from a food-based tournament ("Starch Madness") to compile data, gain insights, and tell data stories
- **Target Users:** Tournament organizers and participants

## Technical Flow

The Python notebook performs the following:
1. Recursively read all JSON files from the `/recipes` directory
2. Calculate tournament score for each recipe using formula: `tournament_score = (won_round_one * 20) + (won_round_two * 30) + (won_round_three * 40) + (won_round_four * 50) + (won_round_five * 60)`
3. Store scores in in-memory objects and add to a single in-memory array
4. Create charts based on the data

## Required Data Charts

### 1. Scores per Recipe
- **Chart Type:** Bar chart
- **Ordering:** Descending by scores

### 2. Scores per Ingredient Type
- **Chart Type:** Bar chart
- **Ordering:** Descending by scores

### 3. Number of Times an Ingredient Appeared in Dataset
- **Chart Type:** Pie Chart

### 4. How Each Ingredient Scored Over Time (Per Round)
- **Chart Type:** Line Chart
- **Ordering:** Ascending by round (won_round_one, won_round_two, etc.)

### 5. Scores per Recipe's Ethnic Origin
- **Chart Type:** Bar chart
- **Ordering:** Descending by scores

### 6. Number of Times a Particular Ethnic Origin Appeared in Dataset
- **Chart Type:** Pie Chart

## User Stories

1. As a tournament organizer, I want to load all recipe data from JSON files so that I can perform analysis
2. As a tournament organizer, I want to see recipes ranked by their tournament score so that I can identify winners
3. As a tournament organizer, I want to analyze performance by ingredient type so that I can identify popular ingredients
4. As a tournament organizer, I want to analyze performance by ethnic origin so that I can understand cuisine representation
5. As a tournament organizer, I want to visualize round-by-round progression so that I can tell the tournament story

## Acceptance Criteria

1. All JSON files in `/recipes` directory are correctly parsed
2. Tournament scores are calculated correctly using the specified formula
3. All 6 chart types are generated with correct data
4. Charts are properly labeled with titles and axes
5. Data is sorted according to each chart's requirements
6. Notebook runs without errors and produces reproducible results

## Data Schema

Recipe JSON files must contain:
- `title`: Recipe name (string)
- `ethnic_origin`: Cultural/regional origin (string)
- `ingredients`: List of ingredients (array of strings)
- `won_round_one` through `won_round_five`: Binary (0/1) indicating tournament round wins (integers)
- `cooked_url`: Link to recipe on cooked.wiki (optional string)
- `source_url`: Original recipe source URL (optional string)
