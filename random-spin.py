import discogs_client, random
d = discogs_client.Client('kesmit/0.1', user_token='---YOUR_API_TOKEN_GOES_HERE---')
me = d.identity()
albums = []
print('Fetching collection information from Discogs...')
print('Skipping singles, 7", 10"...')
for item in me.collection_folders[0].releases:
	try:
		if not "7\"" in item.release.formats[0]['descriptions'] and not "10\"" in item.release.formats[0]['descriptions']:
			albums.append(item)
	except KeyError:
		continue
		# print(f"skipping {item}...")
		
print(f"{len(albums)} albums in collection")
		
random_number = random.randint(0,len(albums)-1)
		
album_artist = albums[random_number].release.artists[0].name
album_title = albums[random_number].release.title

print(f'\nYour random selection is :\n\t >>> {album_artist} - {album_title} <<<\n')
		

