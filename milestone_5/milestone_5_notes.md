
```bash
sudo apt install python3.10-venv
python3 -m venv .venv # Create a virtual environment
source ./venv/bin/activate
pip install -r requirements
```

- [X] Remove the following fields:
    - ObtainMethod
    - WeaponDescription
- [X] Add the following fields:
    - DamageType

```mermaid
---
title: Site Architecture Overview
---

flowchart LR
    user[User Browser]
    admin[Admin Browser]
    subgraph flask[Flask App]
        main[Main.py]
        data[Data.py]
    end
    subgraph db["Database (Docker)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"]
        sql[MySQL Database]
        phpmyadmin[PHPMyAdmin Console]
    end

    user <-.-> main
    main <-.-> data
    data <-.-> sql
    phpmyadmin <-.-> sql
    admin <-.-> phpmyadmin
```