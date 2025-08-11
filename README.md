# PDF Report Generator from CSV Data

## 📌 Overview

This Python project reads data from a CSV file, analyzes it, visualizes the results, and generates a PDF report that includes a chart and summary statistics.

---

## 📁 Project Structure

TASK 2/
│
├── data/
│ └── sample_data.csv
│
├── reports/
│ ├── mean_chart.png
│ └── report.pdf
│
├── utils/
│ ├── pdf_generator.py
│ └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Technologies Used

- **Python 3**
- **Libraries:**
  - `pandas` – for data analysis
  - `matplotlib` – for generating charts
  - `reportlab` – for creating PDF files

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
2. Run the Main File
bash
Copy
Edit
python main.py
3. Output
A chart image will be saved to: reports/mean_chart.png

A PDF report will be saved to: reports/report.pdf

📊 Sample Data
The sample CSV should contain numerical columns for meaningful analysis. Example format:

pgsql
Copy
Edit
Name,Maths,Science,English
Krish,75,88,90
Ravi,66,79,85
Anjali,80,90,92
✍️ Author
Your Lavish bhardwaj

✅ Status
✅ Completed and tested locally.

