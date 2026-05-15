import time
import random
import concurrent.futures
import multiprocessing


# Membuat kategori serangan sebagai contoh uji
kategori_serangan = ["NORMAL","SQL-INJECTION","DDOS-ATTACK","XSS-ATTACK"]


def proses_log(tugas):
    deteksi = random.choice(kategori_serangan)

    # Simulasi delay pemrosesan log
    time.sleep(0.002)
    return deteksi

def cetak_hasil(metode, rekap_traffic, waktu):
    print(f"\n=====================================================")
    print(f"-- HASIL ANALISIS KOMPUTASI {metode} --")
    print(f"\n=====================================================")
    print(f"Total Traffic NORMAL        : {rekap_traffic.get('NORMAL',0)}")
    print(f"Total Traffic SQL INJECTION : {rekap_traffic.get('SQL-INJECTION',0)}")
    print(f"Total Traffic DDOS ATTACK   : {rekap_traffic.get('DDOS-ATTACK',0)}")
    print(f"Total Traffic XSS ATTACK    : {rekap_traffic.get('XSS-ATTACK',0)}")
    print(f"-------------------------------------------------------------------")
    print(f"Total Waktu : {waktu:.2f} detik")
    print(f"========================================================")

def main():
    total_tugas     = 5000
    daftar_tugas    = list(range(1, total_tugas + 1)) 

    # 1. KOMPUTASI SEKUENSIAL
    rekap_sekuensial = {"NORMAL":0,"SQL-INJECTION":0,"DDOS-ATTACK":0,"XSS-ATTACK":0}
    start_time = time.time()

    for tugas in daftar_tugas:
        hasil = proses_log(tugas)
        rekap_sekuensial[hasil] += 1
    
    waktu_sekuensial = time.time() - start_time
    cetak_hasil("SEKUENSIAL", rekap_sekuensial, waktu_sekuensial)

    # 2. KOMPUTASI MULTITHREADING
    rekap_thread = {"NORMAL":0,"SQL-INJECTION":0,"DDOS-ATTACK":0,"XSS-ATTACK":0}
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        hasil_thread = executor.map(proses_log, daftar_tugas)

        for hasil in hasil_thread:
            rekap_thread[hasil] += 1
        
    waktu_thread = time.time() - start_time
    cetak_hasil("MULTITHREADING", rekap_thread, waktu_thread)
    
    # 3. KOMPUTASI MULTIPROSES
    jumlah_core = multiprocessing.cpu_count()
    rekap_process = {"NORMAL":0,"SQL-INJECTION":0,"DDOS-ATTACK":0,"XSS-ATTACK":0}
    with concurrent.futures.ProcessPoolExecutor(max_workers = jumlah_core) as executor:
        hasil_prosess = executor.map(proses_log, rekap_process)

        for hasil in hasil_prosess:
            rekap_process[hasil] += 1
    
    waktu_prosess = time.time() - start_time
    cetak_hasil("MULTIPROSESSING", rekap_process, waktu_prosess)

if __name__ == "__main__":
    main()
