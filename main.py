import svd
from colorama import Fore, Back, Style
def main():
	
	f = open("banner.txt", "r")

	print(Fore.CYAN  + f.read() + Style.RESET_ALL)		

	user_link = input("Paste the video link:")

	if "youtube" in user_link:
		svd.youtube(user_link)
	elif "reddit" in user_link:
		svd.reddit(user_link)
	else:
		print(f"{Back.RED} This platfrom is not supported! {Style.RESET_ALL}")

if __name__ == "__main__":
	main()
