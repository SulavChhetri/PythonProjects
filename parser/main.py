import json


def main():
    filecontainer = list()
    with open('file.txt', 'r')as file:
        lines = [line.rstrip('\n') for line in file]
        lines = lines[5:]
    for item in lines:
        y = 0
        x = item.split("    ")
        for i in range(int(len(x)/3)):
            filecontainer.append({
            'State': x[y],
            'Postal Abbr': x[y+1],
            'FIPS Code': x[y+2]})
            y=3
            
    with open('parsed.json', 'w')as file:
        json.dump(filecontainer, file)

if __name__ == "__main__":
    main()
