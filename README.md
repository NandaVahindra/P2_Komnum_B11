# P2_Komnum_B11
## Kelompok 11

1. Farrela Ranku Mahhisa 5025211129
2. Nur Azizah 5025211252  
3.  Made Nanda Wija Vahindra 5025211160

Metode Trapezoidal merupakan metode yang dinilai paling efisien dalam menghitung luas bangun tak beraturan.
Salah satu kelemahan dari metode Trapezoidal adalah kita harus menggunakan jumlah interval yang besar untuk memperoleh akurasi yang diharapkan.  
  
Program ini dibuat untuk menjelaskan bagaimana metode Integrasi Romberg dapat mengatasi kelemahan tersebut dengan library sebagai berikut  
https://github.com/NandaVahindra/P2_Komnum_B11/blob/43a667182135b9a6326ed4e29c8f83b1e90e2086/Praktikum_KomputasiNumerik.py#L1-L2
  
Terdapat fungsi yang akan diintegrasikan disini digunakan x²  
https://github.com/NandaVahindra/P2_Komnum_B11/blob/43a667182135b9a6326ed4e29c8f83b1e90e2086/Praktikum_KomputasiNumerik.py#L5-L6
  
Fungsi untuk metode trapezoidal  
https://github.com/NandaVahindra/P2_Komnum_B11/blob/43a667182135b9a6326ed4e29c8f83b1e90e2086/Praktikum_KomputasiNumerik.py#L11-L16
  
Menghitung nilai integral dengan metode trapezoidan dan integrasi romberg (scipy.integrate.romberg()) dengan nilai  yang telah ditetapkan sebagai berikut
https://github.com/NandaVahindra/P2_Komnum_B11/blob/f9ef145e757b2d6a4a0d252ccca2c33e46c34468/Praktikum_KomputasiNumerik.py#L19-L23
  
Hasil sebenarnya dari integral x² dari 0 sampai 2 adalah 0.33333333, lalu ditampilkan error masing masing metode sebagai berikut
https://github.com/NandaVahindra/P2_Komnum_B11/blob/f9ef145e757b2d6a4a0d252ccca2c33e46c34468/Praktikum_KomputasiNumerik.py#L26-L28 

terlihat bahwa error relatif dari trapezoidal menunjukkan angka 0.03125 sedangkan pada integrasi romberg dengan nilai 0.0  
![image](https://user-images.githubusercontent.com/114988957/209049341-dc7590a4-0503-49c4-856d-5295cf16d225.png)  
dari hasil yang didapatkan, dapat kita buktikan bahwa Kelemahan dari metode trapezoidal adalah harus menggunakan jumlah interval yang besar untuk akurasi yang tinggi dan hal tersebut dapat diatasi dengan menggunakan Integrasi Romberg
