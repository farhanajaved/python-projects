import pygraphviz as pgv
from IPython.display import Image

# Create a new directed graph
G = pgv.AGraph(strict=False, directed=True)

# Add nodes with custom attributes for paper
G.add_node('Start', shape='ellipse', label='Start')
G.add_node('Agreement_Creation', shape='box', label='Agreement Creation\n& KPI Selection')
G.add_node('SLA_Monitoring', shape='box', label='SLA Monitoring\nbreachRecord.sol & monitorOracle.sol')
G.add_node('Offchain_Data', shape='box', label='Off-chain Data\nChainlink Oracle')
G.add_node('Breach_Assessment', shape='box', label='Breach Assessment\nEquation~\\ref{eq:breach_assessment}')
G.add_node('Consumer_Provider_Relationship', shape='box', label='Consumer-Provider Relationship\nEquation~\\ref{eq:relationship}')
G.add_node('SLA_Logs', shape='box', label='SLA Logs & KPIs')
G.add_node('Uptime_Calculation', shape='box', label='Uptime Calculation\nEquation~\\ref{eq:uptime}')
G.add_node('Penalty_Assessment', shape='box', label='Penalty Assessment\nEquations~\\ref{eq:quadratic_penalty} & \\ref{eq:history_penalty}')
G.add_node('End', shape='ellipse', label='End')

# Add edges
G.add_edge('Start', 'Agreement_Creation')
G.add_edge('Agreement_Creation', 'SLA_Monitoring')
G.add_edge('SLA_Monitoring', 'Offchain_Data')
G.add_edge('Offchain_Data', 'Breach_Assessment')
G.add_edge('Offchain_Data', 'Consumer_Provider_Relationship')
G.add_edge('Consumer_Provider_Relationship', 'SLA_Logs')
G.add_edge('SLA_Logs', 'Uptime_Calculation')
G.add_edge('Uptime_Calculation', 'Penalty_Assessment')
G.add_edge('Breach_Assessment', 'Penalty_Assessment')
G.add_edge('Penalty_Assessment', 'End')

# Render the graph
G.layout(prog='dot')

# Export or display the graph
G.draw('SLA_Monitoring_Flowchart.png')
Image('SLA_Monitoring_Flowchart.png')
