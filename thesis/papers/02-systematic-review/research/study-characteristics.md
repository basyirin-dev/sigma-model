# Paper 02 — Study Characteristics Snapshot (Task 6.5, CC.4.1)

**Included studies**: 286 (S001-S286) — extracted from full texts where retrieved (all 286 included studies have full text)

## 6.5.3 Distribution

### By Year

| Year | Studies |
|------|--------:|
| 2018 | 1 |
| 2019 | 9 |
| 2020 | 21 |
| 2021 | 39 |
| 2022 | 36 |
| 2023 | 41 |
| 2024 | 37 |
| 2025 | 57 |
| 2026 | 45 |

### By Architecture Family

| Family | Studies |
|--------|--------:|
| Transformer-family | 274 |
| RNN-family | 192 |
| CNN | 147 |
| MLP | 133 |
| GNN | 110 |
| RL-agent | 88 |
| VAE/AE | 86 |
| Diffusion | 47 |

### By Benchmark Group

| Group | Studies |
|-------|--------:|
| Math/MW | 161 |
| Vision | 140 |
| SCAN | 102 |
| COGS | 91 |
| NLP-OOD | 66 |
| CFQ | 57 |
| CLOSURE | 44 |
| OOD-CV | 25 |
| gSCAN | 22 |
| NLU-bench | 18 |
| Tabular | 15 |
| PCFG | 15 |
| SLOG | 5 |
| Robotics/RL | 4 |
| CoCoGen | 1 |

### Seeds/Runs Reporting

- Studies reporting seeds/runs: **86** of 286 (30%)

## 6.5.4 Gap Assessment (automated snapshot)

- **Architectures**: coverage by family per table above; families with no detected studies are gaps to check in Phase 7 extraction.
- **Benchmarks**: SCAN/COGS/CFQ-family coverage per table above; benchmarks with zero hits may still appear via synonyms — verified in Phase 7.
- **Temporal**: year distribution above; note the 2017-2019 tail vs 2022-2026 growth.

## Full Table

