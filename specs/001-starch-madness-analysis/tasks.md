# Tasks: StarchMadness Tournament Data Analysis

**Feature**: 001-starch-madness-analysis
**Generated**: 2026-04-07

## Implementation Strategy

This is a single Python Jupyter notebook. Implementation follows an MVP approach:
- **MVP Scope**: Phase 1-2 (Setup + Data Loading + Score Calculation + First Chart)
- **Incremental Delivery**: Each user story adds one or more charts to the notebook

---

## Phase 1: Setup

Goal: Prepare development environment with all required dependencies

**Independent Test**: `pip install pandas seaborn matplotlib jupyter` succeeds without errors

- [x] T001 Install required Python packages: pandas, seaborn, matplotlib, jupyter

---

## Phase 2: Foundational (US1 + US2)

Goal: Load recipe data and calculate tournament scores, generate first visualization

**Independent Test**: Run notebook and verify recipes loaded + scores calculated + bar chart displays

- [x] T002 [US1] Create Jupyter notebook starch_madness_analysis.ipynb in repository root
- [x] T003 [US1] Add import cell: import os, json, glob, pandas, numpy, seaborn, matplotlib.pyplot
- [x] T004 [US1] Implement data loading: glob.glob('recipes/*.json'), read all JSON files into list
- [x] T005 [US1] Convert recipes list to pandas DataFrame
- [x] T006 [US2] Calculate tournament_score using formula: (won_round_one*20 + won_round_two*30 + won_round_three*40 + won_round_four*50 + won_round_five*60)
- [x] T007 [US2] Generate bar chart: Scores per Recipe in descending order using Seaborn barplot
- [x] T008 [US2] Add chart title "Tournament Scores per Recipe" and axis labels

---

## Phase 3: Ingredient Analysis (US3)

Goal: Analyze performance by ingredient type

**Independent Test**: Run notebook and verify ingredient bar chart and pie chart display correctly

- [x] T009 [P] [US3] Extract all ingredients from DataFrame into flat list with scores
- [x] T010 [P] [US3] Group by ingredient and calculate average tournament_score
- [x] T011 [US3] Generate bar chart: Scores per Ingredient Type (top 15, descending)
- [x] T012 [US3] Generate pie chart: Ingredient Frequency (top 10)
- [x] T013 [US3] Add titles and labels to both charts

---

## Phase 4: Ethnic Origin Analysis (US4)

Goal: Analyze performance by ethnic origin

**Independent Test**: Run notebook and verify ethnic origin bar chart and pie chart display correctly

- [x] T014 [P] [US4] Group by ethnic_origin and calculate total tournament_score
- [x] T015 [P] [US4] Count recipes per ethnic_origin
- [x] T016 [US4] Generate bar chart: Scores per Ethnic Origin (descending)
- [x] T017 [US4] Generate pie chart: Ethnic Origin Frequency
- [x] T018 [US4] Add titles and labels to both charts

---

## Phase 5: Round Progression (US5)

Goal: Track recipe advancement through tournament rounds

**Independent Test**: Run notebook and verify line chart shows progression across rounds

- [x] T019 [US5] Create round columns list: won_round_one through won_round_five
- [x] T020 [US5] For top 5 ingredients, calculate average wins per round
- [x] T021 [US5] Generate line chart: Ingredient Performance Over Time (x=round, y=avg_wins)
- [x] T022 [US5] Add legend for multiple ingredients, title, and axis labels

---

## Phase 6: Voting Patterns (US6)

Goal: Analyze vote counts per round

**Independent Test**: Run notebook and verify voting line chart displays correctly

- [x] T023 [US6] Create vote_count columns list: vote_count_round_one through vote_count_round_five
- [x] T024 [US6] Sum vote counts per round across all recipes
- [x] T025 [US6] Generate line chart: Total Votes per Round (x=round, y=total_votes)
- [x] T026 [US6] Handle null values gracefully using fillna(0)
- [x] T027 [US6] Add title and axis labels

---

## Phase 7: Celebrity Author (US7)

Goal: Compare celebrity vs non-celebrity authored recipes

**Independent Test**: Run notebook and verify box plot compares both groups

- [x] T028 [US7] Create author_type column: map written_by_celebrity_author to "Celebrity Author" / "Non-Celebrity"
- [x] T029 [US7] Generate box plot: Score distribution by author type
- [x] T030 [US7] Add title "Score Distribution: Celebrity vs Non-Celebrity Authors"
- [x] T031 [US7] Handle edge case: if no celebrity authors, show appropriate message

---

## Phase 8: Normalized Voting (US8)

Goal: Normalize votes by matchup count per round

**Independent Test**: Run notebook and verify normalized line chart displays correctly

- [x] T032 [US8] Define matchups per round: [16, 8, 4, 2, 1]
- [x] T033 [US8] Calculate normalized votes: total_votes / matchups per round
- [x] T034 [US8] Generate line chart: Normalized Votes per Matchup by Round
- [x] T035 [US8] Add title "Normalized Votes per Matchup by Round"
- [x] T036 [US8] Print normalized data table for verification

---

## Phase 9: Polish

Goal: Add summary statistics and ensure all charts meet quality standards

**Independent Test**: Run notebook and verify summary statistics print correctly

- [x] T037 Add markdown cell with section "Summary Statistics"
- [x] T038 Print: Total Recipes, Average Tournament Score, Highest Score
- [x] T039 Print: Total Votes Round 1, Celebrity vs Non-Celebrity counts
- [x] T040 Review all charts have Seaborn default styling
- [x] T041 Verify all 9 charts render without errors

---

## Dependencies

```
Phase 2 (US1+US2) ─────┐
                        ├──> Phase 3 (US3) ──> Phase 4 (US4) ──> Phase 5 (US5)
Phase 2 is prerequisite                     (parallel to Phase 5)
for all subsequent phases
                                            └──> Phase 6 (US6) ──> Phase 7 (US7) ──> Phase 8 (US8)
                                                                      │
                                                                      └──> Phase 9 (Polish)
```

## Parallel Opportunities

- T009/T010 can run in parallel with T014/T015 (different data aggregations)
- T011 can run in parallel with T016 (different charts)
- T012 can run in parallel with T017 (different charts)

## MVP Scope

**Minimum Viable Product**: Phase 1 + Phase 2 (Tasks T001-T008)
- Install dependencies
- Load 32 recipe JSON files
- Calculate tournament scores
- Display bar chart of scores per recipe

All remaining phases add incremental charts and analysis capabilities.

---

## Task Summary

| Phase | Tasks | User Story |
|-------|-------|------------|
| Phase 1: Setup | T001 | - |
| Phase 2: Foundational | T002-T008 | US1, US2 |
| Phase 3: Ingredient | T009-T013 | US3 |
| Phase 4: Ethnic Origin | T014-T018 | US4 |
| Phase 5: Progression | T019-T022 | US5 |
| Phase 6: Voting | T023-T027 | US6 |
| Phase 7: Celebrity | T028-T031 | US7 |
| Phase 8: Normalized | T032-T036 | US8 |
| Phase 9: Polish | T037-T041 | - |

**Total Tasks**: 41