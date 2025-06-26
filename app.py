import streamlit as st
from gwo import gwo, f3, f8

st.set_page_config(page_title="Grey Wolf Optimizer", layout="wide")
st.title("GWO Implementation with Benchmark Functions")
st.divider()

st.sidebar.header("Algorithm Configuration")

dim = st.sidebar.number_input("Dimensions (n)", min_value=1, max_value=50, value=10)
max_iter = st.sidebar.number_input("Maximum Iterations", min_value=10, max_value=100, value=100)
agents = st.sidebar.number_input("Number of Particles (Wolf)", min_value=3, max_value=30, value=30)
view = st.sidebar.selectbox("Select View:", ["f3(x) - Rotated Hyper-Ellipsoid", "f8(x) - Schwefel", "Both Functions Comparison"])

if st.sidebar.button("Run", type="secondary"):
    if view == "f3(x) - Rotated Hyper-Ellipsoid":
        curve, log = gwo(f3, dim, agents, max_iter, -100, 100)

        st.line_chart(curve, use_container_width=True)
        st.text_area("Iteration Log f3(x):", value=log, height=300)
    elif view == "f8(x) - Schwefel":
        curve, log = gwo(f8, dim, agents, max_iter, -500, 500)

        st.line_chart(curve, use_container_width=True)
        st.text_area("Iteration Log f8(x):", value=log, height=300)
    else:
        curve1, log1 = gwo(f3, dim, agents, max_iter, -100, 100)
        curve2, log2 = gwo(f8, dim, agents, max_iter, -500, 500)
        
        st.line_chart({"f3(x)": curve1, "f8(x)": curve2}, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.text_area("Iteration Log f3(x):", value=log1, height=300)
        with col2:
            st.text_area("Iteration Log f8(x):", value=log2, height=300)