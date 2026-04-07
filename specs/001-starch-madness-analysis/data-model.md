# Data Model: StarchMadness Tournament Data Analysis

## Core Entities

### Recipe

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Recipe name |
| ethnic_origin | string | Yes | Cultural/regional origin of the dish |
| ingredients | array of strings | Yes | List of ingredients |
| won_round_one | integer (0/1) | Yes | Won first round |
| won_round_two | integer (0/1) | Yes | Won second round |
| won_round_three | integer (0/1) | Yes | Won third round |
| won_round_four | integer (0/1) | Yes | Won fourth round |
| won_round_five | integer (0/1) | Yes | Won final round |
| written_by_celebrity_author | boolean | Yes | Recipe written by celebrity |
| vote_count_round_one | integer or null | Yes | Vote count round 1 |
| vote_count_round_two | integer or null | Yes | Vote count round 2 |
| vote_count_round_three | integer or null | Yes | Vote count round 3 |
| vote_count_round_four | integer or null | Yes | Vote count round 4 |
| vote_count_round_five | integer or null | Yes | Vote count round 5 |
| vote_percentage_round_one | float or null | Yes | Vote percentage round 1 |
| vote_percentage_round_two | float or null | Yes | Vote percentage round 2 |
| vote_percentage_round_three | float or null | Yes | Vote percentage round 3 |
| vote_percentage_round_four | float or null | Yes | Vote percentage round 4 |
| vote_percentage_round_five | float or null | Yes | Vote percentage round 5 |
| cooked_url | string or null | No | Link to recipe on cooked.wiki |
| source_url | string or null | No | Original recipe source URL |

### Calculated Fields

| Field | Type | Description |
|-------|------|-------------|
| tournament_score | integer | Calculated as: (won_round_one × 20) + (won_round_two × 30) + (won_round_three × 40) + (won_round_four × 50) + (won_round_five × 60) |

## Data Relationships

- Each Recipe has exactly one EthnicOrigin
- Each Recipe has multiple Ingredients (1-to-many via array)
- Each Recipe has multiple VoteData entries (one per round)
- TournamentScore is derived from Recipe's round win fields

## Validation Rules

- won_round_n fields must be 0 or 1
- vote_count_round_n must be non-negative integers or null
- vote_percentage_round_n must be 0-100 floats or null
- ingredients array must contain at least one element
- title must not be empty