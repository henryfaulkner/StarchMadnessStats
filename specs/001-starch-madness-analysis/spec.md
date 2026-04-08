# Feature Specification: StarchMadness Tournament Data Analysis

**Feature Branch**: `001-starch-madness-analysis`  
**Created**: 2026-04-07  
**Status**: Draft  
**Input**: User description: "look at C:\Projects\StarchMadnessStats\.speckit\spec.md" with clarification: "Focus on data gather and chart formulation. charts should visually pleasing."

## Clarifications

### Session 2026-04-07

- Q: Chart visual styling preference → A: Use Seaborn and its default styling

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Load and Parse Recipe Data (Priority: P1)

As a tournament organizer, I want to load all recipe data from JSON files so that I can perform analysis on the tournament results.

**Why this priority**: This is the foundational requirement - without loading data, no analysis can occur. All downstream features depend on this.

**Independent Test**: Can be tested by verifying all JSON files in `/recipes` directory are parsed correctly and data is available for subsequent analysis steps.

**Acceptance Scenarios**:

1. **Given** JSON files exist in `/recipes` directory, **When** the notebook runs, **Then** all recipe data is loaded into memory
2. **Given** JSON files contain all required schema fields, **When** the notebook runs, **Then** each recipe object contains title, ethnic_origin, ingredients, round wins, vote counts, and author information
3. **Given** JSON files are missing optional fields (cooked_url, source_url), **When** the notebook runs, **Then** those fields are handled gracefully with null/empty values

---

### User Story 2 - Calculate and Visualize Tournament Scores (Priority: P1)

As a tournament organizer, I want to see recipes ranked by their tournament score so that I can identify winners and understand relative performance.

**Why this priority**: This is the primary output - ranking recipes by their tournament success is the core value proposition of the analysis.

**Independent Test**: Can be verified by running the analysis and checking that bar chart displays all recipes sorted in descending score order with correct score calculations.

**Acceptance Scenarios**:

1. **Given** recipes with round win data, **When** scores are calculated using the formula, **Then** each recipe has a tournament_score = (won_round_one × 20) + (won_round_two × 30) + (won_round_three × 40) + (won_round_four × 50) + (won_round_five × 60)
2. **Given** multiple recipes have been scored, **When** the bar chart is generated, **Then** recipes are displayed in descending order by score
3. **Given** recipes have won zero rounds, **When** score is calculated, **Then** the resulting score is 0

---

### User Story 3 - Ingredient Performance Analysis (Priority: P2)

As a tournament organizer, I want to analyze performance by ingredient type so that I can identify which ingredients are most associated with successful recipes.

**Why this priority**: Provides insights into what ingredients contribute to tournament success, helping future participants make informed choices.

**Independent Test**: Can be verified by checking that bar chart shows ingredient types ranked by average score and pie chart shows ingredient frequency.

**Acceptance Scenarios**:

1. **Given** recipes with ingredient lists, **When** analyzing by ingredient, **Then** each unique ingredient is tracked across all recipes
2. **Given** ingredient performance analysis, **When** bar chart is generated, **Then** ingredients are displayed in descending order by average score
3. **Given** ingredient frequency analysis, **When** pie chart is generated, **Then** each ingredient shows its proportion of total appearances

---

### User Story 4 - Ethnic Origin Analysis (Priority: P2)

As a tournament organizer, I want to analyze performance by ethnic origin so that I can understand cuisine representation and performance across the tournament.

**Why this priority**: Provides cultural insights and helps understand diversity in the tournament - aligns with the "Inclusive Storytelling" principle.

**Independent Test**: Can be verified by checking that bar chart shows ethnic origins ranked by score and pie chart shows cuisine representation.

**Acceptance Scenarios**:

1. **Given** recipes with ethnic_origin field, **When** analyzing by origin, **Then** each unique ethnic origin is tracked
2. **Given** ethnic origin performance analysis, **When** bar chart is generated, **Then** origins are displayed in descending order by aggregate score
3. **Given** ethnic origin frequency analysis, **When** pie chart is generated, **Then** each origin shows its proportion of total recipes

---

### User Story 5 - Round-by-Round Progression Analysis (Priority: P2)

As a tournament organizer, I want to visualize round-by-round progression so that I can tell the tournament story and understand how recipes advanced.

**Why this priority**: Enables narrative storytelling about the tournament - who advanced, when they were eliminated, and overall progression patterns.

**Independent Test**: Can be verified by checking that line chart shows ingredient performance across each round in ascending order.

**Acceptance Scenarios**:

1. **Given** recipes with round win data, **When** analyzing progression, **Then** each round (1-5) is represented on the x-axis
2. **Given** round progression chart, **When** generated, **Then** line chart shows how ingredients or recipes performed at each round
3. **Given** recipes that won multiple rounds, **When** plotted, **Then** the progression shows the cumulative advancement pattern

---

### User Story 6 - Round Voting Patterns Analysis (Priority: P3)

As a tournament organizer, I want to analyze voting patterns across rounds so that I can understand voter engagement and how voting evolved throughout the tournament.

**Why this priority**: Provides behavioral insights about the tournament - whether voting increased/decreased and how engaged voters were at each stage.

**Independent Test**: Can be verified by checking that line chart shows vote counts and/or percentages per round.

**Acceptance Scenarios**:

