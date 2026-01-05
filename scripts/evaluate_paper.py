"""
Q1 Journal Multi-Agent Paper Evaluation System
===============================================
Three AI agents act as SEVERE but CONSTRUCTIVE academic reviewers
for a top-tier Q1 journal (Journal of Financial Economics / Health Economics level)

Evaluators:
- Reviewer 1: OpenAI GPT-4o (using chat endpoint)
- Reviewer 2: Anthropic Claude Opus 4.5 
- Reviewer 3: Google Gemini 3-Pro

Synthesis: Claude Opus 4.5 creates improved V2
"""
import os
import json
from dotenv import load_dotenv
import openai
import anthropic
import google.generativeai as genai

load_dotenv()

# === API Configuration (Load from environment variables) ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# MOST POWERFUL MODELS (No cost savings)
OPENAI_REASONING_MODEL = "o3-pro"
OPENAI_MODEL = "gpt-4o"  # Fallback for chat endpoint
ANTHROPIC_MODEL = "claude-opus-4-5-20251101"  # Opus 4.5 - Most Powerful
GEMINI_MODEL = "gemini-3-pro-preview"  # Gemini 3 Pro Preview (User Specified)

# === CFE Evaluation Criteria ===
EVALUATION_CRITERIA = """
## CFE Empirical Work Evaluation Matrix (PhD Level - 50% of final grade)

| Criterion | Weight | Excellent (18-20) | Good (14-17) | Satisfactory (10-13) | Insufficient (<10) |
|-----------|--------|-------------------|--------------|---------------------|-------------------|
| Research Question | 10% | Original, significant, clearly stated | Good research question | Adequate question | Vague or trivial |
| Literature Review | 10% | Comprehensive, current, well-integrated | Good coverage | Adequate review | Superficial |
| Theoretical Framework | 10% | Strong theoretical grounding with clear hypotheses | Good theoretical basis | Basic framework | Weak theory |
| Methodology Design | 15% | Rigorous, appropriate, well-justified | Sound methodology | Adequate methodology | Flawed |
| Data Quality | 10% | Excellent data selection, sources, handling | Good data work | Adequate data | Poor quality |
| Empirical Analysis | 20% | Sophisticated analysis with robust techniques | Good analytical work | Basic analysis | Weak analysis |
| Results Interpretation | 10% | Insightful interpretation with clear implications | Good interpretation | Adequate interpretation | Superficial |
| Replicability | 5% | Fully replicable with clear documentation | Mostly replicable | Partially replicable | Not replicable |
| Writing Quality | 5% | Excellent academic writing, well-structured | Good writing | Adequate writing | Poor writing |
| AI Tools Usage | 5% | Appropriate, transparent, well-integrated | Good AI use | Adequate AI usage | Inappropriate |
"""

# === SEVERE Q1 JOURNAL REVIEWER PROMPT ===
Q1_REVIEWER_PROMPT = """You are a SENIOR ASSOCIATE EDITOR at a top-tier Q1 economics journal (Journal of Financial Economics, Health Economics, or Journal of Health Economics level).

You are known for being:
- RIGOROUS and demanding in methodological standards
- SKEPTICAL of causal claims without proper identification
- THOROUGH in identifying limitations authors may have overlooked
- CONSTRUCTIVE in suggesting specific, actionable improvements
- FAIR but SEVERE - you maintain high standards but acknowledge genuine contributions

## YOUR REVIEW TASK

Evaluate this PhD-level empirical work for a Corporate Finance course. While this is coursework (not a publication submission), apply the standards of a Q1 journal reviewer to provide maximum learning value.

## EVALUATION CRITERIA (Score each 0-20):

{criteria}

## PAPER TO REVIEW:

{paper_content}

---

## REQUIRED OUTPUT FORMAT (JSON):

Provide your review as a structured JSON response:
{{
    "reviewer": "Your assigned reviewer name",
    "recommendation": "ACCEPT_WITH_MAJOR_REVISIONS | ACCEPT_WITH_MINOR_REVISIONS | REJECT_AND_RESUBMIT",
    "overall_score": <weighted_average_0_to_20>,
    "summary_assessment": "2-3 sentence overall assessment",
    "main_contribution": "What is the paper's main contribution in one sentence?",
    "fatal_flaws": ["List any issues that would prevent publication if unfixed"],
    "criteria_scores": {{
        "research_question": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "literature_review": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "theoretical_framework": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "methodology_design": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "data_quality": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "empirical_analysis": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "results_interpretation": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "replicability": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "writing_quality": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}},
        "ai_tools_usage": {{"score": X, "strengths": "...", "weaknesses": "...", "specific_improvement": "..."}}
    }},
    "priority_revisions": [
        "Revision 1: Most critical issue to address",
        "Revision 2: Second priority",
        "Revision 3: Third priority"
    ],
    "minor_comments": ["List of smaller issues to address"]
}}

Be SEVERE but CONSTRUCTIVE. Identify real weaknesses but also acknowledge genuine strengths.
"""


