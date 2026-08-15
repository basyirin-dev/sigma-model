# Phase 05 — Grammar Induction Probe Tasks

**Deadline**: 10 Jan 2027
**Dependencies**: Phase 02 (model and dataset); overlapped with Phase 03
**Output**: Probe task results, H2 test, structural vs lexical accuracy comparison

---

### Task 5.1: Probe task architecture (`proteins/probes.py`)

- [ ] 5.1.1: Implement `NextDomainProbe(nn.Module)`:
  - Input: frozen PLM hidden states (last layer, mean-pooled over unmasked positions)
  - Classifier: `nn.Linear(d_model, vocab_size)` — predict next domain in architecture
  - Training: linear probe (only classifier weights trained, PLM frozen)
  - Loss: `CrossEntropyLoss(ignore_index=0)`
- [ ] 5.1.2: Implement `MaskedDomainProbe(nn.Module)`:
  - Input: frozen PLM hidden state at a masked position
  - Classifier: `nn.Linear(d_model, vocab_size)` — predict masked domain identity
  - Training: same as NextDomainProbe but on masked positions
  - Masking: random 15% of positions, same as BERT MLM objective
- [ ] 5.1.3: Implement `DomainAnalogyProbe(nn.Module)`:
  - Task: given A:B :: C:?, predict the missing domain (analogical reasoning over domain architectures)
  - Input: mean-pooled representation of A, B, C → predict D such that A:B :: C:D
  - Classifier: `nn.Linear(3 * d_model, vocab_size)` — takes concatenated representations
  - Data construction: find pairs (A,B) and (C,D) where A/B and C/D share similar domain relationships (same recombination pattern)
- [ ] 5.1.4: Implement `train_probe(probe, plm, train_loader, val_loader, epochs=20) -> dict`
  - Input: probe module, frozen PLM, data loaders
  - Returns: `{acc_train, acc_val, loss_history, epoch_trained}`
- [ ] 5.1.5: Implement `evaluate_probe_ood(probe, plm, id_loader, ood_loader) -> dict`
  - Returns: `{acc_id, acc_ood, deltaCG}` for both structural and lexical OOD splits
- [ ] 5.1.6: Write tests in `tests/test_proteins_probes.py`:
  - Test probe forward shapes
  - Test training loop converges on synthetic data (small random PLM + small vocab)
  - Test OOD evaluation on known-easy and known-hard splits

### Task 5.2: Structural vs lexical OOD split construction

- [ ] 5.2.1: Define **structural OOD** splits: domain combinations that violate known fold compatibility or domain neighbour preferences
  - Example: two domains from incompatible folds that rarely co-occur in nature
- [ ] 5.2.2: Define **lexical OOD** splits: domain combinations that are unseen but structurally plausible
  - Example: familiar domains combined in a novel but viable order
- [ ] 5.2.3: Implement `build_structural_lexical_splits(architectures, similarity_matrix, clan_map) -> dict`
  - Structural OOD: low fold compatibility score (phi < threshold)
  - Lexical OOD: unseen architecture but all domains from familiar families with high compatibility
  - ID: familiar architectures (seen during training)
- [ ] 5.2.4: Validate splits:
  - Structural OOD should be harder (lower probe accuracy) than lexical OOD for models that learned surface statistics
  - ΔCG should be larger for structural split than lexical split (if σ_A is low)

### Task 5.3: Probe training pipeline

- [ ] 5.3.1: Select trained PLMs from Phase 03 for probe evaluation:
  - 10 high-σ_A models (top quartile) — from each condition
  - 10 low-σ_A models (bottom quartile) — from each condition
  - 5 randomly selected mid-range models
  - Total: 75 models probed (15 per condition × 3 conditions / 3 split types)
- [ ] 5.3.2: For each model, train all 3 probes on the ID split:
  - Freeze PLM weights
  - Train probe for 20 epochs, early stopping on validation loss
  - Record: training curve, validation accuracy, convergence epoch
- [ ] 5.3.3: Evaluate each probe on structural OOD and lexical OOD splits:
  - Record: `acc_id`, `acc_ood_struct`, `acc_ood_lex`, `deltaCG_struct`, `deltaCG_lex`
- [ ] 5.3.4: Save all probe results to `results/pfam-grammar/probe_results.parquet`
  - Columns: model_id, condition, sigma_A, probe_type, acc_id, acc_ood_struct, acc_ood_lex, deltaCG_struct, deltaCG_lex

### Task 5.4: H2 hypothesis test

- [ ] 5.4.1: H2 primary test: paired t-test on structural vs lexical OOD accuracy
  - H0: μ(Acc_OOD_struct) — μ(Acc_OOD_lex) ≥ 0 (structural is not harder than lexical)
  - H1: μ(Acc_OOD_struct) — μ(Acc_OOD_lex) < 0 (structural is harder — models learned surface stats, not grammar)
  - Effect size threshold: > 10 percentage points difference
- [ ] 5.4.2: Stratified analysis: repeat H2 test per condition (familiar/new/cross-fold)
- [ ] 5.4.3: Per-probe-type analysis: does the effect differ for next-domain vs masked-domain vs analogy probes?
- [ ] 5.4.4: σ_A correlation: within high/low σ_A groups, does the structural-lexical gap differ?
  - Prediction: low σ_A models have larger structural-lexical gap (they rely on surface stats)
  - High σ_A models have smaller gap (they learned the grammar)
- [ ] 5.4.5: Output: `results/pfam-grammar/h2-test-results.json`

### Task 5.5: Analysis and visualisations

- [ ] 5.5.1: Generate Figure 4 (Grammar induction results):
  - Panel A: structural vs lexical OOD accuracy scatter (75 points, coloured by probe type)
  - Panel B: paired difference histogram (acc_ood_lex - acc_ood_struct)
  - Panel C: gap size as function of σ_A (3 probe types × 2 conditions = 6 subplots)
- [ ] 5.5.2: Generate supplementary table: per-model probe accuracies
- [ ] 5.5.3: Generate confusion matrices for worst-performing probes (what domains are confused?)
- [ ] 5.5.4: Qualitative analysis: do certain domain families systematically escape the σ-trap?
  - Rank families by prediction accuracy in OOD splits
  - Check if high-accuracy families share structural properties (e.g., all from same clan, all single-domain)

### Task 5.6: ICML-readiness assessment

- [ ] 5.6.1: If ICML is the target (Jan 2027 deadline), complete all probe evaluations by Jan 5
- [ ] 5.6.2: Write results section draft for ICML paper covering H1 + H2
- [ ] 5.6.3: Produce all supplementary tables and figures for ICML submission

---

**Phase 05 Exit Criteria**:
- [ ] `code/sigma/proteins/probes.py` implemented with 3 probe types
- [ ] Structural and lexical OOD splits validated
- [ ] 75 models probed, results in `results/pfam-grammar/probe_results.parquet`
- [ ] H2 tested and documented (significant or null)
- [ ] Figures 4 generated and saved to `paper-neurips/figures/`
- [ ] Claims C-041, C-042 updated with outcomes
