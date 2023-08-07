import matplotlib.pyplot as plt

# Create the diagram
plt.figure(figsize=(8, 6))

# Input layer
plt.text(0.1, 0.5, 'Input Image', fontsize=12, ha='center', va='center', bbox=dict(facecolor='lightgray', edgecolor='black'))

# CNN layers
plt.text(0.4, 0.75, 'Convolutional Layers', fontsize=12, ha='center', va='center')
plt.text(0.4, 0.5, 'Residual Blocks', fontsize=12, ha='center', va='center')
plt.text(0.4, 0.25, 'Global Feature Map', fontsize=12, ha='center', va='center')

# Appearance descriptors
plt.text(0.8, 0.5, 'Appearance Descriptors', fontsize=12, ha='center', va='center')

# Arrows
plt.arrow(0.15, 0.5, 0.2, 0, length_includes_head=True, head_width=0.02, color='black')
plt.arrow(0.5, 0.6, 0, 0.15, length_includes_head=True, head_width=0.02, color='black')
plt.arrow(0.5, 0.4, 0, -0.15, length_includes_head=True, head_width=0.02, color='black')
plt.arrow(0.7, 0.5, 0.1, 0, length_includes_head=True, head_width=0.02, color='black')

# Adjust the plot settings
plt.axis('off')
plt.title('Network Architecture')
plt.tight_layout()

# Save the diagram
plt.savefig('network_diagram.png', dpi=300)
plt.show()
