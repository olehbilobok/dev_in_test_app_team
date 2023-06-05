import os
import subprocess
from dotenv import load_dotenv

load_dotenv()


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'takesScreenshot': True,
        'udid': get_device_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        # 'app': os.path.abspath('Ajax Security System_2.28.0_Apkpure.apk')
    }


def get_device_udid():

    try:

        result = subprocess.run([f'{os.environ.get("ADB_PATH")}/adb', 'devices', '-l'], capture_output=True, text=True)
        output = result.stdout.strip()
        lines = output.split('\n')
        if len(lines) > 1:
            udid = lines[1].split()[0]
            return udid

    except subprocess.CalledProcessError:
        print("ADB executable not found.")
        return None
