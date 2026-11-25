import networkx as nx
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(page_title="Family Office", page_icon="👨‍👩‍👧‍👦", layout="wide")
st.title("👨‍👩‍👧‍👦 Family Office")
st.markdown("### Family Office Management")
st.markdown("### 📊 Family Office Services Network")

services = {
    "Wealth Management": ["Investment Policy", "Portfolio Management", "Cash Management"],
    "Wealth Planning": ["Goal Planning", "Retirement", "Education Funding"],
    "Tax Planning": ["US Tax", "India Tax", "Cross-border Tax"],
    "Estate Planning": ["Wills", "Trusts", "Succession"],
    "Risk Management": ["Insurance", "Cyber Risk", "Concentration Risk"],
    "Family Governance": ["Meeting Structure", "Reporting", "Education"],
    "Real Estate": ["Acquisition", "Operations", "Disposition"],
    "Legal Services": ["Entity Structure", "Contracts", "Compliance"],
}

graph = nx.Graph()
graph.add_node("Family Office")
graph.add_node("Customer")
for category, subs in services.items():
    graph.add_edge("Family Office", category)
    graph.add_edge(category, "Customer") if category == "Wealth Management" else None
    for subcategory in subs:
        graph.add_edge(category, subcategory)

positions = nx.spring_layout(graph, seed=42)
x_values = [positions[node][0] for node in graph.nodes]
y_values = [positions[node][1] for node in graph.nodes]

edge_x, edge_y = [], []
for source, target in graph.edges:
    edge_x += [positions[source][0], positions[target][0], None]
    edge_y += [positions[source][1], positions[target][1], None]
figure = go.Figure()
figure.add_trace(go.Scatter(x=edge_x, y=edge_y, mode="lines", line={"color": "rgba(31,119,180,0.6)", "width": 1.5}, hoverinfo="none"))

for node in graph.nodes:
    x, y = positions[node]
    if node == "Family Office":
        figure.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", marker={"symbol": "square", "size": 40, "color": "gold"}, text=[node], textfont={"size": 12, "color": "black", "family": "Arial Black"}, hoverinfo="text", textposition="middle center"))
    elif node == "Customer":
        figure.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", marker={"size": 60, "color": "green"}, text=[node], textfont={"size": 11, "color": "black", "family": "Arial Black"}, hoverinfo="text", textposition="middle center"))
    elif node in services:
        figure.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", marker={"symbol": "square", "size": 36, "color": "#4a90e2"}, text=[node], textfont={"size": 11, "color": "black", "family": "Arial Black"}, hoverinfo="text", textposition="middle center"))
    else:
        figure.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", marker={"size": 22, "color": "lightgray"}, text=[node], textfont={"size": 10, "color": "black"}, hoverinfo="text", textposition="middle center"))

figure.update_layout(title="Family Office Services Network Structure", height=800, paper_bgcolor="rgba(245,245,250,0.5)", plot_bgcolor="rgba(245,245,250,0.5)", showlegend=False, xaxis={"visible": False}, yaxis={"visible": False}, margin={"b": 20, "l": 5, "t": 40})
st.plotly_chart(figure, use_container_width=True)
