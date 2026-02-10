
import sympy as sp

def verify_model():
    # Define variables
    N, S, A = sp.symbols('N S A', positive=True, real=True)
    
    # Parameters (symbolic)
    alpha1, alpha2, alpha3 = sp.symbols('alpha1 alpha2 alpha3', positive=True) # Linear coefs
    beta1, beta2, beta3 = sp.symbols('beta1 beta2 beta3', positive=True) # Nonlinear coefs
    gamma_NS = sp.symbols('gamma_NS', positive=True) # Congestion penalty coef
    epsilon = sp.symbols('epsilon', positive=True) # Small regularizer for denominator
    
    # Revised Model Formulation
    # E_base = alpha1*N + alpha2*S + alpha3*A
    # E_nonlinear = beta1*N**1.3 + beta2*S**1.2 + beta3*A**1.15
    # E_congestion = gamma_NS * (N**2 / (S + epsilon)) # Penalty for insufficient stalls
    
    # Let's simplify for analysis:
    # We want to see if dE/dS = 0 gives a valid S* > 0
    
    E = alpha1*N + alpha2*S + alpha3*A + \
        beta1*N**1.3 + beta2*S**1.2 + beta3*A**1.15 + \
        gamma_NS * (N**2 / S) 
        
    print("Objective Function E:")
    sp.pprint(E)
    
    # First derivative w.r.t S
    dE_dS = sp.diff(E, S)
    print("\nPartial derivative dE/dS:")
    sp.pprint(dE_dS)
    
    # Solve for S where dE/dS = 0 (Simplified check)
    # Equation: alpha2 + 1.2*beta2*S^0.2 - gamma_NS*N^2/S^2 = 0
    # This implies gamma_NS*N^2/S^2 = alpha2 + 1.2*beta2*S^0.2
    # LHS decreases with S, RHS increases with S.
    # There must be a unique intersection S* for any N > 0.
    
    print("\nExistence of Optimal S* for fixed N:")
    print("LHS (Marginal Benefit of S):", gamma_NS*N**2/S**2)
    print("RHS (Marginal Cost of S):", alpha2 + 1.2*beta2*S**0.2)
    
    # Check convexity w.r.t S
    d2E_dS2 = sp.diff(E, S, 2)
    print("\nSecond derivative d2E/dS2 (Convexity check):")
    sp.pprint(d2E_dS2)
    # If d2E_dS2 > 0, it's a minimum.
    
    # Check Unconstrained Global Minimum
    # dE/dN
    dE_dN = sp.diff(E, N)
    print("\nPartial derivative dE/dN:")
    sp.pprint(dE_dN)
    
    # Since alpha1 > 0, beta1 > 0, gamma_NS > 0, N, S > 0
    # dE/dN is strictly positive?
    # Term: 2*gamma_NS*N/S is positive.
    # So dE/dN > 0 always.
    # Thus global min is at N=0.
    
if __name__ == "__main__":
    verify_model()
