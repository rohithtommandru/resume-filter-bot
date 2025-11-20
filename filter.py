from typing import List, Dict

def filter_and_score_resumes(resumes: List[Dict], skills: List[Dict], min_score: float = 0.0) -> List[Dict]:
    """Filter resumes and compute a normalized score between 0 and 1 based on skill weights.

    skills: list of {'name': <skill>, 'weight': <float>} or list of strings
    """
    # Normalize skills input
    processed = []
    if len(skills) and isinstance(skills[0], str):
        processed = [{'name': s.lower(), 'weight': 1.0} for s in skills]
    else:
        # ensure lowercase
        processed = [{'name': s.get('name','').lower(), 'weight': float(s.get('weight',1.0))} for s in skills if s.get('name')]

    max_possible = sum(s['weight'] for s in processed) or 1.0

    results = []
    for r in resumes:
        matched = []
        score = 0.0
        text = r.get('content','')
        for s in processed:
            if s['name'] in text:
                matched.append(s['name'])
                score += s['weight']
        normalized = score / max_possible
        if normalized >= min_score:
            out = dict(r)  # copy
            out['matched_skills'] = matched
            out['raw_score'] = score
            out['score'] = round(normalized, 4)
            results.append(out)
    # sort by score descending
    results.sort(key=lambda x: x['score'], reverse=True)
    return results
