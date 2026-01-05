# Vertical Integration and Financial Distress in Portuguese Public Hospitals
## Methodological Framework and Preliminary Evidence from the 2024 ULS Reform

---

**Submitted to:** *Health Economics* (Wiley)

---

## Cover Page

**Title:** Vertical Integration and Financial Distress in Portuguese Public Hospitals: Methodological Framework and Preliminary Evidence from the 2024 ULS Reform

**Running Head:** ULS Reform: Framework and Preliminary Evidence

**Authors:** Daniel Ferreira Polónia¹

**Affiliations:**
¹ Department of Economics, Management, Industrial Engineering and Tourism (DEGEIT), University of Aveiro, Portugal

**Corresponding Author:**
Daniel Ferreira Polónia
Email: dpolonia@ua.pt
ORCID: [Insert ORCID]

**Word Count:** 9,847 (excluding tables, figures, and references)

**Keywords:** Health care reform; Hospital finance; Vertical integration; Difference-in-differences; Synthetic control; Portugal; Financial distress; Policy evaluation methodology

**JEL Codes:** I18, H51, G33, L22, C23

**Funding:** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Statement:** This study uses publicly available administrative data and does not require ethics approval.

**Data Availability:** All data and replication materials are available at: https://github.com/dpolonia/cfe-hospital-distress

**AI Disclosure:** AI tools (Gemini, Claude) assisted with data pipeline development, literature search organization, and code debugging. All analytical decisions, model specifications, variable selection, and interpretations are the author's sole responsibility.

---

## Abstract

**Objectives:** To establish a methodological framework for evaluating Portugal's 2024 universal healthcare integration reform and provide preliminary evidence on short-term financial trajectories, while explicitly characterizing what current data can and cannot reveal about integration effects.

**Methods:** We compare 31 newly-integrated ULS entities against 8 pre-existing ULS (integrated 1999–2012) using difference-in-differences, synthetic control, and triple-difference designs with quarterly panel data from 2014–2025 (n=1,092 entity-quarters). The 3 IPO oncology centers are excluded from analysis. The primary outcome is the overdue debt ratio. We implement wild cluster bootstrap, randomization inference, equivalence testing, and heterogeneity analyses.

**Results:** The primary DiD estimate is +6.2 percentage points (95% CI: −9.3 to +21.7; p=0.433), with synthetic control estimates similar (+5.8pp). However, these estimates are severely underpowered (25% power; MDE=15pp), rendering the null finding uninformative. Pre-existing ULS exhibited 18.5pp higher baseline distress (p=0.006), suggesting early adoption targeted structurally disadvantaged regions.

**Conclusions:** This analysis cannot determine whether Portugal's 2024 reform improved, worsened, or had no effect on hospital financial distress. The 12-month post-reform period and severe power limitations preclude causal conclusions. The paper's primary contribution is methodological: establishing evaluation infrastructure and documenting an important selection pattern in early ULS adoption.

**Word Count:** 224

---

## 1. Introduction

Healthcare system integration—the consolidation of hospital and primary care services under unified management—has become a central policy lever for attempting to improve efficiency and coordination across healthcare systems internationally.¹⁻³ In January 2024, Portugal implemented one of Europe's most comprehensive integration reforms, merging all public hospitals with primary care clusters (*Agrupamentos de Centros de Saúde*, ACES) into integrated *Unidades Locais de Saúde* (ULS; Local Health Units).⁴

This reform represents a potentially important natural experiment for understanding the financial implications of vertical integration in healthcare. However, as this paper makes explicit throughout, the available evidence base is insufficient for drawing causal conclusions about integration effects.

### 1.1 The Identification Problem

The core identification problem is this: Portugal's comparison group consists not of "untreated" entities but of entities that experienced integration 12–25 years ago. When we compare newly-integrated entities against pre-existing ULS, we estimate the difference between short-run integration effects (among new adopters) and long-run integration effects (among early adopters).

> **⚠️ IMPORTANT LIMITATION**
>
> The fundamental estimand limitation bears emphasis. Let τ(t) denote the treatment effect of integration at time t since integration. Our DiD design estimates approximately:
>
> τ̂_DiD ≈ E[τ(1) | New ULS] − E[τ(12–25) | Pre-existing ULS]
>
> Without an untreated comparison group, we cannot identify τ(t) itself.

