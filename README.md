
git add README.md
git commit -m "docs: add project overview and setup instructions to README"
git push


# Automated Sales Analytics Pipeline

A modular, automated data engineering pipeline built in Python to extract, transform, and analyze retail sales data.

## Features
- **Modular Architecture:** Separated concerns into Extract, Transform, and Analyze modules.
- **Data Validation:** Automatic cleanup and missing-value detection.
- **Statistical Analysis:** Performs independent t-tests to validate spending differences between product categories.
- **Automated Execution:** Orchestrated via `main.py` for end-to-end processing.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the pipeline: `python main.py`
63e34ac9da25af74f2391242d3a7822f9f135d8e
