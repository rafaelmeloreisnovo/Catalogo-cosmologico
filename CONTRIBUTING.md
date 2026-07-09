# Contributing to Catálogo Cosmológico

## Scope

Contributions should relate to:

- Astronomical observations (comets, minor planets, transient phenomena)
- MPC/JPL-compatible data formats (JSON, CSV following MPC schema)
- RAFAELIA symbolic interpretations of celestial events
- Data processing scripts (`scripts/`)
- Visualizations (`visual/`)

## Data Standards

All observational data must:

1. Follow MPC observation format (observatory code, date, RA/Dec, magnitude)
2. Be placed in `data/` with descriptive filenames (`comet_YYYY_XX_obs.csv`)
3. Include a header comment citing the source observatory and date range
4. Be accompanied by a doc note in `docs/` explaining the dataset

## Branch Naming

| Type | Pattern |
|---|---|
| New catalog entry | `feat/catalog-<designation>` |
| Data correction | `fix/data-<designation>` |
| Script | `feat/script-<name>` |
| Docs | `docs/<topic>` |

## Commit Convention

```
feat: add C/2026 A1 observation data from MPC
fix: correct perihelion date for 24P/Schaumasse
docs: add notes on RAFAELIA candidate methodology
data: update candidato_rafaelia_2025.json with new epoch
```

## Pull Request Checklist

- [ ] Data placed in `data/` with descriptive filename
- [ ] Source observatory and date cited in file header
- [ ] `README.md` catalog table updated
- [ ] `CHANGELOG.md` updated under `[Unreleased]`
- [ ] No personally identifiable information in data files
