"""Axiomatic Formal Grammar and Homomorphic Denotational Semantics for H-Bar (Paper 02).

This module formalizes the Chomsky grammar G_hbar = (V_N, V_T, P, S) and its exact
homomorphic execution semantics [[ . ]]: L(G_hbar) -> A*, eliminating logical-form
parsing and variable-binding syntax artifacts (Wu et al. 2023 - ReCOGS).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class HBarGrammar:
    """Formal grammar definition and algebraic denotational execution mapping."""

    # Atomic Primitives (Actions / Directions)
    ACTIONS: ClassVar[list[str]] = ["jump", "run", "walk", "turn"]
    DIRECTIONS: ClassVar[list[str]] = ["left", "right", "around"]
    MODIFIERS: ClassVar[list[str]] = ["twice", "thrice", "opposite"]
    CONNECTORS: ClassVar[list[str]] = ["and", "after"]

    # Canonical Denotational Action Mappings
    ACTION_MAP: ClassVar[dict[str, str]] = {
        "jump": "JUMP",
        "run": "RUN",
        "walk": "WALK",
        "turn": "TURN",
    }
    DIR_MAP: ClassVar[dict[str, str]] = {
        "left": "LTURN",
        "right": "RTURN",
        "around": "AROUND",
    }

    @classmethod
    def get_full_vocabulary(cls) -> list[str]:
        """Return canonical 27-token vocabulary for H-Bar."""
        tokens = [
            "<pad>",
            "<sos>",
            "<eos>",
            "<unk>",
            # Actions
            "jump",
            "run",
            "walk",
            "turn",
            # Directions
            "left",
            "right",
            "around",
            # Modifiers
            "twice",
            "thrice",
            "opposite",
            # Connectors
            "and",
            "after",
            # Output Action Atoms
            "JUMP",
            "RUN",
            "WALK",
            "LTURN",
            "RTURN",
            "AROUND",
            # Structural markers
            "(",
            ")",
            "[",
            "]",
            "NONE",
        ]
        return tokens

    @classmethod
    def execute_primitive(cls, action: str, direction: str | None = None) -> list[str]:
        """Denotational evaluation of an atomic command [[ action direction ]]."""
        act_token = cls.ACTION_MAP.get(action, action.upper())
        if direction is None:
            return [act_token]

        if direction == "left":
            return ["LTURN", act_token] if action != "turn" else ["LTURN"]
        elif direction == "right":
            return ["RTURN", act_token] if action != "turn" else ["RTURN"]
        elif direction == "around":
            if action == "turn":
                return ["LTURN", "LTURN", "LTURN", "LTURN"]
            return ["LTURN", act_token, "LTURN", act_token, "LTURN", act_token, "LTURN", act_token]
        return [act_token]

    @classmethod
    def execute_command_string(cls, command: str) -> list[str]:
        """Evaluate a sequence of commands into a canonical action trace [[ C ]].

        Supports modifiers ('twice', 'thrice', 'opposite') and connectors ('and', 'after').
        """
        tokens = command.strip().split()
        if not tokens:
            return []

        # Handle binary connectors
        if "after" in tokens:
            idx = tokens.index("after")
            c1 = " ".join(tokens[:idx])
            c2 = " ".join(tokens[idx + 1 :])
            return cls.execute_command_string(c2) + cls.execute_command_string(c1)

        if "and" in tokens:
            idx = tokens.index("and")
            c1 = " ".join(tokens[:idx])
            c2 = " ".join(tokens[idx + 1 :])
            return cls.execute_command_string(c1) + cls.execute_command_string(c2)

        # Handle unary repetition modifiers
        if tokens[-1] == "twice":
            base_cmd = " ".join(tokens[:-1])
            base_res = cls.execute_command_string(base_cmd)
            return base_res + base_res

        if tokens[-1] == "thrice":
            base_cmd = " ".join(tokens[:-1])
            base_res = cls.execute_command_string(base_cmd)
            return base_res + base_res + base_res

        if tokens[0] == "opposite":
            direction = tokens[1] if len(tokens) > 1 else "left"
            opp_dir = "right" if direction == "left" else "left"
            rest = " ".join(tokens[2:]) if len(tokens) > 2 else ""
            cmd = f"{rest} {opp_dir}".strip() if rest else f"turn {opp_dir}"
            return cls.execute_command_string(cmd)

        # Parse base action + direction
        action = tokens[0]
        direction = tokens[1] if len(tokens) > 1 else None
        return cls.execute_primitive(action, direction)
