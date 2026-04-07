# Implementation Plan: StarchMadness Tournament Data Analysis

**Branch**: `001-starch-madness-analysis` | **Date**: 2026-04-07 | **Spec**: specs/001-starch-madness-analysis/spec.md

**Input**: Feature specification from `/specs/001-starch-madness-analysis/spec.md`

## Summary

Python Jupyter notebook that loads recipe JSON files from `/recipes`, calculates tournament scores using the weighted formula (20×R1 + 30×R2 + 40×R3 + 50×R4 + 60×R5), and generates 9 Seaborn visualizations including score rankings, ingredient analysis, ethnic origin breakdown, voting patterns, and normalized participation trends.

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: pandas, seaborn, matplotlib, jupyter  
**Storage**: JSON files in `/recipes` directory (32 recipe files)  
**Testing**: Not applicable - reproducibility verified by re-running notebook  
**Target Platform**: Local Jupyter environment  
**Project Type**: Data analysis notebook  
**Performance Goals**: N/A - post-mortem analysis, small dataset (~32 recipes)  
**Constraints**: Must handle null/missing optional fields gracefully  
**Scale**: 32 recipe entries, 9 visualizations

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Constitution Principle | Status | Notes |
|------------------------|--------|-------|
| Data-First Approach | PASS | All analysis grounded in actual recipe JSON data |
| Reproducible Analysis | PASS | Python notebook regenerates all insights from raw JSON |
| Clear Visualization | PASS | Seaborn charts with proper titles and labels |
| Inclusive Storytelling | PASS | Ethnic origin analysis celebrates all cuisines |
| Technical Standards | PASS | Python/Jupyter, JSON, Matplotlib/Seaborn, correct formula |

## Project Structure

### Documentation (this feature)

```text
specs/001-starch-madness-analysis/
├── plan.md              # This file (/speckit.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0 output (N/A - no unknowns)
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── tasks.md             # Phase 2 output (NOT created by /speckit.plan)
└── checklists/          # Validation checklists
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)

```text
recipes/                 # Input data - 32 JSON files
starch_madness_analysis.ipynb  # Main analysis notebook (to be created)
```

**Structure Decision**: Single Jupyter notebook in repository root; all data loaded from `/recipes` directory. No additional source code structure needed.

## Phase 0: Research

No research needed - all technical details are known:
- Python + Jupyter standard stack
- Seaborn + Matplotlib for visualization
- JSON file format already defined in constitution
- Score formula explicitly specified in requirements

## Phase 1: Design

### Data Model

From spec.md Key Entities:
- **Recipe**: title, ethnic_origin, ingredients[], won_round_one through won_round_five (0/1), written_by_celebrity_author (bool), vote_count_round_one through vote_count_round_five (int, may be null), vote_percentage_round_one through vote_percentage_round_five (float, may be null), cooked_url (optional), source_url (optional)
- **TournamentScore**: calculated integer = sum(weight × won_round_n) for n in 1-5
- **Ingredient**: string from recipe.ingredients array
- **EthnicOrigin**: string from recipe.ethnic_origin
- **VoteData**: {vote_count, vote_percentage} per round

### Interface Contracts

No external interfaces - this is a local analysis notebook. Users run the notebook directly in Jupyter.

### Quickstart

1. Install dependencies: `pip install pandas seaborn matplotlib jupyter`
2. Place recipe JSON files in `/recipes` directory
3. Run notebook: `jupyter notebook starch_madness_analysis.ipynb`
4. View generated charts

### Agent Context Update

New technologies introduced: pandas, seaborn, matplotlib, jupyter