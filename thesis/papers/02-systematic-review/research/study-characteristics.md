# Paper 02 — Study Characteristics Snapshot (Task 6.5, CC.4.1)

**Included studies**: 228 (S001-S228) — extracted from full texts where retrieved (all 228 included studies have full text)

## 6.5.3 Distribution

### By Year

| Year | Studies |
|------|--------:|
| 2018 | 1 |
| 2019 | 9 |
| 2020 | 19 |
| 2021 | 36 |
| 2022 | 32 |
| 2023 | 37 |
| 2024 | 27 |
| 2025 | 38 |
| 2026 | 29 |

### By Architecture Family

| Family | Studies |
|--------|--------:|
| Transformer-family | 219 |
| RNN-family | 169 |
| MLP | 97 |
| CNN | 97 |
| GNN | 81 |
| RL-agent | 71 |
| VAE/AE | 59 |
| Diffusion | 32 |

### By Benchmark Group

| Group | Studies |
|-------|--------:|
| Math/MW | 132 |
| Vision | 109 |
| SCAN | 98 |
| COGS | 83 |
| CFQ | 57 |
| NLP-OOD | 53 |
| CLOSURE | 43 |
| gSCAN | 22 |
| PCFG | 15 |
| NLU-bench | 15 |
| OOD-CV | 13 |
| Tabular | 12 |
| SLOG | 5 |
| Robotics/RL | 2 |
| CoCoGen | 1 |

### Seeds/Runs Reporting

- Studies reporting seeds/runs: **76** of 228 (33%)

## 6.5.4 Gap Assessment (automated snapshot)

- **Architectures**: coverage by family per table above; families with no detected studies are gaps to check in Phase 7 extraction.
- **Benchmarks**: SCAN/COGS/CFQ-family coverage per table above; benchmarks with zero hits may still appear via synonyms — verified in Phase 7.
- **Temporal**: year distribution above; note the 2017-2019 tail vs 2022-2026 growth.

## Full Table

