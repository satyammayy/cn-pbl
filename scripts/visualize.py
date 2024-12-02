import networkx as nx
import matplotlib.pyplot as plt

def visualize_topology():
    G = nx.Graph()

    # Add nodes and edges
    G.add_node('h1')
    G.add_node('h2')
    G.add_node('r1')
    G.add_node('r2')
    G.add_edges_from([('h1', 'r1'), ('h2', 'r2'), ('r1', 'r2')])

    # Draw topology
    nx.draw(G, with_labels=True, node_size=2000, font_size=10)
    plt.title("Network Topology")
    plt.show()

if __name__ == '__main__':
    visualize_topology()
