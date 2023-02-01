import urllib
import urllib.parse, urllib.request, re


def findYt(search):
    try:
        queryString = urllib.parse.urlencode({"search_query": search})
        html_content = urllib.request.urlopen(
            "http://www.youtube.com/results?" + queryString)

        searchResults = re.findall(r"watch\?v=(\S{11})",
                                   html_content.read().decode())

        return "http://www.youtube.com/watch?v=" + searchResults[0]

    except:
        return "Cant find something :( try again"
