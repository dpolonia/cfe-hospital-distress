# Enhanced Regression Results
## P1 & P2 Improvements Implemented

### Main Model (Quarterly, Time FE, Clustered SE)

| Variable | Coefficient | Std. Err. | P-value |
|----------|-------------|-----------|---------|
| Is_ULS | 0.1391 | 0.1704 | 0.4150 |
| Log_Staff | -0.0785 | 0.1361 | 0.5646 |
| Log_GDP | -0.0175 | 1.5320 | 0.9909 |
| Clinical_Intensity | 1.1365 | 2.6437 | 0.6675 |

**N = 448, R² = 0.0577**

### Robustness Checks
- **log_overdue**: is_uls = 1.1661 (p=0.1563)
- **large_hospitals**: is_uls = 0.0056 (p=0.9608)


---
## Full Model Output
```
                          PanelOLS Estimation Summary                           
================================================================================
Dep. Variable:     overdue_ratio_wins   R-squared:                        0.0577
Estimator:                   PanelOLS   R-squared (Between):              0.1012
No. Observations:                 448   R-squared (Within):              -0.0120
Date:                Sat, Jan 03 2026   R-squared (Overall):              0.0564
Time:                        21:05:38   Log-likelihood                   -79.797
Cov. Estimator:             Clustered                                           
                                        F-statistic:                      6.3651
Entities:                          16   P-value                           0.0001
Avg Obs:                       28.000   Distribution:                   F(4,416)
Min Obs:                       28.000                                           
Max Obs:                       28.000   F-statistic (robust):             0.8982
                                        P-value                           0.4650
Time periods:                      28   Distribution:                   F(4,416)
Avg Obs:                       16.000                                           
Min Obs:                       16.000                                           
Max Obs:                       16.000                                           
                                                                                
                                 Parameter Estimates                                  
======================================================================================
                    Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
--------------------------------------------------------------------------------------
const                  0.5911     5.4509     0.1084     0.9137     -10.124      11.306
is_uls                 0.1391     0.1704     0.8159     0.4150     -0.1960      0.4741
log_staff             -0.0785     0.1361    -0.5765     0.5646     -0.3460      0.1891
log_gdp               -0.0175     1.5320    -0.0114     0.9909     -3.0290      2.9939
clinical_intensity     1.1365     2.6437     0.4299     0.6675     -4.0603      6.3333
======================================================================================

F-test for Poolability: 0.3056
P-value: 0.9998
Distribution: F(27,416)

Included effects: Time
```
