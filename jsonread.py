import json


def readjson():
    lines = []
    dataSet = []
    with open("jobs.csv", "r", encoding="utf-8") as file:
        lines = file.read().split("\n")
        file.close()

    for line in lines:
        try:
            obj = {}
            obj["title"] = line.split(",")[0]
            obj["location"] = line.split(",")[1]
            obj["company"] = line.split(",")[2]
            obj["link"] = line.split(",")[3]
            # obj["image"] = line.split(",")[4]
            dataSet.append(obj)

        except:
            pass

        # jobsread = str(dataSet)
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(dataSet, f, indent=4)  # indent for pretty printing
        # f.write(jobsread)
        f.close()


readjson()
