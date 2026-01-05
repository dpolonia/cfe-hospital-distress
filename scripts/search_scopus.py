"""
Scopus Literature Search for CFE Empirical Work
Uses Scopus API to find relevant academic citations for the paper.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

SCOPUS_API_KEY = os.getenv("SCOPUS_API_KEY")
BASE_URL = "https://api.elsevier.com/content/search/scopus"

def search_scopus(query: str, count: int = 10) -> list:
    """
    Search Scopus for academic articles.
    
    Args:
        query: Search query string
        count: Number of results to return
        
    Returns:
        List of article dictionaries with title, authors, year, doi
    """
    headers = {
        "X-ELS-APIKey": SCOPUS_API_KEY,
        "Accept": "application/json"
    }
    
    params = {
        "query": query,
        "count": count,
        "sort": "-citedby-count",  # Most cited first
        "field": "dc:title,dc:creator,prism:coverDate,prism:doi,citedby-count"
    }
    
    try:
        response = requests.get(BASE_URL, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        results = []
        entries = data.get("search-results", {}).get("entry", [])
        
        for entry in entries:
            results.append({
                "title": entry.get("dc:title", "N/A"),
                "authors": entry.get("dc:creator", "N/A"),
                "year": entry.get("prism:coverDate", "N/A")[:4] if entry.get("prism:coverDate") else "N/A",
                "doi": entry.get("prism:doi", "N/A"),
                "citations": entry.get("citedby-count", 0)
            })
        
        return results
        
    except Exception as e:
        print(f"Scopus API error: {e}")
        return []


def find_related_literature():
    """
    Search for literature related to our research topics.
    """
    queries = [
        # Core topic
        'TITLE-ABS-KEY("financial distress" AND "public hospital")',
        'TITLE-ABS-KEY("soft budget constraint" AND healthcare)',
        'TITLE-ABS-KEY("vertical integration" AND hospital AND finance)',
        # Methodology
        'TITLE-ABS-KEY("panel data" AND hospital AND "financial performance")',
        # Portugal specific
        'TITLE-ABS-KEY(Portugal AND hospital AND (reform OR restructuring))',
    ]
    
    all_results = {}
    
    for query in queries:
        print(f"\n--- Searching: {query[:60]}... ---")
        results = search_scopus(query, count=5)
        all_results[query] = results
        
        for r in results:
            print(f"  [{r['year']}] {r['title'][:70]}... (Cited: {r['citations']})")
    
    return all_results


def generate_bibliography_suggestions(results: dict) -> str:
    """
    Generate formatted bibliography entries from search results.
    """
    output = "# Scopus Literature Suggestions\n\n"
    
    for query, articles in results.items():
        output += f"## Query: {query[:50]}...\n\n"
        for art in articles:
            if art['doi'] != 'N/A':
                output += f"- {art['authors']} ({art['year']}). *{art['title']}*. DOI: {art['doi']} [Cited: {art['citations']}]\n"
            else:
                output += f"- {art['authors']} ({art['year']}). *{art['title']}*. [Cited: {art['citations']}]\n"
        output += "\n"
    
    return output


if __name__ == "__main__":
    print("=" * 60)
    print("SCOPUS LITERATURE SEARCH FOR CFE EMPIRICAL WORK")
    print("=" * 60)
    
    results = find_related_literature()
    
    # Save suggestions
    bibliography = generate_bibliography_suggestions(results)
    with open("results/scopus_literature.md", "w", encoding="utf-8") as f:
        f.write(bibliography)
    
    print("\n\nResults saved to results/scopus_literature.md")
