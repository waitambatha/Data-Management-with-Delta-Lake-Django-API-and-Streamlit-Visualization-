from django.http import JsonResponse
from deltalake import DeltaTable, write_deltalake
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(["GET", "POST"])
def employee_data(request):
    delta_path = "delta_tables/employee_data"

    if request.method == "GET":
        try:
            # Load the Delta table
            dt = DeltaTable(delta_path)
            df = dt.to_pandas()

            # Convert the DataFrame to a JSON-friendly format
            data = df.to_dict(orient="records")

            # Return the data as a JSON response
            return Response({"status": "success", "data": data})

        except Exception as e:
            # Handle errors
            return Response({"status": "error", "message": str(e)}, status=500)

    elif request.method == "POST":
        try:
            # Get the new data from the request
            new_data = request.data

            # Validate required fields
            required_fields = [
                "name", "age", "salary", "department", "city",
                "job_title", "years_of_experience", "performance_score",
                "joining_date", "is_manager"
            ]
            for field in required_fields:
                if field not in new_data:
                    return Response(
                        {"status": "error", "message": f"Missing required field: {field}"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # Convert joining_date to a datetime object
            try:
                new_data["joining_date"] = pd.to_datetime(new_data["joining_date"]).date()
            except ValueError:
                return Response(
                    {"status": "error", "message": "Invalid date format for joining_date. Use YYYY-MM-DD."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Load the existing Delta table
            dt = DeltaTable(delta_path)
            df = dt.to_pandas()

            # Auto-generate ID
            new_data["id"] = len(df) + 1

            # Append the new data to the DataFrame
            new_df = pd.DataFrame([new_data])

            # Ensure joining_date is in datetime64[ns] format
            new_df["joining_date"] = pd.to_datetime(new_df["joining_date"])

            # Append the new data to the existing DataFrame
            updated_df = pd.concat([df, new_df], ignore_index=True)

            # Save the updated DataFrame back to the Delta table
            write_deltalake(delta_path, updated_df, mode="overwrite")

            # Return success response
            return Response(
                {"status": "success", "message": "Employee data added successfully", "data": new_data},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            # Handle errors
            return Response({"status": "error", "message": str(e)}, status=500)