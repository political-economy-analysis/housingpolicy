# Codebook: Affordability

Each bill is coded on a three-point scale for its effect on affordability (the cost of living, such as housing, health care, food, energy, childcare, and consumer prices).

| Code | Label | Definition |
|------|-------|------------|
| **1** | Focused on affordability | The bill's main purpose is to make things more affordable, for example by lowering costs, expanding supply, adding subsidies or credits, or capping prices or fees. |
| **0** | Irrelevant | The bill has no meaningful effect on affordability. |
| **-1** | Makes affordability worse | The bill would raise costs or reduce supply, for example through new taxes, tariffs, fees, restrictions, or cuts to assistance. |

## Coding rules

- Code the bill's main purpose and likely direct effect, not its title or its sponsors' stated intent.
- If a bill has both positive and negative effects, code the dominant one. If they are roughly equal, code **0**.
- Do not code **1** for bills that only mention affordability in passing.
- Do not infer indirect or speculative effects. If the text does not clearly affect costs or supply, code **0**.
- Commemorative, naming, procedural, and technical bills are **0**.
