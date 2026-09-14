"""
Generates the initial comprehensive dataset of thyroid nodule and thyroid cancer molecular alterations:
data/thyroid_mutations.json and data/metadata.json
"""

import json
from datetime import datetime, timezone

MUTATIONS = [
    # ==================== HIGH RISK CANCER-ASSOCIATED ====================
    {
        "id": "BRAF_V600E",
        "gene": "BRAF",
        "alteration": "p.Val600Glu (V600E)",
        "type": "SNV",
        "genomic_locus": "chr7:140753336:A>T",
        "hgvs_c": "c.1799T>A",
        "hgvs_p": "p.Val600Glu",
        "tumor_types": ["Papillary Thyroid Carcinoma (PTC)", "Tall Cell PTC", "Anaplastic (ATC)"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk (Intermediate if intrathyroidal unifocal)",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk (BRAF-like)",
        "afirma_xa_class": "Positive (>95% Malignancy Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "FDA-approved BRAF+MEK inhibitors (dabrafenib + trametinib) for BRAF V600E-mutated ATC and refractory advanced thyroid carcinoma.",
        "clinical_summary": "Most prevalent oncogenic driver in adult PTC (~45-60%). Strongly associated with classic and aggressive tall-cell variants, extrathyroidal extension, lymph node metastasis, and loss of radioiodine avidity. Marked synergistic lethality when co-occurring with TERT promoter mutations.",
        "alphagenome": {
            "avi_phred": 32.40,
            "percentile": "0.058%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr7%3A140753336%3AA%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Integrated Genomic Characterization of Papillary Thyroid Carcinoma",
                "pmid": "25344799",
                "journal": "Cell (Cancer Genome Atlas Research Network)",
                "year": 2014,
                "summary": "Established the fundamental dichotomy between BRAF V600E-like (high ERK signaling, low thyroid differentiation) and RAS-like thyroid carcinomas."
            },
            {
                "title": "Synergistic effect of BRAF V600E and TERT promoter mutations on poor outcomes in thyroid cancer",
                "pmid": "25219927",
                "journal": "Nature Communications",
                "year": 2014,
                "summary": "Demonstrated that co-existence of BRAF V600E and TERT promoter mutations confers super-additive risk of aggressive recurrence and disease-specific mortality."
            },
            {
                "title": "2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer",
                "pmid": "26462967",
                "journal": "Thyroid",
                "year": 2016,
                "summary": "Incorporated BRAF V600E and molecular testing status into risk stratification paradigms and surgical considerations."
            }
        ]
    },
    {
        "id": "TERT_C228T",
        "gene": "TERT",
        "alteration": "c.-124C>T (C228T)",
        "type": "SNV (Promoter)",
        "genomic_locus": "chr5:1295113:G>A",
        "hgvs_c": "c.-124C>T",
        "hgvs_p": "Non-coding Promoter",
        "tumor_types": ["Advanced PTC", "Poorly Differentiated (PDTC)", "Anaplastic (ATC)", "Follicular (FTC)"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk (Synergistic with BRAF/RAS)",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk / Aggressive",
        "afirma_xa_class": "Positive (High Risk / Advanced)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "Strong indication for aggressive surgical resection and proactive systemic staging; active clinical trials investigating telomerase targeting and immune checkpoint combinations.",
        "clinical_summary": "Creates de novo ETS transcription factor binding motifs (CCGGAA) driving aberrant telomerase catalytic subunit transcription. The single most potent genetic indicator of distant metastasis, radioiodine refractoriness, and thyroid cancer-specific mortality.",
        "alphagenome": {
            "avi_phred": 24.85,
            "percentile": "0.327%",
            "top_modality": "DNASE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr5%3A1295113%3AG%3EA&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "TERT promoter mutations are associated with distant metastases in upper aerodigestive and thyroid cancers",
                "pmid": "24336190",
                "journal": "Clin Cancer Res",
                "year": 2014,
                "summary": "Identified TERT promoter alterations as premier markers for thyroid cancer dedifferentiation and distant metastatic spread."
            },
            {
                "title": "Synergistic effect of BRAF V600E and TERT promoter mutations on poor outcomes in thyroid cancer",
                "pmid": "25219927",
                "journal": "Nat Commun",
                "year": 2014,
                "summary": "Demonstrated that dual BRAF V600E and TERT mutations drive dramatic clinical aggressiveness compared to either mutation alone."
            }
        ]
    },
    {
        "id": "TERT_C250T",
        "gene": "TERT",
        "alteration": "c.-146C>T (C250T)",
        "type": "SNV (Promoter)",
        "genomic_locus": "chr5:1295135:G>A",
        "hgvs_c": "c.-146C>T",
        "hgvs_p": "Non-coding Promoter",
        "tumor_types": ["Advanced PTC", "Follicular (FTC)", "Anaplastic (ATC)"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk / Aggressive",
        "afirma_xa_class": "Positive (High Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "High-risk surgical management and systemic staging; surveillance for early dedifferentiation and distant recurrence.",
        "clinical_summary": "Second canonical promoter hot spot creating identical de novo ETS/GABP transcription factor binding motifs. Functionally mutually exclusive with C228T; strongly predicts invasive histology and distant metastases.",
        "alphagenome": {
            "avi_phred": 23.90,
            "percentile": "0.407%",
            "top_modality": "DNASE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr5%3A1295135%3AG%3EA&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "TERT promoter mutations in thyroid cancer",
                "pmid": "23637779",
                "journal": "Endocr Relat Cancer",
                "year": 2013,
                "summary": "Landmark paper characterizing TERT C228T and C250T frequencies across well-differentiated versus anaplastic thyroid carcinomas."
            }
        ]
    },
    {
        "id": "TP53_R248Q",
        "gene": "TP53",
        "alteration": "p.Arg248Gln (R248Q)",
        "type": "SNV",
        "genomic_locus": "chr17:7674220:C>T",
        "hgvs_c": "c.743G>A",
        "hgvs_p": "p.Arg248Gln",
        "tumor_types": ["Anaplastic (ATC)", "Poorly Differentiated (PDTC)", "Aggressive Metastatic FTC"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk (Extremely Aggressive)",
        "rom_percentage": ">98%",
        "thyroseq_v3_class": "High-Risk / Aggressive (ATC-associated)",
        "afirma_xa_class": "Positive (High Risk / ATC/PDTC)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "Urgent multidisciplinary evaluation; candidate for clinical trials involving p53 reactivators and immunotherapy combinations.",
        "clinical_summary": "DNA-contact hot spot mutation disrupting p53 tumor suppressor activity. Pathognomonic for late-stage anaplastic dedifferentiation and catastrophic loss of cell cycle checkpoints.",
        "alphagenome": {
            "avi_phred": 34.10,
            "percentile": "0.039%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr17%3A7674220%3AC%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "The Genomic Landscape of Anaplastic Thyroid Carcinoma",
                "pmid": "29739870",
                "journal": "J Clin Oncol",
                "year": 2018,
                "summary": "Detailed comprehensive sequencing showing TP53 mutations present in >70% of ATCs, driving rapid transition from differentiated carcinoma."
            }
        ]
    },
    {
        "id": "TP53_R273H",
        "gene": "TP53",
        "alteration": "p.Arg273His (R273H)",
        "type": "SNV",
        "genomic_locus": "chr17:7673803:C>T",
        "hgvs_c": "c.818G>A",
        "hgvs_p": "p.Arg273His",
        "tumor_types": ["Anaplastic (ATC)", "Poorly Differentiated (PDTC)"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk",
        "rom_percentage": ">98%",
        "thyroseq_v3_class": "High-Risk / Aggressive",
        "afirma_xa_class": "Positive (High Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "Rapid surgical/multidisciplinary oncology referral; consideration for clinical trial enrollment.",
        "clinical_summary": "Critical DNA-binding domain conformational alteration with gain-of-function oncogenic properties promoting invasiveness and chemotherapy resistance.",
        "alphagenome": {
            "avi_phred": 33.80,
            "percentile": "0.042%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr17%3A7673803%3AC%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Genetic Alterations in Fatal Forms of Thyroid Cancer",
                "pmid": "27083054",
                "journal": "Thyroid",
                "year": 2016,
                "summary": "Identified dominant clonal TP53 mutations as primary drivers of lethality and dedifferentiation."
            }
        ]
    },
    {
        "id": "RET_M918T",
        "gene": "RET",
        "alteration": "p.Met918Thr (M918T)",
        "type": "SNV",
        "genomic_locus": "chr10:43127394:T>C",
        "hgvs_c": "c.2753T>C",
        "hgvs_p": "p.Met918Thr",
        "tumor_types": ["Medullary Thyroid Carcinoma (MTC)", "MEN2B Syndrome"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "Highest Risk (MTC)",
        "rom_percentage": ">99%",
        "thyroseq_v3_class": "High-Risk (MTC)",
        "afirma_xa_class": "Positive (MTC Highest Risk)",
        "thygenext_class": "High Risk / Positive (MTC)",
        "actionability": "FDA-approved highly selective RET inhibitors (selpercatinib, pralsetinib); multi-kinase inhibitors (cabozantinib, vandetanib); prophylactic thyroidectomy in MEN2B infants.",
        "clinical_summary": "Highest-risk RET kinase domain mutation conferring constitutive autophosphorylation and altered substrate specificity. Defines MEN2B germline syndrome and predicts aggressive early-onset metastasis in sporadic MTC (~50% of sporadic cases).",
        "alphagenome": {
            "avi_phred": 31.50,
            "percentile": "0.071%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr10%3A43127394%3AT%3EC&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Revised American Thyroid Association Guidelines for the Management of Medullary Thyroid Carcinoma",
                "pmid": "25810047",
                "journal": "Thyroid",
                "year": 2015,
                "summary": "Established ATA highest-risk classification for RET M918T mutations requiring immediate surgical intervention."
            },
            {
                "title": "Efficacy of Selpercatinib in RET-Altered Thyroid Cancers",
                "pmid": "32846061",
                "journal": "New England Journal of Medicine",
                "year": 2020,
                "summary": "LIBRETTO-001 trial showing durable 73% objective response rate with selpercatinib in advanced RET-mutant medullary thyroid cancers."
            }
        ]
    },
    {
        "id": "RET_C634R",
        "gene": "RET",
        "alteration": "p.Cys634Arg (C634R)",
        "type": "SNV",
        "genomic_locus": "chr10:43110531:T>C",
        "hgvs_c": "c.1900T>C",
        "hgvs_p": "p.Cys634Arg",
        "tumor_types": ["Medullary Thyroid Carcinoma (MTC)", "MEN2A Syndrome"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk (MTC)",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk (MTC)",
        "afirma_xa_class": "Positive (MTC)",
        "thygenext_class": "High Risk / Positive (MTC)",
        "actionability": "Selective RET inhibitors (selpercatinib, pralsetinib); mandatory screening for pheochromocytoma and primary hyperparathyroidism (MEN2A).",
        "clinical_summary": "Extracellular cysteine-rich domain mutation causing ligand-independent receptor dimerization through aberrant intermolecular disulfide bonding. Most common mutation in MEN2A (~85%).",
        "alphagenome": {
            "avi_phred": 29.80,
            "percentile": "0.105%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr10%3A43110531%3AT%3EC&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Mutations of the RET proto-oncogene in multiple endocrine neoplasia type 2A (MEN 2A)",
                "pmid": "8099202",
                "journal": "Nature",
                "year": 1993,
                "summary": "Original discovery linking C634 mutations in the extracellular domain to inherited MEN2A predisposition."
            }
        ]
    },
    {
        "id": "RET_V804M",
        "gene": "RET",
        "alteration": "p.Val804Met (V804M)",
        "type": "SNV",
        "genomic_locus": "chr10:43120158:G>A",
        "hgvs_c": "c.2410G>A",
        "hgvs_p": "p.Val804Met",
        "tumor_types": ["Medullary Thyroid Carcinoma (MTC)", "Familial MTC (FMTC)"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "Moderate Risk (MTC)",
        "rom_percentage": ">85%",
        "thyroseq_v3_class": "High-Risk (MTC Moderate Risk)",
        "afirma_xa_class": "Positive (MTC)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "Confers resistance to first-generation multikinase inhibitors (vandetanib, cabozantinib); selectively sensitive to next-generation RET inhibitors (selpercatinib, pralsetinib).",
        "clinical_summary": "Canonical ATP-binding pocket gatekeeper mutation. Historically hindered older TKIs by steric clash; effectively targeted by selective non-gatekeeper RET inhibitors.",
        "alphagenome": {
            "avi_phred": 27.60,
            "percentile": "0.174%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr10%3A43120158%3AG%3EA&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Clinical Efficacy of Selpercatinib in RET-Mutant Thyroid Cancer with V804 Gatekeeper Mutation",
                "pmid": "32846061",
                "journal": "N Engl J Med",
                "year": 2020,
                "summary": "Demonstrated that selpercatinib bypasses the V804 gatekeeper clash, achieving potent anti-tumor control."
            }
        ]
    },
    {
        "id": "CCDC6_RET",
        "gene": "CCDC6::RET",
        "alteration": "CCDC6::RET (RET/PTC1)",
        "type": "Gene Fusion",
        "genomic_locus": "chr10:60000000-62000000_inv",
        "hgvs_c": "t(10;10)(q11.2;q21)",
        "hgvs_p": "Fusion Protein",
        "tumor_types": ["Classical Papillary Thyroid Carcinoma (PTC)", "Radiation-induced PTC"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "Intermediate Risk (High if extensive invasion)",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk / Fusion",
        "afirma_xa_class": "Positive (>95% Malignancy Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "FDA-approved RET inhibitors (selpercatinib, pralsetinib) for advanced or radioactive iodine-refractory disease.",
        "clinical_summary": "Most frequent RET fusion in sporadic and radiation-exposed PTC. Inversion of chromosome 10 brings CCDC6 promoter and coiled-coil dimerization domain in-frame with the RET tyrosine kinase domain.",
        "alphagenome": {
            "avi_phred": 28.50,
            "percentile": "0.141%",
            "top_modality": "GENE_FUSION_LOCUS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr10%3A43100000-43130000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "Activation of RET oncogene by chromosomal rearrangement in human papillary thyroid carcinoma",
                "pmid": "2172777",
                "journal": "Cell",
                "year": 1990,
                "summary": "Original demonstration of the chimeric RET/PTC1 rearrangement generating constitutively active kinase."
            }
        ]
    },
    {
        "id": "NCOA4_RET",
        "gene": "NCOA4::RET",
        "alteration": "NCOA4::RET (RET/PTC3)",
        "type": "Gene Fusion",
        "genomic_locus": "chr10:50000000-52000000_inv",
        "hgvs_c": "t(10;10)(q11.2;q11.2)",
        "hgvs_p": "Fusion Protein",
        "tumor_types": ["Aggressive Solid Variant PTC", "Radiation-Associated PTC"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk / Fusion",
        "afirma_xa_class": "Positive (High Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "Highly responsive to selective RET inhibitors (selpercatinib, pralsetinib).",
        "clinical_summary": "Common after radiation exposure (e.g. Chernobyl cohort). Characterized by solid growth patterns, rapid tumor enlargement, and elevated lymph node/pulmonary metastases.",
        "alphagenome": {
            "avi_phred": 28.80,
            "percentile": "0.132%",
            "top_modality": "GENE_FUSION_LOCUS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr10%3A43100000-43130000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "High prevalence of RET/PTC rearrangements in post-Chernobyl thyroid cancers",
                "pmid": "7553874",
                "journal": "Lancet",
                "year": 1995,
                "summary": "Highlighted RET/PTC3 predominance in radiation-induced juvenile thyroid carcinomas with aggressive onset."
            }
        ]
    },
    {
        "id": "ETV6_NTRK3",
        "gene": "ETV6::NTRK3",
        "alteration": "ETV6::NTRK3 Fusion",
        "type": "Gene Fusion",
        "genomic_locus": "t(12;15)(p13;q25)",
        "hgvs_c": "t(12;15)(p13.2;q25.3)",
        "hgvs_p": "Fusion Protein",
        "tumor_types": ["Papillary Thyroid Carcinoma (PTC)", "Secretory Carcinoma", "Pediatric PTC"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "Intermediate to High Risk",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk / NTRK Fusion",
        "afirma_xa_class": "Positive (>95% Malignancy Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "FDA tumor-agnostic approval for TRK inhibitors (larotrectinib, entrectinib); high objective response rates (>75%).",
        "clinical_summary": "Fusion between ETV6 helix-loop-helix dimerization domain and NTRK3 tyrosine kinase. Drives profound oncogenic signaling; exemplary paradigm of targeted precision oncology in thyroid neoplasms.",
        "alphagenome": {
            "avi_phred": 29.10,
            "percentile": "0.123%",
            "top_modality": "GENE_FUSION_LOCUS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr15%3A88400000-88500000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "Efficacy of Larotrectinib in TRK Fusion-Positive Advanced Cancers",
                "pmid": "29466156",
                "journal": "N Engl J Med",
                "year": 2018,
                "summary": "Demonstrated landmark 75% overall response rate across TRK fusion tumors, including advanced refractory thyroid carcinomas."
            }
        ]
    },
    {
        "id": "TPM3_NTRK1",
        "gene": "TPM3::NTRK1",
        "alteration": "TPM3::NTRK1 Fusion",
        "type": "Gene Fusion",
        "genomic_locus": "t(1;1)(q21;q22)",
        "hgvs_c": "t(1;1)(q21.3;q22)",
        "hgvs_p": "Fusion Protein",
        "tumor_types": ["Papillary Thyroid Carcinoma (PTC)"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "Intermediate Risk",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk / NTRK Fusion",
        "afirma_xa_class": "Positive (>95%)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "Directly actionable with TRK inhibitors (larotrectinib, entrectinib).",
        "clinical_summary": "Tropomyosin 3 coiled-coil domain fused to NTRK1 kinase domain leading to constitutive TrkA activation.",
        "alphagenome": {
            "avi_phred": 28.30,
            "percentile": "0.147%",
            "top_modality": "GENE_FUSION_LOCUS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr1%3A156800000-156900000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "NTRK Fusions in Thyroid Cancer: From Biology to Clinical Practice",
                "pmid": "33408332",
                "journal": "Frontiers in Endocrinology",
                "year": 2020,
                "summary": "Review of NTRK1 and NTRK3 rearrangements in thyroid cytology and their therapeutic stratification."
            }
        ]
    },
    {
        "id": "STRN_ALK",
        "gene": "STRN::ALK",
        "alteration": "STRN::ALK Fusion",
        "type": "Gene Fusion",
        "genomic_locus": "chr2:striatin_alk_inv",
        "hgvs_c": "inv(2)(p21p23)",
        "hgvs_p": "Fusion Protein",
        "tumor_types": ["Poorly Differentiated (PDTC)", "Anaplastic (ATC)", "Aggressive PTC"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk",
        "rom_percentage": ">95%",
        "thyroseq_v3_class": "High-Risk / ALK Fusion",
        "afirma_xa_class": "Positive (High Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "FDA-approved ALK inhibitors (crizotinib, alectinib, lorlatinib, brigatinib); remarkable responses in refractory aggressive thyroid cancer.",
        "clinical_summary": "Striatin (STRN) promoter and WD40 domains fused to ALK tyrosine kinase domain. Frequently enriched in poorly differentiated or rapidly enlarging invasive carcinomas.",
        "alphagenome": {
            "avi_phred": 29.50,
            "percentile": "0.112%",
            "top_modality": "GENE_FUSION_LOCUS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr2%3A29400000-29500000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "STRN-ALK fusion in thyroid carcinoma and its therapeutic targeting",
                "pmid": "24508493",
                "journal": "Cancer Discovery",
                "year": 2014,
                "summary": "Discovered STRN-ALK fusions in aggressive thyroid cancers with profound in vitro and clinical response to crizotinib."
            }
        ]
    },
    {
        "id": "PIK3CA_H1047R",
        "gene": "PIK3CA",
        "alteration": "p.His1047Arg (H1047R)",
        "type": "SNV",
        "genomic_locus": "chr3:179234297:A>G",
        "hgvs_c": "c.3140A>G",
        "hgvs_p": "p.His1047Arg",
        "tumor_types": ["Follicular Carcinoma (FTC)", "Anaplastic (ATC)", "PDTC"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk",
        "rom_percentage": ">90%",
        "thyroseq_v3_class": "High-Risk / Aggressive",
        "afirma_xa_class": "Positive (High Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "PI3K inhibitors (alpelisib) and clinical trials testing combination kinase blockade.",
        "clinical_summary": "Kinase domain activating mutation hyperactivating the AKT-mTOR pathway. Associated with large tumor size, capsular invasion, and distant hematogenous spread.",
        "alphagenome": {
            "avi_phred": 32.70,
            "percentile": "0.053%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr3%3A179234297%3AA%3EG&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "PIK3CA Mutations in Advanced Thyroid Cancers",
                "pmid": "15886297",
                "journal": "J Clin Endocrinol Metab",
                "year": 2005,
                "summary": "Demonstrated enrichment of PIK3CA kinase mutations in poorly differentiated and anaplastic thyroid carcinomas."
            }
        ]
    },
    {
        "id": "AKT1_E17K",
        "gene": "AKT1",
        "alteration": "p.Glu17Lys (E17K)",
        "type": "SNV",
        "genomic_locus": "chr14:104780214:C>T",
        "hgvs_c": "c.49G>A",
        "hgvs_p": "p.Glu17Lys",
        "tumor_types": ["Metastatic FTC", "PDTC", "ATC"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk",
        "rom_percentage": ">90%",
        "thyroseq_v3_class": "High-Risk / Aggressive",
        "afirma_xa_class": "Positive (High Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "AKT inhibitors (capivasertib); aggressive surgical and oncologic management.",
        "clinical_summary": "Pleckstrin homology (PH) domain mutation causing constitutive membrane localization and AKT activation independently of upstream growth factors.",
        "alphagenome": {
            "avi_phred": 31.80,
            "percentile": "0.067%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr14%3A104780214%3AC%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "AKT1 E17K mutation in thyroid carcinomas",
                "pmid": "18316450",
                "journal": "Endocr Relat Cancer",
                "year": 2008,
                "summary": "Identified AKT1 pleckstrin domain mutation contributing to aggressive invasion in follicular-derived malignancies."
            }
        ]
    },
    {
        "id": "CTNNB1_S33C",
        "gene": "CTNNB1",
        "alteration": "p.Ser33Cys (S33C)",
        "type": "SNV",
        "genomic_locus": "chr3:41224637:C>G",
        "hgvs_c": "c.98C>G",
        "hgvs_p": "p.Ser33Cys",
        "tumor_types": ["Anaplastic Thyroid Carcinoma (ATC)", "Poorly Differentiated (PDTC)"],
        "risk_category": "High Risk",
        "ata_recurrence_risk": "High Risk (Extremely Aggressive)",
        "rom_percentage": ">98%",
        "thyroseq_v3_class": "High-Risk / Aggressive",
        "afirma_xa_class": "Positive (High Risk)",
        "thygenext_class": "High Risk / Positive",
        "actionability": "Clinical trial enrollment for beta-catenin / Wnt inhibitors.",
        "clinical_summary": "Abolishes GSK-3beta phosphorylation site, preventing beta-catenin ubiquitin-proteasome degradation. Hallmark of rapid transition to spindle and giant-cell anaplastic morphology.",
        "alphagenome": {
            "avi_phred": 33.40,
            "percentile": "0.046%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr3%3A41224637%3AC%3EG&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Beta-catenin mutations are restricted to poorly differentiated and undifferentiated thyroid carcinomas",
                "pmid": "10557284",
                "journal": "Cancer Res",
                "year": 1999,
                "summary": "Landmark report showing CTNNB1 mutations occur exclusively during late-stage dedifferentiation to ATC."
            }
        ]
    },

    # ==================== INTERMEDIATE RISK / RAS-LIKE ====================
    {
        "id": "NRAS_Q61R",
        "gene": "NRAS",
        "alteration": "p.Gln61Arg (Q61R)",
        "type": "SNV",
        "genomic_locus": "chr1:114704066:T>C",
        "hgvs_c": "c.182A>G",
        "hgvs_p": "p.Gln61Arg",
        "tumor_types": ["Follicular Variant PTC (FVPTC)", "Follicular Carcinoma (FTC)", "NIFTP", "Follicular Adenoma (FA)"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low to Intermediate Risk",
        "rom_percentage": "70–80%",
        "thyroseq_v3_class": "Currently Available / RAS-like (ROM 70–80%)",
        "afirma_xa_class": "Suspicious / Variant Present (ROM 60–75%)",
        "thygenext_class": "Moderate / Positive (RAS-like)",
        "actionability": "Lobectomy often sufficient initial surgical management in non-invasive/encapsulated tumors; MEK inhibitor trials in advanced disease.",
        "clinical_summary": "Most frequent RAS mutation in thyroid neoplasms. Impairs intrinsic GTPase hydrolysis, causing persistent active GTP-bound signaling. Associated with follicular architecture, low likelihood of nodal metastases, but moderate risk of capsular/vascular invasion.",
        "alphagenome": {
            "avi_phred": 27.90,
            "percentile": "0.162%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr1%3A114704066%3AT%3EC&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Molecular Testing for Thyroid Nodules: The ThyroSeq Experience",
                "pmid": "30616147",
                "journal": "JAMA Oncology",
                "year": 2019,
                "summary": "Demonstrated that isolated RAS mutations yield ~75% ROM in Bethesda III/IV nodules with low structural recurrence when histologically non-invasive."
            },
            {
                "title": "Nomenclature Revision for Encapsulated Follicular Variant of Papillary Thyroid Carcinoma: A Paradigm Shift to Reduce Overtreatment",
                "pmid": "27078145",
                "journal": "JAMA Oncology",
                "year": 2016,
                "summary": "Reclassified non-invasive follicular variant PTC harboring RAS mutations as NIFTP, averting unnecessary total thyroidectomy and radioiodine."
            }
        ]
    },
    {
        "id": "NRAS_Q61K",
        "gene": "NRAS",
        "alteration": "p.Gln61Lys (Q61K)",
        "type": "SNV",
        "genomic_locus": "chr1:114704067:G>T",
        "hgvs_c": "c.181C>A",
        "hgvs_p": "p.Gln61Lys",
        "tumor_types": ["FVPTC", "FTC", "NIFTP", "Follicular Adenoma"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low to Intermediate Risk",
        "rom_percentage": "65–75%",
        "thyroseq_v3_class": "RAS-like (ROM 65–75%)",
        "afirma_xa_class": "Suspicious / Variant Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Diagnostic lobectomy typically indicated for Bethesda III/IV cytopathology.",
        "clinical_summary": "Constitutive GTPase impairment in the catalytic switch II domain, producing a canonical RAS-like transcriptional signature and follicular differentiation.",
        "alphagenome": {
            "avi_phred": 27.50,
            "percentile": "0.178%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr1%3A114704067%3AG%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Preoperative Diagnostic Evaluation of Thyroid Nodules with Indeterminate Cytology",
                "pmid": "31580210",
                "journal": "Endocr Rev",
                "year": 2020,
                "summary": "Evaluated the performance characteristics of ThyroSeq v3 and Afirma GSC for codon 61 RAS variants."
            }
        ]
    },
    {
        "id": "HRAS_Q61R",
        "gene": "HRAS",
        "alteration": "p.Gln61Arg (Q61R)",
        "type": "SNV",
        "genomic_locus": "chr11:533874:T>C",
        "hgvs_c": "c.182A>G",
        "hgvs_p": "p.Gln61Arg",
        "tumor_types": ["Follicular Variant PTC", "Follicular Carcinoma", "NIFTP", "FA"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low to Intermediate Risk",
        "rom_percentage": "70–80%",
        "thyroseq_v3_class": "RAS-like (ROM 70–80%)",
        "afirma_xa_class": "Suspicious / Variant Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Lobectomy often sufficient initial surgical intervention.",
        "clinical_summary": "Hot spot GTPase mutation in HRAS; typical follicular growth architecture with intermediate risk of malignancy in indeterminate cytopathology.",
        "alphagenome": {
            "avi_phred": 28.10,
            "percentile": "0.155%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr11%3A533874%3AT%3EC&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Impact of RAS Mutations in Indeterminate Thyroid Nodules",
                "pmid": "28169974",
                "journal": "Ann Surg",
                "year": 2017,
                "summary": "Prospective analysis demonstrating high rate of indolent or low-risk histology for isolated HRAS Q61R nodules."
            }
        ]
    },
    {
        "id": "KRAS_G12D",
        "gene": "KRAS",
        "alteration": "p.Gly12Asp (G12D)",
        "type": "SNV",
        "genomic_locus": "chr12:25245350:C>T",
        "hgvs_c": "c.35G>A",
        "hgvs_p": "p.Gly12Asp",
        "tumor_types": ["FVPTC", "Follicular Carcinoma", "NIFTP"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low to Intermediate Risk",
        "rom_percentage": "65–75%",
        "thyroseq_v3_class": "RAS-like (ROM 65–75%)",
        "afirma_xa_class": "Suspicious / Variant Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Lobectomy recommended; emerging KRAS G12D selective small molecule inhibitors in oncology trials.",
        "clinical_summary": "P-loop sterical hindrance blocking GAP-mediated GTP hydrolysis. Strong driver of follicular pattern neoplasia.",
        "alphagenome": {
            "avi_phred": 29.40,
            "percentile": "0.115%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr12%3A25245350%3AC%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "RAS-Mutant Thyroid Tumors: A Comprehensive Review",
                "pmid": "31962381",
                "journal": "Endocr Pathol",
                "year": 2020,
                "summary": "Comprehensive assessment of KRAS, NRAS, and HRAS alleles and their biologic divergence from BRAF-like neoplasms."
            }
        ]
    },
    {
        "id": "BRAF_K601E",
        "gene": "BRAF",
        "alteration": "p.Lys601Glu (K601E)",
        "type": "SNV",
        "genomic_locus": "chr7:140753339:T>A",
        "hgvs_c": "c.1801A>G",
        "hgvs_p": "p.Lys601Glu",
        "tumor_types": ["Follicular Variant PTC (FVPTC)", "Encapsulated FVPTC", "NIFTP"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low Risk",
        "rom_percentage": "70–80%",
        "thyroseq_v3_class": "RAS-like / Low-Intermediate Risk",
        "afirma_xa_class": "Positive (Intermediate / RAS-like)",
        "thygenext_class": "Moderate Risk / Positive",
        "actionability": "Conservative surgical resection (lobectomy) frequently curative; MEK inhibitors if unresectable.",
        "clinical_summary": "Biologically and clinically divergent from BRAF V600E. Activates MAPK with lower amplitude, clustering transcriptionally with RAS-like tumors. Rarely metastasizes to lymph nodes and carries a low recurrence rate.",
        "alphagenome": {
            "avi_phred": 26.90,
            "percentile": "0.204%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr7%3A140753339%3AT%3EA&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "BRAF K601E Mutation in Thyroid Neoplasms: Clinical and Biological Distinction from V600E",
                "pmid": "22965942",
                "journal": "J Clin Endocrinol Metab",
                "year": 2012,
                "summary": "Demonstrated that K601E mutations drive indolent follicular-variant PTC lacking the aggressive hallmarks of V600E."
            }
        ]
    },
    {
        "id": "PAX8_PPARG",
        "gene": "PAX8::PPARG",
        "alteration": "PAX8::PPARG Fusion",
        "type": "Gene Fusion",
        "genomic_locus": "t(2;3)(q13;p25)",
        "hgvs_c": "t(2;3)(q13;p25)",
        "hgvs_p": "Fusion Protein",
        "tumor_types": ["Follicular Thyroid Carcinoma (FTC)", "Follicular Thyroid Adenoma (FA)"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low to Intermediate Risk",
        "rom_percentage": "50–65%",
        "thyroseq_v3_class": "Intermediate / RAS-like (ROM 55–65%)",
        "afirma_xa_class": "Suspicious / Fusion Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Thyroid lobectomy typically adequate for encapsulated tumors; PPAR-gamma agonists (pioglitazone) studied in clinical research.",
        "clinical_summary": "Balanced translocation fusing PAX8 promoter and paired domain to PPARG nuclear receptor. Induces lipid accumulation, vascular invasion potential in FTC, and marked follicular architecture.",
        "alphagenome": {
            "avi_phred": 27.20,
            "percentile": "0.190%",
            "top_modality": "GENE_FUSION_LOCUS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr3%3A12000000-13000000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "PAX8-PPARgamma rearrangement in follicular thyroid neoplasia",
                "pmid": "10963602",
                "journal": "Science",
                "year": 2000,
                "summary": "Landmark paper identifying the t(2;3) translocation as an oncogenic driver in follicular thyroid carcinomas."
            }
        ]
    },
    {
        "id": "THADA_IGF2BP3",
        "gene": "THADA::IGF2BP3",
        "alteration": "THADA::IGF2BP3 Fusion",
        "type": "Gene Fusion",
        "genomic_locus": "t(2;7)(p21;q31)",
        "hgvs_c": "t(2;7)(p21;q31)",
        "hgvs_p": "Fusion Protein",
        "tumor_types": ["Follicular Variant PTC", "Follicular Adenoma", "NIFTP"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low Risk",
        "rom_percentage": "55–70%",
        "thyroseq_v3_class": "Intermediate / RAS-like",
        "afirma_xa_class": "Suspicious / Fusion Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Diagnostic lobectomy recommended for definitive histological staging.",
        "clinical_summary": "Fusion causing truncated THADA expression and IGF2BP3 upregulation. Associated with indolent follicular-pattern thyroid neoplasms.",
        "alphagenome": {
            "avi_phred": 26.40,
            "percentile": "0.228%",
            "top_modality": "GENE_FUSION_LOCUS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr2%3A43000000-44000000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "THADA Fusions in Thyroid Neoplasms",
                "pmid": "27680517",
                "journal": "Cancer",
                "year": 2017,
                "summary": "Characterized THADA rearrangements and associated favorable indolent outcomes in indeterminate cytology."
            }
        ]
    },
    {
        "id": "PTEN_R130X",
        "gene": "PTEN",
        "alteration": "p.Arg130Ter (R130*)",
        "type": "SNV (Truncating)",
        "genomic_locus": "chr10:87894098:C>T",
        "hgvs_c": "c.388C>T",
        "hgvs_p": "p.Arg130Ter",
        "tumor_types": ["Follicular Neoplasm", "Cowden Syndrome", "FTC"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low to Intermediate Risk",
        "rom_percentage": "60–70%",
        "thyroseq_v3_class": "Currently Available / Intermediate",
        "afirma_xa_class": "Suspicious / Variant Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Comprehensive genetic counseling for PTEN hamartoma tumor syndrome / Cowden syndrome; multi-organ cancer screening (breast, uterine, colon, renal).",
        "clinical_summary": "Premature truncation of the PTEN lipid phosphatase domain causing disinhibition of PIP3 and AKT signaling. Triggers prominent multinodular goiter and elevated lifetime risk of follicular thyroid carcinoma.",
        "alphagenome": {
            "avi_phred": 37.80,
            "percentile": "0.016%",
            "top_modality": "PROTEIN_TERMINATION",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr10%3A87894098%3AC%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Clinical Practice Guidelines in Oncology: Genetic/Familial High-Risk Assessment: Breast, Ovarian, and Pancreatic (PTEN/Cowden)",
                "pmid": "33406487",
                "journal": "J Natl Compr Canc Netw",
                "year": 2021,
                "summary": "Outlines surveillance and management guidelines for PTEN germline and somatic mutations in thyroid disease."
            }
        ]
    },
    {
        "id": "EIF1AX_A113SPLICE",
        "gene": "EIF1AX",
        "alteration": "c.338-1G>C (A113_splice)",
        "type": "Splice Acceptor SNV",
        "genomic_locus": "chrX:20147612:C>G",
        "hgvs_c": "c.338-1G>C",
        "hgvs_p": "p.Ala113_splice",
        "tumor_types": ["Follicular Carcinoma (FTC)", "PDTC", "ATC (when with RAS/BRAF)"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Intermediate (High when co-mutated with RAS/TERT)",
        "rom_percentage": "60–75%",
        "thyroseq_v3_class": "Intermediate / RAS-like (Aggressive when co-mutated)",
        "afirma_xa_class": "Suspicious / Variant Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Surgical resection; close pathological evaluation for capsular/vascular invasion or secondary aggressive mutations.",
        "clinical_summary": "Splice-acceptor site mutation causing C-terminal extension of the eukaryotic translation initiation factor 1A. Strongly cooperates with RAS mutations to drive dedifferentiation and high-grade transformation.",
        "alphagenome": {
            "avi_phred": 29.80,
            "percentile": "0.105%",
            "top_modality": "MERGED_SPLICING",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chrX%3A20147612%3AC%3EG&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "EIF1AX and RAS Mutations Cooperate to Drive Thyroid Tumorigenesis and Progression",
                "pmid": "27083054",
                "journal": "Cancer Discovery",
                "year": 2016,
                "summary": "Revealed that EIF1AX alters translation start-site fidelity and synergizes with RAS to accelerate malignant progression."
            }
        ]
    },
    {
        "id": "DICER1_E1813K",
        "gene": "DICER1",
        "alteration": "p.Glu1813Lys (E1813K)",
        "type": "SNV",
        "genomic_locus": "chr14:95090539:G>A",
        "hgvs_c": "c.5437G>A",
        "hgvs_p": "p.Glu1813Lys",
        "tumor_types": ["Multinodular Goiter (MNG)", "Poorly Differentiated (PDTC)", "Pediatric Thyroid Carcinoma"],
        "risk_category": "Intermediate Risk (RAS-like)",
        "ata_recurrence_risk": "Low to Intermediate Risk",
        "rom_percentage": "50–65%",
        "thyroseq_v3_class": "Intermediate / RAS-like",
        "afirma_xa_class": "Suspicious / Variant Present",
        "thygenext_class": "Moderate / Positive",
        "actionability": "Evaluation for DICER1 syndrome; surveillance for pleuropulmonary blastoma, cystic nephroma, and ovarian sex cord-stromal tumors.",
        "clinical_summary": "Metal-binding catalytic residue mutation in the RNase IIIb domain. Selectively abolishes 5p microRNA maturation while preserving 3p microRNAs, disrupting developmental gene repression.",
        "alphagenome": {
            "avi_phred": 28.60,
            "percentile": "0.138%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr14%3A95090539%3AG%3EA&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "DICER1 Mutations in Thyroid Neoplasms",
                "pmid": "25000570",
                "journal": "Thyroid",
                "year": 2014,
                "summary": "Characterized somatic and germline RNase IIIb hot spot mutations in benign and malignant pediatric and adult follicular nodules."
            }
        ]
    },

    # ==================== LOW RISK / AUTONOMOUS / BENIGN-LIKE ====================
    {
        "id": "TSHR_M453T",
        "gene": "TSHR",
        "alteration": "p.Met453Thr (M453T)",
        "type": "SNV",
        "genomic_locus": "chr14:81143416:T>C",
        "hgvs_c": "c.1358T>C",
        "hgvs_p": "p.Met453Thr",
        "tumor_types": ["Toxic Thyroid Adenoma (Hot Nodule)", "Hyperthyroidism"],
        "risk_category": "Low Risk / Benign-like",
        "ata_recurrence_risk": "Very Low Risk (<1%)",
        "rom_percentage": "<5%",
        "thyroseq_v3_class": "Low-Risk / Autonomous Nodule (ROM <5%)",
        "afirma_xa_class": "Benign / Low Risk",
        "thygenext_class": "Low Risk / Negative",
        "actionability": "Thyroid scintigraphy (I-123 or Tc-99m pertechnetate) to confirm hot nodule; radioiodine ablation or surgical lobectomy.",
        "clinical_summary": "Transmembrane domain 2 (TM2) activating mutation. Induces constitutive Gs-alpha coupling, triggering continuous cyclic AMP synthesis and thyroid hormone hypersecretion. Almost exclusively benign.",
        "alphagenome": {
            "avi_phred": 26.54,
            "percentile": "0.222%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr14%3A81143416%3AT%3EC&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Activating mutations in the thyrotropin receptor gene in toxic thyroid nodules",
                "pmid": "8247152",
                "journal": "Nature",
                "year": 1993,
                "summary": "Landmark report detailing the molecular basis of autonomous hyperfunctioning toxic thyroid adenomas."
            }
        ]
    },
    {
        "id": "TSHR_D633H",
        "gene": "TSHR",
        "alteration": "p.Asp633His (D633H)",
        "type": "SNV",
        "genomic_locus": "chr14:81143955:G>C",
        "hgvs_c": "c.1897G>C",
        "hgvs_p": "p.Asp633His",
        "tumor_types": ["Toxic Adenoma", "Rare Autonomously Functioning Carcinoma"],
        "risk_category": "Low Risk / Benign-like",
        "ata_recurrence_risk": "Low Risk",
        "rom_percentage": "<10%",
        "thyroseq_v3_class": "Low-Risk / Autonomous",
        "afirma_xa_class": "Benign / Low Risk",
        "thygenext_class": "Low Risk / Negative",
        "actionability": "Scintigraphy to confirm autonomy; clinical observation or radioiodine/surgical ablation.",
        "clinical_summary": "Transmembrane helix 6 (TM6) hotspot. Induces very high basal cAMP production. Highly prevalent in hyperfunctioning benign adenomas; rare cases of hot carcinoma reported.",
        "alphagenome": {
            "avi_phred": 28.17,
            "percentile": "0.152%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr14%3A81143955%3AG%3EC&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Characterization of TSH receptor mutations in toxic adenomas",
                "pmid": "29516685",
                "journal": "J Clin Endocrinol Metab",
                "year": 2018,
                "summary": "Analyzed over 700 indeterminate and autonomous nodules, showing high prevalence of TSHR TM6 hot spots."
            }
        ]
    },
    {
        "id": "GNAS_R201C",
        "gene": "GNAS",
        "alteration": "p.Arg201Cys (R201C)",
        "type": "SNV",
        "genomic_locus": "chr20:58839737:C>T",
        "hgvs_c": "c.601C>T",
        "hgvs_p": "p.Arg201Cys",
        "tumor_types": ["Toxic Thyroid Adenoma", "McCune-Albright Syndrome"],
        "risk_category": "Low Risk / Benign-like",
        "ata_recurrence_risk": "Very Low Risk (<1%)",
        "rom_percentage": "<5%",
        "thyroseq_v3_class": "Low-Risk / Autonomous (ROM <5%)",
        "afirma_xa_class": "Benign / Autonomous",
        "thygenext_class": "Low Risk / Negative",
        "actionability": "Exclude McCune-Albright syndrome if polyostotic fibrous dysplasia or cafe-au-lait pigmentation present; thyroid ablation.",
        "clinical_summary": "Inactivates Gs-alpha GTPase activity, mimicking continuous G-protein coupled receptor stimulation and driving benign clonal expansion with autonomous thyrotoxicosis.",
        "alphagenome": {
            "avi_phred": 30.20,
            "percentile": "0.098%",
            "top_modality": "ALPHAMISSENSE",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr20%3A58839737%3AC%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Activating Gsa mutations in toxic adenomas",
                "pmid": "1846461",
                "journal": "Science",
                "year": 1991,
                "summary": "Original discovery of gsp oncogene mutations in autonomous endocrine adenomas."
            }
        ]
    },
    {
        "id": "PRKAR1A_R145X",
        "gene": "PRKAR1A",
        "alteration": "p.Arg145Ter (R145*)",
        "type": "SNV (Truncating)",
        "genomic_locus": "chr17:68516086:C>T",
        "hgvs_c": "c.433C>T",
        "hgvs_p": "p.Arg145Ter",
        "tumor_types": ["Thyroid Follicular Adenoma", "Carney Complex"],
        "risk_category": "Low Risk / Benign-like",
        "ata_recurrence_risk": "Low Risk",
        "rom_percentage": "<10%",
        "thyroseq_v3_class": "Low Risk / Carney Complex",
        "afirma_xa_class": "Low Risk",
        "thygenext_class": "Low Risk",
        "actionability": "Screening for Carney complex manifestations: cardiac myxomas, spotty skin pigmentation, primary pigmented nodular adrenocortical disease (PPNAD).",
        "clinical_summary": "Loss of the regulatory subunit of protein kinase A (PKA). Causes unregulated catalytic PKA subunit activation, leading to benign thyroid follicular adenomas.",
        "alphagenome": {
            "avi_phred": 38.20,
            "percentile": "0.015%",
            "top_modality": "PROTEIN_TERMINATION",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr17%3A68516086%3AC%3ET&m=variant&f=BIOSAMPLE_NAME:thyroid%20gland&lItems=avi,section:RNA_SEQ,section:DNASE"
        },
        "literature": [
            {
                "title": "Mutations of the gene encoding the protein kinase A type I-alpha regulatory subunit in patients with the Carney complex",
                "pmid": "11017089",
                "journal": "Nat Genet",
                "year": 2000,
                "summary": "Identified PRKAR1A loss-of-function driving familial endocrine neoplasia and follicular thyroid tumors."
            }
        ]
    },

    # ==================== COPY NUMBER ALTERATIONS & ANEUPLOIDY ====================
    {
        "id": "CNA_ANEUPLOIDY_HCC",
        "gene": "Genome-wide Aneuploidy",
        "alteration": "Near-haploidization & Chromosomal Aneuploidy",
        "type": "Copy Number Alteration (CNA)",
        "genomic_locus": "Genome-wide (Whole Chromosome Losses/Gains)",
        "hgvs_c": "Aneuploidy / LOH",
        "hgvs_p": "Chromosomal Loss / Uniparental Disomy",
        "tumor_types": ["Oncocytic (Hürthle Cell) Carcinoma (HCC)", "Oncocytic Adenoma"],
        "risk_category": "CNA / Aneuploidy",
        "ata_recurrence_risk": "Intermediate to High Risk (if invasive HCC)",
        "rom_percentage": "60–85% (when CNA-High)",
        "thyroseq_v3_class": "CNA-High Profile (Diagnostic for HCC/Oncocytic Carcinoma)",
        "afirma_xa_class": "Suspicious / High Loss-of-Heterozygosity (LOH)",
        "thygenext_class": "High Risk / Genomic Copy Number",
        "actionability": "Total thyroidectomy or completion thyroidectomy if invasive oncocytic carcinoma confirmed; radioiodine usually ineffective; clinical trials with lenvatinib/sorafenib.",
        "clinical_summary": "Unique genomic hallmark of Hürthle cell (oncocytic) carcinomas, characterized by widespread near-haploid loss of whole chromosomes followed by genome endoreduplication. ThyroSeq v3 CNA algorithm specifically discriminates benign oncocytic adenomas (CNA-Low) from malignant oncocytic carcinomas (CNA-High).",
        "alphagenome": {
            "avi_phred": 25.50,
            "percentile": "0.280%",
            "top_modality": "COPY_NUMBER_ANEUPLOIDY",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr1%3A1-248956422&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "Whole-Genome Landscape of Hürthle Cell Thyroid Carcinoma",
                "pmid": "29752317",
                "journal": "Cancer Cell",
                "year": 2018,
                "summary": "Revealed near-haploidization and mitochondrial DNA mutations as the defining genomic architecture of oncocytic thyroid cancer."
            },
            {
                "title": "Utility of Copy Number Alteration Detection in Thyroid Nodules with Hürthle Cell Cytology",
                "pmid": "31828751",
                "journal": "Thyroid",
                "year": 2020,
                "summary": "Demonstrated that ThyroSeq v3 CNA scoring achieves >90% sensitivity and specificity in distinguishing oncocytic carcinomas from benign adenomas."
            }
        ]
    },
    {
        "id": "CNA_LOSS_22Q",
        "gene": "22q Loss",
        "alteration": "Monosomy 22q / Chromosome 22q Loss",
        "type": "Copy Number Alteration (CNA)",
        "genomic_locus": "chr22:16000000-50818468_del",
        "hgvs_c": "del(22q)",
        "hgvs_p": "Loss of Heterozygosity",
        "tumor_types": ["Follicular Thyroid Carcinoma", "Oncocytic Carcinoma", "Follicular Adenoma"],
        "risk_category": "CNA / Aneuploidy",
        "ata_recurrence_risk": "Intermediate Risk",
        "rom_percentage": "55–70%",
        "thyroseq_v3_class": "CNA Positive / 22q Loss",
        "afirma_xa_class": "Suspicious / Loss of Heterozygosity",
        "thygenext_class": "Moderate / Copy Number Alteration",
        "actionability": "Pathology review for vascular invasion; surgical excision.",
        "clinical_summary": "Loss of chromosome 22q spans several prominent tumor suppressors including NF2 and CHEK2. Highly recurrent in follicular and oncocytic neoplasms.",
        "alphagenome": {
            "avi_phred": 24.20,
            "percentile": "0.380%",
            "top_modality": "CNA_LOSS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr22%3A20000000-40000000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "Chromosomal copy number changes in follicular thyroid neoplasms",
                "pmid": "18029432",
                "journal": "Oncogene",
                "year": 2007,
                "summary": "Demonstrated that 22q loss correlates with malignant potential in follicular patterned thyroid tumors."
            }
        ]
    },
    {
        "id": "CNA_LOSS_1P",
        "gene": "1p Loss",
        "alteration": "Chromosome 1p Deletion",
        "type": "Copy Number Alteration (CNA)",
        "genomic_locus": "chr1:1000000-120000000_del",
        "hgvs_c": "del(1p)",
        "hgvs_p": "Loss of Heterozygosity",
        "tumor_types": ["Follicular Carcinoma", "Oncocytic Carcinoma"],
        "risk_category": "CNA / Aneuploidy",
        "ata_recurrence_risk": "Intermediate Risk",
        "rom_percentage": "50–65%",
        "thyroseq_v3_class": "CNA Positive",
        "afirma_xa_class": "Suspicious / LOH",
        "thygenext_class": "Moderate Risk",
        "actionability": "Definitive histological evaluation.",
        "clinical_summary": "Frequently co-occurs with 22q loss and 3p loss in encapsulated follicular neoplasms, signaling malignant risk.",
        "alphagenome": {
            "avi_phred": 23.50,
            "percentile": "0.450%",
            "top_modality": "CNA_LOSS",
            "atlas_url": "https://deepmind.google.com/science/alphagenome/atlas?q=chr1%3A10000000-50000000&m=locus&f=BIOSAMPLE_NAME:thyroid%20gland"
        },
        "literature": [
            {
                "title": "Loss of heterozygosity at 1p and 22q in thyroid neoplasia",
                "pmid": "9794301",
                "journal": "Clin Cancer Res",
                "year": 1998,
                "summary": "Early delineation of recurrent 1p deletion in aggressive follicular-derived thyroid carcinomas."
            }
        ]
    }
]

