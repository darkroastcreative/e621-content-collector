import json
import requests
from requests import Response

## Declare and initialize a set representing the tag sets that the downloader
# should download content with.
tag_sets: set = {}

# TODO: Document!
# TODO: Add option for alternative tag_sets.txt file name/location.
def read_tag_sets() -> set:
    # Declare and initialize a localized version of tag_sets that can be
    # manipulated independent of the "main" set of tag sets.
    tag_sets: set = {}

    # Open the tag sets file (tag_sets.txt by default), read its contents in as
    # a set, clean the values read into the set, and sort the set to prepare it
    # for use by the core downloader logic.
    with open('tag_sets.txt', 'r') as tag_sets_file:
        # Read the tag set file's contents in as a set.
        tag_sets = set(tag_sets_file.readlines())

        # Clean the values in the tag sets set by removing newlines. This will
        # make it easier to use these values in the core downloader logic.
        for tag_set in tag_sets:
            # Remove the raw value from the set.
            tag_sets.remove(tag_set)

            # Replace any escaped newlines with the empty string in the tag
            # set.
            tag_set = tag_set.replace('\n', '')

            # Added the cleaned version of the tag set back to tag_sets for
            # further processing.
            tag_sets.add(tag_set)

        # Sort the set of tag sets. This isn't necessary, but can make it
        # easier to track download progress.
        #
        # TODO: Consider making this optional (with the default being that
        # tag_sets is not sorted). This could be helpful for more extreme cases
        # where users are trying to download content associated with a massive
        # number of tag sets at once.
        tag_sets = sorted(tag_sets)

        return tag_sets
        

# TODO: Document!
# TODO: Consider adding an option where no tag set is specified, which would
# trigger a download of the latest posts.
def download(tag_set: str) -> None:
    # Replace spaces in the tag set with the URL encoded version of the space
    # character. While this isn't necessarily necessary, it makes requests to
    # the e621 API more proper.
    tag_set_string: str = tag_set.replace(' ', '%20')

    # Declare and initialize a variable to track which page of posts the
    # downloader is requesting content from. This is necessary because the e621
    # API returns content data in pages rather than all at once.
    page_number = 1

    # Decare and initialize a dictionary of headers to include with the content
    # request to e621. This *should* just be the user agent that identifies the
    # tool to e621 (per e621's requirement for user agent information for API
    # requests).
    headers: dict = {'User-Agent': 'darkroastcreative/e621-content-collector'}

    # Submit a request to the e621 API for posts matching the provided tag set and page number.
    response: Response = requests.get(url=f'https://e621.net/posts.json?tags={tag_set_string}&page={page_number}', headers=headers)

    # Process the response from the e621 API.
    if response.status_code == 200:
        print()
        # TODO: Implement logic to parse the returned JSON, download posts, and
        # navigate through pages of posts.
        # NOTE: The e621 API doesn't provide the number of pages or whether
        # there is a next page in responses to the API request used. However,
        # the API will only return up to 750 pages of data. With this in mind,
        # the way to see if there is more content available to download is to
        # keep requesting additional pages until either we receive a page with
        # no posts or we reach the 750th page (whichever comes first).
        
        # Parse the response JSON from the e621 API to a Python object for
        # processing. This line grabs justs the content of the "posts" property
        # of the response because that's the part needed to parse and download
        # the posts referenced in the response.
        posts = json.loads(response.content)['posts']

        for post in posts:
            id: int = post['id']
            url: str = post['file']['url']
            tags_general = []
            tags_artist = []
            tags_contributor = []
            tags_copyright = []
            tags_character = []
            tags_species = []
            tags_meta = []
            tags_lore = []

tag_sets = read_tag_sets()

# Loop through the set of tag sets to download posts associated with each tag
# set.
for tag_set in tag_sets:
    download(tag_set=tag_set)