import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Fetch data from Django API
def fetch_employee_data():
    response = requests.get("http://127.0.0.1:8000/api/employee-data/")
    if response.status_code == 200:
        return pd.DataFrame(response.json()["data"])
    else:
        st.error("Failed to fetch data from the API")
        return pd.DataFrame()

# Add new employee data via Django API
def add_employee_data(new_data):
    response = requests.post("http://127.0.0.1:8000/api/employee-data/", json=new_data)
    if response.status_code == 201:
        st.success("Employee data added successfully!")
    else:
        st.error(f"Failed to add employee data: {response.json()}")

# Streamlit app
st.title("Employee Data Visualizations")

# Fetch data
df = fetch_employee_data()


# Add Employee Form
st.header("Add New Employee")
with st.form("employee_form"):
    st.write("Fill in the details below to add a new employee:")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=65)
    salary = st.number_input("Salary", min_value=30000, max_value=150000)
    department = st.selectbox("Department", ["HR", "Finance", "Engineering", "Marketing", "Sales", "IT"])
    city = st.selectbox("City", ["New York", "San Francisco", "Chicago", "Los Angeles", "Seattle", "Boston"])
    job_title = st.selectbox("Job Title", ["Manager", "Developer", "Analyst", "Designer", "Engineer", "Consultant"])
    years_of_experience = st.number_input("Years of Experience", min_value=1, max_value=20)
    performance_score = st.number_input("Performance Score", min_value=1, max_value=100)
    joining_date = st.date_input("Joining Date")
    is_manager = st.checkbox("Is Manager?")

    # Submit button
    submitted = st.form_submit_button("Add Employee")
    if submitted:
        new_employee = {
            "name": name,
            "age": age,
            "salary": salary,
            "department": department,
            "city": city,
            "job_title": job_title,
            "years_of_experience": years_of_experience,
            "performance_score": performance_score,
            "joining_date": joining_date.isoformat(),  # Ensure the date is in YYYY-MM-DD format
            "is_manager": is_manager,
        }
        add_employee_data(new_employee)

# Visualization 1: Age Distribution
st.header("1. Age Distribution")
fig1 = px.histogram(df, x="age", nbins=20, title="Age Distribution")
st.plotly_chart(fig1)

# Visualization 2: Salary Distribution
st.header("2. Salary Distribution")
fig2 = px.histogram(df, x="salary", nbins=20, title="Salary Distribution")
st.plotly_chart(fig2)

# Visualization 3: Department-wise Employee Count
st.header("3. Department-wise Employee Count")
dept_count = df["department"].value_counts().reset_index()
dept_count.columns = ["Department", "Count"]
fig3 = px.bar(dept_count, x="Department", y="Count", title="Department-wise Employee Count")
st.plotly_chart(fig3)

# Visualization 4: Age vs Salary Scatter Plot
st.header("4. Age vs Salary Scatter Plot")
fig4 = px.scatter(df, x="age", y="salary", color="department", title="Age vs Salary")
st.plotly_chart(fig4)

# Visualization 5: Average Salary by Department
st.header("5. Average Salary by Department")
avg_salary = df.groupby("department")["salary"].mean().reset_index()
fig5 = px.bar(avg_salary, x="department", y="salary", title="Average Salary by Department")
st.plotly_chart(fig5)

# Visualization 6: Salary Distribution by Department
st.header("6. Salary Distribution by Department")
fig6 = px.box(df, x="department", y="salary", title="Salary Distribution by Department")
st.plotly_chart(fig6)

# Visualization 7: Age Distribution by Department
st.header("7. Age Distribution by Department")
fig7 = px.box(df, x="department", y="age", title="Age Distribution by Department")
st.plotly_chart(fig7)

# Visualization 8: Correlation Heatmap
st.header("8. Correlation Heatmap")
corr = df[["age", "salary", "years_of_experience", "performance_score"]].corr()
fig8 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
st.plotly_chart(fig8)

# Visualization 9: Top 10 Highest Paid Employees
st.header("9. Top 10 Highest Paid Employees")
top_10 = df.nlargest(10, "salary")
fig9 = px.bar(top_10, x="name", y="salary", title="Top 10 Highest Paid Employees")
st.plotly_chart(fig9)

# Visualization 10: Performance Score Distribution
st.header("10. Performance Score Distribution")
fig10 = px.histogram(df, x="performance_score", nbins=20, title="Performance Score Distribution")
st.plotly_chart(fig10)