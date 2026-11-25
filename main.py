import os

LINE = ("My manager promised unlimited growth — he meant the meetings, not my salary.")

def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
