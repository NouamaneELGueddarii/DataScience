import matplotlib.pyplot as plt
import numpy as np

def plot_posterior(posterior, group_name):
    """
    Plot the posterior distribution for a given group.
    
    Parameters:
    - posterior: Beta distribution object
    - group_name: str, name of the group (e.g., 'Group A')
    """
    x = np.linspace(0, 0.10, 1000)  # Conversion rates from 0 to 10%
    y = posterior.pdf(x)
    
    plt.plot(x, y, label=f'{group_name} Posterior')
    plt.title(f'Posterior Distribution for {group_name}')
    plt.xlabel('Conversion Rate')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
