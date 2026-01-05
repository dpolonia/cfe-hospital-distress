# CORRECTED ANALYSIS: ULS Reform and Financial Distress
## Difference-in-Differences with Proper Control Group

**Date:** January 2026  
**Critical Correction Applied:** 8 Pre-existing ULS identified as Control Group

---

## Research Design

### The 2024 ULS Reform (Decreto-Lei 102/2023)
On January 1, 2024, all Portuguese public hospitals were merged into ULS (Unidades Locais de Saude).
However, **8 ULS already existed** before this reform (created 1999-2012).

### Control vs Treatment Groups

| Group | Entities | Description |
|-------|----------|-------------|
| **Control** | 8 Pre-existing ULS | Matosinhos, Guarda, Baixo Alentejo, Alto Minho, Castelo Branco, Nordeste, Litoral Alentejano, Alto Alentejo |
| **Treatment** | All other hospitals | EPE hospitals that merged into NEW ULS on Jan 1, 2024 |

### DiD Model Specification

```
Overdue_Ratio = a + b1(Treatment) + b2(Post_2024) + b3(Treatment x Post_2024) + e

Where b3 = DiD estimator (causal effect of becoming NEW ULS)
```

---

## Results

### Difference-in-Differences Estimates

| Coefficient | Estimate | P-value | Interpretation |
|-------------|----------|---------|----------------|
| Treatment (New ULS) | -0.1851 | 0.0058 | Pre-existing difference |
| Post-2024 | -0.0701 | 0.2636 | Time trend for control |
| **DiD (Treatment x Post)** | **0.0620** | **0.4325** | **Causal Effect** |

### Interpretation

The DiD estimator is **0.0620** (not statistically significant).

This means that hospitals which became NEW ULS in 2024 experienced a 
**6.2 percentage point increase** 
in overdue debt ratio compared to the pre-existing ULS control group.

---

## Parallel Trends Visualization

![DiD Parallel Trends](results/did_parallel_trends.png)

---

## Validity Assessment

### Parallel Trends Assumption
- Visual inspection required (see figure above)
- If pre-2024 trends are parallel, DiD estimate is valid

### Selection Concerns
- Pre-existing ULS were created in regions with specific characteristics
- May not be perfectly comparable to hospitals that became ULS in 2024

---

*Report generated: January 2026*
*Corrected analysis with proper treatment/control classification*
