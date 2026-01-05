# Descriptive Analysis Report

**Total Observations**: 47004
**Total Entities**: 61
**Time Period**: 2014 - 2025

## 1. Variable Availability (Top 50)
| Variable | Non-Null Count | Coverage % |
|---|---|---|
| month | 47004 | 100.0% |
| year | 47004 | 100.0% |
| instituicao | 45685 | 97.2% |
| periodo_hr | 45685 | 97.2% |
| date_key_hr | 45685 | 97.2% |
| date_hr | 45685 | 97.2% |
| total_geral | 45685 | 97.2% |
| regiao_hr | 45685 | 97.2% |
| outros | 45684 | 97.2% |
| at | 45670 | 97.2% |
| localizacao_geografica_hr | 45138 | 96.0% |
| ao | 45056 | 95.9% |
| date | 44728 | 95.2% |
| regiao | 44728 | 95.2% |
| date_key | 44728 | 95.2% |
| periodo | 44728 | 95.2% |
| localizacao_geografica | 44728 | 95.2% |
| entidade | 44728 | 95.2% |
| pagamentos_em_atraso | 44507 | 94.7% |
| divida_vencida_fornecedores_externos | 44507 | 94.7% |
| divida_total_fornecedores_externos | 44507 | 94.7% |
| medicos_s_internos | 44176 | 94.0% |
| enfermeiros | 44130 | 93.9% |
| tdt | 44075 | 93.8% |
| tss | 41714 | 88.7% |
| medicos_internos | 41377 | 88.0% |
| informaticos | 30495 | 64.9% |
| ts | 29487 | 62.7% |
| farmaceuticos | 14027 | 29.8% |
| entity_nif | 9190 | 19.6% |
| region_nuts2 | 9190 | 19.6% |
| entity_type | 9190 | 19.6% |
| region_nuts1 | 9190 | 19.6% |
| entity_name | 9190 | 19.6% |
| contracts_amount | 7173 | 15.3% |
| contracts_count | 7173 | 15.3% |
| unemployment_rate | 3968 | 8.4% |
| farmaceuticos_residentes | 3902 | 8.3% |
| gdp_per_capita | 2464 | 5.2% |
| ao0 | 613 | 1.3% |
| tas | 503 | 1.1% |
| population | 0 | 0.0% |

## 2. Key Financial Statistics (Mean/Median)
|                                      |        mean |         50% |          min |         max |         std |
|:-------------------------------------|------------:|------------:|-------------:|------------:|------------:|
| divida_total_fornecedores_externos   | 3.69797e+07 | 1.94573e+07 | -1.29588e+07 | 3.20678e+08 | 5.19613e+07 |
| divida_vencida_fornecedores_externos | 2.44545e+07 | 1.10097e+07 | -3.00228e+07 | 2.50339e+08 | 3.74169e+07 |

## 3. Macro & Context Statistics
|                   |   count |          mean |           std |   min |      25% |      50% |          75% |            max |
|:------------------|--------:|--------------:|--------------:|------:|---------:|---------:|-------------:|---------------:|
| gdp_per_capita    |    2464 |  42.1653      |   2.00745     |  37.1 |     40.8 |     42.7 |  43.5        |   45           |
| unemployment_rate |    3968 |  45.5295      |  64.9172      |   1   |     13   |     21   |  30          |  232           |
| population        |       0 | nan           | nan           | nan   |    nan   |    nan   | nan          |  nan           |
| contracts_amount  |    7173 |   3.49723e+06 |   1.31142e+07 |   0   | 184377   | 831216   |   3.0636e+06 |    8.82912e+08 |
| contracts_count   |    7173 |  67.4967      | 143.661       |   1   |      6   |     23   |  68          | 3256           |

## 4. Top 10 Ratios (Overdue / Total Debt)
| entity_name                                      |   year |   month |   debt_ratio |   divida_vencida_fornecedores_externos |   divida_total_fornecedores_externos |
|:-------------------------------------------------|-------:|--------:|-------------:|---------------------------------------:|-------------------------------------:|
| UNIDADE LOCAL DE SAÚDE DA ARRÁBIDA, E. P. E.     |   2024 |       5 |      2.31679 |                           -3.00228e+07 |                         -1.29588e+07 |
| ADMINISTRAÇÃO REGIONAL DE SAÚDE DO CENTRO, I. P. |   2025 |       4 |      1.57065 |                       -49204           |                     -31327.2         |
| ADMINISTRAÇÃO REGIONAL DE SAÚDE DO CENTRO, I. P. |   2025 |      10 |      1.38945 |                       -61901.6         |                     -44551.3         |
| HOSPITAL DA HORTA, EPER                          |   2018 |      12 |      1.11639 |                            7.03097e+06 |                          6.29794e+06 |
| HOSPITAL DA HORTA, EPER                          |   2018 |      12 |      1.11639 |                            7.03097e+06 |                          6.29794e+06 |
| HOSPITAL DA HORTA, EPER                          |   2018 |      12 |      1.11639 |                            7.03097e+06 |                          6.29794e+06 |
| HOSPITAL DA HORTA, EPER                          |   2018 |      12 |      1.11639 |                            7.03097e+06 |                          6.29794e+06 |
| HOSPITAL DA HORTA, EPER                          |   2017 |      12 |      1.02447 |                            3.49508e+07 |                          3.41161e+07 |
| HOSPITAL DA HORTA, EPER                          |   2017 |      12 |      1.02447 |                            3.49508e+07 |                          3.41161e+07 |
| HOSPITAL DA HORTA, EPER                          |   2017 |      12 |      1.02447 |                            3.49508e+07 |                          3.41161e+07 |