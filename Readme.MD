 # YouTube Shorts Presence Reminder

 A Chrome Extension that redirects YouTube Shorts pages to a reminder page, encouraging you to stay present in the real world.

 ## Features

 - Redirects any YouTube Shorts URL (https://www.youtube.com/shorts/*) to a custom reminder page.
 - Displays an encouraging message to stay present.
 - Simple "Go Back" button to return to the previous page.

 ## Installation

 1. Download or clone this repository:
    ```bash
    git clone https://github.com/<username>/<repository>.git
    ```
 2. Open Chrome (or any Chromium-based browser).
 3. Go to `chrome://extensions`.
 4. Enable "Developer mode".
 5. Click "Load unpacked" and select the root directory of this repository.
 6. The extension should now be installed.

 ## Usage

 1. Navigate to any YouTube Shorts video (e.g., `https://www.youtube.com/shorts/{video_id}`).
 2. You'll be redirected to a reminder page.
 3. Click "Go Back" to return to the previous page.

 ## File Structure

 ```
 .
 ├── content.js          # Content script: redirects Shorts pages
 ├── manifest.json       # Extension manifest (v3)
 ├── present.html        # Reminder page
 ├── images/
 │   ├── icon-16.png     # Icon for size 16x16
 │   ├── icon-32.png     # Icon for size 32x32
 │   ├── icon-48.png     # Icon for size 48x48
 │   ├── icon-128.png    # Icon for size 128x128
 │   └── icon.png        # Original icon file (optional)
 └── README.md           # This file
 ```

 ## Contributing

 Contributions are welcome! Feel free to submit issues or pull requests.