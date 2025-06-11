import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def surface_function(x, y):
    """Define the surface z = x² + y²"""
    return x**2 + y**2

def calculate_volume_analytical():
    """
    Calculate the exact volume analytically.
    Volume = ∫∫(x² + y²) dx dy over [0,1] × [0,1]
    = ∫₀¹ ∫₀¹ (x² + y²) dx dy
    = ∫₀¹ [x³/3 + xy²]₀¹ dy
    = ∫₀¹ (1/3 + y²) dy
    = [y/3 + y³/3]₀¹
    = 1/3 + 1/3 = 2/3
    """
    return 2/3

def calculate_volume_numerical():
    """Calculate volume using numerical integration (scipy)"""
    result, error = integrate.dblquad(
        surface_function, 
        0, 1,  # y limits
        lambda y: 0, lambda y: 1  # x limits (functions of y)
    )
    return result, error

def calculate_volume_monte_carlo(n_samples=1000000):
    """Calculate volume using Monte Carlo integration"""
    # Generate random points in the unit square
    x_random = np.random.uniform(0, 1, n_samples)
    y_random = np.random.uniform(0, 1, n_samples)
    
    # Calculate z values at these points
    z_values = surface_function(x_random, y_random)
    
    # Volume = area of base × average height
    volume = np.mean(z_values) * 1  # base area is 1×1 = 1
    
    return volume

def calculate_volume_riemann(n_intervals=1000):
    """Calculate volume using Riemann sum approximation"""
    dx = dy = 1.0 / n_intervals
    volume = 0
    
    for i in range(n_intervals):
        for j in range(n_intervals):
            # Use midpoint of each rectangle
            x = (i + 0.5) * dx
            y = (j + 0.5) * dy
            volume += surface_function(x, y) * dx * dy
    
    return volume

def visualize_surface():
    """Create a 3D visualization of the surface"""
    x = np.linspace(0, 1, 50)
    y = np.linspace(0, 1, 50)
    X, Y = np.meshgrid(x, y)
    Z = surface_function(X, Y)
    
    fig = plt.figure(figsize=(12, 5))
    
    # 3D surface plot
    ax1 = fig.add_subplot(121, projection='3d')
    surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z = x² + y²')
    ax1.set_title('Surface z = x² + y²')
    fig.colorbar(surf, ax=ax1, shrink=0.5)
    
    # Contour plot
    ax2 = fig.add_subplot(122)
    contour = ax2.contour(X, Y, Z, levels=20)
    ax2.clabel(contour, inline=True, fontsize=8)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Contour Plot of z = x² + y²')
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.show()

def main():
    print("Volume Under Surface z = x² + y² over Unit Square [0,1] × [0,1]")
    print("=" * 65)
    
    # Analytical solution
    analytical_volume = calculate_volume_analytical()
    print(f"1. Analytical Solution: {analytical_volume:.10f}")
    
    # Numerical integration using scipy
    numerical_volume, error = calculate_volume_numerical()
    print(f"2. Numerical Integration (scipy): {numerical_volume:.10f}")
    print(f"   Estimated error: {error:.2e}")
    
    # Monte Carlo integration
    mc_volume = calculate_volume_monte_carlo(1000000)
    print(f"3. Monte Carlo Integration: {mc_volume:.10f}")
    
    # Riemann sum approximation
    riemann_volume = calculate_volume_riemann(1000)
    print(f"4. Riemann Sum (1000×1000): {riemann_volume:.10f}")
    
    print("\nComparison with Analytical Solution:")
    print(f"Numerical error: {abs(numerical_volume - analytical_volume):.2e}")
    print(f"Monte Carlo error: {abs(mc_volume - analytical_volume):.2e}")
    print(f"Riemann sum error: {abs(riemann_volume - analytical_volume):.2e}")
    
    # Show convergence of Riemann sum
    print("\nRiemann Sum Convergence:")
    intervals = [10, 50, 100, 500, 1000]
    for n in intervals:
        vol = calculate_volume_riemann(n)
        error = abs(vol - analytical_volume)
        print(f"n={n:4d}: Volume = {vol:.8f}, Error = {error:.2e}")
    
    # Create visualization
    print("\nGenerating 3D visualization...")
    visualize_surface()

if __name__ == "__main__":
    main()
