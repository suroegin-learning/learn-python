from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()

arguments = [
    "--headless",
    "--no-sandbox",
    "--no-referrers",
    "--start-maximized",
    "--ignore-certificate-errors",
    "--disable-breakpad", "--disable-client-side-phishing-detection", "--disable-session-crashed-bubble",
    "--disable-cast-streaming-hw-encoding", "--disable-cloud-import", "--disable-popup-blocking",
    "--disable-ipv6",
    "--disable-impl-side-painting", "--disable-setuid-sandbox", "--disable-seccomp-filter-sandbox",
    "--disable-cast",
    "--allow-http-screen-capture"
]

for argument in arguments:
    options.add_argument(argument)

chrome_for_google = Chrome(
    executable_path='/home/suroegin/chromedriver',
    options=options
)
chrome_for_yandex = Chrome(
    executable_path='/home/suroegin/chromedriver',
    options=options
)


