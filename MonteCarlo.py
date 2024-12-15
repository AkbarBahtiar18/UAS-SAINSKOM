import numpy as np

def BilanganAcak(n_simulations):
    random_array = np.random.rand(n_simulations)
    return random_array

def Frekuensi(i, array, distribusi):
    jarak = array[i] * 100
    for j in range(len(distribusi) - 1):
        if jarak < distribusi[j]:
            return j
        elif distribusi[j] <= jarak < distribusi[j + 1]:
            return j + 1
    return len(distribusi) - 1

def tabelsimulasi(n, array, distribusi, variabel):
    print("Tabel Simulasi")
    print("Hari ke\t\tBilangan Acak\t\tFrekuensi")
    total_frekuensi = 0  # Variabel untuk menyimpan total frekuensi
    
    for i in range(n):
        indeks_frekuensi = Frekuensi(i, array, distribusi)
        nilai_frekuensi = variabel[indeks_frekuensi]
        total_frekuensi += nilai_frekuensi
        print(i + 1, "\t\t", round(array[i], 4), "\t\t", nilai_frekuensi)
    
    rata_rata = total_frekuensi / n
    print(f"\nRata-rata frekuensi: {rata_rata}")
    
def main():
    variabel = [] 
    frekuensi = [] 

    n = int(input("Masukkan jumlah variabel: "))
    for i in range(n):
        nilai = float(input(f"Masukkan nilai variabel ke-{i + 1}: "))
        freq = int(input(f"Masukkan frekuensi untuk variabel {nilai}: "))
        variabel.append(nilai)
        frekuensi.append(freq)

    jumlah_frekuensi = sum(frekuensi)
    distribusi_probabilitas = [freq / jumlah_frekuensi for freq in frekuensi]
    print("\nDistribusi Probabilitas:")
    print(distribusi_probabilitas)

    distribusi_komulatif = np.cumsum(distribusi_probabilitas) * 100
    distribusi_komulatif2 = np.cumsum(distribusi_probabilitas)
    print("\nDistribusi Komulatif:")
    print(distribusi_komulatif2)

    n_simulations = int(input("Masukkan jumlah simulasi: "))
    random_array = BilanganAcak(n_simulations)
    print("\nArray Random:")
    print(random_array)

    tabelsimulasi(n_simulations, random_array, distribusi_komulatif, variabel)
