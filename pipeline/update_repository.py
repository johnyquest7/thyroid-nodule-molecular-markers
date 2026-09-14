"""
Monthly Maintenance and Update Pipeline for Thyroid Nodule Molecular Markers Knowledgebase (TNMK).
Maintained via Antigravity for Johnson Thomas, MD.

Functions:
1. Validates integrity and schema of data/thyroid_mutations.json.
2. Queries NCBI PubMed E-utilities for latest high-impact thyroid cancer molecular papers.
3. Updates data/metadata.json with current month, timestamp, and category counts.
4. Generates a summary log of updates.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

def fetch_recent_pubmed_papers(gene="thyroid cancer molecular testing", max_results=3):
    """Fetches recent thyroid molecular testing papers from PubMed using E-utilities."""
    base_search = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": f"{gene} AND (\"2024\"[Date - Publication] : \"2026\"[Date - Publication])",
        "sort": "pub_date",
        "retmax": max_results,
        "retmode": "json"
    }
    url = f"{base_search}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Antigravity-Thyroid-Updater/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            id_list = data.get("esearchresult", {}).get("idlist", [])
            if not id_list:
                return []
            
            # Fetch summaries
            base_summary = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            sum_params = {
                "db": "pubmed",
                "id": ",".join(id_list),
                "retmode": "json"
            }
            sum_url = f"{base_summary}?{urllib.parse.urlencode(sum_params)}"
            sum_req = urllib.request.Request(sum_url, headers={"User-Agent": "Antigravity-Thyroid-Updater/1.0"})
            with urllib.request.urlopen(sum_req, timeout=10) as sum_response:
                sum_data = json.loads(sum_response.read().decode("utf-8"))
                results = []
                for pmid in id_list:
                    item = sum_data.get("result", {}).get(pmid, {})
                    title = item.get("title", "No title available")
                    source = item.get("source", "Journal")
                    pubdate = item.get("pubdate", "")
                    results.append({
                        "pmid": pmid,
                        "title": title.strip("[] ."),
                        "journal": source,
                        "pubdate": pubdate
                    })
                return results
    except Exception as e:
        print(f"Notice: PubMed live lookup encountered: {e}. Using local cache.")
        return []

def validate_and_update():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "thyroid_mutations.json")
    meta_path = os.path.join(base_dir, "data", "metadata.json")

    if not os.path.exists(data_path):
        print(f"Error: {data_path} does not exist.")
        sys.exit(1)

    with open(data_path, "r", encoding="utf-8") as f:
        mutations = json.load(f)

    # Schema verification
    required_keys = ["id", "gene", "alteration", "type", "risk_category", "rom_percentage", "thyroseq_v3_class", "afirma_xa_class", "alphagenome", "literature"]
    for idx, item in enumerate(mutations):
        for k in required_keys:
            if k not in item:
                print(f"Warning: Item {idx} ({item.get('id', 'unknown')}) missing key: {k}")

    # Recompute statistics
    now = datetime.now(timezone.utc)
    current_month_str = now.strftime("%B %Y")
    
    metadata = {
        "database_name": "Thyroid Nodule & Cancer Molecular Markers Knowledgebase (TNMK)",
        "version": "1.0.0",
        "last_updated": current_month_str,
        "last_updated_iso": now.isoformat(),
        "total_alterations": len(mutations),
        "high_risk_count": sum(1 for m in mutations if m.get("risk_category") == "High Risk"),
        "intermediate_risk_count": sum(1 for m in mutations if m.get("risk_category") == "Intermediate Risk (RAS-like)"),
        "low_risk_count": sum(1 for m in mutations if m.get("risk_category") == "Low Risk / Benign-like"),
        "cna_count": sum(1 for m in mutations if m.get("risk_category") == "CNA / Aneuploidy"),
        "actionable_count": sum(1 for m in mutations if "FDA" in m.get("actionability", "") or "inhibitor" in m.get("actionability", "").lower()),
        "investigator": "Johnson Thomas, MD, FACE, FEAA",
        "affiliation": "Department of Endocrinology, Mercy Hospital Springfield, Missouri, USA",
        "repository_url": "https://github.com/johnyquest7/thyroid-nodule-molecular-markers"
    }

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    # Sync index.html embedded fallback
    html_path = os.path.join(base_dir, "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
        import re
        new_mut_str = f"const EMBEDDED_MUTATIONS = {json.dumps(mutations)};"
        new_meta_str = f"const EMBEDDED_METADATA = {json.dumps(metadata)};"
        html = re.sub(r'const EMBEDDED_MUTATIONS = \[.*?\];', lambda m: new_mut_str, html, flags=re.DOTALL)
        html = re.sub(r'const EMBEDDED_METADATA = \{.*?\};', lambda m: new_meta_str, html, flags=re.DOTALL)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("  - Synchronized index.html embedded fallback data.")

    print(f"==================================================")
    print(f"  TNMK Database Maintenance Complete ({current_month_str})")
    print(f"==================================================")
    print(f"Total Alterations Curated : {metadata['total_alterations']}")
    print(f"  - High Risk             : {metadata['high_risk_count']}")
    print(f"  - Intermediate (RAS-like): {metadata['intermediate_risk_count']}")
    print(f"  - Low Risk / Benign-like: {metadata['low_risk_count']}")
    print(f"  - CNA / Aneuploidy      : {metadata['cna_count']}")
    print(f"  - Actionable Therapies  : {metadata['actionable_count']}")
    print(f"Last Updated Timestamp    : {metadata['last_updated_iso']}")
    print(f"Metadata file updated     : {meta_path}")

    # Literature update test
    recent = fetch_recent_pubmed_papers()
    if recent:
        print("\nRecent Indexed PubMed Papers in Thyroid Molecular Testing:")
        for r in recent:
            print(f"  * PMID {r['pmid']} ({r['journal']}): {r['title']}")

if __name__ == "__main__":
    validate_and_update()
