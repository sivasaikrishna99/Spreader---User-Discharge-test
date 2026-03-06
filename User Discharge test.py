import streamlit as st

st.set_page_config(page_title="Agri Drone Spreader Calibration", layout="centered")

st.title("🚁 Spreader Calibration Calculator")
st.caption("Discharge rate calculator based on flight parameters")

st.divider()

ACRE_M2 = 4046.86

# -----------------------
# Main Inputs
# -----------------------

dispense_per_acre = st.number_input(
    "Dispense weight per acre (kg/acre)",
    min_value=1.0,
    max_value=200.0,
    value=25.0,
    step=1.0
)

test_weight = st.number_input(
    "Test sample weight (kg)",
    min_value=1.0,
    max_value=20.0,
    value=5.0,
    step=0.5
)

# -----------------------
# Advanced Settings
# -----------------------

with st.expander("Advanced Settings"):

    speed = st.number_input(
        "Drone Speed (m/s)",
        min_value=1.0,
        max_value=15.0,
        value=5.0,
        step=0.5
    )

    swath = st.number_input(
        "Swath Width (m)",
        min_value=1.0,
        max_value=20.0,
        value=7.0,
        step=0.5
    )

    acres = st.number_input(
        "Area (acres)",
        min_value=0.1,
        max_value=50.0,
        value=1.0,
        step=0.1
    )

    turns = st.number_input(
        "Turns",
        min_value=0,
        max_value=300,
        value=0,
        step=1
    )

st.divider()

# -----------------------
# Calculations
# -----------------------

# Area conversion
area_m2 = acres * ACRE_M2

# Distance to travel
distance = area_m2 / swath

# Flight time
discharge_time = distance / speed

# Total material required
total_weight = dispense_per_acre * acres

# Required discharge rate
discharge_rate_kg_s = total_weight / discharge_time
discharge_rate_kg_min = discharge_rate_kg_s * 60

# Test sample empty time
sample_time = test_weight / discharge_rate_kg_s

# -----------------------
# Output
# -----------------------

st.subheader("📊 Results")

c1, c2 = st.columns(2)

with c1:
    st.metric("Test Sample Empty Time", f"{round(sample_time,1)} sec")
    

with st.expander("Advanced output"):
    st.metric("Required Discharge Rate", f"{round(discharge_rate_kg_min,2)} kg/min")
    st.metric("Total Material Required", f"{round(total_weight,2)} kg")
    st.metric("Discharge Time for Area", f"{round(discharge_time,1)} sec")

st.caption(
    "Model:\n"
    "Distance = Area(m²) / Swath\n"
    "Time = Distance / Speed\n"
    "Total Weight = kg/acre × Area\n"
    "Discharge Rate = TotalWeight / Time\n"
    "Sample Empty Time = TestWeight / DischargeRate"

)