| Study | Year | Venue | Architectures | Benchmarks | Seeds/runs |
|-------|------|-------|---------------|------------|------------|
| S001 | 2021 | 2021 IEEE/CVF Conference on Co | Transformer-family; RNN-family; MLP; GNN | CLOSURE; Vision; NLP-OOD |  |
| S002 | 2022 | Findings of the Association fo | Transformer-family; RNN-family; GNN | SCAN; NLP-OOD |  |
| S003 | 2026 | Proceedings of the AAAI Confer | Transformer-family; MLP | NLP-OOD |  |
| S004 | 2021 | NAACL-HLT 2021 - 2021 Conferen | Transformer-family; RNN-family | CFQ; Math/MW |  |
| S005 | 2023 | Proceedings of the 37th AAAI C | Transformer-family; CNN; VAE/AE | Math/MW; Vision; OOD-CV |  |
| S006 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; PCFG; Math/MW; Vision | 5 |
| S007 | 2025 | arXiv:benchmark | Transformer-family; RNN-family; MLP; RL- | COGS; SLOG |  |
| S008 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP | COGS; SLOG; Math/MW; Vision |  |
| S009 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; VAE/AE | SCAN; CFQ; Math/MW |  |
| S010 | 2024 | arXiv:benchmark | Transformer-family; RNN-family; MLP; RL- | SCAN; COGS; CFQ; PCFG; Math/MW | 2 |
| S011 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; CFQ; CLOSURE; NLU-bench; Vision |  |
| S012 | 2025 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW |  |
| S013 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; RL-agent | SCAN; CLOSURE; Vision |  |
| S014 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW; NLU-bench | 3 |
| S015 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW |  |
| S016 | 2022 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; CFQ |  |
| S017 | 2026 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; gSCAN; Math/MW | 5 |
| S018 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; gSCAN; CLOSURE; Vision |  |
| S019 | 2020 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; CFQ; Math/MW; Vision |  |
| S020 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN | CFQ; Tabular |  |
| S021 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; PCFG; CLOSURE | 5 |
| S022 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN | SCAN; gSCAN; Math/MW; Vision |  |
| S023 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ |  |
| S024 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; RL-agent | CFQ |  |
| S025 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; VAE/AE | SCAN; CFQ |  |
| S026 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; Math/MW; Vision | 1 |
| S027 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; Math/MW; NLU-bench |  |
| S028 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; Math/MW | 5 |
| S029 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; CFQ; PCFG; Math/MW |  |
| S030 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | COGS; Math/MW | 3 |
| S031 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | COGS; gSCAN; CLOSURE; Math/MW; Vision |  |
| S032 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ | 5 |
| S033 | 2022 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS |  |
| S034 | 2019 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; CFQ; Math/MW; Vision |  |
| S035 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; gSCAN; Math/MW; Vision; NLP- |  |
| S036 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP; VAE | COGS; Math/MW | 10 |
| S037 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; RL- | SCAN; CLOSURE; Vision | 5 |
| S038 | 2019 | arXiv:benchmark | Transformer-family; RNN-family; CNN | SCAN; COGS; Vision |  |
| S039 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ |  |
| S040 | 2025 | arXiv:benchmark | Transformer-family; RNN-family; GNN; RL- | SCAN | 4 |
| S041 | 2019 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; Vision | 25 |
| S042 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; MLP; GNN | SCAN; COGS; CLOSURE; Math/MW; Vision |  |
| S043 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; GNN; VAE | SCAN; COGS; CLOSURE; Math/MW; Vision |  |
| S044 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; Math/MW |  |
| S045 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; GNN | SCAN; COGS; Math/MW; Tabular |  |
| S046 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; NLU-bench; Vision |  |
| S047 | 2019 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; Math/MW | 5 |
| S048 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; MLP; GNN | Math/MW |  |
| S049 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; VAE/AE | CLOSURE; Math/MW; Vision |  |
| S050 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | COGS; CFQ; CLOSURE; Math/MW; Vision | 10 |
| S051 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; Math/MW; NLP-OOD | 20 |
| S052 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; gSCAN; CLOSURE; Math/MW; Vision | 3 |
| S053 | 2022 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; CLOSURE; Math/MW; NLU-b |  |
| S054 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; RL- | SCAN; gSCAN; CLOSURE; Vision | 3 |
| S055 | 2019 | arXiv:benchmark | Transformer-family; RNN-family | SCAN |  |
| S056 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; gSCAN | 5 |
| S057 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; Math/MW |  |
| S058 | 2026 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; Math/MW | 3 |
| S059 | 2026 | arXiv:benchmark | Transformer-family; RNN-family; GNN; RL- | SCAN; CLOSURE; Math/MW; NLP-OOD |  |
| S060 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN | SCAN |  |
| S061 | 2025 | arXiv:broad | Transformer-family; CNN; MLP; Diffusion | Math/MW; Vision |  |
| S062 | 2024 | arXiv:broad | Transformer-family; MLP | Math/MW; Vision; OOD-CV | 6 |
| S063 | 2025 | arXiv:broad | Transformer-family; CNN | SCAN; NLU-bench; Vision; OOD-CV |  |
| S064 | 2026 | arXiv:broad | Transformer-family; CNN; MLP; Diffusion | CoCoGen; Math/MW; Vision | 3 |
| S065 | 2024 | arXiv:broad | unknown | Math/MW; OOD-CV |  |
| S066 | 2025 | arXiv:broad | Transformer-family; CNN; MLP; Diffusion | Math/MW; Vision | 10 |
| S067 | 2022 | arXiv:broad | Transformer-family; GNN | NLU-bench | 3 |
| S068 | 2022 | arXiv:broad | Transformer-family; CNN; GNN; VAE/AE | COGS; Vision; OOD-CV |  |
| S069 | 2022 | arXiv:broad | Transformer-family; CNN; MLP; GNN; RL-ag | Math/MW |  |
| S070 | 2025 | arXiv:broad | Transformer-family; CNN; MLP; GNN; RL-ag | Math/MW |  |
| S071 | 2021 | arXiv:broad | Transformer-family; CNN; MLP; VAE/AE | SCAN; Math/MW; Vision; OOD-CV | 10 |
| S072 | 2024 | arXiv:broad | Transformer-family; RNN-family; CNN; VAE | Math/MW; NLU-bench; Vision; OOD-CV | 6 |
| S073 | 2021 | arXiv:broad | CNN; MLP; GNN; VAE/AE | Vision; OOD-CV | 4 |
| S074 | 2023 | arXiv:broad | Transformer-family; CNN; RL-agent; VAE/A | Math/MW; Vision; NLP-OOD |  |
| S075 | 2024 | arXiv:broad | Transformer-family | Math/MW; Vision; NLP-OOD | 10 |
| S076 | 2023 | arXiv:broad | Transformer-family; RL-agent | none-detected |  |
| S077 | 2026 | arXiv:broad | Transformer-family; RNN-family; CNN; MLP | Math/MW; NLU-bench; Vision |  |
| S078 | 2026 | arXiv:broad | Transformer-family; MLP; VAE/AE; Diffusi | CLOSURE |  |
| S079 | 2026 | arXiv:broad | Transformer-family; RNN-family; CNN; Dif | COGS; NLP-OOD |  |
| S080 | 2025 | arXiv:broad | Transformer-family; GNN; RL-agent; VAE/A | Math/MW; NLP-OOD | 16 |
| S081 | 2025 | arXiv:broad | Transformer-family; CNN; MLP; GNN; RL-ag | COGS; Math/MW; Vision; NLP-OOD; Robotics | 10 |
| S082 | 2021 | arXiv:broad | Transformer-family; RNN-family; CNN; GNN | COGS; NLU-bench; Vision; NLP-OOD |  |
| S083 | 2026 | arXiv:broad | Transformer-family; GNN | Math/MW |  |
| S084 | 2025 | arXiv:broad | Transformer-family; RL-agent | none-detected |  |
| S085 | 2025 | arXiv:broad | RNN-family; MLP | SCAN; PCFG | 5 |
| S086 | 2026 | arXiv:broad | Transformer-family; RL-agent | SCAN; Math/MW; OOD-CV | 10 |
| S087 | 2023 | arXiv:broad | RNN-family; CNN | none-detected |  |
| S088 | 2024 | arXiv:broad | Transformer-family; RNN-family; CNN; MLP | SCAN; Vision |  |
| S089 | 2026 | arXiv:broad | Transformer-family; CNN; MLP; GNN; VAE/A | Math/MW |  |
| S090 | 2025 | arXiv:broad | CNN; MLP; GNN | none-detected |  |
| S091 | 2026 | arXiv:broad | Transformer-family; RL-agent | SCAN; CLOSURE; Math/MW |  |
| S092 | 2026 | arXiv:broad | Transformer-family; RNN-family; CNN; GNN | Math/MW |  |
| S093 | 2026 | arXiv:broad | Transformer-family; RNN-family; GNN | SCAN; Math/MW; Vision |  |
| S094 | 2025 | arXiv:broad | Transformer-family; GNN | Math/MW; Vision |  |
| S095 | 2026 | arXiv:broad | Transformer-family; MLP; GNN; RL-agent;  | CLOSURE; Math/MW; Tabular |  |
| S096 | 2025 | arXiv:broad | Transformer-family; RL-agent; VAE/AE | Math/MW; NLP-OOD |  |
| S097 | 2020 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; Vision | 5 |
| S098 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | COGS; CFQ; Math/MW; Vision | 10 |
| S099 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | Math/MW | 5 |
| S100 | 2020 | arXiv:primary | Transformer-family; RNN-family | SCAN; gSCAN; CLOSURE; Vision; NLP-OOD |  |
| S101 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN; RL- | SCAN; COGS; Math/MW |  |
| S102 | 2025 | arXiv:primary | Transformer-family; RL-agent; VAE/AE | Vision |  |
| S103 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | CLOSURE; Math/MW; Vision | 3 |
| S104 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW |  |
| S105 | 2021 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ | 5 |
| S106 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Vision; NLP-OOD |  |
| S107 | 2022 | arXiv:primary | Transformer-family; RNN-family; RL-agent | COGS; CLOSURE; Math/MW; Vision; NLP-OOD | 13 |
| S108 | 2021 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; CFQ; Math/MW |  |
| S109 | 2019 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | Math/MW; Vision |  |
| S110 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ; Math/MW |  |
| S111 | 2023 | arXiv:primary | Transformer-family; CNN; RL-agent; VAE/A | Math/MW | 10 |
| S112 | 2024 | arXiv:primary | Transformer-family; RNN-family; RL-agent | Math/MW |  |
| S113 | 2021 | arXiv:primary | Transformer-family; RNN-family; MLP; VAE | COGS; CFQ; Math/MW | 3 |
| S114 | 2021 | arXiv:primary | Transformer-family; RNN-family; VAE/AE | none-detected |  |
| S115 | 2024 | arXiv:primary | Transformer-family; MLP | Vision |  |
| S116 | 2024 | arXiv:primary | Transformer-family; RNN-family; MLP; VAE | COGS; CLOSURE; Math/MW | 5 |
| S117 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN | SCAN; CFQ; Math/MW; Vision |  |
| S118 | 2024 | arXiv:primary | Transformer-family; RNN-family; GNN | SCAN; COGS; NLP-OOD |  |
| S119 | 2024 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS; Math/MW |  |
| S120 | 2024 | arXiv:primary | Transformer-family; RNN-family | SCAN; COGS; CFQ; PCFG; Math/MW | 1 |
| S121 | 2022 | arXiv:primary | Transformer-family; RNN-family | SCAN; COGS; CLOSURE; Vision |  |
| S122 | 2026 | arXiv:primary | Transformer-family; RNN-family; VAE/AE;  | Math/MW; Vision; NLP-OOD |  |
| S123 | 2025 | arXiv:primary | Transformer-family; CNN; VAE/AE; Diffusi | Vision |  |
| S124 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision |  |
| S125 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; gSCAN; Math/MW |  |
| S126 | 2022 | arXiv:primary | Transformer-family; RNN-family | none-detected | 3 |
| S127 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN | SCAN; CFQ; PCFG; Math/MW |  |
| S128 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | Math/MW; Vision | 5 |
| S129 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | Math/MW; NLP-OOD; Tabular |  |
| S130 | 2026 | arXiv:primary | Transformer-family; RNN-family; MLP; RL- | Vision; NLP-OOD |  |
| S131 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; gSCAN; PCFG; CLOSURE; M |  |
| S132 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | NLP-OOD |  |
| S133 | 2024 | arXiv:primary | Transformer-family; CNN | Math/MW; NLU-bench |  |
| S134 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; CFQ |  |
| S135 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision |  |
| S136 | 2025 | arXiv:primary | Transformer-family; CNN; GNN; VAE/AE; Di | Math/MW; Vision | 10 |
| S137 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; Math/MW; NLP-OOD |  |
| S138 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN; Dif | SCAN; COGS; Vision; NLP-OOD |  |
| S139 | 2020 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; CLOSURE; Math/MW | 3 |
| S140 | 2024 | arXiv:primary | Transformer-family; CNN; GNN; VAE/AE | Math/MW; Vision; OOD-CV; NLP-OOD | 3 |
| S141 | 2024 | arXiv:primary | Transformer-family; RNN-family | COGS; NLP-OOD |  |
| S142 | 2022 | arXiv:primary | Transformer-family; RNN-family | COGS; CFQ |  |
| S143 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ |  |
| S144 | 2021 | arXiv:primary | Transformer-family; RNN-family | SCAN; COGS; CFQ; PCFG; Math/MW | 3 |
| S145 | 2019 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | COGS; Vision |  |
| S146 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN | COGS; gSCAN |  |
| S147 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN | Vision; NLP-OOD |  |
| S148 | 2025 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS; PCFG; SLOG; NLP-OOD |  |
| S149 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; gSCAN; Math/MW; Vision | 5 |
| S150 | 2024 | arXiv:primary | Transformer-family; CNN | gSCAN; Math/MW; NLU-bench; Vision |  |
| S151 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision; Tabular |  |
| S152 | 2023 | arXiv:primary | Transformer-family; CNN | Vision | 10 |
| S153 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS | 5 |
| S154 | 2024 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | SCAN; COGS; SLOG; Math/MW | 5 |
| S155 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | SCAN; Math/MW |  |
| S156 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; PCFG; Math/MW |  |
| S157 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | CLOSURE; Vision; NLP-OOD |  |
| S158 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; Dif | COGS; Math/MW; Vision; NLP-OOD |  |
| S159 | 2024 | arXiv:primary | Transformer-family; RNN-family; GNN | COGS; Math/MW |  |
| S160 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; PCFG; CLOSURE; Math/MW; | 5 |
| S161 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; Math/MW |  |
| S162 | 2021 | arXiv:primary | Transformer-family; RNN-family | COGS; CFQ; Tabular | 5 |
| S163 | 2025 | arXiv:primary | Transformer-family; RNN-family; GNN; RL- | SLOG; Math/MW | 192 |
| S164 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS; Math/MW |  |
| S165 | 2026 | arXiv:primary | Transformer-family; RNN-family; MLP; RL- | Math/MW |  |
| S166 | 2022 | arXiv:primary | Transformer-family; RNN-family | COGS; Math/MW; Vision; NLP-OOD |  |
| S167 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision; NLP-OOD |  |
| S168 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | SCAN; COGS; CLOSURE; Math/MW; Vision |  |
| S169 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | none-detected |  |
| S170 | 2025 | arXiv:primary | Transformer-family; CNN; MLP; VAE/AE; Di | Math/MW; Vision; NLP-OOD |  |
| S171 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | COGS; Math/MW; Tabular |  |
| S172 | 2025 | arXiv:primary | Transformer-family; RNN-family; MLP; Dif | Math/MW; NLP-OOD |  |
| S173 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; CLOSURE; Math/MW; Visio | 3 |
| S174 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; CFQ | 6 |
| S175 | 2020 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; gSCAN; Math/MW; Vision; NLP-OOD |  |
| S176 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision; NLP-OOD |  |
| S177 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; RL- | Vision; Robotics/RL | 50 |
| S178 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | CFQ; CLOSURE; Vision; NLP-OOD |  |
| S179 | 2025 | arXiv:primary | Transformer-family; Diffusion | Vision |  |
| S180 | 2026 | arXiv:primary | Transformer-family; RL-agent | Math/MW; Vision; NLP-OOD |  |
| S181 | 2022 | arXiv:primary | Transformer-family | none-detected |  |
| S182 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | none-detected | 5 |
| S183 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN | CFQ; CLOSURE; Vision |  |
| S184 | 2024 | arXiv:primary | Transformer-family; MLP; GNN; Diffusion | NLU-bench |  |
| S185 | 2021 | arXiv:primary | RNN-family; CNN; MLP; RL-agent; VAE/AE | COGS; CLOSURE; Math/MW; Vision; NLP-OOD |  |
| S186 | 2026 | arXiv:primary | Transformer-family; GNN; RL-agent; VAE/A | CLOSURE; Math/MW |  |
| S187 | 2018 | arXiv:primary | Transformer-family; RNN-family; CNN | SCAN; Vision | 5 |
| S188 | 2025 | arXiv:primary | Transformer-family; VAE/AE; Diffusion | Vision |  |
| S189 | 2022 | arXiv:primary | Transformer-family; RL-agent | Math/MW; Tabular |  |
| S190 | 2025 | arXiv:primary | Transformer-family; RNN-family; MLP; RL- | SCAN; COGS; CFQ; CLOSURE; Math/MW; NLP-O | 25 |
| S191 | 2025 | arXiv:primary | Transformer-family; Diffusion | Math/MW; Vision; NLP-OOD |  |
| S192 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision |  |
| S193 | 2023 | arXiv:primary | Transformer-family; MLP | Math/MW; Vision |  |
| S194 | 2020 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; gSCAN; CLOSURE; Vision |  |
| S195 | 2020 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; CFQ; CLOSURE; Vision |  |
| S196 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; gSCAN; CLOSURE; Vision | 5 |
| S197 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN | COGS; CLOSURE; NLU-bench; Vision; NLP-OO |  |
| S198 | 2020 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; Math/MW |  |
| S199 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ; gSCAN; Math/MW; Vision; |  |
| S200 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | COGS; CLOSURE; Vision; NLP-OOD |  |
| S201 | 2026 | arXiv:primary | Transformer-family; GNN; VAE/AE; Diffusi | Vision |  |
| S202 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | PCFG; Math/MW | 5 |
| S203 | 2024 | arXiv:primary | Transformer-family; CNN | Vision |  |
| S204 | 2021 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; PCFG; CLOSURE; Math/MW; | 5 |
| S205 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | gSCAN |  |
| S206 | 2021 | arXiv:primary | CNN; MLP; VAE/AE | Vision; NLP-OOD |  |
| S207 | 2019 | arXiv:primary | Transformer-family; RNN-family; GNN | Math/MW |  |
| S208 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; gSCAN; PCFG; CLOSURE; M | 5 |
| S209 | 2019 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; CLOSURE; Math/MW; Vision; Tabular | 10 |
| S210 | 2026 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW |  |
| S211 | 2022 | arXiv:primary | Transformer-family; CNN; MLP | Vision; NLP-OOD | 10 |
| S212 | 2021 | arXiv:primary | Transformer-family; RNN-family; GNN | SCAN; COGS; CFQ; NLU-bench; NLP-OOD | 3 |
| S213 | 2021 | arXiv:primary | Transformer-family; RNN-family | SCAN |  |
| S214 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | NLP-OOD |  |
| S215 | 2025 | arXiv:primary | Transformer-family; RNN-family; GNN; RL- | none-detected | 20 |
| S216 | 2026 | arXiv:primary | RL-agent | Vision |  |
| S217 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | COGS; gSCAN; Vision | 3 |
| S218 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; CLOSURE; Math/MW; Vision; NLP-OOD |  |
| S219 | 2025 | arXiv:primary | Transformer-family; RNN-family; RL-agent | Math/MW; NLP-OOD | 3 |
| S220 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | Math/MW |  |
| S221 | 2023 | arXiv:primary | Transformer-family; CNN; RL-agent; VAE/A | Math/MW; Vision; OOD-CV; Tabular | 10 |
| S222 | 2026 | arXiv:primary | Transformer-family; CNN | SCAN; Vision; NLP-OOD | 4 |
| S223 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; Math/MW |  |
| S224 | 2023 | arXiv:primary | Transformer-family; RL-agent; VAE/AE | none-detected | 10 |
| S225 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN | gSCAN; Vision | 5 |
| S226 | 2022 | arXiv:primary | MLP; GNN; VAE/AE | NLP-OOD; Tabular |  |
| S227 | 2026 | arXiv:safety | Transformer-family; MLP; GNN; RL-agent | none-detected | 3 |
| S228 | 2025 | arXiv:safety | Transformer-family; CNN; VAE/AE | Math/MW; Vision; NLP-OOD; Tabular |  |
