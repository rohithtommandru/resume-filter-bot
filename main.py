from parser import parse_resumes
from filter import filter_and_score_resumes
from exporter import export_results
import argparse
import json

def cli():
    parser = argparse.ArgumentParser(description='Resume Filter Bot - upgraded')
    parser.add_argument('--resumes', default='resumes', help='Folder containing resumes (txt, pdf)')
    parser.add_argument('--skills', default='skills.json', help='JSON file with required skills and weights')
    parser.add_argument('--min-score', type=float, default=0.0, help='Minimum score to include in output (0-1)')
    parser.add_argument('--out-prefix', default='results', help='Output file prefix (CSV/Excel)')
    args = parser.parse_args()

    skills = []
    try:
        with open(args.skills, 'r', encoding='utf-8') as f:
            skills = json.load(f)
    except Exception as e:
        print(f"Could not load skills.json: {e}. Using default skill list.")
        # default skill list with optional weights
        skills = [{"name":"python","weight":1.0},{"name":"selenium","weight":1.0},{"name":"pytest","weight":0.8},{"name":"java","weight":0.6},{"name":"javascript","weight":0.5}]

    resumes = parse_resumes(args.resumes)
    filtered = filter_and_score_resumes(resumes, skills, min_score=args.min_score)
    print(f"Found {len(filtered)} matching resumes (min_score={args.min_score})\n")
    for r in filtered:
        print(f"{r['name']} — score: {r['score']:.2f} — matched: {r['matched_skills']}")

    export_results(filtered, prefix=args.out_prefix)

if __name__ == '__main__':
    cli()
