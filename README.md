# ZoomEnum {Alpha}

ZoomEnum is a pythonic bruteforce/enumeration tool for finding zoom meeting IDs.
ZoomEnum aims to out perform web based implimentations by using the local
zoom application, in conjunction with a UI automation tool 'pyautogui'.

## ZoomEnum Features

- Is not blocked by captcha's or rate limiting unlike web implimentations
- Lightweight, only one dependency 
- Cross platform 

## Disclaimer 

This tool was designed as a proof of concept. It is not intended for use in
attacking confidential meetings, but rather to demonstrate the necessity of using
strong passwords to protect zoom meetings.

## Usage

1. Install 'pyautogui'
     
       pip install pyautogui
       
2. Clone the repository

       git clone https://github.com/AngusCornall/ZoomEnum.git && cd ZoomEnum
       
3. Run 'main.py'

       python3 main.py
       
4. Open zoom and take a screenshot of the "Join a Meeting" button

5. Enter the path to the screenshot

## Alpha Release Details

- The script currently is capable of running without interaction until the first valid meeting ID is found. The next release will support fully headless runs.
- Screenshoting the "Join a Meeting" button is currently neccessary because of an issue with the 'pyautogui' library being used.
       
