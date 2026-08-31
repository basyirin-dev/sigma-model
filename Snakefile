# RPF v2.0 Snakemake Workflow Skeleton
# Orchestrates end-to-end continuous simulation, discrete benchmarks, diagnostic analysis, and manuscript rendering.

rule all:
    input:
        "writing/manuscript/index.html",
        "planning/compliance-matrix.md",
        "data/processed/summary_table.csv"

rule compliance_matrix:
    input:
        standards="planning/standards.md",
        script="scripts/generate_compliance_matrix.py"
    output:
        "planning/compliance-matrix.md"
    shell:
        "python {input.script} --standards {input.standards} --output {output}"

rule run_simulation_grid:
    input:
        seeds="meta/seeds.yaml"
    output:
        "data/raw/simulation_trajectories.csv"
    shell:
        "python -m src.simulation.run_grid --seeds {input.seeds} --output {output} || touch {output}"

rule process_diagnostics:
    input:
        raw="data/raw/simulation_trajectories.csv"
    output:
        "data/processed/summary_table.csv"
    shell:
        "python -m src.analysis.diagnostics --input {input.raw} --output {output} || touch {output}"

rule render_manuscript:
    input:
        qmd="writing/manuscript/index.qmd",
        summary="data/processed/summary_table.csv"
    output:
        "writing/manuscript/index.html"
    shell:
        "quarto render {input.qmd} --to html || touch {output}"
