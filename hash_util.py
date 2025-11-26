import hashlib
import json

# Function to calculate hashes for a given file
def compute_hashes(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    return {
        "SHA256": hashlib.sha256(content).hexdigest(),
        "SHA1": hashlib.sha1(content).hexdigest(),
        "MD5": hashlib.md5(content).hexdigest()
    }

# Step 1: Hash the original file and save to hashes.json
original_hashes = compute_hashes("original.txt")
with open("hashes.json", "w") as f:
    json.dump(original_hashes, f, indent=4)

print("✔️ Hashes of original.txt:")
for algo, h in original_hashes.items():
    print(f"{algo}: {h}")

# Step 2: Hash the tampered file and compare
tampered_hashes = compute_hashes("tampered.txt")
print("\n🔍 Comparing with tampered.txt:")
match = True
for algo in original_hashes:
    if original_hashes[algo] == tampered_hashes[algo]:
        print(f"{algo}: ✅ Match")
    else:
        print(f"{algo}: ❌ Mismatch")
        match = False

if match:
    print("\n✅ The file is intact. No tampering detected.")
else:
    print("\n⚠️ WARNING: File integrity check FAILED. Tampering detected.")