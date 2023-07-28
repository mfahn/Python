import sys, re, requests, os

#download TOR exit nodes
url = "https://check.torproject.org/torbulkexitlist"
destPath = os.path.join(os.getcwd(), "exitNodes.txt")

response = requests.get(url)
with open(destPath, "wb") as file:
    file.write(response.content)

pattern = r"((\d){1,}\.[\d]{1,}\.[\d]{1,}\.[\d]{1,})"
extractedHosts = []

logFilePath = sys.argv[1]
with open(logFilePath, "r") as logFile:
    # Read lines from log file
    for line in logFile:
        # Get IP addresses from log file
        hosts = re.findall(pattern, line)
        extractedHosts.extend([host[0] for host in hosts])

for host in extractedHosts:
    print(host)

exitNodes = []
with open (destPath, "r") as exitNodesFile:
    for line in exitNodes:
        exitNodes.add(line.strip())

torCount = 0
for host in extractedHosts:
    if host in exitNodes:
        torCount += 1
        print(host + " is a TOR exit Node")

outputFilePath = sys.argv[2]
with open(outputFilePath, "w") as outputFile:
    for host in extractedHosts:
        outputFile.write(str(host) + "\n")

print("Ended with " + str(torCount) + " TOR exit nodes in the log file")