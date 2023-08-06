import os

# Specifies the number of minutes to wait before updating the data.
NEWS_TOOLKIT_UPDATE_INTERVAL_MINUTES = int(
    os.getenv("NEWS_TOOLKIT_UPDATE_INTERVAL_MINUTES", 60)
)

# Sets the timeout duration (in seconds) for HTTP requests.
NEWS_TOOLKIT_REQUEST_TIMEOUT = int(os.getenv("NEWS_TOOLKIT_REQUEST_TIMEOUT", 60))

# Determines the maximum depth to which data can be recursively fetched.
NEWS_TOOLKIT_MAX_RECURSION_DEPTH = int(os.getenv("NEWS_TOOLKIT_MAX_RECURSION_DEPTH", 1))
