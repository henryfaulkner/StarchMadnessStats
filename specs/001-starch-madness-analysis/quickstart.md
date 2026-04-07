# Quickstart: StarchMadness Tournament Data Analysis

## Prerequisites

- Python 3.10+
- Jupyter Notebook or JupyterLab

## Installation

Install required dependencies:

```bash
pip install pandas seaborn matplotlib jupyter
```

## Data Setup

Place your recipe JSON files in the `/recipes` directory. Each JSON file should follow the schema defined in `data-model.md`.

## Running the Analysis

1. Start Jupyter:
   ```bash
   jupyter notebook
   ```

2. Open `starch_madness_analysis.ipynb` in the Jupyter interface

3. Run all cells (Cell → Run All)

## Output

The notebook generates 9 charts:
1. Scores per Recipe (bar chart, descending order)
2. Scores per Ingredient Type (bar chart, top 15 by average score)
3. Ingredient Frequency (pie chart, top 10)
4. Ingredient Performance Over Time (line chart by round)
5. Scores per Ethnic Origin (bar chart, descending)
6. Ethnic Origin Frequency (pie chart)
7. Round Voting Patterns (line chart)
8. Celebrity Author Performance (box plot)
9. Normalized Voting Participation (line chart, normalized by matchups)

## Troubleshooting

- **Empty charts**: Ensure `/recipes` directory contains valid JSON files
- **Missing data**: Null/missing optional fields (cooked_url, source_url, vote data) are handled gracefully
- **Import errors**: Ensure all dependencies are installed