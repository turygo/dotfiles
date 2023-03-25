#!/usr/bin/env python

import os
import sys


def main():
	if len(sys.argv) != 2:
		print("This script check all files in the dir and remove files small than 1GB")
		print("Usage: ./clean_small_files.py <dir_path>")
		sys.exit(1)

	dir_path = sys.argv[1]

	if not os.path.isdir(dir_path):
		print(f"Error: {dir_path} is not a valid directory path.")
		sys.exit(1)

	video_files_exist = False
	for root, dirs, files in os.walk(dir_path):
		for file in files:
			if file.endswith(".mp4") or file.endswith(".mkv"):
				video_files_exist = True
				break
		if video_files_exist:
			break

	if not video_files_exist:
		print("No mp4/mkv files found in the specified directory and its sub-directories.")
		return

	# Get all files less than 1 GB
	file_size_threshold = 1000000000  # bytes
	small_files = []
	for root, dirs, files in os.walk(dir_path):
		for file in files:
			file_path = os.path.join(root, file)
			if os.path.getsize(file_path) <= file_size_threshold:
				small_files.append(file_path)

	# Print the list of small files
	if not small_files:
		print("No small files found.")
	else:
		print("The following small files (<1GB) were found:")
		for file in small_files:
			print(file)

	# Ask user if they want to delete files
	response = input("Do you want to remove these files? (Y/N): ")
	if response.lower() == "y":
		for file in small_files:
			os.remove(file)


if __name__ == "__main__":
	main()
