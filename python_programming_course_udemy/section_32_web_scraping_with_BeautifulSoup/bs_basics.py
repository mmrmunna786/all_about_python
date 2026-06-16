from bs4 import BeautifulSoup  # library for web scraping

# arbitray html to demonstrate how to use BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
# ==========================================================
"""
Parsing and Navigating HTML with BeautifulSoup
=> BeautifulSoup is a library that makes it easy to scrape information from web pages.
=> It sits on top of an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
=> BeautifulSoup transforms a complex HTML document into a complex tree of Python objects, such as tags, navigable strings, or comments.

=> BeautifulSoup( html_string, "html.parser" ) - parse HTML using the built-in HTML parser
=> Once parsed, there are several ways to navigate through the HTML tree:
  => By Tag Name
  => Using find - returns one matching element
  => Using find_all - returns a list of all matching tags
"""
soup = BeautifulSoup(html, "html.parser")
d = soup.find("div")  # returns first occurence of div element as an object
print(d, "\n")
d2 = soup.find_all("div")  # returns all occurence of div elements in a list
print(d2, "\n")
using_id = soup.find(
    id="first"
)  # returns the element as an object which has the id equal to "first"
print(using_id, "\n")
using_class = soup.find_all(
    class_="special"
)  # returns the elements in a list which has the class equal to "special"
print(using_class, "\n")
using_html_attributes = soup.find_all(
    attrs={"data-example": "yes"}
)  # returns the elements in a list which has the attribuite equal to "data-example"
print(using_html_attributes, "\n")
"""
Using CSS style selectors
=> select - returns a list of elements matching a css selector
=> CSS slector basic cheatsheet
  => select by id of foo: #foo
  => select by class of bar: .bar
  => select children: div > p
  => select descendents: div p
"""
css_id_selector = soup.select(
    "#first"
)  # returns a list containing html tag which is associated with id equal to "#first"
print(css_id_selector, "\n")
css_class_selector = soup.select(
    ".special"
)  # returns a list containing html tags which is associated with class equal to ".special"
print(css_class_selector, "\n")
tag_selector = soup.select(
    "div"
)  # returns a list containing all html div tags separated by a comma
print(tag_selector, "\n")
attribute_selector = soup.select(
    "[data-example='yes']"
)  # returns a list containing html tags which have the attribute data-example equal to 'yes'
print(
    attribute_selector, "\n"
)  # note the square brackets around the attribute selector in the previous line of code
"""
Accessing Data in Elements
=> get_text - access the inner text in an element
=> name - tag name
=> attrs - dictionary of attributes associated with the tag
=> we can also access attributes values using brackets
"""
an_html_element = soup.select(".special")
print(
    an_html_element[0].get_text(), "\n"
)  # returns the inner text of the first element in the list
for element in soup.select(".special"):
    print(element.name)  # returns the name of the tag for each element in the list
    print(element.attrs["class"][0], "\n")  # returns the attributes of the tag for each element in the list
'''
Navigating with BeautifulSoup via HTML tags using:
=> Via tags:
	=> parent / parents
	=> contents
	=> next_sibling / next_siblings
	=> previous_sibling / previous_siblings
 => Via Searching:
	=> find_parent / find_parents
	=> find_next_sibling / find_next_siblings
	=> find_previous_sibling / find_previous_siblings
'''
parent_tag = soup.select(".special")[0].parent  # returns the parent tag of the first element in the list which is the <ol> tag 
print(parent_tag, "\n") 
using_next_sibling = soup.body.contents[1].next_sibling.next_sibling # using contents and next_sibling to get the second div tag in the body
print( using_next_sibling, "\n" )
using_previous_sibling = soup.body.contents[3].previous_sibling.previous_sibling # using contents and previous_sibling to get the fourth div tag in the body
print( using_previous_sibling, "\n" )

using_find_parent = soup.select(".special")[0].find_parent() # returns the parent tag of the first element in the list which is the <ol> tag
print(using_find_parent, "\n")
using_find_next_sibling = soup.select(".special")[0].find_next_sibling() # returns the next sibling tag of the first element in the list which is the <li> tag
print(using_find_next_sibling, "\n")
using_find_previous_sibling = soup.select(".special")[1].find_previous_sibling() # returns the previous sibling tag of the first element in the list which is None since the first element in the list is the first <li> tag
print(using_find_previous_sibling, "\n")
