# 📊 Student Performance: Data Insights & Analysis

This project explores a dataset of student habits to identify which factors most significantly impact academic scores. Using **Python**, **Pandas**, and **Matplotlib**, the script performs exploratory data analysis, calculates correlations, and generates visualizations.

---

## 📈 Key Insights & Findings
Based on the analysis of the dataset, here are the main takeaways:

*   **🏆 Study Hours are King (Correlation: ~0.88)**  
    There is a **strong positive correlation** between study hours and scores. This suggests that for every additional hour studied, there is a predictable increase in the student's score.
*   **🏫 Attendance is a Minor Factor (Correlation: ~0.27)**  
    While being in class helps, the correlation is **weak**. This indicates that simply showing up isn't enough; focused study time is more important.
*   **😴 Sleep has No Significant Impact (Correlation: ~0.07)**  
    Surprisingly, in this specific dataset, sleep hours showed **almost zero correlation** with the final score.

---

## 🚀 Features
- **Exploratory Data Analysis (EDA):** Automatically generates summary statistics (`head`, `info`, `describe`).
- **Correlation Mapping:** Calculates the mathematical relationship between study, sleep, attendance, and scores.
- **Data Visualization:** Produces scatter plots to visually represent how different habits influence performance.

---

## 🛠️ Requirements & Installation
To run this project, you need to install the following Python libraries:

```bash
pip install pandas matplotlib
```

---

# 📂 Project Structure
- **main.py** - The primary analysis script.
- **data/students.csv** - The raw dataset containing study habits and scores.
