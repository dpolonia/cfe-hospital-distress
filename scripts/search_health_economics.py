"""
Search Scopus for similar articles in Health Economics journal
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SCOPUS_API_KEY = os.getenv('SCOPUS_API_KEY', '7f59af901d2d86f78a1fd60c1bf9426a')

def search_health_economics_articles():
    """Search for similar articles in Health Economics journal."""
    
    queries = [
        # DiD studies in Health Economics
        'SRCTITLE("Health Economics") AND KEY("difference-in-differences")',
        # Hospital reform studies
        'SRCTITLE("Health Economics") AND KEY("hospital reform" OR "healthcare reform")',
        # Vertical integration in healthcare
        'SRCTITLE("Health Economics") AND KEY("vertical integration" OR "integrated care")',
        # Public hospital finance
        'SRCTITLE("Health Economics") AND KEY("public hospital" OR "hospital finance")',
    ]
    
    headers = {
        'X-ELS-APIKey': SCOPUS_API_KEY,
        'Accept': 'application/json'
    }
    
    all_results = []
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print('='*60)
        
        params = {
            'query': query,
            'count': 5,
            'sort': 'citedby-count',
            'date': '2019-2026'
        }
        
        try:
            response = requests.get(
                'https://api.elsevier.com/content/search/scopus',
                headers=headers,
                params=params,
                timeout=30
            )
            
            data = response.json()
            results = data.get('search-results', {}).get('entry', [])
            
            print(f"Found {len(results)} articles")
            
            for article in results:
                title = article.get('dc:title', 'N/A')
                authors = article.get('dc:creator', 'N/A')
                year = article.get('prism:coverDate', 'N/A')[:4]
                citations = article.get('citedby-count', '0')
                doi = article.get('prism:doi', '')
                
                print(f"\n  [{year}] {title[:70]}...")
                print(f"       Author: {authors}")
                print(f"       Citations: {citations}, DOI: {doi}")
                
                all_results.append({
                    'title': title,
                    'author': authors,
                    'year': year,
                    'citations': citations,
                    'doi': doi
                })
                
        except Exception as e:
            print(f"  Error: {e}")
    
    # Write results to file
    with open('results/health_economics_similar_articles.md', 'w', encoding='utf-8') as f:
        f.write("# Similar Articles in Health Economics Journal\n\n")
        f.write("## Search Criteria\n")
        f.write("- Journal: Health Economics (Wiley)\n")
        f.write("- Topics: DiD, hospital reform, vertical integration, public hospitals\n")
        f.write("- Period: 2019-2026\n\n")
        f.write("## Results\n\n")
        
        seen_titles = set()
        for i, article in enumerate(all_results, 1):
            if article['title'] not in seen_titles:
                seen_titles.add(article['title'])
                f.write(f"{i}. **{article['title']}**\n")
                f.write(f"   - Authors: {article['author']}\n")
                f.write(f"   - Year: {article['year']}, Citations: {article['citations']}\n")
                if article['doi']:
                    f.write(f"   - DOI: {article['doi']}\n")
                f.write("\n")
    
    print(f"\n\nResults saved to results/health_economics_similar_articles.md")
    print(f"Total unique articles: {len(seen_titles)}")

if __name__ == "__main__":
    search_health_economics_articles()
