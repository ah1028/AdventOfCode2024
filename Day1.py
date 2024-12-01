from urllib.request import Request, urlopen

# The URL for the input data
url = "https://adventofcode.com/2024/day/1/input"

# Replace this with your session cookie from Advent of Code

# Create a request with the session cookie in the headers
request = Request(url)
request.add_header("Cookie", f"session={SESSION_COOKIE}")
request.add_header("User-Agent", "Python urllib for Advent of Code")

# Fetch the page
try:
    with urlopen(request) as response:
        html_bytes = response.read()
        html = html_bytes.decode("utf-8")
        data = (html.replace("\n", " ")).split(" ")
        list1, list2 = [], []
        for a in range(0, len(data)-1, 4):
            list1.append(data[a])
            list2.append(data[a+3])
except Exception as e:
    print(f"An error occurred: {e}")

