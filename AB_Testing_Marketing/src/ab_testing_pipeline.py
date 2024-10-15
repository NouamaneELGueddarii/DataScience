from data_loader import load_data
from bayesian_model import calculate_posterior, monte_carlo_simulation
from visualizations import plot_posterior

def run_ab_test(data_path):
    # Load and preprocess data
    data = load_data(data_path)
    
    # Separate groups
    group_a_data = data[data['test group'] == 'ad']
    group_b_data = data[data['test group'] == 'psa']
    
    # Calculate posterior for Group A and Group B
    group_a_posterior = calculate_posterior(successes=group_a_data['converted'].sum(),
                                            total=len(group_a_data))
    group_b_posterior = calculate_posterior(successes=group_b_data['converted'].sum(),
                                            total=len(group_b_data))
    
    # Visualize posteriors
    plot_posterior(group_a_posterior, 'Group A')
    plot_posterior(group_b_posterior, 'Group B')
    
    # Monte Carlo Simulation
    prob_b_better = monte_carlo_simulation(group_a_posterior, group_b_posterior)
    print(f"Probability that Group B is better than Group A: {prob_b_better:.2%}")

# If running as the main script
if __name__ == '__main__':
    data_file = '../data/marketing_AB.csv'
    run_ab_test(data_file)