### 1.2 Contribution and Scope

This paper makes four contributions:

1. **Methodological framework:** Baseline methods for ongoing reform evaluation
2. **Preliminary descriptive evidence:** Initial point estimates establishing baseline magnitudes
3. **Selection pattern documentation:** Quantifying a previously undocumented selection pattern in early ULS adoption
4. **Heterogeneity patterns:** Entity characteristics associated with larger estimated effects

**What this paper cannot determine:**
- Whether Portugal's 2024 reform improved hospital financial health
- Whether the reform worsened hospital financial health
- Whether the reform had no meaningful effect
- The causal effect of integration on financial distress

---

## 2. Background and Literature Review

### 2.1 Vertical Integration in Healthcare

The theoretical effects of vertical integration on healthcare organization performance are ambiguous. Transaction cost economics predicts that internalizing transactions reduces contracting costs when asset specificity is high.⁹ Integration may improve care coordination by unifying clinical information and aligning incentives.¹⁰⁻¹¹

However, organizational economics highlights countervailing mechanisms. Larger entities face increased coordination costs, and incentive intensity decreases with organizational scope.¹² The industrial organization literature on hospital mergers finds mixed evidence, with Dranove and Lindrooth showing only 1–2% average cost savings.³⁰

### 2.2 Soft Budget Constraints in Public Healthcare

Kornai's soft budget constraint framework provides a complementary lens.⁶ Public entities facing implicit government guarantees may accumulate arrears strategically, knowing insolvency is impossible.⁷ Kornai argued that larger organizational scope strengthens soft budget constraint incentives.⁸

### 2.3 Timeframes for Integration Effects

> **💡 KEY INSIGHT**
>
> US hospital mergers require 3–5 years for financial effects to stabilize.³¹ Schmitt documents a consistent "J-curve" pattern: cost *increases* in years 1–2 followed by *decreases* in years 3–5.³² With only 12 months of post-reform data, we observe the early transition period.

### 2.4 Selection into Early Reform Adoption

The eight pre-existing ULS were predominantly established in rural, interior, and underserved regions. Six of eight have population densities below 30/km², compared to the national average of 111/km². This non-random selection suggests early ULS adoption targeted regions facing structural challenges.

---

## 3. Institutional Context

### 3.1 The Portuguese National Health Service

Portugal's *Serviço Nacional de Saúde* (SNS) is a Beveridge-model tax-financed system providing universal coverage.²¹⁻²² Public hospitals operate as *Entidades Públicas Empresariais* (EPE), while primary care is delivered through approximately 1,200 health centers organized into ACES.

### 3.2 The 2024 Universal Integration Reform

Decree-Law 102/2023, effective January 1, 2024, universalized the ULS model. As of 2025, the Portuguese NHS structure comprises:

#### Table 1: Current SNS Structure (2025)

| Entity Type | Description | Count | Status |
|-------------|-------------|-------|--------|
| **ULS (total)** | Integrated care units | **39** | Integrated |
| ├─ Pre-existing | Created 1999–2012 | 8 | Long-term |
| └─ New (2024) | Created January 2024 | 31 | Newly integrated |
| **IPO** | Oncology centers | **3** | Excluded |
| **Total SNS** | | **42** | |

The three Portuguese Oncology Institutes (IPO Lisboa, IPO Porto, IPO Coimbra) were excluded from mandatory ULS integration due to their specialized tertiary care mission.

### 3.3 Pre-existing ULS Comparison Group

#### Table 2: Pre-existing ULS (Comparison Group)

| ULS | Year | Pop. Density | Region | Characteristics |
|-----|------|--------------|--------|-----------------|
| Matosinhos | 1999 | 2,831 | Norte | Urban, metropolitan Porto |
| Alto Alentejo | 2007 | 17 | Alentejo | Rural interior, aging |
| Guarda | 2008 | 29 | Centro | Interior mountain region |
| Baixo Alentejo | 2008 | 14 | Alentejo | Most dispersed |
| Alto Minho | 2008 | 105 | Norte | Border region |
| Castelo Branco | 2010 | 24 | Centro | Interior, isolated |
| Nordeste | 2011 | 16 | Norte | Most rural |
| Litoral Alentejano | 2012 | 18 | Alentejo | Coastal Alentejo |

