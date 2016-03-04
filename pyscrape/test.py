import browser

def main():
	mybrowser = browser.Browser()
	print mybrowser.get("http://www.google.com")
	print mybrowser.post("http://www.google.com")

if __name__ == "__main__":
	main()