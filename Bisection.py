import math
def bisection_method(f, a, b, tolerance=0.001, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("Metode biseksi gagal: tidak ada akar dalam interval ini.")
        return None
    
    print(f"{'Iterasi':<10}{'a':<12}{'b':<12}{'f(a)':<12}{'f(b)':<12}{'x':<12}{'f(x)':<12}{'Error':<12}{'Tanda':<20}")
    print("-" * 100)
    
    iterations = 0
    while iterations < max_iterations:
        x = (a + b) / 2
        
        fa = f(a)
        fb = f(b)
        fx = f(x)
        error = abs(b - a)
        
        if fa * fx < 0:
            tanda = "berlawanan tanda"
        else:
            tanda = "sama tanda"

        print(f"{iterations + 1:<10}{a:<12.6f}{b:<12.6f}{fa:<12.6f}{fb:<12.6f}{x:<12.6f}{fx:<12.6f}{error:<12.6f}{tanda:<20}")
        
        if abs(fx) < tolerance:
            return x
        
        if fa * fx < 0:
            b = x
        else:
            a = x
        
        iterations += 1
    
    print("Metode biseksi mencapai iterasi maksimum.")
    return None

def fungsi(x):
    return x * math.exp(-x) + 1

def main():
    a = -1  
    b = 0  
    toleransi = 0.0001
    iterasi_maks = 11

    akar = bisection_method(fungsi, a, b, toleransi, iterasi_maks)

    if akar is not None:
        print(f"\nAkar persamaan: {akar:.6f}")
        print(f"Nilai fungsi di titik akar: {fungsi(akar):.6f}")
        
main()