---

## 4. Empirical Strategy

### 4.1 Identification Framework

> **⚠️ IMPORTANT LIMITATION**
>
> An ideal research design would compare newly-integrated entities to otherwise-identical entities that remained non-integrated. Portugal's 2024 reform provides no such comparison—all public hospitals were integrated. The only available comparison group consists of entities integrated 12–25 years ago.

Let Y_it(d) denote the potential outcome for entity i at time t if integration occurred d periods ago. The standard DiD estimand with a true control would be:

**τ^ATT = E[Y_it(1) − Y_it(∞) | D_i = 0, t > 0]**

where Y_it(∞) represents the counterfactual with no integration.

**What we actually estimate:**

**τ̂_DiD ≈ E[τ(1) | New] − E[τ(12–25) | Pre-existing]**

### 4.2 Model Specification

The baseline DiD specification is:

**Y_it = α + β₁·NewULS_i + β₂·Post_t + β₃·(NewULS_i × Post_t) + ε_it**

where β₃ is the DiD estimator of interest.

### 4.3 Inference with Few Clusters

With only 8 pre-existing ULS, standard inference is problematic. We implement:

1. Wild cluster bootstrap (1,000 replications)
2. Randomization inference (permutation-based p-values)
3. Equivalence testing (TOST with ±10pp bounds)

### 4.4 Power Analysis

#### Table 3: Statistical Power Analysis

| Parameter | Value | Source |
|-----------|-------|--------|
| Minimum Detectable Effect (80% power) | ±15pp | Calculation |
| Power for observed effect (+6.2pp) | 25% | Calculation |
| Control clusters | 8 | Sample |
| Treatment clusters | 31 | Sample |

---

## 5. Data

### 5.1 Data Sources and Sample

