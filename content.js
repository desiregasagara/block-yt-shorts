// content.js
// Redirect YouTube Shorts pages to a reminder page
if (window.location.pathname.startsWith('/shorts/')) {
  const reminderUrl = chrome.runtime.getURL('present.html');
  window.location.replace(reminderUrl);
}