def load_paper():
    """Load the current paper content."""
    with open("CFE_Empirical_Work_V4_HealthEconomics.md", "r", encoding="utf-8") as f:
        return f.read()


def evaluate_with_openai(paper_content):
    """Reviewer 1: OpenAI GPT-4o"""
    print("\n" + "=" * 70)
    print("REVIEWER 1: OpenAI GPT-4o (Econometrics Specialist)")
    print("=" * 70)
    
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are Reviewer 1, an econometrics specialist known for rigorous methodological standards. Respond only in valid JSON."},
                {"role": "user", "content": Q1_REVIEWER_PROMPT.format(
                    criteria=EVALUATION_CRITERIA, 
                    paper_content=paper_content[:20000]
                )}
            ],
            response_format={"type": "json_object"},
            max_tokens=4000,
            temperature=0.3
        )
        
        result = json.loads(response.choices[0].message.content)
        result["reviewer"] = "Reviewer 1: Econometrics Specialist (GPT-4o)"
        print(f"  Recommendation: {result.get('recommendation', 'N/A')}")
        print(f"  Overall Score: {result.get('overall_score', 'N/A')}/20")
        return result
        
    except Exception as e:
        print(f"  Error: {e}")
        return {"reviewer": "OpenAI Reviewer 1", "error": str(e)}


def evaluate_with_anthropic(paper_content):
    """Reviewer 2: Claude Opus 4.5"""
    print("\n" + "=" * 70)
    print("REVIEWER 2: Claude Opus 4.5 (Healthcare Finance Expert)")
    print("=" * 70)
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=4000,
            messages=[
                {"role": "user", "content": f"""You are Reviewer 2, a healthcare finance expert with extensive publication experience in Health Economics and Journal of Health Economics.

{Q1_REVIEWER_PROMPT.format(criteria=EVALUATION_CRITERIA, paper_content=paper_content[:20000])}"""}
            ]
        )
        
        content = response.content[0].text
        # Parse JSON from response
        start = content.find("{")
        end = content.rfind("}") + 1
        if start >= 0 and end > start:
            result = json.loads(content[start:end])
            result["reviewer"] = "Reviewer 2: Healthcare Finance Expert (Claude Opus 4.5)"
            print(f"  Recommendation: {result.get('recommendation', 'N/A')}")
            print(f"  Overall Score: {result.get('overall_score', 'N/A')}/20")
            return result
        else:
            print("  Warning: Could not parse JSON, returning raw response")
            return {"reviewer": "Claude Opus 4.5", "raw_response": content[:1000]}
            
    except Exception as e:
        print(f"  Error: {e}")
        return {"reviewer": "Anthropic Reviewer 2", "error": str(e)}


def evaluate_with_gemini(paper_content):
    """Reviewer 3: Gemini 2.0"""
    print("\n" + "=" * 70)
    print("REVIEWER 3: Gemini 2.0 (Public Sector Finance Specialist)")  
    print("=" * 70)
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL)
    
    try:
        response = model.generate_content(
            f"""You are Reviewer 3, a public sector finance specialist who has published extensively on government budgeting and soft budget constraints.

{Q1_REVIEWER_PROMPT.format(criteria=EVALUATION_CRITERIA, paper_content=paper_content[:20000])}""",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                temperature=0.3
            )
        )
        
        result = json.loads(response.text)
        result["reviewer"] = "Reviewer 3: Public Sector Finance (Gemini 2.0)"
        print(f"  Recommendation: {result.get('recommendation', 'N/A')}")
        print(f"  Overall Score: {result.get('overall_score', 'N/A')}/20")
        return result
        
    except Exception as e:
        print(f"  Error: {e}")
        return {"reviewer": "Gemini Reviewer 3", "error": str(e)}


def synthesize_and_improve(paper_content, evaluations):
    """Senior Editor (Claude Opus 4.5) synthesizes reviews and creates V2."""
    print("\n" + "=" * 70)
    print("SENIOR EDITOR: Claude Opus 4.5 - Synthesizing Reviews & Creating V2")
    print("=" * 70)
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    synthesis_prompt = f"""You are the SENIOR EDITOR at a top Q1 journal. You have received three reviewer reports on a PhD coursework submission.

## REVIEWER REPORTS:

{json.dumps(evaluations, indent=2, default=str)[:15000]}

## ORIGINAL PAPER:

{paper_content[:20000]}

## YOUR TASK AS SENIOR EDITOR:

1. Synthesize the three reviews into a coherent editorial decision
2. Identify the CONSENSUS priority revisions (issues raised by 2+ reviewers)
3. Create an IMPROVED VERSION (V2) of the paper that addresses:
   - All "fatal flaws" identified
   - Top 3 priority revisions from each reviewer
   - Maintains academic rigor while improving clarity

Output the COMPLETE improved paper in Markdown format.
Start with a brief editorial summary (what was changed), then the full revised paper.
Focus on SUBSTANTIVE improvements, not cosmetic changes.
"""
    
    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=8000,
            messages=[{"role": "user", "content": synthesis_prompt}]
        )
        
        v2_content = response.content[0].text
        
        with open("CFE_Empirical_Work_V5_HealthEconomics.md", "w", encoding="utf-8") as f:
            f.write(v2_content)
        
        print("  V5 saved: CFE_Empirical_Work_V5_HealthEconomics.md")
        return v2_content
        
    except Exception as e:
        print(f"  Synthesis Error: {e}")
        return None


