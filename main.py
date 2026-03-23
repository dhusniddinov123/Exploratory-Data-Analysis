import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    return pd.read_csv("data/students.csv")


def show_basic_info(df):
    print(df.head())
    print(df.info())
    print(df.describe())


def correlation_analysis(df):
    print("\nStudy vs Score:")
    print(df[["study_hours", "score"]].corr())

    print("\nSleep vs Score:")
    print(df[["sleep_hours", "score"]].corr())

    print("\nAttendance vs Score:")
    print(df[["attendance", "score"]].corr())


def plot_relationship(x, y, x_label, y_label, title):
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def main():
    df = load_data()

    show_basic_info(df)
    correlation_analysis(df)

    plot_relationship(df["study_hours"], df["score"], "Study Hours", "Score", "Study vs Score")
    plot_relationship(df["sleep_hours"], df["score"], "Sleep Hours", "Score", "Sleep vs Score")
    plot_relationship(df["attendance"], df["score"], "Attendance", "Score", "Attendance vs Score")


if __name__ == "__main__":
    main()