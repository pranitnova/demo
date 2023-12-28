# app.py
import streamlit as st


# functions
def calculate_cost(layer, year):
    if year == 1:
        if layer == 1:
            return round(
                (layer_1 + added_cost_per_bar) * slider_val + (20000 * conversion_rate),
                4,
            )
        if layer == 2:
            return round(
                (layer_2 + added_cost_per_bar) * slider_val + (20000 * conversion_rate),
                4,
            )
        if layer == 3:
            return round(
                (layer_3 + added_cost_per_bar) * slider_val + (20000 * conversion_rate),
                4,
            )
    else:
        if layer == 1:
            return round((layer_1 + added_cost_per_bar) * slider_val, 4)
        if layer == 2:
            return round((layer_2 + added_cost_per_bar) * slider_val, 4)
        if layer == 3:
            return round((layer_3 + added_cost_per_bar) * slider_val, 4)


# Constants
conversion_rate = st.sidebar.slider("**Conversion (Eur € - Dol $)**", 1.0, 1.5, 1.11)

layer_1 = round(1400 * conversion_rate)
layer_2 = round(2000 * conversion_rate)
layer_3 = round(2600 * conversion_rate)

st.sidebar.divider()

# Sidebar Section
st.sidebar.write("**Cartridge Cost**")

st.sidebar.write(
    f"Layer 1 Security - *€{round(layer_1/conversion_rate)}*: **`${layer_1}`**"
)
st.sidebar.write(
    f"Layer 2 Security - *€{round(layer_2/conversion_rate)}*: **`${layer_2}`**"
)
st.sidebar.write(
    f"Layer 3 Security - *€{round(layer_3/conversion_rate)}*: **`${layer_3}`**"
)


st.sidebar.divider()
production_capacity = st.sidebar.number_input(
    "**Production Capacity (month)**",
    min_value=10000,
    max_value=60000,
    step=1000,
    value=30000,
)


st.sidebar.divider()
slider_val = st.sidebar.slider(
    "**Number of Cartridges (year)**", 1, 150, round((production_capacity / 5000) * 12)
)
st.sidebar.caption(f"*Annual Production:* `{slider_val*5000}`")


# Main Page

st.caption(
    f"Annual Production: **`{slider_val*5000}`**,\t  Annual Cartridge Required: **`{slider_val}`**"
)
st.write("With Contract (**`1 Year`**)")
st.caption(
    f"""
- **100** cartridges to be bought in the first year!
- No cost for device + shipping
- **Ink Price remains constant for 1 year**

Paying for **`100`** cartridges
"""
)

annual_cost_l1 = layer_1 * 100
annual_cost_l2 = layer_2 * 100
annual_cost_l3 = layer_3 * 100

with_contract = {
    "Cost ($)": ["Per Bar", "Per Month", "Per Year"],
    "Layer 1": [
        round((layer_1) / 5000, 4),
        round(annual_cost_l1 / 12, 4),
        round(annual_cost_l1, 4),
    ],
    "Layer 2": [
        round((layer_2) / 5000, 4),
        round(annual_cost_l2 / 12, 4),
        round(annual_cost_l2, 4),
    ],
    "Layer 3": [
        round((layer_3) / 5000, 4),
        round(annual_cost_l3 / 12, 4),
        round(annual_cost_l3, 4),
    ],
}
st.table(with_contract)

st.divider()

st.write("Without Contract")
st.caption(
    f"""
- This does not include the device & the shipping cost.
- Devices + Shipping Cost (*€{20000}*): **`${round(20000 * conversion_rate)}`**   
- Variable Ink Price (Future changes in prices are not covered).

Paying for - **`{slider_val}`** cartridges, device & shipping! 
"""
)

# Added cost per bar for the production of the entire year
cost_per_bar = (20000 * conversion_rate) / (slider_val * 5000)
added_cost_per_bar = round(cost_per_bar, 1)

actual_cost_l1 = (layer_1 + added_cost_per_bar) * slider_val + (20000 * conversion_rate)
actual_cost_l2 = (layer_2 + added_cost_per_bar) * slider_val + (20000 * conversion_rate)
actual_cost_l3 = (layer_3 + added_cost_per_bar) * slider_val + (20000 * conversion_rate)

st.caption(f"Extra cost per bar: **`{round(cost_per_bar, 5)}`**")

without_contract = {
    "Cost ($)": ["Per Bar", "Per Month", "Per Year"],
    "Layer 1 (1st Year)": [
        round((layer_1) / 5000 + cost_per_bar, 4),
        calculate_cost(layer=1, year=1) // 12,
        calculate_cost(layer=1, year=1),
    ],
    "Layer 1 (2nd Year)": [
        round((layer_1) / 5000, 4),
        calculate_cost(layer=1, year=2) // 12,
        calculate_cost(layer=1, year=2),
    ],
    "Layer 2 (1st Year)": [
        round((layer_2) / 5000 + cost_per_bar, 4),
        calculate_cost(layer=2, year=1) // 12,
        calculate_cost(layer=2, year=1),
    ],
    "Layer 2 (2nd Year)": [
        round((layer_2) / 5000, 4),
        calculate_cost(layer=2, year=2) // 12,
        calculate_cost(layer=2, year=2),
    ],
    "Layer 3 (1st Year)": [
        round((layer_3) / 5000 + cost_per_bar, 4),
        calculate_cost(layer=3, year=1) // 12,
        calculate_cost(layer=3, year=1),
    ],
    "Layer 3 (2nd Year)": [
        round((layer_2) / 5000, 4),
        calculate_cost(layer=3, year=2) // 12,
        calculate_cost(layer=3, year=2),
    ],
}
st.table(without_contract)
