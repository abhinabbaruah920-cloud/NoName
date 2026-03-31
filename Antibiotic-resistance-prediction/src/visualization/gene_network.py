import networkx as nx
import matplotlib.pyplot as plt


def build_gene_network(df, gene_column="gene_name"):
    G = nx.Graph()

    genes = df[gene_column].unique()

    for gene in genes:
        G.add_node(gene)

    # Connect genes if they co-occur
    for _, row in df.iterrows():
        gene = row[gene_column]
        for other_gene in genes:
            if gene != other_gene:
                G.add_edge(gene, other_gene)

    return G


def plot_network(G, save_path="outputs/plots/gene_network.png"):
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_size=500, font_size=8)
    plt.savefig(save_path)
    plt.close()