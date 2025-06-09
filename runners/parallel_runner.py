import os
import subprocess
from multiprocessing import Pool

def run_browser(browser):
    env = os.environ.copy()
    env["BROWSER"] = browser
    return subprocess.call(["behave", "features/"], env=env)

if __name__ == "__main__":
    browsers = ["chrome", "firefox"]
    with Pool(len(browsers)) as p:
        p.map(run_browser, browsers)