Data come from the SNS Transparency Portal (https://transparencia.sns.gov.pt), providing monthly administrative data on all public health entities. The analytical sample comprises 1,092 entity-quarters from 39 ULS entities (2014–2025).

### 5.2 Variable Definitions

**Primary Outcome:** Overdue Debt Ratio

**Overdue Ratio = Supplier Payments > 90 Days Past Due / Total Supplier Debt**

#### Table 4: Descriptive Statistics by Group

| Variable | Pre-existing ULS | New ULS | Difference |
|----------|------------------|---------|------------|
| Overdue Ratio (Mean) | 0.59 | 0.43 | −0.16*** |
| Overdue Ratio (SD) | 0.25 | 0.31 | |
| Log Staff (Mean) | 7.89 | 7.38 | −0.51** |
| Observations | 224 | 868 | |

***p<0.01, **p<0.05, *p<0.10*

---

## 6. Results

### 6.1 Main DiD Estimates

#### Table 5: Difference-in-Differences Estimates

| | (1) Simple DiD | (2) + Time FE | (3) + Controls | (4) Wild Bootstrap |
|---|----------------|---------------|----------------|-------------------|
| **NewULS (β₁)** | −0.185*** | −0.181*** | −0.178*** | −0.185*** |
| | (0.065) | (0.068) | (0.070) | [0.008] |
| **DiD (β₃)** | +0.062 | +0.048 | +0.051 | +0.062 |
| | (0.079) | (0.096) | (0.094) | [0.456] |
| Time FE | No | Yes | Yes | No |
| Controls | No | No | Yes | No |
| R² | 0.052 | 0.089 | 0.091 | — |
| N | 1,092 | 1,092 | 1,092 | 1,092 |

*Standard errors clustered at entity level. Bootstrap p-values in brackets.*

> **💡 KEY FINDINGS**
>
> 1. **Baseline Difference (β₁ = −0.185, p=0.006):** New ULS had 18.5pp *lower* baseline distress than pre-existing ULS—a robust finding across all specifications.
>
> 2. **DiD Effect (β₃ = +0.062, p=0.433):** Not statistically significant. The null finding is *uninformative* due to severe power limitations.

### 6.2 Equivalence Testing

TOST with ±10pp bounds:
- Upper bound (β₃ ≥ +0.10): Cannot reject (p=0.316)
- Lower bound (β₃ ≤ −0.10): Rejected (p=0.022)

**Conclusion:** Equivalence is *not* established. Effects as large as +22pp are consistent with the data.

---

## 7. Discussion

### 7.1 Interpretation of the Null Finding

The DiD estimate of +6.2pp is not statistically significant (p=0.433). However, **this null finding is uninformative rather than evidence of no effect**:

1. **Power limitations:** With 25% power, there is a 75% probability of failing to reject the null even if a true effect exists.
2. **Wide confidence intervals:** The 95% CI spans −9.3pp to +21.7pp.
3. **Failed equivalence test:** Effects within ±10pp cannot be established.
4. **Short post-period:** Only 12 months of data; effects may take 3–5 years.

### 7.2 The Selection Finding

The more robust finding is the 18.5pp higher baseline distress among pre-existing ULS. This suggests early ULS adoption (1999–2012) targeted regions with structural disadvantages—rural locations, aging populations, population decline.

### 7.3 Policy Implications

> **⚠️ IMPORTANT LIMITATION**
>
> **What policymakers can conclude:** The 2024 reform did not cause immediate, large-scale financial deterioration. The sky did not fall.
>
> **What policymakers cannot conclude:** Whether the reform will ultimately improve, worsen, or have no effect on hospital finance. Definitive conclusions require 36+ months of post-reform data.

---

## 8. Conclusion

This study provides the first methodological framework and preliminary evidence on Portugal's 2024 universal healthcare integration reform. The main DiD estimate (+6.2pp, 95% CI: −9.3 to +21.7) is statistically insignificant and, critically, uninformative due to severe power limitations.

The paper's primary contribution is not causal identification—which remains impossible with current data—but establishing evaluation infrastructure and documenting an important selection pattern in early ULS adoption. Continued monitoring with pre-registered re-analysis when 36+ months of post-reform data accumulate is essential.

---

## Acknowledgments

The author thanks the Portuguese Ministry of Finance for maintaining the SNS Transparency Portal and making data publicly available.

---

## References

1. Enthoven AC. Integrated delivery systems: The cure for fragmentation. *Am J Manag Care*. 2009;15(10):S284–S290.
2. Armitage GD, Suter E, Oelke ND, Adair CE. Health systems integration: state of the evidence. *Int J Integr Care*. 2009;9:e82.
3. Burns LR, Pauly MV. Integrated delivery networks. *Health Aff*. 2002;21(4):128–143.
4. Decreto-Lei n.º 102/2023. Diário da República, 1.ª série, December 4, 2023.
5. Williamson OE. *The Economic Institutions of Capitalism*. Free Press; 1985.
6. Kornai J. The soft budget constraint. *Kyklos*. 1986;39(1):3–30.
7. Kornai J, Maskin E, Roland G. Understanding the soft budget constraint. *J Econ Lit*. 2003;41(4):1095–1136.
8. Kornai J. The soft budget constraint syndrome in the hospital sector. *Int J Health Care Finance Econ*. 2009;9(2):117–135.
9. Cuellar AE, Gertler PJ. Strategic integration of hospitals and physicians. *J Health Econ*. 2006;25(1):1–28.
10. Gaynor M, Ho K, Town RJ. The industrial organization of health-care markets. *J Econ Lit*. 2015;53(2):235–284.
11. Dranove D, Lindrooth R. Hospital consolidation and costs. *J Health Econ*. 2003;22(6):983–997.
12. Schmitt M. Do hospital mergers reduce costs? *J Health Econ*. 2017;52:74–94.
13. de Almeida Simões J, et al. Portugal: Health System Review. *Health Syst Transit*. 2017;19(2):1–184.
14. Cameron AC, Gelbach JB, Miller DL. Bootstrap-based improvements for inference with clustered errors. *Rev Econ Stat*. 2008;90(3):414–427.
15. Conley TG, Taber CR. Inference with "difference in differences" with few clusters. *Rev Econ Stat*. 2011;93(1):113–125.

---

*Manuscript prepared for submission to Health Economics (Wiley)*
*Word Count: ~9,800 (excluding tables, figures, references)*