| Study | Year | Venue | Architectures | Benchmarks | Seeds/runs |
|-------|------|-------|---------------|------------|------------|
| S001 | 2025 | Proceedings of the ACM on Web  | Transformer-family; CNN; GNN; RL-agent;  | none-detected |  |
| S002 | 2024 | Proceedings of the 32nd ACM In | Transformer-family; CNN | Vision; NLP-OOD |  |
| S003 | 2026 | Proceedings of the 2025 6th In | Transformer-family; CNN; Diffusion | Vision; OOD-CV; NLP-OOD |  |
| S004 | 2025 | ACM:F2 | Transformer-family; RL-agent; VAE/AE | Math/MW; Vision |  |
| S005 | 2024 | Proceedings of the 2024 2nd In | Transformer-family; CNN; MLP | Math/MW |  |
| S006 | 2026 | Proceedings of the 25th Intern | Transformer-family; RL-agent | Math/MW; Robotics/RL |  |
| S007 | 2026 | Proceedings of the 25th Intern | Transformer-family; MLP; RL-agent; Diffu | Math/MW; Vision |  |
| S008 | 2026 | Proceedings of the ACM Web Con | Transformer-family; RNN-family; CNN; MLP | none-detected |  |
| S009 | 2025 | ACM:F2 | Transformer-family; RNN-family; CNN; MLP | Math/MW |  |
| S010 | 2023 | Proceedings of the 32nd ACM In | Transformer-family; CNN; MLP; GNN; Diffu | Math/MW |  |
| S011 | 2021 | Proceedings of the 27th ACM SI | Transformer-family; RNN-family; CNN; MLP | Vision; OOD-CV; NLP-OOD | 10 |
| S012 | 2023 | ACM:F2 | Transformer-family; RNN-family; CNN; MLP | NLP-OOD |  |
| S013 | 2026 | Proceedings of the 13th ACM In | Transformer-family; RNN-family; CNN; GNN | Math/MW; NLU-bench; Vision | 3 |
| S014 | 2022 | ACM:F2 | RNN-family | Math/MW | 10 |
| S015 | 2025 | ACM:F2 | Transformer-family; RNN-family; CNN; MLP | COGS; Math/MW; Vision; NLP-OOD |  |
| S016 | 2026 | Proceedings of the 2025 15th I | Transformer-family; CNN; MLP; GNN; RL-ag | Math/MW |  |
| S017 | 2025 | ACM:F2 | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision; Robotics/RL; Tabular |  |
| S018 | 2025 | Proceedings of the 2025 CHI Co | Transformer-family; CNN; GNN; Diffusion | COGS; Math/MW; Vision; OOD-CV; NLP-OOD |  |
| S019 | 2023 | Proceedings of the 31st ACM In | Transformer-family; CNN | Vision |  |
| S020 | 2020 | ACM:F2 | Transformer-family; RNN-family; CNN; MLP | OOD-CV |  |
| S021 | 2021 | Proceedings of the 30th ACM In | Transformer-family; RNN-family; CNN; MLP | none-detected |  |
| S022 | 2025 | Proceedings of the 34th ACM In | Transformer-family; CNN; GNN; VAE/AE | Math/MW |  |
| S023 | 2024 | Proceedings of the 2024 on ACM | Transformer-family; RNN-family; CNN | Math/MW; Vision |  |
| S024 | 2025 | 2025 International Conference  | Transformer-family | Tabular |  |
| S025 | 2024 | ICC 2024 - IEEE International  | CNN; VAE/AE | none-detected |  |
| S026 | 2022 | 2022 IEEE/CVF Conference on Co | Transformer-family; CNN; MLP; VAE/AE | COGS; Math/MW; Vision; OOD-CV; NLP-OOD |  |
| S027 | 2026 | IEEE Transactions on Cognitive | Transformer-family; RNN-family; CNN; MLP | none-detected |  |
| S028 | 2025 | 2025 IEEE/CVF Conference on Co | Transformer-family; RNN-family; CNN; GNN | COGS; gSCAN; Vision | 3 |
| S029 | 2026 | ICASSP 2026 - 2026 IEEE Intern | Transformer-family; CNN; MLP; GNN | none-detected |  |
| S030 | 2025 | IEEE Transactions on Pattern A | Transformer-family; RNN-family; CNN; MLP | Vision; NLP-OOD |  |
| S031 | 2026 | IEEE Transactions on Artificia | Transformer-family; CNN; MLP; GNN | Vision | 3 |
| S032 | 2026 | IEEE Transactions on Pattern A | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; Math/MW | 16 |
| S033 | 2025 | IEEE Transactions on Knowledge | Transformer-family; RNN-family; CNN; MLP | SCAN; Math/MW; NLU-bench; Vision; OOD-CV |  |
| S034 | 2021 | 2021 IEEE/CVF International Co | Transformer-family; CNN; MLP; RL-agent;  | Vision |  |
| S035 | 2026 | IEEE Access | Transformer-family; RNN-family; CNN; MLP | NLP-OOD |  |
| S036 | 2025 | 2025 IEEE World AI IoT Congres | Transformer-family; CNN; VAE/AE; Diffusi | none-detected |  |
| S037 | 2026 | 2026 38th Chinese Control and  | Transformer-family; CNN; MLP; VAE/AE; Di | Vision |  |
| S038 | 2024 | 2024 IEEE/CVF Conference on Co | Transformer-family; CNN; GNN | Vision; OOD-CV |  |
| S039 | 2021 | 2021 IEEE/CVF Conference on Co | Transformer-family; RNN-family; MLP; GNN | CLOSURE; Vision; NLP-OOD |  |
| S040 | 2023 | IEEE Transactions on Pattern A | Transformer-family; CNN; GNN | NLU-bench; Vision; NLP-OOD |  |
| S041 | 2025 | IEEE Transactions on Computati | Transformer-family; RNN-family; CNN; GNN | Math/MW |  |
| S042 | 2022 | Neural Networks | CNN; MLP; VAE/AE | Vision; NLP-OOD |  |
| S043 | 2025 | Knowledge-Based Systems | Transformer-family; CNN; MLP; GNN; VAE/A | none-detected | 10 |
| S044 | 2025 | Agriculture (Switzerland) | Transformer-family; RNN-family; CNN; MLP | COGS; Vision |  |
| S045 | 2024 | Expert Systems with Applicatio | Transformer-family; CNN; GNN | Math/MW |  |
| S046 | 2026 | WWW 2026 - Proceedings of the  | Transformer-family; CNN; MLP; GNN; VAE/A | Vision; OOD-CV |  |
| S047 | 2026 | Proceedings of the ACM SIGKDD  | Transformer-family; CNN; MLP; GNN; RL-ag | Math/MW |  |
| S048 | 2025 | Limnology and Oceanography: Me | Transformer-family; CNN; GNN | Math/MW; Vision; NLP-OOD |  |
| S049 | 2026 | Engineering Applications of Ar | Transformer-family; RNN-family; CNN; MLP | Math/MW |  |
| S050 | 2025 | Frontiers of Computer Science | Transformer-family; CNN | COGS; Math/MW; NLU-bench; Vision; NLP-OO |  |
| S051 | 2022 | Findings of the Association fo | Transformer-family; RNN-family; GNN | SCAN; NLP-OOD |  |
| S052 | 2025 | International Journal of Intel | Transformer-family; RNN-family; CNN; MLP | SCAN; OOD-CV |  |
| S053 | 2025 | Proceedings of the ACM SIGKDD  | Transformer-family; CNN; MLP; GNN; RL-ag | Math/MW | 5 |
| S054 | 2026 | Proceedings of the AAAI Confer | Transformer-family; MLP | NLP-OOD |  |
| S055 | 2021 | NAACL-HLT 2021 - 2021 Conferen | Transformer-family; RNN-family | CFQ; Math/MW |  |
| S056 | 2024 | ICMR 2024 - Proceedings of the | Transformer-family; RNN-family; CNN; MLP | COGS; Vision |  |
| S057 | 2024 | ACM Transactions on Knowledge  | Transformer-family; MLP; GNN; RL-agent;  | Math/MW; Vision; OOD-CV |  |
| S058 | 2023 | Proceedings of the 37th AAAI C | Transformer-family; CNN; VAE/AE | Math/MW; Vision; OOD-CV |  |
| S059 | 2025 | Lecture Notes in Computer Scie | Transformer-family; CNN | Math/MW; Vision | 3 |
| S060 | 2025 | Proceedings of the ACM SIGKDD  | Transformer-family; CNN; MLP | COGS; Vision; OOD-CV |  |
| S061 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; PCFG; Math/MW; Vision | 5 |
| S062 | 2025 | arXiv:benchmark | Transformer-family; RNN-family; MLP; RL- | COGS; SLOG |  |
| S063 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP | COGS; SLOG; Math/MW; Vision |  |
| S064 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; VAE/AE | SCAN; CFQ; Math/MW |  |
| S065 | 2024 | arXiv:benchmark | Transformer-family; RNN-family; MLP; RL- | SCAN; COGS; CFQ; PCFG; Math/MW | 2 |
| S066 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; CFQ; CLOSURE; NLU-bench; Vision |  |
| S067 | 2025 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW |  |
| S068 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; RL-agent | SCAN; CLOSURE; Vision |  |
| S069 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW; NLU-bench | 3 |
| S070 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW |  |
| S071 | 2022 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; CFQ |  |
| S072 | 2026 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; gSCAN; Math/MW | 5 |
| S073 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; gSCAN; CLOSURE; Vision |  |
| S074 | 2020 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; CFQ; Math/MW; Vision |  |
| S075 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN | CFQ; Tabular |  |
| S076 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; PCFG; CLOSURE | 5 |
| S077 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN | SCAN; gSCAN; Math/MW; Vision |  |
| S078 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ |  |
| S079 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; RL-agent | CFQ |  |
| S080 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; VAE/AE | SCAN; CFQ |  |
| S081 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; Math/MW; Vision | 1 |
| S082 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; Math/MW; NLU-bench |  |
| S083 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; Math/MW | 5 |
| S084 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; CFQ; PCFG; Math/MW |  |
| S085 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | COGS; Math/MW | 3 |
| S086 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | COGS; gSCAN; CLOSURE; Math/MW; Vision |  |
| S087 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ | 5 |
| S088 | 2022 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS |  |
| S089 | 2019 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; CFQ; Math/MW; Vision |  |
| S090 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; gSCAN; Math/MW; Vision; NLP- |  |
| S091 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; MLP; VAE | COGS; Math/MW | 10 |
| S092 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; RL- | SCAN; CLOSURE; Vision | 5 |
| S093 | 2019 | arXiv:benchmark | Transformer-family; RNN-family; CNN | SCAN; COGS; Vision |  |
| S094 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ |  |
| S095 | 2025 | arXiv:benchmark | Transformer-family; RNN-family; GNN; RL- | SCAN | 4 |
| S096 | 2019 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; Vision | 25 |
| S097 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; MLP; GNN | SCAN; COGS; CLOSURE; Math/MW; Vision |  |
| S098 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; GNN; VAE | SCAN; COGS; CLOSURE; Math/MW; Vision |  |
| S099 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; Math/MW |  |
| S100 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; GNN | SCAN; COGS; Math/MW; Tabular |  |
| S101 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; NLU-bench; Vision |  |
| S102 | 2019 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; Math/MW | 5 |
| S103 | 2022 | arXiv:benchmark | Transformer-family; RNN-family; MLP; GNN | Math/MW |  |
| S104 | 2023 | arXiv:benchmark | Transformer-family; RNN-family; VAE/AE | CLOSURE; Math/MW; Vision |  |
| S105 | 2021 | arXiv:benchmark | Transformer-family; RNN-family | COGS; CFQ; CLOSURE; Math/MW; Vision | 10 |
| S106 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; Math/MW; NLP-OOD | 20 |
| S107 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; CNN; GNN | SCAN; gSCAN; CLOSURE; Math/MW; Vision | 3 |
| S108 | 2022 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; CLOSURE; Math/MW; NLU-b |  |
| S109 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN; RL- | SCAN; gSCAN; CLOSURE; Vision | 3 |
| S110 | 2019 | arXiv:benchmark | Transformer-family; RNN-family | SCAN |  |
| S111 | 2021 | arXiv:benchmark | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; gSCAN | 5 |
| S112 | 2023 | arXiv:benchmark | Transformer-family; RNN-family | SCAN; COGS; CFQ; Math/MW |  |
| S113 | 2026 | arXiv:benchmark | Transformer-family; RNN-family; MLP | SCAN; Math/MW | 3 |
| S114 | 2026 | arXiv:benchmark | Transformer-family; RNN-family; GNN; RL- | SCAN; CLOSURE; Math/MW; NLP-OOD |  |
| S115 | 2020 | arXiv:benchmark | Transformer-family; RNN-family; CNN | SCAN |  |
| S116 | 2025 | arXiv:broad | Transformer-family; CNN; MLP; Diffusion | Math/MW; Vision |  |
| S117 | 2024 | arXiv:broad | Transformer-family; MLP | Math/MW; Vision; OOD-CV | 6 |
| S118 | 2025 | arXiv:broad | Transformer-family; CNN | SCAN; NLU-bench; Vision; OOD-CV |  |
| S119 | 2026 | arXiv:broad | Transformer-family; CNN; MLP; Diffusion | CoCoGen; Math/MW; Vision | 3 |
| S120 | 2024 | arXiv:broad | unknown | Math/MW; OOD-CV |  |
| S121 | 2025 | arXiv:broad | Transformer-family; CNN; MLP; Diffusion | Math/MW; Vision | 10 |
| S122 | 2022 | arXiv:broad | Transformer-family; GNN | NLU-bench | 3 |
| S123 | 2022 | arXiv:broad | Transformer-family; CNN; GNN; VAE/AE | COGS; Vision; OOD-CV |  |
| S124 | 2022 | arXiv:broad | Transformer-family; CNN; MLP; GNN; RL-ag | Math/MW |  |
| S125 | 2021 | arXiv:broad | Transformer-family; CNN; MLP; VAE/AE | SCAN; Math/MW; Vision; OOD-CV | 10 |
| S126 | 2024 | arXiv:broad | Transformer-family; RNN-family; CNN; VAE | Math/MW; NLU-bench; Vision; OOD-CV | 6 |
| S127 | 2021 | arXiv:broad | CNN; MLP; GNN; VAE/AE | Vision; OOD-CV | 4 |
| S128 | 2023 | arXiv:broad | Transformer-family; CNN; RL-agent; VAE/A | Math/MW; Vision; NLP-OOD |  |
| S129 | 2024 | arXiv:broad | Transformer-family | Math/MW; Vision; NLP-OOD | 10 |
| S130 | 2023 | arXiv:broad | Transformer-family; RL-agent | none-detected |  |
| S131 | 2026 | arXiv:broad | Transformer-family; RNN-family; CNN; MLP | Math/MW; NLU-bench; Vision |  |
| S132 | 2026 | arXiv:broad | Transformer-family; MLP; VAE/AE; Diffusi | CLOSURE |  |
| S133 | 2026 | arXiv:broad | Transformer-family; RNN-family; CNN; Dif | COGS; NLP-OOD |  |
| S134 | 2025 | arXiv:broad | Transformer-family; GNN; RL-agent; VAE/A | Math/MW; NLP-OOD | 16 |
| S135 | 2025 | arXiv:broad | Transformer-family; CNN; MLP; GNN; RL-ag | COGS; Math/MW; Vision; NLP-OOD; Robotics | 10 |
| S136 | 2026 | arXiv:broad | Transformer-family; GNN | Math/MW |  |
| S137 | 2025 | arXiv:broad | Transformer-family; RL-agent | none-detected |  |
| S138 | 2025 | arXiv:broad | RNN-family; MLP | SCAN; PCFG | 5 |
| S139 | 2026 | arXiv:broad | Transformer-family; RL-agent | SCAN; Math/MW; OOD-CV | 10 |
| S140 | 2023 | arXiv:broad | RNN-family; CNN | none-detected |  |
| S141 | 2024 | arXiv:broad | Transformer-family; RNN-family; CNN; MLP | SCAN; Vision |  |
| S142 | 2026 | arXiv:broad | Transformer-family; CNN; MLP; GNN; VAE/A | Math/MW |  |
| S143 | 2025 | arXiv:broad | CNN; MLP; GNN | none-detected |  |
| S144 | 2026 | arXiv:broad | Transformer-family; RL-agent | SCAN; CLOSURE; Math/MW |  |
| S145 | 2026 | arXiv:broad | Transformer-family; RNN-family; CNN; GNN | Math/MW |  |
| S146 | 2026 | arXiv:broad | Transformer-family; RNN-family; GNN | SCAN; Math/MW; Vision |  |
| S147 | 2025 | arXiv:broad | Transformer-family; GNN | Math/MW; Vision |  |
| S148 | 2026 | arXiv:broad | Transformer-family; MLP; GNN; RL-agent;  | CLOSURE; Math/MW; Tabular |  |
| S149 | 2025 | arXiv:broad | Transformer-family; RL-agent; VAE/AE | Math/MW; NLP-OOD |  |
| S150 | 2020 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; Vision | 5 |
| S151 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | COGS; CFQ; Math/MW; Vision | 10 |
| S152 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | Math/MW | 5 |
| S153 | 2020 | arXiv:primary | Transformer-family; RNN-family | SCAN; gSCAN; CLOSURE; Vision; NLP-OOD |  |
| S154 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN; RL- | SCAN; COGS; Math/MW |  |
| S155 | 2025 | arXiv:primary | Transformer-family; RL-agent; VAE/AE | Vision |  |
| S156 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | CLOSURE; Math/MW; Vision | 3 |
| S157 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; Math/MW |  |
| S158 | 2021 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ | 5 |
| S159 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Vision; NLP-OOD |  |
| S160 | 2022 | arXiv:primary | Transformer-family; RNN-family; RL-agent | COGS; CLOSURE; Math/MW; Vision; NLP-OOD | 13 |
| S161 | 2021 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; CFQ; Math/MW |  |
| S162 | 2019 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | Math/MW; Vision |  |
| S163 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ; Math/MW |  |
| S164 | 2023 | arXiv:primary | Transformer-family; CNN; RL-agent; VAE/A | Math/MW | 10 |
| S165 | 2024 | arXiv:primary | Transformer-family; RNN-family; RL-agent | Math/MW |  |
| S166 | 2021 | arXiv:primary | Transformer-family; RNN-family; MLP; VAE | COGS; CFQ; Math/MW | 3 |
| S167 | 2021 | arXiv:primary | Transformer-family; RNN-family; VAE/AE | none-detected |  |
| S168 | 2024 | arXiv:primary | Transformer-family; MLP | Vision |  |
| S169 | 2024 | arXiv:primary | Transformer-family; RNN-family; MLP; VAE | COGS; CLOSURE; Math/MW | 5 |
| S170 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN | SCAN; CFQ; Math/MW; Vision |  |
| S171 | 2024 | arXiv:primary | Transformer-family; RNN-family; GNN | SCAN; COGS; NLP-OOD |  |
| S172 | 2024 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS; Math/MW |  |
| S173 | 2024 | arXiv:primary | Transformer-family; RNN-family | SCAN; COGS; CFQ; PCFG; Math/MW | 1 |
| S174 | 2022 | arXiv:primary | Transformer-family; RNN-family | SCAN; COGS; CLOSURE; Vision |  |
| S175 | 2026 | arXiv:primary | Transformer-family; RNN-family; VAE/AE;  | Math/MW; Vision; NLP-OOD |  |
| S176 | 2025 | arXiv:primary | Transformer-family; CNN; VAE/AE; Diffusi | Vision |  |
| S177 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision |  |
| S178 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; gSCAN; Math/MW |  |
| S179 | 2022 | arXiv:primary | Transformer-family; RNN-family | none-detected | 3 |
| S180 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN | SCAN; CFQ; PCFG; Math/MW |  |
| S181 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | Math/MW; Vision | 5 |
| S182 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | Math/MW; NLP-OOD; Tabular |  |
| S183 | 2026 | arXiv:primary | Transformer-family; RNN-family; MLP; RL- | Vision; NLP-OOD |  |
| S184 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; gSCAN; PCFG; CLOSURE; M |  |
| S185 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | NLP-OOD |  |
| S186 | 2024 | arXiv:primary | Transformer-family; CNN | Math/MW; NLU-bench |  |
| S187 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; CFQ |  |
| S188 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision |  |
| S189 | 2025 | arXiv:primary | Transformer-family; CNN; GNN; VAE/AE; Di | Math/MW; Vision | 10 |
| S190 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; Math/MW; NLP-OOD |  |
| S191 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN; Dif | SCAN; COGS; Vision; NLP-OOD |  |
| S192 | 2020 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; CLOSURE; Math/MW | 3 |
| S193 | 2024 | arXiv:primary | Transformer-family; CNN; GNN; VAE/AE | Math/MW; Vision; OOD-CV; NLP-OOD | 3 |
| S194 | 2024 | arXiv:primary | Transformer-family; RNN-family | COGS; NLP-OOD |  |
| S195 | 2022 | arXiv:primary | Transformer-family; RNN-family | COGS; CFQ |  |
| S196 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ |  |
| S197 | 2021 | arXiv:primary | Transformer-family; RNN-family | SCAN; COGS; CFQ; PCFG; Math/MW | 3 |
| S198 | 2019 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | COGS; Vision |  |
| S199 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN | COGS; gSCAN |  |
| S200 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN | Vision; NLP-OOD |  |
| S201 | 2025 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS; PCFG; SLOG; NLP-OOD |  |
| S202 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; gSCAN; Math/MW; Vision | 5 |
| S203 | 2024 | arXiv:primary | Transformer-family; CNN | gSCAN; Math/MW; NLU-bench; Vision |  |
| S204 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision; Tabular |  |
| S205 | 2023 | arXiv:primary | Transformer-family; CNN | Vision | 10 |
| S206 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS | 5 |
| S207 | 2024 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | SCAN; COGS; SLOG; Math/MW | 5 |
| S208 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | SCAN; Math/MW |  |
| S209 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; PCFG; Math/MW |  |
| S210 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | CLOSURE; Vision; NLP-OOD |  |
| S211 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; Dif | COGS; Math/MW; Vision; NLP-OOD |  |
| S212 | 2024 | arXiv:primary | Transformer-family; RNN-family; GNN | COGS; Math/MW |  |
| S213 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; PCFG; CLOSURE; Math/MW; | 5 |
| S214 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; Math/MW |  |
| S215 | 2021 | arXiv:primary | Transformer-family; RNN-family | COGS; CFQ; Tabular | 5 |
| S216 | 2025 | arXiv:primary | Transformer-family; RNN-family; GNN; RL- | SLOG; Math/MW | 192 |
| S217 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | COGS; Math/MW |  |
| S218 | 2026 | arXiv:primary | Transformer-family; RNN-family; MLP; RL- | Math/MW |  |
| S219 | 2022 | arXiv:primary | Transformer-family; RNN-family | COGS; Math/MW; Vision; NLP-OOD |  |
| S220 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision; NLP-OOD |  |
| S221 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | SCAN; COGS; CLOSURE; Math/MW; Vision |  |
| S222 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | none-detected |  |
| S223 | 2025 | arXiv:primary | Transformer-family; CNN; MLP; VAE/AE; Di | Math/MW; Vision; NLP-OOD |  |
| S224 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | COGS; Math/MW; Tabular |  |
| S225 | 2025 | arXiv:primary | Transformer-family; RNN-family; MLP; Dif | Math/MW; NLP-OOD |  |
| S226 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; CLOSURE; Math/MW; Visio | 3 |
| S227 | 2023 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; CFQ | 6 |
| S228 | 2020 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; gSCAN; Math/MW; Vision; NLP-OOD |  |
| S229 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision; NLP-OOD |  |
| S230 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; RL- | Vision; Robotics/RL | 50 |
| S231 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | CFQ; CLOSURE; Vision; NLP-OOD |  |
| S232 | 2025 | arXiv:primary | Transformer-family; Diffusion | Vision |  |
| S233 | 2026 | arXiv:primary | Transformer-family; RL-agent | Math/MW; Vision; NLP-OOD |  |
| S234 | 2022 | arXiv:primary | Transformer-family | none-detected |  |
| S235 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | none-detected | 5 |
| S236 | 2022 | arXiv:primary | Transformer-family; RNN-family; CNN | CFQ; CLOSURE; Vision |  |
| S237 | 2024 | arXiv:primary | Transformer-family; MLP; GNN; Diffusion | NLU-bench |  |
| S238 | 2021 | arXiv:primary | RNN-family; CNN; MLP; RL-agent; VAE/AE | COGS; CLOSURE; Math/MW; Vision; NLP-OOD |  |
| S239 | 2026 | arXiv:primary | Transformer-family; GNN; RL-agent; VAE/A | CLOSURE; Math/MW |  |
| S240 | 2018 | arXiv:primary | Transformer-family; RNN-family; CNN | SCAN; Vision | 5 |
| S241 | 2025 | arXiv:primary | Transformer-family; VAE/AE; Diffusion | Vision |  |
| S242 | 2022 | arXiv:primary | Transformer-family; RL-agent | Math/MW; Tabular |  |
| S243 | 2025 | arXiv:primary | Transformer-family; RNN-family; MLP; RL- | SCAN; COGS; CFQ; CLOSURE; Math/MW; NLP-O | 25 |
| S244 | 2025 | arXiv:primary | Transformer-family; Diffusion | Math/MW; Vision; NLP-OOD |  |
| S245 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision |  |
| S246 | 2023 | arXiv:primary | Transformer-family; MLP | Math/MW; Vision |  |
| S247 | 2020 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; gSCAN; CLOSURE; Vision |  |
| S248 | 2020 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; CFQ; CLOSURE; Vision |  |
| S249 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; gSCAN; CLOSURE; Vision | 5 |
| S250 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN | COGS; CLOSURE; NLU-bench; Vision; NLP-OO |  |
| S251 | 2020 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; Math/MW |  |
| S252 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | SCAN; COGS; CFQ; gSCAN; Math/MW; Vision; |  |
| S253 | 2023 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | COGS; CLOSURE; Vision; NLP-OOD |  |
| S254 | 2026 | arXiv:primary | Transformer-family; GNN; VAE/AE; Diffusi | Vision |  |
| S255 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | PCFG; Math/MW | 5 |
| S256 | 2024 | arXiv:primary | Transformer-family; CNN | Vision |  |
| S257 | 2021 | arXiv:primary | Transformer-family; RNN-family; MLP | SCAN; COGS; CFQ; PCFG; CLOSURE; Math/MW; | 5 |
| S258 | 2025 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | gSCAN |  |
| S259 | 2021 | arXiv:primary | CNN; MLP; VAE/AE | Vision; NLP-OOD |  |
| S260 | 2019 | arXiv:primary | Transformer-family; RNN-family; GNN | Math/MW |  |
| S261 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CFQ; gSCAN; PCFG; CLOSURE; M | 5 |
| S262 | 2019 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; CLOSURE; Math/MW; Vision; Tabular | 10 |
| S263 | 2026 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | Math/MW |  |
| S264 | 2022 | arXiv:primary | Transformer-family; CNN; MLP | Vision; NLP-OOD | 10 |
| S265 | 2021 | arXiv:primary | Transformer-family; RNN-family; GNN | SCAN; COGS; CFQ; NLU-bench; NLP-OOD | 3 |
| S266 | 2021 | arXiv:primary | Transformer-family; RNN-family | SCAN |  |
| S267 | 2026 | arXiv:primary | Transformer-family; RNN-family; RL-agent | NLP-OOD |  |
| S268 | 2021 | arXiv:primary | Transformer-family; RNN-family; VAE/AE | Math/MW |  |
| S269 | 2025 | arXiv:primary | Transformer-family; RNN-family; GNN; RL- | none-detected | 20 |
| S270 | 2026 | arXiv:primary | RL-agent | Vision |  |
| S271 | 2021 | arXiv:primary | Transformer-family; RNN-family; CNN; MLP | SCAN; CLOSURE; Math/MW; Vision; NLP-OOD |  |
| S272 | 2025 | arXiv:primary | Transformer-family; RNN-family; RL-agent | Math/MW; NLP-OOD | 3 |
| S273 | 2022 | arXiv:primary | Transformer-family; RNN-family; MLP; GNN | Math/MW |  |
| S274 | 2023 | arXiv:primary | Transformer-family; CNN; RL-agent; VAE/A | Math/MW; Vision; OOD-CV; Tabular | 10 |
| S275 | 2026 | arXiv:primary | Transformer-family; CNN | SCAN; Vision; NLP-OOD | 4 |
| S276 | 2024 | arXiv:primary | Transformer-family; RNN-family; CNN; GNN | SCAN; COGS; CFQ; Math/MW |  |
| S277 | 2023 | arXiv:primary | Transformer-family; RL-agent; VAE/AE | none-detected | 10 |
| S278 | 2023 | arXiv:primary | Transformer-family; RNN-family; GNN | gSCAN; Vision | 5 |
| S279 | 2022 | arXiv:primary | MLP; GNN; VAE/AE | NLP-OOD; Tabular |  |
| S280 | 2026 | arXiv:safety | Transformer-family; MLP; GNN; RL-agent | none-detected | 3 |
| S281 | 2025 | arXiv:safety | Transformer-family; CNN; VAE/AE | Math/MW; Vision; NLP-OOD; Tabular |  |
| S282 | 2022 | ACM:F2 | Transformer-family; RNN-family; CNN; MLP | Math/MW; Vision | 10 |
| S283 | 2024 | Advances in Neural Information | Transformer-family; CNN; MLP; VAE/AE; Di | Vision |  |
| S284 | 2026 | Proceedings of Machine Learnin | Transformer-family; MLP; GNN; VAE/AE; Di | Math/MW |  |
| S285 | 2020 | Proceedings of the Annual Meet | Transformer-family; RNN-family; CNN; MLP | SCAN; COGS; CLOSURE; Vision | 25 |
| S286 | 2024 | Advances in Neural Information | Transformer-family; CNN; GNN | Math/MW; Vision; OOD-CV |  |
