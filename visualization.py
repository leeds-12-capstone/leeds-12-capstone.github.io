import pandas as pd

# # Load your data (replace 'your_file.csv' with your actual file name or path)
# # Assuming the dataset is in a CSV file format, if not, you'll need to load it accordingly (e.g., from Excel).
# df = pd.read_csv('/Users/josephallred/Documents/cu_undergrad/fall_24/capstone/repo/Capstone_2024_2025/scripts/2_matching/confidence_data/frequency_analyst_matches.csv')

# # Top 4 Contributors to focus on
# top_contributors = ['BofA Global Research', 'Morgan Stanley', 'JPMorgan', 'Jefferies']

# # Step 1: Filter the data to include only rows where the Contributor is one of the top 4
# filtered_df = df[df['Contributor'].isin(top_contributors)]

# # Step 2: Randomly sample 10 analysts for each contributor (if there are fewer than 10, take all available analysts)
# sampled_analysts = filtered_df.groupby('Contributor').apply(lambda x: x.sample(min(len(x), 10), random_state=42)).reset_index(drop=True)

# # Step 3: Display the sampled data to confirm it's correct
# print(sampled_analysts.head(30))  # Show the first 30 rows of the sampled data

# # Step 4: Save the sampled data to a new CSV file (optional)
# sampled_analysts.to_csv('sampled_analysts_for_top_contributors.csv', index=False)

# Load the sampled data
import pandas as pd
import plotly.graph_objects as go
import random

# Load the data
df = pd.read_csv('sampled_analysts_for_top_contributors.csv')

# Extract the unique nodes
contributors = df['Contributor'].unique().tolist()
analysts = df['Analysts'].unique().tolist()
estimids = df['ESTIMID'].unique().tolist()

# Shuffle analysts to randomize their order in the diagram
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

# Populate the links
for _, row in df.iterrows():
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
sankey.update_layout(title_text="Sankey Diagram of Contributors -> Analysts -> ESTIMIDs thrid try", font_size=10)
sankey.show()

