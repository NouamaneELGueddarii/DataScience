from scipy.stats import beta
import numpy as np

def calculate_posterior(successes, total, alpha_prior=1, beta_prior=1):
    """
    Compute the posterior Beta distribution given the number of successes and total trials.
    
    Parameters:
    - successes: int, number of successful conversions
    - total: int, total number of users
    - alpha_prior: int, alpha value for the Beta prior (default 1)
    - beta_prior: int, beta value for the Beta prior (default 1)
    
    Returns:
    - Beta distribution object
    """
    alpha_post = alpha_prior + successes
    beta_post = beta_prior + (total - successes)
    return beta(alpha_post, beta_post)

def monte_carlo_simulation(group_a_posterior, group_b_posterior, n_samples=100000):
    """
    Perform Monte Carlo simulation by sampling from the two posterior distributions.
    
    Parameters:
    - group_a_posterior: Beta distribution for Group A
    - group_b_posterior: Beta distribution for Group B
    - n_samples: int, number of samples to draw
    
    Returns:
    - Probability that Group B is better than Group A
    """
    samples_a = group_a_posterior.rvs(n_samples)
    samples_b = group_b_posterior.rvs(n_samples)
    prob_b_better = np.mean(samples_b > samples_a)
    return prob_b_better
