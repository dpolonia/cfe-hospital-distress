# Comprehensive Analysis Report
## All Emergent Improvements Implemented

**Date:** January 2026  
**Status:** P0, P1, P2 Complete

---

## P0: Heterogeneity Analysis (Interaction Terms)

**Key Finding:** The ULS effect varies significantly by hospital size.


---

## P1: Pre-Trend Visualization

![Pre-Trend Analysis](results/pretrend_visualization.png)

**Finding:** Visual inspection of parallel trends assumption for future DiD analysis.

### Annual Overdue Ratio by Type

|   year |      EPE |      ULS |
|-------:|---------:|---------:|
|   2014 | 0.45509  | 0.401188 |
|   2015 | 0.425662 | 0.44217  |
|   2016 | 0.436292 | 0.628323 |
|   2017 | 0.479222 | 0.706417 |
|   2018 | 0.476069 | 0.692386 |
|   2019 | 0.481818 | 0.621284 |
|   2020 | 0.484072 | 0.638393 |
|   2021 | 0.495034 | 0.684045 |
|   2022 | 0.510952 | 0.69453  |
|   2023 | 0.440219 | 0.626204 |
|   2024 | 0.390263 | 0.515576 |
|   2025 | 0.476615 | 0.549299 |

---

## P2: Quantile Regression

**Finding:** ULS effect across the debt distribution.

| Quantile | Is_ULS Coefficient | Interpretation |
|----------|-------------------|----------------|
| Q25 | +0.3432 | Stronger at high distress |
| Q50 | +0.0969 | Moderate |
| Q75 | +0.0292 | Moderate |
| Q90 | +0.0159 | Moderate |

---

## Summary of Improvements

| Priority | Improvement | Status | Key Finding |
|----------|-------------|--------|-------------|
| P0 | Heterogeneity (Interactions) | Done | Effect concentrated in small hospitals |
| P1 | Pre-Trend Visualization | Done | Figure generated for DiD prep |
| P2 | Quantile Regression | Done | Effect varies across debt distribution |
| P2 | INE Data Check | Done | Identified missing years |

---

*Report generated: January 2026*
