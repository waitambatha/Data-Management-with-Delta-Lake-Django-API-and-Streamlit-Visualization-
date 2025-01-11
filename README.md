
# Delta Lake with Django API and Streamlit Visualization

This project demonstrates how to use **Delta Lake** as a standalone data storage solution, **Django** for building a RESTful API, and **Streamlit** for interactive data visualization. The application allows users to:
1. **View** employee data stored in a Delta table.
2. **Add** new employee data using a user-friendly form.
3. **Visualize** the data using interactive charts and graphs.

---

## **Project Flow Diagram**
Below is a diagram illustrating the flow of data in the project:



---

## **How to Run the Project**

### **1. Install Dependencies**
Install the required Python packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### **2. Generate the Dataset**
Run the `data_generator.py` script to create the Delta table:
```bash
python data_generator.py
```

### **3. Run the Django API**
Navigate to the `delta_api` folder and start the Django server:
```bash
cd delta_api
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/employee-data/`.

### **4. Run the Streamlit App**
Navigate to the `streamlit_app` folder and start the Streamlit app:
```bash
cd ../streamlit_app
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

---

## **Features**
- **View Employee Data**: Fetch and display employee data from the Delta table.
- **Add Employee Data**: Use a form to add new employee data to the Delta table.
- **Interactive Visualizations**: Explore the data through 10+ interactive charts.

---

## **Technologies Used**
- **Delta Lake**: For scalable and efficient data storage.
- **Django**: For building the RESTful API.
- **Streamlit**: For interactive data visualization.
- **Pandas**: For data manipulation.
- **Plotly**: For creating visualizations.

---

## **Project Flow Diagram**
Below is a diagram illustrating the flow of data in the project:

![Project Flow Diagram]

---

.
```

---

## **Project Flow Diagram** 

+-------------------+       +-------------------+       +-------------------+
| Data Generator     |      | Django API        |       | Streamlit App     |
| (data_generator.py)| ---> | (delta_api/)      | <--->| (streamlit_app/)   |
+-------------------+       +-------------------+       +-------------------+
        |                           |                           |
        v                           v                           v
+-------------------+       +-------------------+       +---------------------+
| Delta Lake Table  |       | Delta Lake Table  |       | Interactive         |
| (delta_tables/)   | <---> | (delta_tables/)   |       | Visualizations      |
+-------------------+       +-------------------+       +---------------------+ 



