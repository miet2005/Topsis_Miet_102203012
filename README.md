# TOPSIS Python Package

## Overview

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) is a popular multi-criteria decision analysis (MCDA) method. It ranks and selects options based on multiple criteria, considering varying weights and impacts. This package implements the TOPSIS method to rank alternatives using input data, weights, and impacts. It generates results with rankings, distances to ideal best/worst solutions, and TOPSIS scores.

## Features

- **Flexible Ranking**: Ranks options based on customizable criteria.
- **Weight and Impact Support**: Handles criteria with different importance (weights) and impacts (positive/negative).
- **Distance Calculations**: Computes distances to ideal best and worst solutions.
- **CSV Input/Output**: Accepts input data in CSV format and outputs results in CSV format.

## Installation

Install the package using pip:

```bash
pip install Topsis-Miet-102203012
```

## Usage

### Command-Line Interface

Run the TOPSIS method from the command line using the following syntax:

```bash
python -m topsis.topsis <input_data.csv> <weights> <impacts> <result.csv>
```

#### Parameters

1. **`<input_data.csv>`** (Required):
   - Path to the input CSV file containing options and criteria values.
   - The first column should represent the options (e.g., Option1, Option2).
   - The remaining columns should contain numerical values for the criteria.

2. **`<weights>`** (Required):
   - A comma-separated string representing the weights for each criterion.
   - Higher values indicate greater importance.

3. **`<impacts>`** (Required):
   - A comma-separated string representing the impacts for each criterion.
   - Use `+` for positive impacts (higher values are better) and `-` for negative impacts (lower values are better).

4. **`<result.csv>`** (Required):
   - Path to the output CSV file where the results will be saved.
   - The output includes:
     - **Option**: Option names.
     - **Distance from Ideal Best**: Euclidean distance to the ideal best solution.
     - **Distance from Ideal Worst**: Euclidean distance to the ideal worst solution.
     - **TOPSIS Score**: Indicates closeness to the ideal solution.
     - **Rank**: Ranking of each option based on the TOPSIS score.

### Example

#### Input CSV: `input_data.csv`

```csv
Option,Criterion1,Criterion2,Criterion3,Criterion4,Criterion5
Option1,7,9,6,8,7
Option2,8,7,9,7,8
Option3,6,5,8,6,5
```

#### Command

```bash
python -m topsis.topsis input_data.csv "1,1,2,2,1" "+,+,-,-,-" result.csv
```

#### Output CSV: `result.csv`

```csv
Option,Distance from Ideal Best,Distance from Ideal Worst,TOPSIS Score,Rank
Option1,2.5,5.0,0.6667,1
Option2,3.0,4.5,0.6,2
Option3,3.5,3.0,0.4615,3
```

### Understanding the Output

- **Distance from Ideal Best**: Measures how far each option is from the best possible solution.
- **Distance from Ideal Worst**: Measures how far each option is from the worst possible solution.
- **TOPSIS Score**: A normalized score indicating closeness to the ideal solution (higher is better).
- **Rank**: Orders the options based on their TOPSIS scores (1 is the best).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Additional Information

- Python 3.6 or higher is required.
- Ensure the input data contains numerical values only for criteria columns.
- For questions or issues, please reach out to the package maintainer.

