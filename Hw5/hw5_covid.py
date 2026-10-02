import requests
import json

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

# Read the states and populations
states_data = []

with open("/home/ubuntu/data5500_mycode/Hw5/states.csv", "r") as file:
    for line in file:
        state, population = line.strip().split(",")
        states_data.append({
            "STATE_ABBREV": state,
            "POPULATION": int(population)
        })

# Store results for all states
state_results = []

# Go through each state
for row in states_data:
    state = row["STATE_ABBREV"]
    population = row["POPULATION"]

    params = {
        "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
        "$order": "end_date ASC"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Save this state's raw JSON data
    with open(f"{state}.json", "w") as file:
        json.dump(data, file, indent=2)

    print("State name:", state)

    # Convert new_cases from strings to numbers
    for record in data:
        record["new_cases"] = float(record["new_cases"])

    # Average number of new weekly cases
    total_cases = sum(record["new_cases"] for record in data)
    average_weekly_cases = total_cases / len(data)

    print(
        "Average number of new weekly cases for the entire state dataset:",
        average_weekly_cases
    )

    # Date with the highest number of new COVID cases
    highest_case = max(data, key=lambda record: record["new_cases"])

    print(
        "Date with highest new number of COVID cases:",
        highest_case["end_date"],
        "(",
        highest_case["new_cases"],
        ")"
    )

    # Add up cases by month
    monthly_cases = {}

    for record in data:
        month = record["end_date"][:7]

        if month not in monthly_cases:
            monthly_cases[month] = 0

        monthly_cases[month] += record["new_cases"]

    # Month with the highest total cases
    highest_month = max(monthly_cases, key=monthly_cases.get)
    highest_month_cases = monthly_cases[highest_month]

    print(
        "Month and Year, with the highest new number of COVID cases:",
        highest_month,
        "(",
        highest_month_cases,
        ")"
    )

    # Highest monthly cases as a percentage of population
    monthly_percentage = {}

    for month, cases in monthly_cases.items():
        monthly_percentage[month] = (cases / population) * 100

    highest_percentage_month = max(
        monthly_percentage,
        key=monthly_percentage.get
    )

    highest_percentage = monthly_percentage[highest_percentage_month]

    print(
        "Month and Year, with highest new number, percentage of population:",
        f"{highest_percentage:.2f}%",
        "(Population:",
        population,
        ")"
    )

    # Save this state's summary information
    state_results.append({
        "state": state,
        "percentage": highest_percentage,
        "month": highest_percentage_month,
        "cases": monthly_cases[highest_percentage_month],
        "population": population
    })

    print()


# ==================== SUMMARY ACROSS ALL STATES ====================

print("==================== SUMMARY ACROSS ALL STATES ====================")

highest_state = max(state_results, key=lambda x: x["percentage"])
lowest_state = min(state_results, key=lambda x: x["percentage"])

print()
print("State with HIGHEST percentage of population during its highest month:")
print(
    f'{highest_state["state"]} - '
    f'{highest_state["percentage"]:.2f}% in '
    f'{highest_state["month"]} '
    f'({highest_state["cases"]} cases; '
    f'Population: {highest_state["population"]})'
)

print()
print("State with LOWEST percentage of population during its highest month:")
print(
    f'{lowest_state["state"]} - '
    f'{lowest_state["percentage"]:.2f}% in '
    f'{lowest_state["month"]} '
    f'({lowest_state["cases"]} cases; '
    f'Population: {lowest_state["population"]})'
)