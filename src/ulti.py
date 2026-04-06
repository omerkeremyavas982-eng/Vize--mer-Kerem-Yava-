import socket

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except:
        return None

def save_results(target, results):
    filename = f"{target}_scan.txt"
    with open(filename, "w") as f:
        for port, banner in results:
            f.write(f"Port {port} açık | Servis: {banner}\n")
    
    print(f"\n[+] Sonuçlar {filename} dosyasına kaydedildi.")