1. **Given** vote data exists for rounds, **When** analyzing patterns, **Then** vote counts and/or percentages are plotted per round
2. **Given** vote percentage data exists, **When** chart is generated, **Then** percentages show the relative share of votes at each round
3. **Given** null vote data for some rounds, **When** chart is generated, **Then** missing data is handled gracefully without errors

---

### User Story 7 - Celebrity Author Performance Analysis (Priority: P3)

As a tournament organizer, I want to compare celebrity-authored recipes against others so that I can identify any "celebrity effect" on consistency and performance.

**Why this priority**: Interesting analytical insight - whether celebrity association correlates with tournament success or consistency.

**Independent Test**: Can be verified by checking that box plot compares score distributions between celebrity and non-celebrity authored recipes.

**Acceptance Scenarios**:

1. **Given** recipes with written_by_celebrity_author flag, **When** analyzing, **Then** recipes are split into two groups
2. **Given** celebrity vs non-celebrity comparison, **When** box plot is generated, **Then** both groups show median, quartiles, and outliers
3. **Given** no celebrity-authored recipes exist, **When** analysis runs, **Then** the chart handles this gracefully with appropriate message

---

### User Story 8 - Normalized Voting Participation Analysis (Priority: P2)

As a tournament organizer, I want to see how voting participation changed per round, normalized for the 32-entry elimination bracket structure, so that I can understand voter engagement trends as the tournament narrowed.

**Why this priority**: Raw vote counts decrease naturally as recipes are eliminated. Normalizing shows whether voter engagement increased, decreased, or stayed constant throughout the tournament independent of the bracket structure.

**Independent Test**: Can be verified by checking that line chart shows normalized vote participation per round accounting for the decreasing number of contestants (Round 1: 32, Round 2: 16, Round 3: 8, Round 4: 4, Round 5: 2).

**Acceptance Scenarios**:

1. **Given** vote counts per round and round win data, **When** normalizing, **Then** votes are divided by the number of matchups in that round (16 in R1, 8 in R2, 4 in R3, 2 in R4, 1 in R5)
2. **Given** normalized voting data, **When** line chart is generated, **Then** x-axis shows rounds 1-5 in ascending order, y-axis shows normalized votes per matchup
3. **Given** trend analysis, **When** chart is generated, **Then** the line clearly shows whether participation increased, decreased, or plateaued across rounds

---

### Edge Cases

- What happens when `/recipes` directory is empty?
- How does system handle malformed JSON files?
- How are duplicate recipe titles handled?
- What happens when vote_count is null for some rounds?
- How are recipes with missing ethnic_origin handled?
- What happens when ingredients array is empty?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST recursively read all JSON files from the `/recipes` directory
- **FR-002**: System MUST calculate tournament scores using the formula: `tournament_score = (won_round_one × 20) + (won_round_two × 30) + (won_round_three × 40) + (won_round_four × 50) + (won_round_five × 60)`
- **FR-003**: System MUST store calculated scores in in-memory objects and add to a single in-memory array
- **FR-004**: System MUST generate bar chart for Scores per Recipe in descending order
- **FR-005**: System MUST generate bar chart for Scores per Ingredient Type in descending order
- **FR-006**: System MUST generate pie chart for Ingredient Frequency (number of times each ingredient appeared)
- **FR-007**: System MUST generate line chart for Ingredient Performance Over Time (per round in ascending order)
- **FR-008**: System MUST generate bar chart for Scores per Ethnic Origin in descending order
- **FR-009**: System MUST generate pie chart for Ethnic Origin Frequency
- **FR-010**: System MUST generate line chart for Round Voting Patterns showing vote counts and/or percentages per round
- **FR-011**: System MUST generate side-by-side box plot for Celebrity Author Performance comparing score distributions
- **FR-012**: System MUST generate line chart for Normalized Voting Participation showing votes per matchup per round, normalized for the 32-entry bracket structure
- **FR-013**: System MUST properly label all charts with titles and axis labels
- **FR-014**: System MUST handle null/missing optional fields gracefully (cooked_url, source_url, vote data)
- **FR-015**: System MUST use Seaborn with its default styling for all charts
- **FR-016**: Notebook MUST run without errors and produce reproducible results

### Key Entities *(include if feature involves data)*

- **Recipe**: Represents a tournament entry with title, ethnic_origin, ingredients, round wins, vote data, and author information
- **TournamentScore**: Calculated metric based on round wins using the weighted formula
- **Ingredient**: Individual ingredient from recipe ingredient lists, tracked for performance analysis
- **EthnicOrigin**: Cultural/regional classification of recipes
- **VoteData**: Vote counts and percentages per round (may be null)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All JSON files in `/recipes` directory are correctly parsed and loaded into memory
- **SC-002**: Tournament scores are calculated correctly using the specified formula for all recipes
- **SC-003**: All 9 chart types are generated with correct data and proper labeling using Seaborn default styling
- **SC-004**: Charts display data sorted according to each chart's requirements (descending for bar charts, ascending by round for line charts)
- **SC-005**: Notebook executes without errors and produces reproducible results
- **SC-006**: Optional data fields (vote counts, percentages, URLs) are handled gracefully when null or missing

## Assumptions

- Users have Python environment with Jupyter/IPython notebook support
- `/recipes` directory exists and contains valid JSON files
- Seaborn and Matplotlib visualization libraries are available
- Recipe JSON files conform to the defined data schema
- Target users have basic familiarity with reading charts and data visualizations
- Analysis is post-mortem (retrospective) - no live data updates during analysis