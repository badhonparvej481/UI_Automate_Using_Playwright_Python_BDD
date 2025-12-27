UI_Automate_Using_Playwright_Python_BDD/
│
├── features/ # Behave feature files
│ ├── login.feature
│ ├── invalid_login.feature # Optional future test
│ ├── logout.feature # Optional future test
│ ├── steps/ # Step definitions
│ │ └── login_steps.py
│ │ └── logout_steps.py # Optional
│ └── environment.py # Hooks (before_all, after_all)
│
├── pages/ # Page Objects
│ ├── login_page.py
│ ├── dashboard_page.py # Optional
│ └── base_page.py # Optional common methods
│
├── conftest.py # Optional for pytest integration
├── requirements.txt # Python packages
├── pytest.ini # Optional if pytest integration needed
└── README.md
