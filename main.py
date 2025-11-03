
import pandas as pd


def main():
    data_path = "sample_data/students.csv"
    df = pd.read_csv(data_path)

    print("Student grade data:")
    print(df.to_string(index=False))

    # Show descriptive statistics for the grade distribution
    stats = df["grade"].describe()
    print("\nGrade statistics:")
    print(stats.to_string())


if __name__ == "__main__":
    main()
