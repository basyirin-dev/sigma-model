import json
import random


def format_for_kaggle(
    task_id: str,
    prompt: str,
    expected: str,
    track_name: str,
    condition: str,
    temperature: float = 0.0,
) -> dict:
    return {
        "id": f"{track_name}_{condition}_{task_id}",
        "prompt": prompt,
        "expected": expected,
        "temperature": temperature,
    }


def write_jsonl(path: str, records: list[dict]) -> None:
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print(f"  Wrote {len(records)} items -> {path}")


def generate_hptb_payload(train_data: list[dict], output_dir: str, n: int = 200) -> list[dict]:
    payload = []
    train_copy = list(train_data)
    random.Random(42).shuffle(train_copy)
    iid = train_copy[:n]
    for i, item in enumerate(iid):
        payload.append(format_for_kaggle(
            f"A_{i}",
            f"Translate: {item['source']}",
            item["target"], "H-PTB", "Cond_A"))
    return payload


def generate_hmcb_payload(ood: list[dict], id_ctrl: list[dict], output_dir: str) -> list[dict]:
    payload = []
    item_type_descriptions = [
        "applying a noun-phrase rule to novel agent-theme combinations",
        "applying a verb-phrase rule to unseen verb inflections",
        "applying a recursive embedding rule to three-clause structures",
        "applying a passivisation rule to held-out verbs",
        "applying a prepositional-phrase attachment rule to novel nouns",
    ]
    for i, desc in enumerate(item_type_descriptions):
        payload.append(format_for_kaggle(
            f"pred_{i}", f"Estimate accuracy (0-100): {desc}", "[0-100]",
            "H-MCB", "Stage1_Prediction", temperature=0.7))
    return payload


def generate_hafb_payload(
    train_items: list[dict], test_items: list[dict],
    output_dir: str, n: int = 200,
) -> list[dict]:
    payload = []
    test_copy = list(test_items)
    random.Random(42).shuffle(test_copy)
    for i, item in enumerate(test_copy[:n]):
        payload.append(format_for_kaggle(
            f"id_{i}", f"Execute: {item['commands']}", item["actions"],
            "H-AFB", "ID"))
    return payload


def generate_hdcb_payload(
    ood: list[dict], train: list[dict],
    output_dir: str, n: int = 200,
) -> list[dict]:
    payload = []
    rng = random.Random(77)
    rho_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    train_pool = [f"{t['source']} -> {t['target']}" for t in train[:n]]
    for i, item in enumerate(ood):
        for rho in rho_levels:
            rho_label = str(rho).replace(".", "p")
            n_examples = int(rho * 5)
            if n_examples == 0:
                prompt = f"Map: {item['source']}"
            else:
                context = " | ".join(rng.sample(train_pool, min(n_examples, len(train_pool))))
                prompt = f"Context: {context}\n\nMap: {item['source']}"
            payload.append(format_for_kaggle(
                f"rho{rho_label}_{i}", prompt, item["target"],
                "H-DCB", f"RAG_Rho{rho_label}"))
    return payload


def generate_hstb_payload(ood: list[dict], output_dir: str) -> list[dict]:
    payload = []
    schema_rule = (
        "Verbs become event predicates; "
        "nouns become entity variables linked by thematic roles."
    )
    for i, item in enumerate(ood):
        payload.append(format_for_kaggle(
            f"schema_{i}",
            f"Rule: '{schema_rule}'\nMap: {item['source']}",
            item["target"], "H-STB", "Cond_Schema"))
    return payload
