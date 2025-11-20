# Resume Filter Bot (Upgraded)

This upgraded Resume Filter Bot matches resumes against required skills and exports results to CSV and Excel.


## Features

- Parses `.txt` and `.pdf` resumes (PDF parsing requires `PyPDF2`).
- Configurable skill list with weights (via `skills.json`).
- Scores resumes (normalized 0-1) and filters by minimum score.
- Exports results to CSV and Excel.

## Quick start

1. Install requirements:

```bash
pip install -r requirements.txt
```

2. Put resumes into the `resumes/` folder. Supported: `.txt`, `.pdf`.

3. Edit `skills.json` (optional) to provide skills and weights.

4. Run:

```bash
python main.py --resumes resumes --skills skills.json --min-score 0.0 --out-prefix results
```

## Example `skills.json`

```json
[
  {"name": "python", "weight": 1.0},
  {"name": "selenium", "weight": 1.0},
  {"name": "pytest", "weight": 0.8}
]
```

## Notes

- If `PyPDF2` is not installed, PDF parsing will be skipped but the rest will work.
- The project is ready to upload to GitHub as a resume-backed project.
