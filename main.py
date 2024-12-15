import os
import Maktrik as matrix
import InversMatrks as invers
import LUDecomposition as lu
import gauss as elimgaus
import jacobiSeidel as jacodel
import iterasiSederhana as iterasiseder
import NewtonRhapson as newraphson
import Secant as secant
import Bisection as biseksi
import interpoLinier as polinier
import interpolKuadrat as polkuadrat
import polinomNewton as newton
import regulafalsi as regufals
import markovchain as mchain
import MonteCarlo as mc


def TeknikKomputasi():
    while True:
        print(
            """
        === Program Teknik Komputasi ===
        1. Invers Matriks
        2. LU Decomposition
        3. Exit
        """
        )
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            invers.main()
        elif pilihan == 2:
            lu.main()
        elif pilihan == 3:
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


def persamaanlinear():
    while True:
        print(
            """
        === Program Persamaan Linear ===
        TERBUKA
        1. iterasi sederhana
        2. Newton-Raphson
        3. Secant
        TERTUTUP
        4. Tabel Biseksi
        5. Regula Falsi
        0. Exit
        """
        )
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                iterasiseder.main()
            elif pilihan == 2:
                newraphson.main()
            elif pilihan == 3:
                secant.main()
            elif pilihan == 4:
                biseksi.main()
            elif pilihan == 5:
                regufals.regula_falsi_with_input()
            elif pilihan == 0:
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def interpolasi():
    while True:
        print(
            """=== Program Interpolasi ===
        1. Interpolasi Linier
        2. Interpolasi Kuadrat
        3. Polinom Newton
        4. Exit
        """
        )
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                polinier.maininterpolasi()
            elif pilihan == 2:
                polkuadrat.maininterpolkuadrat()
            elif pilihan == 3:
                newton.main()
            elif pilihan == 4:
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def simmod():
    while True:
        print(
            """
        === Program Simulasi Modeling ===
        1. Markov Chain
        2. Monte Carlo
        3. Exit
        """
        )
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                mchain.main()
            elif pilihan == 2:
                mc.main()
            elif pilihan == 3:
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def MainSainkomputasi():
    while True:
        print(
            """
            ===================================
            ===PROJECT AKHIR SAINS KOMPUTASI===
            ===================================
            1. OPERASI MATRIKS
            2. TEKNIK KOMPUTASI
            3. ELIMINASI GAUS
            4. ITERASI
            5. PERSAMAAN LINEAR
            6. INTERPOLASI
            7. SIMULASI MODELING 
            8. exit
            """
        )

        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            matrix.main()
        elif pilihan == 2:
            TeknikKomputasi()
        elif pilihan == 3:
            elimgaus.main()
        elif pilihan == 4:
            jacodel.main()
        elif pilihan == 5:
            persamaanlinear()
        elif pilihan == 6:
            interpolasi()
        elif pilihan == 7:
            simmod()
        elif pilihan == 8:
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


MainSainkomputasi()
