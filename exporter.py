import pandas as pd
import os

def export_results(results, prefix='results'):
    if not results:
        print('No results to export.')
        return
    # Build dataframe
    rows = []
    for r in results:
        rows.append({
            'name': r.get('name'),
            'path': r.get('path'),
            'score': r.get('score'),
            'raw_score': r.get('raw_score'),
            'matched_skills': ','.join(r.get('matched_skills', []))
        })
    df = pd.DataFrame(rows)
    csv_path = f"{prefix}.csv"
    xlsx_path = f"{prefix}.xlsx"
    try:
        df.to_csv(csv_path, index=False)
        df.to_excel(xlsx_path, index=False)
        print(f"Exported CSV -> {csv_path} and Excel -> {xlsx_path}")
    except Exception as e:
        print('Failed to export results:', e)
