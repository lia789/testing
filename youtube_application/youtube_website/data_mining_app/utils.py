import googleapiclient.discovery




DEVELOPER_KEY = "AIzaSyAYXQEgYUWmuZC6bkTYnBK01Fo58Y1uEXk"



def get_channel_info(my_input, max_results=5):
    """
    Get information about YouTube channels based on a search query.

    Parameters:
    - my_input (str): The search query to use for retrieving channel information.
    - max_results (int, optional): The maximum number of results to retrieve (default is 5).

    Returns:
    - channel_info (dict): A dictionary where each key is a number from 0 to `max_results`-1,
      and each value is a dictionary with keys 'title', 'description', and 'published' that
      contain the corresponding information about the channel.
    """

    # YouTube API credentials and setup
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name,
        api_version,
        developerKey=DEVELOPER_KEY
    )

    # Search for channels based on the input query
    search_request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        q=my_input,
        type="channel"
    )
    search_response = search_request.execute()

    # Extract the channel IDs from the search results
    channel_ids = [result["id"]["channelId"] for result in search_response["items"]]
    channel_ids_string = ','.join(str(id) for id in channel_ids)

    # Get information about the channels using their IDs
    channel_request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_ids_string
    )
    channel_response = channel_request.execute()

    # Format the channel information as a dictionary
    channel_info = {
        i: {
            "title": channel["snippet"]["title"],
            "description": channel["snippet"]["description"],
            "published": channel["snippet"]["publishedAt"],
        }
        for i, channel in enumerate(channel_response["items"])
    }

    return channel_info



# data = get_channel_info("Python", max_results=5)