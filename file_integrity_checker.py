import hashlib


def calculate_hash(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


print("=" * 45)
print("      FILE INTEGRITY CHECKER")
print("=" * 45)

filename = input("Enter file name: ")

file_hash = calculate_hash(filename)

if file_hash:
    print("\nSHA-256 Hash:")
    print(file_hash)

    print("\nSave this hash safely.")
    print("Use it later to verify whether the file has changed.")
else:
    print("\nFile not found.")