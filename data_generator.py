import pandas as pd
import numpy as np
import random
from deltalake import write_deltalake

# Generate synthetic data
def generate_data(num_rows=400):
    departments = ["HR", "Finance", "Engineering", "Marketing", "Sales", "IT"]
    cities = ["New York", "San Francisco", "Chicago", "Los Angeles", "Seattle", "Boston"]
    job_titles = ["Manager", "Developer", "Analyst", "Designer", "Engineer", "Consultant"]
    data = {
        "id": range(1, num_rows + 1),
        "name": [f"Person_{i}" for i in range(1, num_rows + 1)],
        "age": np.random.randint(18, 65, size=num_rows),
        "salary": np.random.randint(30_000, 150_000, size=num_rows),
        "department": [random.choice(departments) for _ in range(num_rows)],
        "city": [random.choice(cities) for _ in range(num_rows)],
        "job_title": [random.choice(job_titles) for _ in range(num_rows)],
        "years_of_experience": np.random.randint(1, 20, size=num_rows),
        "performance_score": np.random.randint(1, 100, size=num_rows),
        "joining_date": pd.date_range(start="2010-01-01", periods=num_rows, freq="D"),
        "is_manager": np.random.choice([True, False], size=num_rows),
    }
    return pd.DataFrame(data)

# Save the dataset as a Delta Lake table
def save_to_delta_lake(df):
    delta_path = "delta_api/delta_tables/employee_data"  # Local path for Delta table
    write_deltalake(delta_path, df)
    print(f"Data saved to Delta Lake at: {delta_path}")

if __name__ == "__main__":
    # Generate synthetic data
    df = generate_data(num_rows=400)
    save_to_delta_lake(df)