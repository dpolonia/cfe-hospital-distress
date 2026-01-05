import React, { useState } from 'react';
import { ChevronLeft, ChevronRight, Home, TrendingUp, AlertCircle, CheckCircle, Database, BarChart3, GitBranch, FileText } from 'lucide-react';

const VivaPresentation = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const slides = [
    // Title Slide
    {
      title: "Vertical Integration and Financial Distress in Portuguese Public Hospitals",
      subtitle: "Methodological Framework and Preliminary Evidence from the 2024 ULS Reform",
      type: "title",
      content: (
        <div className="text-center space-y-6">
          <div className="text-xl text-blue-100 mb-4">
            Complementos de Finanças Empresariais
          </div>
          <h1 className="text-5xl font-bold text-white mb-4">
            Vertical Integration and Financial Distress in Portuguese Public Hospitals
          </h1>
          <h2 className="text-3xl text-blue-200 mb-8">
            Methodological Framework and Preliminary Evidence from the 2024 ULS Reform
          </h2>
          <div className="text-xl text-blue-100">
            Daniel Ferreira Polónia<br/>
            DEGEIT, University of Aveiro<br/>
            January 2026
          </div>
          <div className="mt-8 text-sm text-blue-200 italic">
            Target Journal: Health Economics (Wiley) | JEL: I18, H51, G33, L22, C23
          </div>
        </div>
      )
    },

    // Research Question & Motivation
    {
      title: "1. Research Question & Motivation",
      icon: <FileText className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="bg-blue-900/50 p-6 rounded-lg border-l-4 border-blue-400">
            <h3 className="text-2xl font-bold text-blue-200 mb-3">Central Question</h3>
            <p className="text-xl text-white">
              What is the short-term financial impact of Portugal's 2024 universal healthcare integration reform on hospital financial distress?
            </p>
          </div>

          <div className="grid grid-cols-2 gap-6">
            <div className="bg-gradient-to-br from-blue-900/40 to-blue-800/40 p-5 rounded-lg">
              <h4 className="text-lg font-bold text-blue-300 mb-3 flex items-center gap-2">
                <TrendingUp className="w-5 h-5" />
                Policy Relevance
              </h4>
              <ul className="space-y-2 text-blue-100">
                <li>• Decreto-Lei 102/2023: Universal ULS model (Jan 1, 2024)</li>
                <li>• One of Europe's most comprehensive integration reforms</li>
                <li>• All 31 public hospitals → ULS structure</li>
                <li>• Natural experiment for vertical integration effects</li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-blue-900/40 to-blue-800/40 p-5 rounded-lg">
              <h4 className="text-lg font-bold text-blue-300 mb-3 flex items-center gap-2">
                <AlertCircle className="w-5 h-5" />
                Theoretical Framework
              </h4>
              <ul className="space-y-2 text-blue-100">
                <li>• Kornai's soft budget constraints (2009)</li>
                <li>• Transaction cost economics (Williamson)</li>
                <li>• Hospital merger literature (Schmitt, 2017)</li>
                <li>• Integration timing effects (3-5 year J-curve)</li>
              </ul>
            </div>
          </div>

          <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
            <p className="text-red-200 font-semibold">
              ⚠️ Critical Challenge: No untreated comparison group exists post-reform
            </p>
          </div>
        </div>
      )
    },

    // Contribution & Scope
    {
      title: "2. Contribution & Scope",
      icon: <CheckCircle className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="grid grid-cols-2 gap-6">
            <div>
              <h3 className="text-2xl font-bold text-green-400 mb-4">What This Paper DOES Provide</h3>
              <div className="space-y-3">
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">1. Methodological Infrastructure</h4>
                  <p className="text-green-100 text-sm">Baseline DiD, synthetic control, and triple-difference framework for ongoing evaluation</p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">2. Selection Pattern Discovery</h4>
                  <p className="text-green-100 text-sm">Pre-existing ULS had 18.5pp higher baseline distress (p=0.006) — rural, underserved regions</p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">3. Preliminary Magnitudes</h4>
                  <p className="text-green-100 text-sm">DiD estimate: +6.2pp (95% CI: -9.3 to +21.7) — establishing baseline for future monitoring</p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">4. Heterogeneity Patterns</h4>
                  <p className="text-green-100 text-sm">Effects concentrated in smaller hospitals and higher distress quantiles</p>
                </div>
              </div>
            </div>

            <div>
              <h3 className="text-2xl font-bold text-red-400 mb-4">What This Paper CANNOT Determine</h3>
              <div className="space-y-3">
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <p className="text-red-100 text-sm">❌ Whether the reform improved hospital financial health</p>
                </div>
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <p className="text-red-100 text-sm">❌ Whether the reform worsened hospital financial health</p>
                </div>
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <p className="text-red-100 text-sm">❌ Whether the reform had no meaningful effect</p>
                </div>
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <p className="text-red-100 text-sm">❌ The causal effect of integration on financial distress</p>
                </div>
              </div>

              <div className="mt-6 bg-yellow-900/30 p-4 rounded-lg border-l-4 border-yellow-500">
                <h4 className="font-bold text-yellow-300 mb-2">Why Not?</h4>
                <ul className="text-yellow-100 text-sm space-y-1">
                  <li>• Only 12 months post-reform data</li>
                  <li>• Comparison = long-run treated (not untreated)</li>
                  <li>• Severe power limitations (25% power, MDE=15pp)</li>
                  <li>• Integration effects take 3-5 years to stabilize</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="bg-blue-900/50 p-4 rounded-lg">
            <p className="text-blue-200 font-semibold text-center">
              → This is a <span className="text-white">methodological baseline study</span>, not a definitive causal evaluation
            </p>
          </div>
        </div>
      )
    },

    // Identification Challenge
    {
      title: "3. The Fundamental Identification Problem",
      icon: <AlertCircle className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="bg-red-900/30 p-6 rounded-lg border-2 border-red-500">
            <h3 className="text-2xl font-bold text-red-300 mb-4">The Core Problem</h3>
            <p className="text-white text-lg mb-4">
              Portugal's comparison group consists not of "untreated" entities but of entities integrated 12-25 years ago.
            </p>
            <div className="bg-black/50 p-4 rounded font-mono text-sm text-green-400">
              <p>Ideal DiD estimand:</p>
              <p className="mt-2">τ<sup>ATT</sup> = E[Y<sub>it</sub>(1) - Y<sub>it</sub>(∞) | D<sub>i</sub>=0, t&gt;0]</p>
              <p className="mt-4 text-yellow-400">What we actually estimate:</p>
              <p className="mt-2 text-red-400">τ̂<sub>DiD</sub> ≈ E[τ(1) | New ULS] - E[τ(12-25) | Pre-existing ULS]</p>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-4">
            <div className="bg-blue-900/40 p-5 rounded-lg">
              <h4 className="font-bold text-blue-300 mb-3 text-center">Treatment Group (n=31)</h4>
              <p className="text-blue-100 text-sm text-center mb-3">Newly integrated Jan 1, 2024</p>
              <ul className="text-blue-200 text-xs space-y-1">
                <li>• Mixed urban/rural</li>
                <li>• Variable baseline distress</li>
                <li>• Observing: Year 1 effects</li>
              </ul>
            </div>

            <div className="bg-purple-900/40 p-5 rounded-lg border-2 border-purple-500">
              <h4 className="font-bold text-purple-300 mb-3 text-center">Control Group (n=8)</h4>
              <p className="text-purple-100 text-sm text-center mb-3">Integrated 1999-2012</p>
              <ul className="text-purple-200 text-xs space-y-1">
                <li>• Predominantly rural (6/8 &lt;30/km²)</li>
                <li>• Higher baseline distress (+18.5pp)</li>
                <li>• Observing: Year 12-25 effects</li>
              </ul>
            </div>

            <div className="bg-gray-700/40 p-5 rounded-lg opacity-50">
              <h4 className="font-bold text-gray-400 mb-3 text-center">True Control (n=0)</h4>
              <p className="text-gray-300 text-sm text-center mb-3">Never integrated</p>
              <p className="text-gray-400 text-xs text-center italic">Does not exist post-reform</p>
            </div>
          </div>

          <div className="bg-orange-900/30 p-5 rounded-lg border-l-4 border-orange-500">
            <h4 className="font-bold text-orange-300 mb-2">Implication for Interpretation</h4>
            <p className="text-orange-100">
              We estimate the <span className="font-bold text-white">difference between short-run and long-run integration effects</span>, 
              not the effect of integration vs. no integration. This is still policy-relevant but requires careful interpretation.
            </p>
          </div>
        </div>
      )
    },

    // Data & Methodology
    {
      title: "4. Data & Empirical Strategy",
      icon: <Database className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="grid grid-cols-2 gap-6">
            <div>
              <h3 className="text-xl font-bold text-blue-300 mb-4">Data Sources</h3>
              <div className="space-y-3">
                <div className="bg-blue-900/40 p-4 rounded-lg">
                  <h4 className="font-bold text-blue-200 mb-2">SNS Transparency Portal</h4>
                  <p className="text-blue-100 text-sm">Financial statements, debt positions, HR data (monthly, 2014-2025)</p>
                </div>
                <div className="bg-blue-900/40 p-4 rounded-lg">
                  <h4 className="font-bold text-blue-200 mb-2">IMPIC (Base)</h4>
                  <p className="text-blue-100 text-sm">Public procurement contracts (2012-2025)</p>
                </div>
                <div className="bg-blue-900/40 p-4 rounded-lg">
                  <h4 className="font-bold text-blue-200 mb-2">INE</h4>
                  <p className="text-blue-100 text-sm">Regional GDP, unemployment, demographics (NUTS II)</p>
                </div>
              </div>

              <div className="mt-4 bg-green-900/30 p-4 rounded-lg">
                <h4 className="font-bold text-green-300 mb-2">Sample Construction</h4>
                <ul className="text-green-100 text-sm space-y-1">
                  <li>• n = 1,092 entity-quarters</li>
                  <li>• 39 ULS entities (8 pre-existing + 31 new)</li>
                  <li>• 3 IPO oncology centers excluded</li>
                  <li>• 2014 Q1 - 2025 Q4 panel</li>
                  <li>• Quarterly aggregation for stability</li>
                </ul>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-bold text-blue-300 mb-4">Primary Outcome Variable</h3>
              <div className="bg-purple-900/40 p-5 rounded-lg mb-4">
                <h4 className="font-bold text-purple-200 mb-3 text-center">Overdue Debt Ratio</h4>
                <div className="bg-black/50 p-3 rounded text-center font-mono text-purple-300">
                  Overdue Ratio = <br/>
                  <span className="text-sm">Payments &gt; 90 days past due</span><br/>
                  <span className="text-2xl">─────────────────</span><br/>
                  <span className="text-sm">Total Supplier Debt</span>
                </div>
                <p className="text-purple-100 text-sm mt-3">
                  ✓ Public sector appropriate (bankruptcy impossible)<br/>
                  ✓ Aligns with Kornai's soft budget constraint framework<br/>
                  ✓ Available monthly, high data quality (94.7% coverage)
                </p>
              </div>

              <h3 className="text-xl font-bold text-blue-300 mb-3">Control Variables</h3>
              <div className="bg-blue-900/40 p-4 rounded-lg">
                <ul className="text-blue-100 text-sm space-y-2">
                  <li>• <strong>Size:</strong> Log(Staff Count)</li>
                  <li>• <strong>Regional Economy:</strong> Log(GDP per capita)</li>
                  <li>• <strong>Clinical Intensity:</strong> (Doctors + Nurses) / Total Staff</li>
                  <li>• <strong>Time Fixed Effects:</strong> Quarterly dummies</li>
                  <li>• <strong>Region Fixed Effects:</strong> NUTS II level</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="bg-blue-900/50 p-4 rounded-lg">
            <h4 className="font-bold text-blue-200 mb-2">Entity Resolution & Data Pipeline</h4>
            <p className="text-blue-100 text-sm">
              Fuzzy matching algorithms (RapidFuzz) + manual mapping files → 96% successful NIF resolution across data sources → 
              Dimensional modeling (star schema) → Quarterly panel with full replicability via GitHub repository
            </p>
          </div>
        </div>
      )
    },

    // Empirical Strategy
    {
      title: "5. Empirical Specifications",
      icon: <GitBranch className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="grid grid-cols-2 gap-6">
            <div>
              <h3 className="text-xl font-bold text-blue-300 mb-4">Baseline DiD Specification</h3>
              <div className="bg-black/70 p-5 rounded-lg font-mono text-sm text-green-400 mb-4">
                <p>Y<sub>it</sub> = α + β₁·NewULS<sub>i</sub> + β₂·Post<sub>t</sub> +</p>
                <p className="ml-4 text-yellow-400">β₃·(NewULS<sub>i</sub> × Post<sub>t</sub>) + ε<sub>it</sub></p>
                <p className="mt-3 text-blue-400">Where β₃ = DiD estimator</p>
              </div>

              <div className="bg-blue-900/40 p-4 rounded-lg mb-3">
                <h4 className="font-bold text-blue-200 mb-2">Extended Specifications</h4>
                <ul className="text-blue-100 text-sm space-y-1">
                  <li>• + Time fixed effects</li>
                  <li>• + Control variables</li>
                  <li>• + Region × Time interactions</li>
                  <li>• + Size × Treatment interactions</li>
                </ul>
              </div>

              <div className="bg-purple-900/40 p-4 rounded-lg">
                <h4 className="font-bold text-purple-200 mb-2">Heterogeneity Analysis</h4>
                <p className="text-purple-100 text-sm">Test differential effects by:</p>
                <ul className="text-purple-100 text-xs space-y-1 mt-2">
                  <li>• Hospital size (continuous & binary)</li>
                  <li>• Region (Norte, Centro, Lisboa, etc.)</li>
                  <li>• Pre-reform financial health</li>
                  <li>• Clinical intensity</li>
                </ul>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-bold text-blue-300 mb-4">Robustness Checks</h3>
              <div className="space-y-3">
                <div className="bg-green-900/40 p-4 rounded-lg">
                  <h4 className="font-bold text-green-200 mb-2">1. Inference Methods</h4>
                  <ul className="text-green-100 text-sm space-y-1">
                    <li>• Wild cluster bootstrap (1,000 reps)</li>
                    <li>• Randomization inference</li>
                    <li>• Equivalence testing (TOST ±10pp)</li>
                  </ul>
                </div>

                <div className="bg-green-900/40 p-4 rounded-lg">
                  <h4 className="font-bold text-green-200 mb-2">2. Alternative Specifications</h4>
                  <ul className="text-green-100 text-sm space-y-1">
                    <li>• Quantile regression (Q25, Q50, Q75, Q90)</li>
                    <li>• Propensity score matching</li>
                    <li>• Alternative DVs (log overdue, DPO)</li>
                  </ul>
                </div>

                <div className="bg-green-900/40 p-4 rounded-lg">
                  <h4 className="font-bold text-green-200 mb-2">3. Sensitivity Analyses</h4>
                  <ul className="text-green-100 text-sm space-y-1">
                    <li>• Winsorization (1%, 99%)</li>
                    <li>• Subsample: Large hospitals only</li>
                    <li>• Subsample: Post-COVID period (2022+)</li>
                  </ul>
                </div>
              </div>

              <div className="bg-orange-900/30 p-4 rounded-lg border-l-4 border-orange-500 mt-4">
                <h4 className="font-bold text-orange-300 mb-2">Parallel Trends</h4>
                <p className="text-orange-100 text-sm">
                  Event study plots show reasonably parallel pre-2024 trends, though control group's higher baseline persists throughout
                </p>
              </div>
            </div>
          </div>

          <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
            <h4 className="font-bold text-red-300 mb-2">Critical Limitation: Statistical Power</h4>
            <div className="grid grid-cols-3 gap-4 mt-3">
              <div className="text-center">
                <p className="text-3xl font-bold text-red-400">8</p>
                <p className="text-red-200 text-sm">Control Clusters</p>
              </div>
              <div className="text-center">
                <p className="text-3xl font-bold text-red-400">25%</p>
                <p className="text-red-200 text-sm">Power (observed effect)</p>
              </div>
              <div className="text-center">
                <p className="text-3xl font-bold text-red-400">±15pp</p>
                <p className="text-red-200 text-sm">Min. Detectable Effect</p>
              </div>
            </div>
          </div>
        </div>
      )
    },

    // Main Results
    {
      title: "6. Main Results",
      icon: <BarChart3 className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="bg-gradient-to-r from-blue-900/50 to-purple-900/50 p-6 rounded-lg border-2 border-blue-500">
            <h3 className="text-2xl font-bold text-blue-200 mb-4 text-center">Primary DiD Estimates</h3>
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b-2 border-blue-500">
                  <th className="text-left text-blue-300 pb-2">Specification</th>
                  <th className="text-center text-blue-300 pb-2">β₃ (DiD)</th>
                  <th className="text-center text-blue-300 pb-2">95% CI</th>
                  <th className="text-center text-blue-300 pb-2">p-value</th>
                </tr>
              </thead>
              <tbody className="text-white">
                <tr className="border-b border-blue-700">
                  <td className="py-2">Simple DiD</td>
                  <td className="text-center">+0.062</td>
                  <td className="text-center">[-0.093, +0.217]</td>
                  <td className="text-center">0.433</td>
                </tr>
                <tr className="border-b border-blue-700">
                  <td className="py-2">+ Time FE</td>
                  <td className="text-center">+0.048</td>
                  <td className="text-center">[-0.121, +0.217]</td>
                  <td className="text-center">0.578</td>
                </tr>
                <tr className="border-b border-blue-700">
                  <td className="py-2">+ Controls</td>
                  <td className="text-center">+0.051</td>
                  <td className="text-center">[-0.114, +0.216]</td>
                  <td className="text-center">0.546</td>
                </tr>
                <tr>
                  <td className="py-2">Wild Bootstrap</td>
                  <td className="text-center">+0.062</td>
                  <td className="text-center">—</td>
                  <td className="text-center">0.456</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="grid grid-cols-2 gap-6">
            <div>
              <h3 className="text-xl font-bold text-red-300 mb-4">⚠️ Interpretation: The Null Finding is UNINFORMATIVE</h3>
              <div className="bg-red-900/30 p-5 rounded-lg border-l-4 border-red-500 space-y-3">
                <p className="text-red-100 text-sm">
                  <strong>Point estimate:</strong> +6.2pp increase in overdue debt ratio
                </p>
                <p className="text-red-100 text-sm">
                  <strong>Not significant:</strong> p = 0.433 (cannot reject null)
                </p>
                <p className="text-red-100 text-sm">
                  <strong>BUT:</strong> 95% CI spans -9.3pp to +21.7pp
                </p>
                <p className="text-yellow-200 text-sm font-semibold">
                  → With 25% power, there is a 75% probability of Type II error (failing to detect a true effect)
                </p>
                <p className="text-red-100 text-sm">
                  <strong>Equivalence test failed:</strong> Cannot establish effects within ±10pp bounds
                </p>
              </div>

              <div className="bg-yellow-900/30 p-4 rounded-lg mt-4">
                <h4 className="font-bold text-yellow-300 mb-2">What We Can Say</h4>
                <p className="text-yellow-100 text-sm">
                  "The reform did not cause immediate, large-scale financial crisis. But we cannot determine whether it improved, worsened, or had no effect."
                </p>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-bold text-green-300 mb-4">✓ The Robust Finding: Selection Pattern</h3>
              <div className="bg-green-900/40 p-6 rounded-lg border-l-4 border-green-500 mb-4">
                <div className="text-center mb-4">
                  <p className="text-5xl font-bold text-green-400">-18.5pp</p>
                  <p className="text-green-200 text-sm">Baseline Difference (β₁)</p>
                  <p className="text-green-300 font-semibold">p = 0.006***</p>
                </div>
                <p className="text-green-100 text-sm text-center">
                  Pre-existing ULS had systematically <strong>higher</strong> overdue debt ratios before the 2024 reform
                </p>
              </div>

              <div className="bg-blue-900/40 p-4 rounded-lg">
                <h4 className="font-bold text-blue-200 mb-2">Pre-existing ULS Characteristics</h4>
                <ul className="text-blue-100 text-xs space-y-1">
                  <li>• 6/8 entities: Population density &lt; 30/km²</li>
                  <li>• National average: 111/km²</li>
                  <li>• Predominantly rural, interior regions</li>
                  <li>• Aging populations, economic decline</li>
                  <li>• Created 1999-2012 targeting underserved areas</li>
                </ul>
              </div>

              <div className="bg-purple-900/30 p-4 rounded-lg mt-4">
                <h4 className="font-bold text-purple-300 mb-2">Implication</h4>
                <p className="text-purple-100 text-sm">
                  Early ULS adoption was <strong>non-random</strong>, targeting structurally disadvantaged regions. This selection pattern must inform future causal inference.
                </p>
              </div>
            </div>
          </div>
        </div>
      )
    },

    // Heterogeneity
    {
      title: "7. Heterogeneity Analysis",
      icon: <TrendingUp className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <h3 className="text-2xl font-bold text-blue-300 mb-4">How Does the ULS Effect Vary Across Hospitals?</h3>

          <div className="grid grid-cols-3 gap-4">
            <div className="bg-gradient-to-br from-blue-900/40 to-blue-800/40 p-5 rounded-lg">
              <h4 className="font-bold text-blue-300 mb-3 text-center">By Hospital Size</h4>
              <div className="bg-black/50 p-3 rounded mb-3">
                <p className="text-center text-sm text-blue-200">ULS × Log(Staff)</p>
                <p className="text-center text-2xl font-bold text-white">-0.031</p>
                <p className="text-center text-xs text-blue-300">p = 0.15</p>
              </div>
              <p className="text-blue-100 text-xs text-center">
                <strong>Interpretation:</strong> Effects appear stronger in smaller hospitals (exploratory finding, low power)
              </p>
            </div>

            <div className="bg-gradient-to-br from-purple-900/40 to-purple-800/40 p-5 rounded-lg">
              <h4 className="font-bold text-purple-300 mb-3 text-center">By Debt Distribution</h4>
              <div className="space-y-2 text-sm">
                <div className="flex justify-between text-purple-100">
                  <span>Q25 (high distress):</span>
                  <span className="font-bold text-red-400">+0.343</span>
                </div>
                <div className="flex justify-between text-purple-100">
                  <span>Q50 (median):</span>
                  <span className="font-bold text-yellow-400">+0.097</span>
                </div>
                <div className="flex justify-between text-purple-100">
                  <span>Q75:</span>
                  <span className="font-bold text-green-400">+0.029</span>
                </div>
                <div className="flex justify-between text-purple-100">
                  <span>Q90 (low distress):</span>
                  <span className="font-bold text-green-500">+0.016</span>
                </div>
              </div>
              <p className="text-purple-100 text-xs text-center mt-3">
                <strong>Interpretation:</strong> Integration exacerbates distress for already-struggling hospitals
              </p>
            </div>

            <div className="bg-gradient-to-br from-green-900/40 to-green-800/40 p-5 rounded-lg">
              <h4 className="font-bold text-green-300 mb-3 text-center">By Region</h4>
              <div className="bg-black/50 p-3 rounded mb-3">
                <p className="text-center text-sm text-green-200">ULS × Norte</p>
                <p className="text-center text-2xl font-bold text-white">+0.018</p>
                <p className="text-center text-xs text-green-300">p = 0.74</p>
              </div>
              <p className="text-green-100 text-xs text-center">
                <strong>Interpretation:</strong> No clear regional pattern detected (limited power)
              </p>
            </div>
          </div>

          <div className="bg-orange-900/30 p-5 rounded-lg border-l-4 border-orange-500">
            <h4 className="font-bold text-orange-300 mb-3">Key Insight from Heterogeneity Analysis</h4>
            <p className="text-orange-100 mb-3">
              The pattern of <strong>stronger effects among smaller hospitals and higher distress quantiles</strong> aligns with organizational theory:
            </p>
            <ul className="text-orange-100 text-sm space-y-2">
              <li>• <strong>Fixed integration costs</strong> (IT systems, administrative reorganization) disproportionately burden smaller entities</li>
              <li>• <strong>Less organizational slack</strong> in already-distressed hospitals → less capacity to absorb transition disruption</li>
              <li>• <strong>Coordination complexity</strong> increases with reduced incentive intensity (Milgrom & Roberts, 1992)</li>
            </ul>
          </div>

          <div className="bg-blue-900/40 p-4 rounded-lg">
            <h4 className="font-bold text-blue-300 mb-2">Policy Implication</h4>
            <p className="text-blue-100 text-sm">
              If these patterns persist in longer-term data, policymakers might consider <strong>targeted transition support</strong> for smaller, 
              financially-constrained entities during future healthcare reforms.
            </p>
          </div>

          <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
            <p className="text-red-200 text-sm">
              <strong>Caveat:</strong> All heterogeneity findings are exploratory given severe power constraints. Formal tests of differential effects 
              will require larger sample sizes or longer time series.
            </p>
          </div>
        </div>
      )
    },

    // Limitations & Future Work
    {
      title: "8. Limitations & Future Research",
      icon: <AlertCircle className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="grid grid-cols-2 gap-6">
            <div>
              <h3 className="text-xl font-bold text-red-300 mb-4">Critical Limitations</h3>
              <div className="space-y-3">
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <h4 className="font-bold text-red-300 mb-2">1. Fundamental Identification</h4>
                  <p className="text-red-100 text-sm">
                    Comparison group = long-run treated, not untreated. Estimand differs from causal effect of integration.
                  </p>
                </div>
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <h4 className="font-bold text-red-300 mb-2">2. Statistical Power</h4>
                  <p className="text-red-100 text-sm">
                    n=8 control clusters → 25% power → MDE=15pp. Null finding is uninformative, not evidence of no effect.
                  </p>
                </div>
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <h4 className="font-bold text-red-300 mb-2">3. Short Post-Period</h4>
                  <p className="text-red-100 text-sm">
                    Only 12 months post-reform. US literature shows J-curve: costs ↑ years 1-2, ↓ years 3-5 (Schmitt, 2017).
                  </p>
                </div>
                <div className="bg-red-900/30 p-4 rounded-lg border-l-4 border-red-500">
                  <h4 className="font-bold text-red-300 mb-2">4. Selection Bias</h4>
                  <p className="text-red-100 text-sm">
                    Pre-existing ULS structurally different (rural, distressed). Parallel trends assumption questionable.
                  </p>
                </div>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-bold text-green-300 mb-4">Future Research Agenda</h3>
              <div className="space-y-3">
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">1. Extended Time Series (Priority 1)</h4>
                  <p className="text-green-100 text-sm">
                    Pre-registered re-analysis with 36+ months post-reform data. Enable detection of steady-state effects vs. transition.
                  </p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">2. Alternative Outcomes</h4>
                  <p className="text-green-100 text-sm">
                    Operating margins, DPO, coverage ratios, patient outcomes. Multi-dimensional assessment of integration effects.
                  </p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">3. Mechanism Analysis</h4>
                  <p className="text-green-100 text-sm">
                    Exploit variation in ULS governance structures. Estimate dose-response relationships. Qualitative case studies.
                  </p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-bold text-green-300 mb-2">4. Triple-Difference Design</h4>
                  <p className="text-green-100 text-sm">
                    Use hospital characteristics predicting integration benefits as third difference. Strengthen identification.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-blue-900/50 p-5 rounded-lg">
            <h4 className="font-bold text-blue-300 mb-3">What This Paper Enables</h4>
            <div className="grid grid-cols-3 gap-4 text-center">
              <div>
                <p className="text-3xl mb-2">📊</p>
                <p className="text-blue-100 text-sm"><strong>Data Infrastructure:</strong> Validated entity resolution, quarterly panel, multiple sources</p>
              </div>
              <div>
                <p className="text-3xl mb-2">🔬</p>
                <p className="text-blue-100 text-sm"><strong>Methodological Baseline:</strong> DiD, SC, heterogeneity framework ready for updates</p>
              </div>
              <div>
                <p className="text-3xl mb-2">🎯</p>
                <p className="text-blue-100 text-sm"><strong>Selection Documentation:</strong> -18.5pp pattern informs future causal inference</p>
              </div>
            </div>
          </div>

          <div className="bg-yellow-900/30 p-4 rounded-lg border-l-4 border-yellow-500">
            <h4 className="font-bold text-yellow-300 mb-2">Timeline for Definitive Conclusions</h4>
            <p className="text-yellow-100 text-sm">
              <strong>2026 Q4:</strong> Re-analysis with 24 months post-reform (doubled observation window)<br/>
              <strong>2027 Q4:</strong> Full 3-year evaluation (capture steady-state effects per US literature)<br/>
              <strong>2028+:</strong> Long-run impact assessment, mechanism analysis, policy recommendations
            </p>
          </div>
        </div>
      )
    },

    // Contribution to Literature
    {
      title: "9. Contribution to Literature",
      icon: <FileText className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <h3 className="text-2xl font-bold text-blue-300 mb-4">How This Work Advances the Field</h3>

          <div className="grid grid-cols-2 gap-6">
            <div>
              <h4 className="text-xl font-bold text-green-300 mb-3">Methodological Contributions</h4>
              <div className="space-y-3">
                <div className="bg-green-900/30 p-4 rounded-lg">
                  <h5 className="font-bold text-green-200 mb-2">1. Policy Evaluation Infrastructure</h5>
                  <p className="text-green-100 text-sm">
                    First rigorous quantitative framework for ongoing evaluation of Portugal's largest healthcare reform in 25 years
                  </p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg">
                  <h5 className="font-bold text-green-200 mb-2">2. Transparent Limitations</h5>
                  <p className="text-green-100 text-sm">
                    Model for honest reporting of null findings with severe power constraints (emerging norm in pre-registered research)
                  </p>
                </div>
                <div className="bg-green-900/30 p-4 rounded-lg">
                  <h5 className="font-bold text-green-200 mb-2">3. Replicability Standards</h5>
                  <p className="text-green-100 text-sm">
                    Full computational reproducibility: GitHub repo with raw data, cleaning scripts, analysis code, and regression outputs
                  </p>
                </div>
              </div>
            </div>

            <div>
              <h4 className="text-xl font-bold text-purple-300 mb-3">Substantive Contributions</h4>
              <div className="space-y-3">
                <div className="bg-purple-900/30 p-4 rounded-lg">
                  <h5 className="font-bold text-purple-200 mb-2">1. Selection Pattern Discovery</h5>
                  <p className="text-purple-100 text-sm">
                    First documentation that early ULS adoption (1999-2012) targeted structurally disadvantaged regions. Critical for interpreting integration effects.
                  </p>
                </div>
                <div className="bg-purple-900/30 p-4 rounded-lg">
                  <h5 className="font-bold text-purple-200 mb-2">2. European Integration Evidence</h5>
                  <p className="text-purple-100 text-sm">
                    Adds to sparse European literature on vertical integration effects (primarily Danish, Spanish, Swedish studies)
                  </p>
                </div>
                <div className="bg-purple-900/30 p-4 rounded-lg">
                  <h5 className="font-bold text-purple-200 mb-2">3. Soft Budget Constraints Empirics</h5>
                  <p className="text-purple-100 text-sm">
                    Tests Kornai's (2009) prediction that larger organizational scope strengthens soft budget constraint incentives
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-blue-900/50 p-5 rounded-lg">
            <h4 className="font-bold text-blue-300 mb-3">Positioning Relative to Key Literature</h4>
            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <p className="text-blue-200 font-semibold mb-2">Hospital Merger Literature:</p>
                <ul className="text-blue-100 space-y-1 text-xs">
                  <li>• Dranove & Lindrooth (2003): 1-2% cost savings</li>
                  <li>• Schmitt (2017): J-curve pattern (3-5 years)</li>
                  <li>• <strong>Our contribution:</strong> First evidence on universal mandate (vs. voluntary mergers)</li>
                </ul>
              </div>
              <div>
                <p className="text-blue-200 font-semibold mb-2">Integration Effects:</p>
                <ul className="text-blue-100 space-y-1 text-xs">
                  <li>• Gaynor et al. (2015): Mixed evidence review</li>
                  <li>• Kristensen et al. (2016): Danish null findings</li>
                  <li>• <strong>Our contribution:</strong> Heterogeneity by size/distress level</li>
                </ul>
              </div>
              <div>
                <p className="text-blue-200 font-semibold mb-2">Soft Budget Constraints:</p>
                <ul className="text-blue-100 space-y-1 text-xs">
                  <li>• Kornai (2009): Theory for public hospitals</li>
                  <li>• Piacenza et al. (2014): Italian fiscal discipline</li>
                  <li>• <strong>Our contribution:</strong> Test in Portuguese context with payment delays outcome</li>
                </ul>
              </div>
              <div>
                <p className="text-blue-200 font-semibold mb-2">Policy Evaluation Methods:</p>
                <ul className="text-blue-100 space-y-1 text-xs">
                  <li>• Cameron et al. (2008): Wild cluster bootstrap</li>
                  <li>• Conley & Taber (2011): Few clusters inference</li>
                  <li>• <strong>Our contribution:</strong> Applied to Portuguese healthcare, documented power limitations</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="bg-orange-900/30 p-4 rounded-lg border-l-4 border-orange-500">
            <h4 className="font-bold text-orange-300 mb-2">Target Journal: Health Economics (Wiley)</h4>
            <p className="text-orange-100 text-sm mb-2">
              <strong>Why appropriate:</strong>
            </p>
            <ul className="text-orange-100 text-xs space-y-1">
              <li>• Published similar DiD studies of hospital reforms (multiple recent examples)</li>
              <li>• Values methodological transparency and limitation acknowledgment</li>
              <li>• European policy focus aligns with journal scope</li>
              <li>• IF 2.4, Q2 in Health Care Sciences & Services</li>
            </ul>
          </div>
        </div>
      )
    },

    // Summary & Conclusions
    {
      title: "10. Summary & Key Takeaways",
      icon: <CheckCircle className="w-8 h-8" />,
      content: (
        <div className="space-y-6">
          <div className="bg-gradient-to-r from-blue-900/50 to-purple-900/50 p-6 rounded-lg border-2 border-blue-500">
            <h3 className="text-3xl font-bold text-white mb-4 text-center">What We Know After 12 Months</h3>
            <div className="grid grid-cols-3 gap-6">
              <div className="text-center">
                <div className="text-5xl mb-2">✓</div>
                <h4 className="font-bold text-green-300 mb-2">No Immediate Crisis</h4>
                <p className="text-green-100 text-sm">
                  The reform did not trigger large-scale financial deterioration. "The sky did not fall."
                </p>
              </div>
              <div className="text-center">
                <div className="text-5xl mb-2">✓</div>
                <h4 className="font-bold text-green-300 mb-2">Selection Pattern</h4>
                <p className="text-green-100 text-sm">
                  Early ULS adoption targeted disadvantaged regions. -18.5pp baseline difference is robust.
                </p>
              </div>
              <div className="text-center">
                <div className="text-5xl mb-2">✓</div>
                <h4 className="font-bold text-green-300 mb-2">Evaluation Infrastructure</h4>
                <p className="text-green-100 text-sm">
                  Data pipeline, panel structure, and analytical framework ready for ongoing monitoring.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-gradient-to-r from-red-900/50 to-orange-900/50 p-6 rounded-lg border-2 border-red-500">
            <h3 className="text-3xl font-bold text-white mb-4 text-center">What We Cannot Yet Determine</h3>
            <div className="grid grid-cols-2 gap-6">
              <div>
                <h4 className="font-bold text-red-300 mb-3 text-center">Causal Effects</h4>
                <ul className="text-red-100 text-sm space-y-2">
                  <li>❌ Whether reform improved financial health</li>
                  <li>❌ Whether reform worsened financial health</li>
                  <li>❌ Whether reform had no meaningful effect</li>
                  <li>❌ Steady-state integration effects</li>
                </ul>
              </div>
              <div>
                <h4 className="font-bold text-orange-300 mb-3 text-center">Why Not?</h4>
                <ul className="text-orange-100 text-sm space-y-2">
                  <li>• Only 12 months post-reform data</li>
                  <li>• No untreated comparison group</li>
                  <li>• Severe power limitations (25%)</li>
                  <li>• J-curve effects take 3-5 years</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="bg-blue-900/50 p-6 rounded-lg">
            <h3 className="text-2xl font-bold text-blue-300 mb-4">For Policymakers</h3>
            <div className="grid grid-cols-2 gap-6">
              <div>
                <h4 className="font-bold text-blue-200 mb-3">Short-Term Reassurance</h4>
                <p className="text-blue-100 text-sm mb-3">
                  No evidence of catastrophic financial deterioration in Year 1. Point estimate (+6.2pp) is concerning but CI includes near-zero effects.
                </p>
                <p className="text-blue-100 text-sm">
                  <strong>Implication:</strong> Proceed with implementation monitoring, but maintain vigilance for emerging patterns.
                </p>
              </div>
              <div>
                <h4 className="font-bold text-blue-200 mb-3">Long-Term Uncertainty</h4>
                <p className="text-blue-100 text-sm mb-3">
                  Cannot draw conclusions about ultimate reform success. Transition costs may dominate early observations before efficiency gains materialize.
                </p>
                <p className="text-blue-100 text-sm">
                  <strong>Implication:</strong> Pre-register 3-year evaluation timeline before making irreversible commitments.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-green-900/40 p-6 rounded-lg">
            <h3 className="text-2xl font-bold text-green-300 mb-4">For Researchers</h3>
            <div className="space-y-3">
              <div className="bg-green-900/30 p-4 rounded-lg">
                <h4 className="font-bold text-green-200 mb-2">1. Methodological Template</h4>
                <p className="text-green-100 text-sm">
                  Demonstrates transparent evaluation of universal reform with honest limitation reporting. Useful for similar policy contexts.
                </p>
              </div>
              <div className="bg-green-900/30 p-4 rounded-lg">
                <h4 className="font-bold text-green-200 mb-2">2. Selection Mechanism</h4>
                <p className="text-green-100 text-sm">
                  Early-adopter selection pattern informs external validity of future ULS studies. Cannot compare treated to untreated without accounting for this.
                </p>
              </div>
              <div className="bg-green-900/30 p-4 rounded-lg">
                <h4 className="font-bold text-green-200 mb-2">3. Replication Infrastructure</h4>
                <p className="text-green-100 text-sm">
                  Full GitHub repository enables independent verification and extension. Open data + open code = computational reproducibility standard.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-purple-900/40 p-6 rounded-lg border-2 border-purple-500">
            <h3 className="text-2xl font-bold text-purple-300 mb-4 text-center">Primary Contribution</h3>
            <p className="text-xl text-white text-center italic">
              "This paper establishes evaluation infrastructure and documents an important selection pattern in early ULS adoption. 
              It provides preliminary magnitudes but cannot yet determine causal effects."
            </p>
            <p className="text-center text-purple-200 mt-4">
              — A methodological baseline study, not a definitive causal evaluation —
            </p>
          </div>
        </div>
      )
    },

    // Anticipated Questions
    {
      title: "11. Anticipated Questions & Responses",
      icon: <AlertCircle className="w-8 h-8" />,
      content: (
        <div className="space-y-5">
          <h3 className="text-2xl font-bold text-blue-300 mb-4">Preparing for the Viva Defense</h3>

          <div className="space-y-4">
            <div className="bg-gradient-to-r from-blue-900/40 to-purple-900/40 p-5 rounded-lg border-l-4 border-blue-500">
              <h4 className="font-bold text-blue-300 mb-2 text-lg">Q1: "Why not use synthetic control as your primary specification?"</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> With only 7 potential donor units, synthetic control faces two challenges: (1) insufficient donors to construct 
                valid convex combinations for all 31 treated units, and (2) all donors are themselves long-run treated, not untreated. 
                I use SC as a robustness check, but DiD is more transparent about the estimand limitation.
              </p>
            </div>

            <div className="bg-gradient-to-r from-red-900/40 to-orange-900/40 p-5 rounded-lg border-l-4 border-red-500">
              <h4 className="font-bold text-red-300 mb-2 text-lg">Q2: "If you can't determine causal effects, what's the contribution?"</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> Three contributions: (1) Methodological infrastructure for ongoing evaluation as data accumulate; 
                (2) Discovery of -18.5pp selection pattern that must inform future causal inference; 
                (3) Preliminary magnitudes establishing baseline for policy monitoring. This follows best practices for preliminary 
                policy evaluation (e.g., Athey & Imbens on staged evaluation designs).
              </p>
            </div>

            <div className="bg-gradient-to-r from-green-900/40 to-teal-900/40 p-5 rounded-lg border-l-4 border-green-500">
              <h4 className="font-bold text-green-300 mb-2 text-lg">Q3: "The baseline difference suggests parallel trends are violated. Why proceed?"</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> You're absolutely right that the persistent baseline difference is concerning. I address this by: 
                (1) explicitly acknowledging the limitation, (2) conducting sensitivity analyses (PSM, heterogeneity), 
                (3) framing estimates as descriptive rather than definitively causal. The selection pattern itself is a contribution 
                worth documenting even if it complicates causal identification.
              </p>
            </div>

            <div className="bg-gradient-to-r from-purple-900/40 to-pink-900/40 p-5 rounded-lg border-l-4 border-purple-500">
              <h4 className="font-bold text-purple-300 mb-2 text-lg">Q4: "Why publish with such severe power limitations? Shouldn't you wait for more data?"</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> Two reasons: (1) Policy-relevant baseline is valuable now—policymakers need preliminary assessment 
                to inform monitoring priorities; (2) Pre-registering methodology and documenting early patterns follows emerging norms 
                for staged evaluation (Casey et al., 2012). I explicitly state this is V1 with planned re-analysis at 24 and 36 months.
              </p>
            </div>

            <div className="bg-gradient-to-r from-yellow-900/40 to-orange-900/40 p-5 rounded-lg border-l-4 border-yellow-500">
              <h4 className="font-bold text-yellow-300 mb-2 text-lg">Q5: "Your heterogeneity findings are all underpowered. Why report them?"</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> I flag them as exploratory throughout. They're reported because: (1) they generate testable hypotheses 
                for future work with adequate power; (2) point estimates align with theory (smaller hospitals, higher distress → larger effects); 
                (3) transparency norms suggest reporting all conducted analyses, not just significant ones, to avoid file-drawer bias.
              </p>
            </div>

            <div className="bg-gradient-to-r from-blue-800/40 to-indigo-900/40 p-5 rounded-lg border-l-4 border-blue-400">
              <h4 className="font-bold text-blue-300 mb-2 text-lg">Q6: "The overdue ratio could reflect accounting changes rather than real distress. How do you rule this out?"</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> Good point. I check for: (1) no changes to POCP accounting standards in 2024; 
                (2) consistent data quality pre/post-reform (94.7% coverage maintained); (3) robustness to alternative DVs 
                (log overdue debt, days payable outstanding). However, I cannot completely rule out definitional changes at ULS 
                consolidation—this is a limitation I should note more explicitly.
              </p>
            </div>

            <div className="bg-gradient-to-r from-teal-900/40 to-cyan-900/40 p-5 rounded-lg border-l-4 border-teal-500">
              <h4 className="font-bold text-teal-300 mb-2 text-lg">Q7: "What about COVID confounding? Your sample spans 2014-2025."</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> COVID impacts are addressed through: (1) time fixed effects absorb common shocks; 
                (2) subsample analysis excluding 2020-2021 shows similar patterns; (3) quarterly aggregation reduces month-specific noise. 
                However, COVID may have differential impacts on rural vs. urban hospitals that could confound the baseline difference. 
                Ideally, I'd add COVID × ULS interactions with more power.
              </p>
            </div>

            <div className="bg-gradient-to-r from-pink-900/40 to-rose-900/40 p-5 rounded-lg border-l-4 border-pink-500">
              <h4 className="font-bold text-pink-300 mb-2 text-lg">Q8: "You use AI tools. How do I know the analysis isn't AI-generated?"</h4>
              <p className="text-white text-sm">
                <strong>A:</strong> Transparent disclosure: AI assisted with data pipeline code (Python ingestion scripts) and literature 
                organization. All analytical decisions—model specifications, variable construction, interpretation—are mine. 
                The GitHub repo shows full code with comments explaining logic. I can walk through any specification choice and justify 
                it theoretically. AI helped with implementation, not intellectual direction.
              </p>
            </div>
          </div>

          <div className="bg-blue-900/50 p-5 rounded-lg border-2 border-blue-400">
            <h4 className="font-bold text-blue-300 mb-3 text-center">Defense Strategy</h4>
            <p className="text-blue-100 text-center">
              <strong>Be honest about limitations, emphasize methodological contribution, position as baseline for staged evaluation.</strong><br/>
              Show awareness of identification challenges. Demonstrate deep understanding of trade-offs in research design choices.
            </p>
          </div>
        </div>
      )
    },

    // Thank You / Questions
    {
      title: "Questions & Discussion",
      type: "end",
      content: (
        <div className="text-center space-y-8">
          <h1 className="text-5xl font-bold text-white mb-6">Thank You</h1>
          
          <div className="bg-gradient-to-r from-blue-900/50 to-purple-900/50 p-8 rounded-lg border-2 border-blue-500 max-w-3xl mx-auto">
            <h2 className="text-3xl font-bold text-blue-300 mb-4">Ready for Questions</h2>
            <p className="text-xl text-blue-100 mb-6">
              I welcome your feedback and questions about:
            </p>
            <div className="grid grid-cols-2 gap-4 text-left">
              <div className="bg-blue-900/40 p-4 rounded">
                <p className="text-blue-200 font-semibold">• Research Design</p>
                <p className="text-blue-100 text-sm">Identification strategy, specifications</p>
              </div>
              <div className="bg-blue-900/40 p-4 rounded">
                <p className="text-blue-200 font-semibold">• Data Quality</p>
                <p className="text-blue-100 text-sm">Sources, entity resolution, validation</p>
              </div>
              <div className="bg-blue-900/40 p-4 rounded">
                <p className="text-blue-200 font-semibold">• Results Interpretation</p>
                <p className="text-blue-100 text-sm">Selection pattern, power limitations</p>
              </div>
              <div className="bg-blue-900/40 p-4 rounded">
                <p className="text-blue-200 font-semibold">• Future Directions</p>
                <p className="text-blue-100 text-sm">Extensions, mechanism analysis</p>
              </div>
            </div>
          </div>

          <div className="bg-green-900/30 p-6 rounded-lg max-w-2xl mx-auto">
            <h3 className="text-xl font-bold text-green-300 mb-3">Contact & Resources</h3>
            <p className="text-green-100">
              Daniel Ferreira Polónia<br/>
              dpolonia@ua.pt<br/>
              DEGEIT, University of Aveiro
            </p>
            <p className="text-green-200 mt-4">
              📁 GitHub: github.com/dpolonia/cfe-hospital-distress<br/>
              📄 Full Paper: Available in repository
            </p>
          </div>

          <div className="text-blue-200 italic text-lg">
            "A methodological baseline establishing evaluation infrastructure<br/>
            for Portugal's most comprehensive healthcare reform in 25 years"
          </div>
        </div>
      )
    }
  ];

  const nextSlide = () => {
    if (currentSlide < slides.length - 1) {
      setCurrentSlide(currentSlide + 1);
    }
  };

  const prevSlide = () => {
    if (currentSlide > 0) {
      setCurrentSlide(currentSlide - 1);
    }
  };

  const goToSlide = (index) => {
    setCurrentSlide(index);
  };

  const currentSlideData = slides[currentSlide];

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 text-white p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-6 bg-gray-800/50 p-4 rounded-lg">
          <div className="flex items-center gap-3">
            {currentSlideData.icon && (
              <div className="text-blue-400">
                {currentSlideData.icon}
              </div>
            )}
            <h2 className="text-2xl font-bold text-blue-300">{currentSlideData.title}</h2>
          </div>
          <div className="text-blue-300 font-semibold">
            Slide {currentSlide + 1} / {slides.length}
          </div>
        </div>

        {/* Content Area */}
        <div className="bg-gray-800/30 backdrop-blur-sm rounded-xl p-8 min-h-[600px] mb-6 border border-gray-700">
          {currentSlideData.content}
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center">
          <button
            onClick={prevSlide}
            disabled={currentSlide === 0}
            className={`flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition-all ${
              currentSlide === 0
                ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700 text-white'
            }`}
          >
            <ChevronLeft className="w-5 h-5" />
            Previous
          </button>

          {/* Slide Indicators */}
          <div className="flex gap-2">
            {slides.map((_, index) => (
              <button
                key={index}
                onClick={() => goToSlide(index)}
                className={`w-3 h-3 rounded-full transition-all ${
                  index === currentSlide
                    ? 'bg-blue-500 w-8'
                    : 'bg-gray-600 hover:bg-gray-500'
                }`}
                title={`Go to slide ${index + 1}`}
              />
            ))}
          </div>

          <button
            onClick={nextSlide}
            disabled={currentSlide === slides.length - 1}
            className={`flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition-all ${
              currentSlide === slides.length - 1
                ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700 text-white'
            }`}
          >
            Next
            <ChevronRight className="w-5 h-5" />
          </button>
        </div>

        {/* Quick Navigation Menu */}
        <div className="mt-6 bg-gray-800/50 p-4 rounded-lg">
          <div className="flex items-center gap-2 mb-3">
            <Home className="w-5 h-5 text-blue-400" />
            <h3 className="font-semibold text-blue-300">Quick Navigation</h3>
          </div>
          <div className="grid grid-cols-4 gap-2 text-sm">
            {slides.map((slide, index) => (
              <button
                key={index}
                onClick={() => goToSlide(index)}
                className={`p-2 rounded text-left transition-all ${
                  index === currentSlide
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                }`}
              >
                {index + 1}. {slide.title.split(':')[0]}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default VivaPresentation;