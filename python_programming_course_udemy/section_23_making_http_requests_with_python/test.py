# making the most basic http get request
# import requests

# url = "http://www.google.com"
# response = requests.get( url )

# print( f"\n\nyour request to {url} came back w/ status code is {response.status_code}\n\n" )
# ============================================================================================

# # requesting json with python
# import requests  # importing the library

# url = "https://icanhazdadjoke.com/search"  # storing the url in a variable
# res = requests.get(
#     url, params={"term": "cat", "limit": 1}, headers={"Accept": "application/json"}
# )  # make a get request and strore the response in variable called res

# json_data = res.json()
# # print( json_res['joke'] )
# print(json_data['results'])
# ============================================================================================


