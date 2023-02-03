import subprocess
import time

print("\nKurulum baslatiliyor...")
time.sleep(2)

subprocess.call(["apt-get", "install", "mitmproxy"])
subprocess.call(["pip", "install", "colorama"])

print("\nKurulum tamamlandi.")
