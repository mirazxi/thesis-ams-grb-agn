# thesis-ams-grb-agn

Code + analysis for thesis figures/tables (AMS-02 / GRB / AGN).

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt



### requirements.txt (auto-generate from your current env)
If your current env is the `thesis` venv you showed (`/home/david/envs/thesis/bin/python`), activate it and freeze:
```bash
source ~/envs/thesis/bin/activate
pip freeze > requirements.txt

cat > LICENSE <<'EOF'
MIT License

Copyright (c) 2026 Miraz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
