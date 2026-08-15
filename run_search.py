cat > run_search.py << 'EOF'
import urllib.request
import xml.etree.ElementTree as ET
import json
import os

# Create directory path if it doesn't exist
output_dir = 'thesis/papers/02-systematic-review/research/search-results/'
os.makedirs(output_dir, exist_ok=True)

# Build arXiv API URL with your search terms
# ANDNOT operators or exact phrases work via specific query rules
query = 'all:"compositional generalization" AND all:"neural network" AND all:"out-of-distribution"'
url = f'http://arxiv.org{urllib.parse.quote(query)}&max_results=200'

print("Fetching papers from arXiv API...")
papers = []

try:
    with urllib.request.urlopen(url) as response:
        xml_data = response.read()

    # Parse the XML response
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://w3.org'}

    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')

        authors = [auth.find('atom:name', ns).text for auth in entry.findall('atom:author', ns)]
        author_str = ', '.join(authors)

        published = entry.find('atom:published', ns).text
        year = published.split('-')[0] if published else ''

        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
        abstract = summary[:500] + '...' if len(summary) > 500 else summary

        paper_url = entry.find('atom:id', ns).text

        papers.append({
            'title': title,
            'authors': author_str,
            'year': year,
            'abstract': abstract,
            'cites': 0, # arXiv does not track citation counts natively
            'url': paper_url
        })

    # Save to your structured path
    output_file = os.path.join(output_dir, 'arxiv-results.json')
    with open(output_file, 'w') as f:
        json.dump(papers, f, indent=2)

    print(f"\nSuccess! Saved {len(papers)} papers to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")
EOF
