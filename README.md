# prism_challenge
Programming challenges for Prism

Challenge 1: The Prism Team

How to run:
Install beautifulsoup4 (Mac: sudo pip install beautifulsoup4) (Linux: sudo apt-get install python-bs4)

Run python the-prism-team.py

* When I tried to do a GET request over HTTPS for the most recent version of the 'About Us' page, I get a 'EOF occurred in violation of protocol' or Connection aborted.', error(54, 'Connection reset by peer') error. So I stored a copy of the HTML of the site in data/aboutus.txt and parses the HTML from the file instead. However, the methods I tried work on other websites such as 'https://yahoo.com' and 'https://google.com'

Why I chose Python:
The Beautiful Soup library for Python is an extremeley powerful and easy-to-use library for parsing HTML.

Primary design decisions:
I chose to use an off-the-shelf library (Beautiful Soup) for parsing HTML instead of writing my own parser because of the library's very strong capablities and ease to use. 

Expected outout:
There are 38 people on the prism team. They are:
	Steve Russell, CEO & Founder
	Mike Fogel, VP of Engineering
	Bob Cutting, SVP of Operations
	...
	Huu Nguyen, Platform Engineer


Challenge 2: Image Library

Example Usage: (Can run by simply calling python image-library.py)
	image = Image(20, 30, 'int', 'rgb')
	print image
	print image.width()
	print image.height()
	print image.copy()
	print image.get(2, 3)
	image.set(2, 3, [2, 3, 4])
	print image.get(2,3)

Expected Output:
	<__main__.Image object at 0x108d9b2d0>
	20
	30
	<__main__.Image object at 0x109161850>
	[0 0 0]
	[2 3 4]

Why I chose Python:
While Java may be the most natural choice for OOP, Python also supports OOP, and Python has very useful libraries for performing computations on images/arrays in NumPy.

Primary design decisions:
I chose to to store the image (RGB or Grey, Int or Float) in 2D NumPy arrays. The upsides are that indexing is intuitive and operations such as scaling and convolution are simple with NumPy. The downside is that more space is needed.

Hoping to do next:
I was hoping to implement convolution and scaling, which can be easily done using NumPy's built-in methods.



Challenge 3: Vacationing Salesman

How to run:
Install geopy (Mac: sudo pip install geopy) (Linux: https://github.com/geopy/geopy)
Run python vacationing-salesman.py --cities=../data/cities.txt --useKM=1
(--cities argument specifies the file containing the locations, default='../data/cities.txt' --useKM argument initiates the conversion from miles to KM, default=False)

Expected output:
	Success! Your vacation itinerary is:
	Paris, France -> New York City, USA: 5816.47439608 kilometers
	New York City, USA -> Nuuk, Greenland: 2962.56011916 kilometers
	Nuuk, Greenland -> Tokyo, Japan: 9000.32749332 kilometers
	Total distance covered in your trip: 17779.3620086 kilometers

Primary design decisions:
I chose to use the Python library geopy, because it contains functionalities of determining longitutde/latitude of estimate address names and computing distances between longitude/lattitude coordinates.

Hoping to do next:
I was hoping to have time to include the option to minimize total distance traveled. I would have done this by building a graph of cities/locations all vertices are connected to all other vertices and the edges are the distances between two cities/locations. Then the Floyd-Warshall algorithm can be used to find the shortest path: minimum travel distance. 

