import os, sys, hashlib, zipfile, json, shutil
from glob import glob as re

"""
file=
hash=$(file).sums
default:: build
size=2G
build: hash split
hash:
	@echo Creating a hash 512 of the file
	@sha512sum $(file) >> $(hash)
verify:
	@echo Verifying the sums file
	@shaa512sum -c $(hash)
split:
	@echo Splitting the original file
	@split -b $(size) --verbose $(file) split_file_
	@echo Zipping files
	@for f in split_file_*;do echo $$f;7z a $$f.zip $$f -sdel -mx=0;done
join:
	@echo Unzipping files
	@for f in split_file_*zip;do echo $$f;7z x $$f;done
	@echo Removing all of the *.zip files
	@rm split_file_*zip
	@echo Joining the files
	@cat split_file_* > $(file)
	@echo Removing the split files
	@rm split_file_*
	@echo Checking the hash file
	@sha512sum -c $(hash)
	#@echo Unzipping the files
	#@7z x $(file)
	@Removing the zip file
	@rm $(file)

"""

def readBin(foil):
	with open(foil,'rb') as reader:
		return reader.read()

def hash(foil, hash_function = hashlib.sha1, sums_file:bool=True):
	hashing = hash_function()
	with open(foil, 'rb') as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hashing.update(chunk)
	if sums_file:
		with open(foil + '.sums', 'a') as f:
			json.dump(str({"hash":hashing.hexdigest()}),f)
	return hashing.hexdigest()

def verify(foil, hash_function = hashlib.sha1):
	verified, set_hash, hash = False, 0, str(foil + '.sums').replace('.sums.sums','.sums')
	with open(hash, 'r') as f:
		set_hash = json.loads(str(f.readlines()[0]).replace('"','').replace("'",'"'))['hash']
	verified = hash_function(readBin(foil)).hexdigest() == set_hash
	if verified:
		os.remove(foil + '.sums')
	return verified

def split(foil, CHUNK_SIZE = 100_000_000): #100MB
	foils_created,file_number, failure = [],1, False
	CHUNK_SIZE = CHUNK_SIZE - 30653
	with open(foil,'rb') as f:
		try:
			chunk = f.read(CHUNK_SIZE)
			while chunk:
				current_file = foil.replace('.zip','') + '_broken_up_' + str(str(file_number).zfill(10))
				with open(current_file, "wb+") as chunk_file:
					chunk_file.write(chunk)
				with zipfile.ZipFile(current_file+".zip", 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
					zip_file.write(current_file, current_file)
				foils_created += [current_file + ".zip"];os.remove(current_file)
				file_number += 1;chunk = f.read(CHUNK_SIZE)
		except Exception as e:
			print(f"Exception :> {e}")
			failure = True

	if not failure:
		os.remove(foil)
	return foils_created

def join(foil, quiet=True):
	foil = foil.replace('.sums','')
	mini_foils,current_binary = re(str(foil).replace('.zip','') + "_broken_up_*.zip"),None
	mini_foils.sort()
	for mini_foil in mini_foils:
		raw_foil = mini_foil.replace('.zip','')
		with zipfile.ZipFile(mini_foil,"r") as f:
			raw_foil = f.extract(member=raw_foil, path=os.path.dirname(mini_foil))
		if current_binary is None:
			current_binary = readBin(raw_foil)
		else:
			current_binary += readBin(raw_foil)
		shutil.rmtree(os.path.dirname(raw_foil), ignore_errors=True);os.remove(mini_foil)
	with open(foil, 'wb') as fp:
		fp.write(current_binary)
	hashFile = foil + ".sums"
	if os.path.exists(hashFile):
		try:
			currentHash = hash(foil)
			with open(hashFile, 'r') as reader:
				oldHash = json.load(reader)['hash']
			equal = "===" if currentHash == oldHash else "=!="
			if not quiet:
				print("The old hash {0} the current hash".format(equal))
		except:
			if not quiet:
				print("File {0} cannot be verified".format(foil))
	else:
		if not quiet:
			print("File {0} cannot be verified".format(foil))
	return foil

def arguments():
	import argparse
	parser = argparse.ArgumentParser(description=f"Enabling the capability to stretch a single large file into many smaller files")
	parser.add_argument("-f","--file", help="The name of the file", nargs='*')
	parser.add_argument("--split", help="Split the file up", action="store_true",default=False)
	parser.add_argument("--join", help="Recreate the file", action="store_true",default=False)
	parser.add_argument("--template", help="Create a copy of this file specific to a large file", action="store_true",default=False)
	return parser.parse_args()

def splitt(foil):
	hash(foil);split(foil)

def joinn(foil):
	join(foil);verify(foil)

def template(workingfoil):
	with open(__file__, "r") as reader:
		with open(workingfoil + ".py", "w+") as writer:
			for line in reader.readlines():
				line = line.rstrip()
				if "workingfoil = argz.file[0]" in line:
					line = line.replace("argz.file[0]", "\""+workingfoil+"\"")
				writer.write(line+"\n")

def main(foil:str,splitfile:bool=False, joinfile:bool=False):
	if splitfile:
		splitt(foil)
	elif joinfile:
		joinn(foil)

if __name__ == '__main__':
	argz = arguments();workingfoil = argz.file[0]
	if argz.template:
		template(workingfoil)
		print(workingfoil + ".py")
	else:
		if argz.split and argz.join:
			print("Cannot use both both split and join")
		elif not os.path.exists(argz.file[0]):
			print("The file {file} does not exist".format(file=argz.file[0]))
		else:
			main(workingfoil, splitfile=argz.split, joinfile=argz.join)