def generate_editorial_report(evaluations):
    """Generate comprehensive editorial report."""
    
    report = """# Q1 Journal Peer Review Report

## Reviewers
- **Reviewer 1**: Econometrics Specialist (OpenAI GPT-4o)
- **Reviewer 2**: Healthcare Finance Expert (Claude Opus 4.5)
- **Reviewer 3**: Public Sector Finance Specialist (Gemini 2.0)

---

## Score Summary

| Criterion | Weight | R1 | R2 | R3 | Average |
|-----------|--------|----|----|----|---------| 
"""
    
    criteria_names = [
        ("research_question", 10), ("literature_review", 10), ("theoretical_framework", 10),
        ("methodology_design", 15), ("data_quality", 10), ("empirical_analysis", 20),
        ("results_interpretation", 10), ("replicability", 5), ("writing_quality", 5), ("ai_tools_usage", 5)
    ]
    
    for crit, weight in criteria_names:
        scores = []
        for eval_result in evaluations:
            if "criteria_scores" in eval_result and crit in eval_result["criteria_scores"]:
                scores.append(eval_result["criteria_scores"][crit].get("score", "N/A"))
            else:
                scores.append("N/A")
        
        numeric_scores = [s for s in scores if isinstance(s, (int, float))]
        avg = f"{sum(numeric_scores)/len(numeric_scores):.1f}" if numeric_scores else "N/A"
        
        report += f"| {crit.replace('_', ' ').title()} | {weight}% | {scores[0]} | {scores[1]} | {scores[2]} | {avg} |\n"
    
    # Overall scores
    report += "\n---\n\n## Overall Recommendations\n\n"
    for eval_result in evaluations:
        reviewer = eval_result.get("reviewer", "Unknown")
        rec = eval_result.get("recommendation", "N/A")
        score = eval_result.get("overall_score", "N/A")
        summary = eval_result.get("summary_assessment", "")
        report += f"**{reviewer}**\n- Recommendation: {rec}\n- Score: {score}/20\n- Assessment: {summary}\n\n"
    
    # Priority revisions
    report += "---\n\n## Consensus Priority Revisions\n\n"
    all_revisions = []
    for eval_result in evaluations:
        if "priority_revisions" in eval_result:
            all_revisions.extend(eval_result["priority_revisions"])
    
    for i, rev in enumerate(all_revisions[:9], 1):
        report += f"{i}. {rev}\n"
    
    # Fatal flaws
    report += "\n---\n\n## Identified Fatal Flaws\n\n"
    for eval_result in evaluations:
        if "fatal_flaws" in eval_result and eval_result["fatal_flaws"]:
            reviewer = eval_result.get("reviewer", "Unknown")
            report += f"**{reviewer}:**\n"
            for flaw in eval_result["fatal_flaws"]:
                report += f"- {flaw}\n"
            report += "\n"
    
    report += "\n---\n\n*Report generated: January 2026*\n"
    
    with open("results/q1_journal_review.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    return report


def main():
    print("\n" + "=" * 70)
    print("Q1 JOURNAL MULTI-AGENT PEER REVIEW SYSTEM")
    print("Severe but Constructive Academic Evaluation")
    print("=" * 70)
    
    # Load paper
    paper = load_paper()
    print(f"\nPaper loaded: {len(paper)} characters")
    
    # Collect reviews
    evaluations = []
    
    # Reviewer 1: OpenAI
    eval1 = evaluate_with_openai(paper)
    evaluations.append(eval1)
    
    # Reviewer 2: Anthropic Opus 4.5
    eval2 = evaluate_with_anthropic(paper)
    evaluations.append(eval2)
    
    # Reviewer 3: Gemini
    eval3 = evaluate_with_gemini(paper)
    evaluations.append(eval3)
    
    # Save raw evaluations
    with open("results/q1_evaluations.json", "w", encoding="utf-8") as f:
        json.dump(evaluations, f, indent=2, default=str)
    print("\nRaw evaluations saved: results/q1_evaluations.json")
    
    # Generate editorial report
    report = generate_editorial_report(evaluations)
    print("Editorial report saved: results/q1_journal_review.md")
    
    # Senior Editor synthesizes and creates V2
    v2 = synthesize_and_improve(paper, evaluations)
    
    print("\n" + "=" * 70)
    print("PEER REVIEW COMPLETE!")
    print("=" * 70)
    print("\nOutputs:")
    print("  - results/q1_evaluations.json (raw reviews)")
    print("  - results/q1_journal_review.md (editorial summary)")
    print("  - CFE_Empirical_Work_V2.md (improved version)")


if __name__ == "__main__":
    main()
