# Thyroid Nodule & Cancer Molecular Markers Knowledgebase (TNMK)

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Portal-blue)](https://johnyquest7.github.io/thyroid-nodule-molecular-markers/)
[![AlphaGenome](https://img.shields.io/badge/Google%20DeepMind-AlphaGenome%20Atlas-purple)](https://deepmind.google.com/science/alphagenome/atlas)
[![Status](https://img.shields.io/badge/Research%20Use%20Only-RUO-amber)](https://github.com/johnyquest7/thyroid-nodule-molecular-markers)
[![Database Version](https://img.shields.io/badge/Database-v1.0.0-emerald)](https://github.com/johnyquest7/thyroid-nodule-molecular-markers)

A comprehensive, interactive web portal and curated genomic repository for all known **thyroid nodule and thyroid cancer molecular alterations**, cross-referenced across major clinical molecular diagnostic platforms (**ThyroSeq v3**, **Afirma GSC / Xpression Atlas**, **ThyGeNEXT / ThyraMIR**), **AlphaGenome Variant Impact (AVI)** scores, and primary clinical literature.

Developed and maintained by **Johnson Thomas, MD, FACE, FEAA** (Department of Endocrinology, Mercy Hospital Springfield, Missouri, USA).

---

## 🌟 Key Features

1. **Multi-Class Molecular Alteration Catalog**:
   * **High-Risk Oncogenic Drivers**: *BRAF* V600E, *TERT* promoter hotspots (-124 C>T [C228T], -146 C>T [C250T]), *TP53* (R248Q, R273H), *RET* M918T / C634 / V804M, *PIK3CA* H1047R, *AKT1* E17K, *CTNNB1* S33C.
   * **Gene Fusions**: *RET* fusions (*CCDC6::RET*, *NCOA4::RET*), *NTRK1/3* fusions (*ETV6::NTRK3*, *TPM3::NTRK1*), *ALK* fusions (*STRN::ALK*), *PAX8::PPARG*, and *THADA::IGF2BP3*.
   * **Intermediate / RAS-Like Alterations**: *NRAS* / *HRAS* / *KRAS* (codons 12, 13, 61), *BRAF* K601E, *PTEN*, *EIF1AX* A113_splice, and *DICER1* RNase IIIb mutations.
   * **Low-Risk / Autonomous / Benign**: *TSHR* activating mutations (*M453T*, *D633H*, etc.), *GNAS* R201C, *PRKAR1A*.
   * **Copy Number Alterations (CNAs) & Aneuploidy**: Genome-wide near-haploidization (pathognomonic for Hürthle / Oncocytic Carcinoma in ThyroSeq v3), 22q loss, 1p loss.

2. **Cross-Platform Diagnostic Classification**:
   * **ThyroSeq v3 (112 genes)**: High-Risk vs. RAS-like vs. Low-Risk vs. CNA-High profiles.
   * **Afirma GSC & Xpression Atlas (593 genes)**: Risk of Malignancy (ROM %) ranges and variant/fusion calls.
   * **ThyGeNEXT / ThyraMIR**: Targeted mutational testing and microRNA risk classification.
   * **ATA Guidelines**: Initial Risk of Recurrence (High, Intermediate, Low).

3. **AlphaGenome Integration**:
   * Deep-learning calibrated **AlphaGenome Variant Impact (AVI)** Phred-scaled scores.
   * Top functional modality attribution (e.g. `ALPHAMISSENSE`, `DNASE`, `MERGED_SPLICING`, `PROTEIN_TERMINATION`).
   * One-click direct launch into the **AlphaGenome Atlas** interactive viewer (`deepmind.google.com/science/alphagenome/atlas`) with preloaded thyroid tissue tracks.

4. **Option C Hybrid Literature Explorer**:
   * Quick-access primary PubMed PMID buttons on every table row.
   * Slide-over **Evidence Drawer** showing paper titles, journal, publication year, clinical takeaways, and direct PubMed links.
   * Real-time "Search PubMed" launcher prefilled with targeted search queries for each alteration.

5. **Monthly Automated Antigravity Maintenance**:
   * Built-in script (`pipeline/update_repository.py`) queries PubMed E-utilities for new publications, validates database integrity, refreshes metadata, and syncs web assets.

---

## 🚀 Live Access & GitHub Pages Deployment

The web portal is designed as a zero-dependency static single-page application (`index.html`) ready for GitHub Pages.

To enable GitHub Pages on your repository:
1. Navigate to your repository on GitHub: [`johnyquest7/thyroid-nodule-molecular-markers`](https://github.com/johnyquest7/thyroid-nodule-molecular-markers).
2. Go to **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, select **Deploy from a branch**.
4. Select branch **`main`** and folder **`/ (root)`**, then click **Save**.
5. Your portal will be live at:
   ```
   https://johnyquest7.github.io/thyroid-nodule-molecular-markers/
   ```

---

## 💻 Local Quickstart

You can view the repository locally without any web server:
1. Clone or open the repository:
   ```bash
   git clone https://github.com/johnyquest7/thyroid-nodule-molecular-markers.git
   cd thyroid-nodule-molecular-markers
   ```
2. Double-click `index.html` to open it directly in any modern web browser (Chrome, Edge, Safari, Firefox).
3. Alternatively, launch a lightweight local server:
   ```bash
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser.

---

## 🔄 Monthly Antigravity Maintenance

To run the monthly synchronization and update the database:

```bash
python pipeline/update_repository.py
```

This pipeline automatically:
1. Checks schema and data integrity across `data/thyroid_mutations.json`.
2. Queries NCBI PubMed E-utilities for newly indexed publications in thyroid molecular diagnostics.
3. Computes updated counts (High Risk, RAS-like, Low Risk, CNAs, Targeted therapies).
4. Updates `data/metadata.json` with the current month and ISO timestamp.
5. Synchronizes the embedded dataset inside `index.html`.

Commit and push updates to GitHub:
```bash
git add data/ index.html
git commit -m "chore: monthly database update [Month Year]"
git push origin main
```

---

## 📊 Repository Structure

```
thyroid-nodule-molecular-markers/
├── index.html                   # Interactive Single-Page Web Application
├── README.md                    # Documentation & Setup Guide
├── LICENSE                      # MIT License
├── data/
│   ├── thyroid_mutations.json  # Comprehensive master alteration callset
│   └── metadata.json           # Version, counts, and update timestamps
└── pipeline/
    ├── update_repository.py    # Antigravity monthly updater & PubMed sync
    ├── generate_initial_database.py # Callset generator & schema builder
    └── inject_embedded_data.py # Zero-dependency HTML data injector
```

---

## ⚠️ Disclaimer (Research Use Only)

> [!IMPORTANT]
> **RESEARCH USE ONLY (RUO)**: This tool, database, and associated computational scores are curated strictly for academic research, scientific inquiry, and educational purposes. They are **not** intended for direct clinical diagnostic, prognostic, or therapeutic decision-making in individual patient care. Clinical management of thyroid nodules and thyroid cancer should always follow established medical guidelines (such as the American Thyroid Association [ATA], NCCN, and WHO 2022 classifications) and CLIA/CAP-accredited molecular pathology reports.

---

## 👤 Author & Contact

**Johnson Thomas, MD, FACE, FEAA**  
Department of Endocrinology  
Mercy Hospital Springfield, Missouri, USA  
GitHub: [@johnyquest7](https://github.com/johnyquest7)
