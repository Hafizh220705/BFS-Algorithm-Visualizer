"""
Simulasi Visual Interaktif Algoritma BFS
Author:
- Muhammad Fadhli (140810230056)
- Hafizh Fadhl Muhammad (140810230070)
- Farhan Zia Rizky (140810230074)
"""

import streamlit as st
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import time

# CSS Styling
st.set_page_config(page_title="BFS Visualizer", layout="wide")
st.markdown("""
<style>
body {
    background-color: #111827;
    color: #f3f4f6;
}
section[data-testid="stSidebar"] {
    background-color: #1f2937;
    color: white;
}
.css-1cpxqw2 {
    font-size: 1.4rem !important;
    font-weight: 600 !important;
}
.stButton > button {
    background-color: #2563eb;
    color: white;
    padding: 0.6em 1.2em;
    border-radius: 8px;
    border: none;
    font-size: 1rem;
}
.stButton > button:hover {
    background-color: #1e40af;
}
</style>
""", unsafe_allow_html=True)

# Fungsi parsing input format "A-B, B-C, C-D"
def parse_edges(edge_str):
    edges = []
    nodes = set()
    parts = edge_str.split(',')
    for part in parts:
        u, v = part.strip().split('-')
        edges.append((u.strip(), v.strip()))
        nodes.update([u.strip(), v.strip()])
    return list(nodes), edges

# Fungsi BFS step-by-step dengan path tracking
def bfs_with_path(graph_dict, start, target=None):
    visited = set()
    queue = deque([(start, [start])])
    steps = []

    while queue:
        node, path = queue.popleft()
        steps.append({
            'current': node,
            'path': path.copy(),
            'queue': list(queue),
            'visited': list(visited)
        })
        if node == target:
            break
        if node not in visited:
            visited.add(node)
            for neighbor in graph_dict.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return steps

# Fungsi menggambar graf menggunakan matplotlib
def draw_graph(edges, highlight_path=[], visited=set()):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='#d1d5db', node_size=900, edge_color='#9ca3af')

    if visited:
        nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='#34d399')
    if highlight_path:
        edge_path = [(highlight_path[i], highlight_path[i+1]) for i in range(len(highlight_path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color='#f97316', width=3)
    st.pyplot(plt)

# Tampilan UI
st.title("🔵 BFS Algorithm Visualizer")

with st.sidebar:
    st.header("📌 Pengaturan BFS")
    st.markdown("Masukkan graf sebagai edges dengan format: `A-B, B-C, C-D`.")
    edge_input = st.text_area("🧩 Graph Edges:", value="A-B, A-C, B-D, B-E, C-F, D-G, E-G, F-H, G-H")

    try:
        nodes, edge_list = parse_edges(edge_input)
        graph_dict = {node: [] for node in nodes}
        for u, v in edge_list:
            graph_dict[u].append(v)
            graph_dict[v].append(u)
        start_node = st.selectbox("🎯 Start Node:", sorted(nodes))
        target_node = st.selectbox("🎯 Target Node (opsional):", [""] + sorted(nodes))
    except:
        st.error("❌ Format input salah. Gunakan A-B, B-C...")
        st.stop()

st.markdown("""
### 💡 Tentang BFS
Algoritma Breadth-First Search (BFS) mengeksplorasi graf secara **level-wise**.
Gunakan tombol navigasi di bawah untuk melihat proses langkah demi langkah.
""")

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("🚀 Jalankan BFS"):
        st.session_state['run'] = True
        st.session_state['step'] = 0
        st.session_state['steps'] = bfs_with_path(graph_dict, start_node, target_node or None)

if 'run' in st.session_state and st.session_state['run']:
    steps = st.session_state['steps']
    max_step = len(steps)

    st.markdown("---")
    st.subheader(f"🧭 Langkah {st.session_state['step']+1} dari {max_step}")

    cols = st.columns([1, 1, 1, 1])
    if cols[0].button("⏮ First"):
        st.session_state['step'] = 0
    if cols[1].button("◀ Prev") and st.session_state['step'] > 0:
        st.session_state['step'] -= 1
    if cols[2].button("▶ Next") and st.session_state['step'] < max_step - 1:
        st.session_state['step'] += 1
    if cols[3].button("⏭ Last"):
        st.session_state['step'] = max_step - 1

    step_data = steps[st.session_state['step']]
    st.markdown(f"**🔎 Simpul saat ini:** `{step_data['current']}`")
    st.markdown(f"**📋 Queue:** `{[q[0] if isinstance(q, tuple) else q for q in step_data['queue']]}`")
    st.markdown(f"**✅ Visited:** `{step_data['visited']}`")
    draw_graph(edge_list, highlight_path=step_data['path'], visited=set(step_data['visited']))

    if target_node and step_data['current'] == target_node:
        st.success(f"🎉 Target '{target_node}' ditemukan! Jarak: {len(step_data['path'])-1}")
        st.markdown(f"**📌 Jalur Terpendek:** {' ➡️ '.join(step_data['path'])}")

    with st.expander("🗺️ Legend"):
        st.markdown("""
        - 🟢 **Visited** nodes → `#34d399`  
        - 🟠 **Shortest path** → `#f97316`  
        - ⚪ **Default node** → `#d1d5db`
        """)

    with st.expander("📊 Statistik Graf"):
        st.metric("Total Simpul", len(graph_dict))
        st.metric("Total Edge", len(edge_list))
        st.metric("Jarak ke Target", len(step_data['path'])-1 if target_node else "-")

    if st.button("💾 Simpan Jalur ke File"):
        with open("bfs_path.txt", "w", encoding="utf-8") as f:
            f.write(" ➡️ ".join(step_data['path']))
        st.success("✅ Jalur berhasil disimpan ke `bfs_path.txt`")

st.markdown("""
---
👨‍💻 **Dibuat oleh:** Muhammad Fadhli (140810230056), Hafizh Fadhl Muhammad (140810230070), Farhan Zia Rizky (140810230074)
""")