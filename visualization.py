import pandas as pd
import plotly.graph_objects as go
import random

# Load the data
df = pd.read_csv('sampled_analysts_for_top_contributors.csv')

# Replace analyst names with random 3-digit numbers
unique_analysts = df['Analysts'].unique()
random_ids = random.sample(range(100, 1000), len(unique_analysts))  # Ensure no duplicates
analyst_id_map = {name: f"Analyst {rid}" for name, rid in zip(unique_analysts, random_ids)}
df['Analysts'] = df['Analysts'].map(analyst_id_map)

# Extract the unique nodes
contributors = df['Contributor'].unique().tolist()
analysts = df['Analysts'].unique().tolist()
estimids = df['ESTIMID'].unique().tolist()

# Randomize the order of analyst nodes
random.shuffle(analysts)

# Combine all nodes into a single list for the Sankey diagram
nodes = contributors + analysts + estimids

# Create a mapping from node name to index
node_dict = {node: i for i, node in enumerate(nodes)}

# Initialize the source, target, and value lists
source = []
target = []
value = []
colors = []

# Define a color map for contributors
contributor_colors = {
    'BofA Global Research': '#1f77b4',
    'JPMorgan': '#ff7f0e',
    'Jefferies': '#2ca02c',
    'Morgan Stanley': '#d62728'
}

# Create a list of analyst rows and shuffle them for randomness
shuffled_rows = df.sample(frac=1).reset_index(drop=True)

# Populate the links
for _, row in shuffled_rows.iterrows():
    contrib_idx = node_dict[row['Contributor']]
    analyst_idx = node_dict[row['Analysts']]
    estimid_idx = node_dict[row['ESTIMID']]

    # Contributor -> Analyst
    source.append(contrib_idx)
    target.append(analyst_idx)
    value.append(1)
    colors.append(contributor_colors[row['Contributor']])

    # Analyst -> ESTIMID
    source.append(analyst_idx)
    target.append(estimid_idx)
    value.append(1)
    colors.append(contributor_colors[row['Contributor']])

# Create the Sankey diagram
sankey = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        label=nodes,
        color=[contributor_colors.get(node, '#cccccc') for node in nodes],
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=colors,
    )
))

# Set the title and display the diagram
sankey.update_layout(title_text="Sankey Diagram of Contributors -> Analysts -> ESTIMIDs (Analysts as Random 3-Digit IDs)", font_size=10)
sankey.show()


# import pandas as pd
# # Load the sampled data
# import pandas as pd
# import plotly.graph_objects as go
# import random

# # Load the data
# df = pd.read_csv('sampled_analysts_for_top_contributors.csv')

# # Extract the unique nodes
# contributors = df['Contributor'].unique().tolist()
# analysts = df['Analysts'].unique().tolist()
# estimids = df['ESTIMID'].unique().tolist()

# # Shuffle analysts to randomize their order in the diagram
# random.shuffle(analysts)

# # Combine all nodes into a single list for the Sankey diagram
# nodes = contributors + analysts + estimids

# # Create a mapping from node name to index
# node_dict = {node: i for i, node in enumerate(nodes)}

# # Initialize the source, target, and value lists
# source = []
# target = []
# value = []
# colors = []

# # Define a color map for contributors
# contributor_colors = {
#     'BofA Global Research': '#1f77b4',
#     'JPMorgan': '#ff7f0e',
#     'Jefferies': '#2ca02c',
#     'Morgan Stanley': '#d62728'
# }

# # Populate the links
# for _, row in df.iterrows():
#     contrib_idx = node_dict[row['Contributor']]
#     analyst_idx = node_dict[row['Analysts']]
#     estimid_idx = node_dict[row['ESTIMID']]
    
#     # Contributor -> Analyst
#     source.append(contrib_idx)
#     target.append(analyst_idx)
#     value.append(1)
#     colors.append(contributor_colors[row['Contributor']])
    
#     # Analyst -> ESTIMID
#     source.append(analyst_idx)
#     target.append(estimid_idx)
#     value.append(1)
#     colors.append(contributor_colors[row['Contributor']])

# # Create the Sankey diagram
# sankey = go.Figure(go.Sankey(
#     node=dict(
#         pad=15,
#         thickness=20,
#         line=dict(color='black', width=0.5),
#         label=nodes,
#         color=[contributor_colors.get(node, '#cccccc') for node in nodes],
#     ),
#     link=dict(
#         source=source,
#         target=target,
#         value=value,
#         color=colors,
#     )
# ))

# # Set the title and display the diagram
# sankey.update_layout(title_text="Sankey Diagram of Contributors -> Analysts -> ESTIMIDs thrid try", font_size=10)
# sankey.show()

