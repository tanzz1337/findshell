# MASIH DALAM TAHAP PENGEMBANGAN !
import requests

def scan_backdoor(url):
    # contoh list file atau penamaan backdoor
    # dapat ditambah jika mengetahui nama backdoor
    backdoor_files = [
        "shell.php",
        "backdoor.php",
        "admin.php",
        "admin/index.php",
        "admin/login.php"
    ]
    for backdoor_file in backdoor_files:
        # konstruksi url
        full_url = url + "/" + backdoor_file
        try:
            # make a GET request to the URL
            response = requests.get(full_url)
            # cek kode respon
            if response.status_code == 200:
                print("[+] Backdoor Found:", full_url)
            #elif response.status_code == 404:
                print("[+] Request Reject: Not Found !")
            else:
                print("[-] No Backdoor Found:", full_url)
        except:
            print("[-] No Backdoor Found:", full_url)

# masukan url target
scan_backdoor("https://www.jakarta.go.id")
