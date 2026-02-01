# Long-Term Stock Analysis Project

## 1. Introduction

### <u>A - Project vision</u>
The Long-Term Stock Analysis Project is a personal tool developed to automate fundamental investment research and remove emotional bias from the decision-making process.

Deeply inspired by Raphaël Carteni’s book, "La Magie des Dividendes", the application implements a strict Dividend Growth Investing (DGI) methodology by analyzing balance sheet safety, payout sustainability, and historical growth trends.

By centralizing key financial metrics and automated scoring into a single dashboard, this project aims to efficiently identify high-quality companies capable of delivering sustainable compound interest over the long term.

### <u>B - Strategy Focus (DGI)</u>
This project is specifically tailored for the **DGI strategy**. It doesn't just look at current prices; it analyzes the sustainability and growth potential of dividends by examining:
- **Profitability & Safety**: Evaluation of ROE, ROA, and Interest Coverage.
- **Dividend Sustainability**: Deep dive into Payout Ratios (Earnings and FCF based).
- **Historical Trends**: 5-year analysis of Revenue, Net Income, and Cash Flow.

---

## 2. Live Demo
The application is deployed and accessible at:  
**[https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)**

---

## 3. Work on the project
In order to launch the project locally, run the following commands:

```shell
pip install -r requirements.txt
streamlit run app.py
```

---

## 4. Project Architecture

```text
.
├── config/
│   └── settings.py           # Application configurations
├── data/
│   └── cac40.csv             # Data with stock list
├── function/
│   ├── domain/               # Business logic & Financial formulas
│   │   ├── metrics.py        # Raw data processing (Revenue, Net Income)
│   │   ├── ratios.py         # Financial ratio calculations (PER, ROE)
│   │   └── stock.py          # Stock object logic
│   └── services/             # External communications
│       ├── fetch.py          # Data retrieval logic
│       └── finance.py        # Financial API wrappers
├── page/                     # Streamlit view layouts
│   ├── _explaination.py      # Methodology documentation page
│   ├── _stock_analysis.py    # Main analysis dashboard
│   └── _stock_info.py        # General company information
├── visual/                   # Reusable UI components
│   ├── info_table.py         # Company info display
│   ├── metric_table.py       # Financial tables (Ratios & Metrics)
│   ├── news_section.py       # Market news integration
│   └── price_chart.py        # Interactive stock charts
├── app.py                    # Main entry point (Streamlit)
├── LICENSE                   # MIT License file
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

---

## 5. Key Features
- Automated fundamental analysis dashboard (Streamlit)
- Dividend Growth Investing (DGI) scoring methodology
- Financial ratios & metrics computation (ROE, ROA, PER, payout ratios, etc.)
- Historical trend analysis on key fundamentals (5-year window)
- Interactive stock price charts
- Market news integration

---

## 6. Dependencies
Main dependencies include (see `requirements.txt` for the full list):
- `streamlit`
- `pandas`
- `numpy`
- `yfinance` (or equivalent data provider)
- `plotly` (or equivalent charting library)
- `requests`

---

## 7. Versioning

| Version | Date           | Status |
| :---    | :---           | :---   |
| **v1.0** | February 2026 | <span style="color: green;">Active</span> |

> *Note: This project is under active development. Upcoming features are subject to change based on personal research priorities.*

---

## License
This project is licensed under the following [LICENSE](LICENSE).
