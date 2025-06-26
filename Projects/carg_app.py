import streamlit as st
from carg_gate import reasoning_gate

st.set_page_config(page_title="CARG: Carbon-Aware Reasoning Gate", layout="centered")

st.title("🔌 CARG — Carbon-Aware Reasoning Gate")
st.write("Control reasoning depth based on energy, complexity, and user intent. Simulate responsible cognitive behavior.")

# --- User Inputs ---
with st.sidebar:
    st.header("🌐 Simulation Controls")
    complexity = st.slider("Task Complexity", 0.0, 1.0, 0.5)
    energy = st.slider("Available Energy", 0.0, 1.0, 0.5)
    intent = st.radio("User Intent", ["Casual", "Critical"])

    st.markdown("---")
    if st.button("Preset: ⚡ Emergency Mode"):
        complexity = 0.9
        energy = 0.2
        intent = "Critical"
    if st.button("Preset: ☀️ Solar AI"):
        complexity = 0.7
        energy = 1.0
        intent = "Critical"
    if st.button("Preset: 💤 Chill Query"):
        complexity = 0.1
        energy = 0.6
        intent = "Casual"

# --- Logic Result ---
mode, explanation, carbon_cost = reasoning_gate(complexity, energy, intent)

st.subheader("🧠 Reasoning Mode Selected")
st.success(mode)

st.markdown(f"**Explanation:** {explanation}")
st.metric("💨 Estimated Carbon Cost", f"{carbon_cost} units")

# --- Reasoning Preview ---
with st.expander("🕹️ Reasoning Preview"):
    if mode.startswith("R1"):
        st.code("Based on past usage, this should work just fine.")
    elif mode.startswith("R2"):
        st.code("There's nuance here, but we'll aim for a balanced solution.")
    elif mode.startswith("R3"):
        st.code("Step 1: Gather evidence...\nStep 2: Evaluate alternatives...\nStep 3: Select optimal path.")

# --- Footer ---
st.markdown("---")
st.caption("Built by SeayCo. Open cognition for a shared future.")