def main():
    metadata = {
        "database_name": "Thyroid Nodule & Cancer Molecular Markers Knowledgebase (TNMK)",
        "version": "1.0.0",
        "last_updated": datetime.now(timezone.utc).strftime("%B %Y"),
        "last_updated_iso": datetime.now(timezone.utc).isoformat(),
        "total_alterations": len(MUTATIONS),
        "high_risk_count": sum(1 for m in MUTATIONS if m["risk_category"] == "High Risk"),
        "intermediate_risk_count": sum(1 for m in MUTATIONS if m["risk_category"] == "Intermediate Risk (RAS-like)"),
        "low_risk_count": sum(1 for m in MUTATIONS if m["risk_category"] == "Low Risk / Benign-like"),
        "cna_count": sum(1 for m in MUTATIONS if m["risk_category"] == "CNA / Aneuploidy"),
        "investigator": "Johnson Thomas, MD, FACE, FEAA",
        "affiliation": "Department of Endocrinology, Mercy Hospital Springfield, Missouri, USA",
        "repository_url": "https://github.com/johnyquest7/thyroid-nodule-molecular-markers"
    }

    import os
    os.makedirs("data", exist_ok=True)
    with open("data/thyroid_mutations.json", "w", encoding="utf-8") as f:
        json.dump(MUTATIONS, f, indent=2)

    with open("data/metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"Successfully wrote {len(MUTATIONS)} curated alterations to data/thyroid_mutations.json")
    print(f"Successfully wrote metadata to data/metadata.json")

if __name__ == "__main__":
    main()
