def results(fields, original_query):
	import urllib
	
	noaa_url = "http://www.wrh.noaa.gov/mtr/getcwfzone.php?sid=MTR&zone=PZ530"
	webcaml_url = "http://www.tradewindssailing.com/publish/img/jpgwebcam.jpg?4463811"

	noaa_weather = urllib.urlopen(noaa_url).read().strip()

	html = """
		<style>
			body {
				background-color: #383534;
				color: #FFFFFF
			}
		</style>
		<h2>NOAA</h2>
			%s
		<h2>Live cam</h2>
			<img src="%s" width="100%%"/>
	"""%(noaa_weather, webcaml_url)
	
	
	return {
		"title": "Treadwinds Weather",
		"run_args": [noaa_url],
		"html": html,
		"webview_links_open_in_browser": True
	}

def run(url):
	import os
	os.system('open "{0}"'.format(url))