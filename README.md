🚀 Resume Filter Bot

A smart automation tool built using Python, designed to parse, filter, and score resumes based on required skills.
Exports results to CSV and Excel — perfect for HR automation, candidate shortlisting, and ATS-style screening.

✨ Features

✔ Parses TXT and PDF resumes
✔ Filters resumes based on required skills
✔ Skill weighting and scoring system (0–1)
✔ Exports results to CSV and Excel (XLSX)
✔ Clean folder structure
✔ Fully customizable skill list using skills.json
✔ Simple CLI-based usage

📁 Folder Structure
resume-filter-bot/
│── main.py
│── parser.py
│── filter.py
│── exporter.py
│── skills.json
│── requirements.txt
│── README.md
└── resumes/
      ├── sample_1.txt
      ├── sample_2.txt

🛠️ Installation
1. Install dependencies
pip install -r requirements.txt

▶️ How to Run
Basic run
python main.py

Advanced usage
python main.py --resumes resumes --skills skills.json --min-score 0.0 --out-prefix results

Arguments
Argument	Description
--resumes	Path to resumes folder
--skills	Skill list JSON file
--min-score	Minimum score (0–1) to include candidates
--out-prefix	Output name for CSV/XLSX
📊 Example skills.json
[
  {"name": "python", "weight": 1.0},
  {"name": "selenium", "weight": 1.0},
  {"name": "pytest", "weight": 0.8},
  {"name": "java", "weight": 0.6},
  {"name": "javascript", "weight": 0.5}
]

📝 Output

After running the bot, you get:

results.csv

results.xlsx

Each containing:

name	score	raw_score	matched_skills
sample_1	0.90	3.4	python, selenium, pytest
🎯 Ideal Use Cases

HR resume shortlisting

Screening candidates for automation roles

ATS basic filtering

Portfolio & GitHub project

Python + automation skill demonstration

🤝 Contributions

Pull requests and improvements are welcome!

👨‍💻 Author

Rohith Tommandru
Python | Selenium | Automation Engineer
