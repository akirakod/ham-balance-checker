import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="HAM Balance Checker", layout="wide", initial_sidebar_state="expanded")
st.title("HAM Balance Checker")

# Function to check if the balance is correct
def is_balanced(lhs_total, rhs_value):
    return abs(lhs_total - rhs_value) <= 0.01

# Function to render input columns
def render_input_columns(labels, default_values, key_prefix):
    cols = st.columns(len(labels))
    values = []
    for col, label, default in zip(cols, labels, default_values):
        values.append(col.number_input(label, value=default, key=f'{key_prefix}_{label}'))
    return values

# Page management using radio buttons in the sidebar
page_options = ["Part 1 Balance Sheet", "Part 2 Income Statement", "Part 3 Cash Flow"]
page = st.sidebar.radio("Select Page", page_options)


### Part 1: Balance Sheet
if page == "Part 1 Balance Sheet":
    st.header("Part 1 Balance Sheet")

    # LHS Inputs
    st.subheader("Left-Hand Side (LHS)")
    lhs_labels = ['C', 'Rec', 'PpdT', 'RRU', 'P', 'H', 'AD']
    lhs_values = render_input_columns(lhs_labels, [0.0] * len(lhs_labels), 'lhs')

    st.markdown("---")  # Add a separator

    # RHS Inputs
    st.subheader("Right-Hand Side (RHS)")
    rhs_labels = ['IP', 'TP', 'MP', 'NP', 'CC', 'RE']
    rhs_values = render_input_columns(rhs_labels, [0.0] * len(rhs_labels), 'rhs')

    # Real-time balance checking
    lhs_total = round(sum(lhs_values), 2)
    rhs_total = round(sum(rhs_values), 2)

    is_eq_balanced = is_balanced(lhs_total, rhs_total)
    result = "Balanced" if is_eq_balanced else "Not Balanced"

    st.write(f"**LHS Total:** {lhs_total:.2f}")
    st.write(f"**RHS Total:** {rhs_total:.2f}")
    st.write(f"**Balance Status:** {result}")

### Part 2: Income Statement
elif page == "Part 2 Income Statement":
    st.header("Part 2 Income Statement")

    # LHS Inputs
    st.subheader("Left-Hand Side (LHS)")
    income_labels = ['RRev', 'SRev', 'MRev', 'G', 'RExp', 'MExp', 'DExp', 'IExp', 'ITExp', 'L']
    income_values = render_input_columns(income_labels, [0.0] * len(income_labels), 'income')

    st.markdown("---")  # Add a separator

    # RHS Inputs
    st.subheader("Right-Hand Side (RHS)")
    rhs_label = 'Net Income'
    rhs_value = st.number_input(rhs_label, value=0.0, key='rhs_net_income')

    # Calculate LHS
    lhs = sum(income_values)

    # Check balance
    is_eq_balanced = is_balanced(lhs, rhs_value)
    result = "Balanced" if is_eq_balanced else "Not Balanced"

    st.write(f"**Calculated LHS Total:** {lhs:.2f}")
    st.write(f"**Balance Status:** {result}")

### Part 3: Cash Flow
elif page == "Part 3 Cash Flow":
    st.header("Part 3 Cash Flow")

    # LHS Inputs
    st.subheader("Left-Hand Side (LHS)")
    cash_flow_labels = ['Operating Activities', 'Investing Activities', 'Financing Activities']
    cash_flow_values = render_input_columns(cash_flow_labels, [0.0] * len(cash_flow_labels), 'cash_flow')

    st.markdown("---")  # Add a separator

    # RHS Input
    st.subheader("Right-Hand Side (RHS)")
    rhs_label = 'Net Cash Flow'
    rhs_value = st.number_input(rhs_label, value=0.0, key='rhs_net_cash_flow')

    # Calculate Total Cash Flow from inputs
    total_cash_flow = sum(cash_flow_values)

    # Check balance
    is_eq_balanced = is_balanced(total_cash_flow, rhs_value)
    result = "Balanced" if is_eq_balanced else "Not Balanced"

    st.write(f"**Calculated Total Cash Flow:** {total_cash_flow:.2f}")
    st.write(f"**Balance Status:** {result}")
