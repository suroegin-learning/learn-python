from io import BytesIO
from os.path import dirname, abspath

from PIL import Image
from selenium.webdriver import Chrome, ChromeOptions


def screenshot_element(url: str = "", filename: str = "", class_name: str = "", id_name: str = ""):
    """
    Opens headlessly web site, search element and take screenshot of it only.

    :param url: URL address
    :param filename: Filename with or without absolute path.
    :param class_name: Class name of element.
    :param id_name: Id name of element.
    :return: Result dict.

    Result example:

    {
        'status': True,
        'filename': 'yandex_logo_screenshot',
        'path': '/home/.../yandex_logo_screenshot.png',
        'width': 140,
        'height': 100
    }

    """

    base_dir = dirname(abspath(__file__))

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")

    browser = Chrome(
        executable_path="/home/suroegin/chromedriver",
        chrome_options=chrome_options
    )

    if not all([url, filename]):
        return {
            'status': False,
            'message': "No URL and\or filename."
        }

    if any([class_name, id_name]):
        browser.get(url)
    else:
        return {
            'status': False,
            'message': "No class_name or id_name."
        }

    if class_name:
        element = browser.find_element_by_class_name(class_name)
    elif id_name:
        element = browser.find_element_by_id(id_name)

    element_location = element.location
    element_size = element.size

    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))

    left = element_location['x']
    top = element_location['y']
    right = left + element_size['width']
    bottom = top + element_size['height']

    screenshot = screenshot.crop((int(left), int(top), int(right), int(bottom)))


    screenshot.save(f'{filename}.png')

    browser.close()
    browser.quit()

    return {
        'status': True,
        'filename': filename,
        'path': f"{base_dir}/{filename}.png",
        'width': element_size['width'],
        'height': element_size['height']
    }


if __name__ == '__main__':
    print(
    screenshot_element(
        url="https://yandex.ru",
        filename="yandex_logo_screenshot",
        class_name="media-stream__thumbnail"
    )
    )