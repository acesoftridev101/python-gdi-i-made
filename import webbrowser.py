import webbrowser


url1 = 'https://www.google.com/search?q=tlabs+engineering+the+future&client=firefox-b-1-d&hs=rR5o&sca_esv=694dde5cb9c6d8d7&sxsrf=AE3TifPUTeQIQVskV1R3GSsbIubBq79MXw%3A1767305726736&ei=_vFWaenWLIasptQP25_26AI&oq=tlabs&gs_lp=Egxnd3Mtd2l6LXNlcnAiBXRsYWJzKgIICDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI13NQ9zBYmDVwAXgBkAEAmAG9AaABwAWqAQMxLjS4AQHIAQD4AQGYAgagAtwFqAIQwgIHECMYJxjqAsICEBAjGKAGGCcY6gIYqwYY3QXCAhcQABiABBiRAhi0AhjnBhiKBRjqAtgBAcICChAjGIAEGCcYigXCAgQQIxgnwgILEAAYgAQYkQIYigXCAgoQABiABBhDGIoFwgIWEC4YgAQYsQMY0QMYQxiDARjHARiKBcICEBAAGIAEGLEDGEMYgwEYigXCAhEQLhiABBixAxjRAxiDARjHAcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMYgwEYigXCAg0QABiABBixAxhDGIoFwgIIEC4YgAQYsQPCAgsQLhiABBjHARivAcICEhAuGIAEGLEDGNEDGMcBGAoYC5gDCfEFxcj4VbVDjG-6BgYIARABGAGSBwMyLjSgB6M_sgcDMS40uAfTBcIHBTAuMi40yAcUgAgA&sclient=gws-wiz-serp'
url2 = 'http://www.stackoverflow.com'

# Open the first URL in a new window/tab (default behavior)
webbrowser.open(url1)

# Open the second URL specifically in a new tab
webbrowser.open_new_tab(url2)

import webbrowser
import time
import random

# List of URLs to choose from
URLS = [
    'https://www.google.com',
    'https://www.wikipedia.org',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.python.org',
    'https://www.reddit.com'
]

def open_random_tabs_for_duration(duration_seconds=10, num_tabs=2):
    """
    Opens random URLs in new browser tabs and waits for a specified duration.
    """
    tabs_opened = []
    try:
        # Open the specified number of random URLs in new tabs
        for _ in range(num_tabs):
            url = random.choice(URLS) # Select a random URL
            # The 'new=2' parameter requests a new tab (default behavior)
            webbrowser.open_new_tab(url)
            tabs_opened.append(url)
        
        print(f"Opened {len(tabs_opened)} random tabs. Waiting for {duration_seconds} seconds...")
        
        # Wait for the specified duration
        time.sleep(duration_seconds)
        
        print("Wait time finished. The tabs will remain open.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # You can change the number of tabs by modifying the num_tabs parameter
    open_random_tabs_for_duration(duration_seconds=10, num_tabs=3)

import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 7
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

# start recording

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=1)

print(f'Recording for {RECORD_SECONDS} seconds...')

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    print(f'Recorded {i * CHUNK} frames')

sys.stdout.flush()

print('I have recorded the audio. if you were doing something weird then stop it now.')

stream.stop_stream()
stream.close()

audio.terminate()
print('we have terminated the audio')

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

print('Hey also your file output.wav is ready btw')

print('Exiting now. Goodbye.')
import pygame
import time

def draw_triangle_for_10_seconds():
    # Initialize the game engine
    pygame.init()

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Set the screen dimensions (width, height)
    size = [400, 400]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("GDI Triangle Effect")

    # Start time
    start_time = time.time()
    running = True

    # Main loop
    while running:
        # Check if 10 seconds have passed
        if time.time() - start_time > 10:
            running = False

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing logic
        screen.fill(BLACK) # Clear screen to black

        # Define the points of the triangle (x, y coordinates)
        # The coordinates are relative to the top-left corner of the window
        points = [
            (200, 70),  # Top point
            (50, 300),  # Bottom-left point
            (350, 300)  # Bottom-right point
        ]
        
        # Draw a filled triangle polygon
        pygame.draw.polygon(screen, WHITE, points)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)

    # Tidy up and close the window
    pygame.quit()

if __name__ == "__main__":
    draw_triangle_for_10_seconds()

import math
import time
import win32gui
import win32api
import win32con
import random

import time
import math
import random
import win32gui
import win32api
import win32con
from threading import Thread
import time
from GDI_effects.GDI import *
from threading import Thread

def run_gdi_effect(duration):
    """
    Runs a GDI effect (color inversion) for a specified duration.
    """
    start_time = time.time()
    # Invert screen colors - this function runs a loop until manually stopped or a condition is met
    # We use a thread to control the duration externally
    # The 'repeat' parameter in the library functions usually refers to the number of effect iterations, not time.
    # We will use our own timer.
    print(f"GDI effect started for {duration} seconds...")
    while time.time() - start_time < duration:
        # Continuously invert the screen
        Effects.invert_screen(repeat=1) # Repeat=1 for continuous effect within the loop
        time.sleep(0.01) # Small sleep to prevent 100% CPU usage
    print("GDI effect stopped.")

if __name__ == '__main__':
    effect_duration = 10 # seconds

    # GDI effects can be disruptive and are best run in their own thread
    # to manage the time limit without blocking the rest of the program.
    effect_thread = Thread(target=run_gdi_effect, args=(effect_duration,))
    effect_thread.start()

    # The main program can continue or simply wait for the effect thread to finish.
    effect_thread.join() # Wait for the GDI effect thread to complete
    print("Program finished.")

import time
from GDI_effects.GDI import Effects
from threading import Thread

def run_gdi_effect():
    # The repeat value determines how many iterations the effect runs.
    # A higher number ensures it runs for the desired duration.
    # The library handles the drawing calls.
    Effects.screen_wavy(repeat=50000)

if __name__ == '__main__':
    # Start the GDI effect in a separate thread so the main program can manage the duration
    effect_thread = Thread(target=run_gdi_effect)
    effect_thread.start()

    # The main thread waits for 10 seconds
    time.sleep(10)

    # Note: The GDI-effects library's functions are typically blocking until 'repeat' is finished.
    # To strictly stop after 10 seconds, you might need a more advanced method to terminate the thread,
    # or use a different library/approach (like Pygame or direct win32gui calls with a time check in a loop)
    # that offers better time control within the effect loop.

import subprocess
import platform

def open_application(app_path):
    """Opens a specified application using subprocess."""
    try:
        if platform.system() == "Windows":
            # Use 'start' command on Windows
            subprocess.Popen(['start', app_path], shell=True)
        elif platform.system() == "Darwin":
            # Use 'open' command on macOS
            subprocess.Popen(['open', app_path])
        else:
            # Assumes Linux/Unix
            subprocess.Popen([app_path])
        print(f"Successfully attempted to open: {app_path}")
    except FileNotFoundError:
        print(f"Error: The application was not found at {app_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
# Replace with the actual path to your application
if platform.system() == "Windows":
    # Example for opening Calculator on Windows
    # Note: Modern UWP apps might need a different approach
    app_to_open = "calc.exe" 
elif platform.system() == "Darwin":
    # Example for opening Safari on macOS
    app_to_open = "/Applications/Safari.app"
else:
    # Example for opening Gnome Terminal on Linux
    app_to_open = "gnome-terminal"

open_application(app_to_open)

import time
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import randrange

def create_splatter_effect():
    # Get the device context (DC) for the entire screen
    desk = GetDC(0)
    x = GetSystemMetrics(0) # Screen width
    y = GetSystemMetrics(1) # Screen height

    # Draw 5000 random colored splats/rectangles
    for i in range(5000):
        # Create a solid brush with a random RGB color
        brush = CreateSolidBrush(RGB(randrange(255), randrange(255), randrange(255)))
        # Select the brush for drawing
        SelectObject(desk, brush)
        # Draw a filled rectangle (PatBlt uses width and height, not end coordinates)
        PatBlt(desk, randrange(x), randrange(y), randrange(100), randrange(200), PATCOPY)
        # Delete the brush to free up resources
        DeleteObject(brush)
        # Optional: Add a small sleep here to slow down the effect, if desired
        # Sleep(1) 

    # Release the device context
    ReleaseDC(desk, GetDesktopWindow())
    DeleteDC(desk)

if __name__ == '__main__':
    print("Running GDI splatter effect. Close the window or stop the script to end.")
    create_splatter_effect()

import time
import random
import win32gui
import win32api
import win32con
    """
    Runs a GDI paint splatter effect on the screen for a specified duration.
    """
    desk = win32gui.GetDC(0)
    x_screen = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y_screen = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    
    start_time = time.time()
    
    while time.time() - start_time < duration:
        # Create a solid brush with a random color
        # RGB function creates a color value from R, G, B components (0-255)
        color = win32api.RGB(random.randrange(256), random.randrange(256), random.randrange(256))
        brush = win32gui.CreateSolidBrush(color)
        win32gui.SelectObject(desk, brush)
        
        # Draw random ellipses (splats) across the screen
        x1 = random.randrange(x_screen)
        y1 = random.randrange(y_screen)
        # Random size for the "splat"
        width = random.randrange(20, 100) 
        height = random.randrange(20, 100)
        
        win32gui.Ellipse(desk, x1, y1, x1 + width, y1 + height)
        
        # Clean up the brush object after use
        win32gui.DeleteObject(brush)
        
        # Small sleep to control the speed of splattering
        time.sleep(0.01)

    # Release the device context
    win32gui.ReleaseDC(0, desk)
    print("GDI effect finished.")

if __name__ == "__main__":
    # Run the effect for 10 seconds
    run_splatter_effect(10)

import ctypes
import random
import time

def create_spray_effect(duration):
    # Load the user32 and gdi32 libraries
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32

    desk = user32.GetDC(0)
    
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    
    start_time = time.time()

    while time.time() - start_time < duration:
        # Draw a large number of random pixels (spray effect)
        for _ in range(50):  # Adjust the loop count for density of the spray
            x = random.randrange(screen_width)
            y = random.randrange(screen_height)
            
            # Generate a random color (RGB)
            color = random.randrange(256) | (random.randrange(256) << 8) | (random.randrange(256) << 16)
            
            # Set the pixel color
            gdi32.SetPixel(desk, x, y, color)
        
        # Short sleep to prevent the CPU from maxing out completely
        time.sleep(0.001)

    # Clean up (release the device context)
    user32.ReleaseDC(0, desk)
    print("GDI spray effect stopped after 10 seconds.")

if __name__ == '__main__':
    # Run the effect for 10 seconds
    create_spray_effect(10)

import time
from GDI_effects.GDI import Effects

def run_darken_effect_for_duration(duration_seconds):
    """
    Applies a screen effect (like inversion) for a specified duration.
    Note: GDI effects are often designed to loop or repeat, not a simple overlay with variable alpha.
    A common GDI effect is 'invert_screen'.
    """
    print(f"Applying screen effect for {duration_seconds} seconds...")
    
    # Run the GDI effect (e.g., invert colors) in a loop for the specified time
    end_time = time.time() + duration_seconds
    # The 'repeat' parameter in GDI-effects controls the *number* of times, not the duration,
    # so we use a while loop to control time.
    while time.time() < end_time:
        Effects.invert_screen(repeat=1) # Invert the screen once per loop iteration
        time.sleep(0.05) # Small sleep to prevent 100% CPU usage and allow some visual consistency
        # To make it a constant "darken" (not inversion), a more complex approach is needed 
        # involving creating an overlay window with specific alpha values, which goes beyond simple GDI_effects.
        # The 'invert_screen' is a readily available GDI effect.

    print("Effect ended.")

if __name__ == "__main__":
    # You can run this script directly in VS Code.
    run_darken_effect_for_duration(10)

import time
from GDI_effects.GDI import *

def run_rgb_effect(duration):
    """
    Runs an RGB (rainbow blink) GDI effect for a specified duration.

    Args:
        duration (int): The duration in seconds for which the effect should run.
    """
    start_time = time.time()
    # The 'repeat' parameter in the library functions controls how many times
    # the effect is applied within a single function call, not the total duration.
    # We use a while loop to control the total time the effect runs.
    while time.time() - start_time < duration:
        # 'rainbow_blink' creates a rapid color-changing effect
        # We pass a small repeat value inside the loop for continuous updates
        Effects.rainbow_blink(repeat=1)
        time.sleep(0.01) # Small sleep to prevent the CPU from running at 100%

    # Optional: Display a message when the effect stops
    print(f"GDI effect finished after {duration} seconds.")

if __name__ == "__main__":
    # Specify the duration in seconds
    effect_duration = 10
    run_rgb_effect(effect_duration)

import time
from GDI_effects.GDI import *
from win32gui import DestroyWindow # Import DestroyWindow if needed to clean up windows

def run_gdi_effect_for_duration(duration):
    start_time = time.time()
    # The repeat parameter in GDI-effects functions typically controls the
    # number of times an action is performed quickly, not the duration.
    # We will use a loop with a time check instead to control duration.
    
    # Invert the screen colors continuously
    while time.time() - start_time < duration:
        invert_screen(repeat=1) # Invert once per loop iteration
        time.sleep(0.01) # Small sleep to prevent 100% CPU usage and allow some screen updates

    # Note: Many GDI effects libraries are designed for "trolling" and might not
    # have a clean "stop" function that restores the screen state automatically.
    # The 'invert_screen' function is a toggle.
    # To stop the effect and potentially return the screen to normal,
    # you may need to run the invert function one more time.
    invert_screen(repeat=1) 
    
    # Some effects might leave artifacts or windows open, so be prepared to
    # close the script or handle potential side effects.

if __name__ == "__main__":
    print("GDI screen effect starting for 10 seconds...")
    run_gdi_effect_for_duration(10)
    print("GDI screen effect finished.")

import time
import random
from win32gui import GetDC, ReleaseDC, GetDesktopWindow, PatBlt
from win32api import GetSystemMetrics, CreateSolidBrush, SelectObject, DeleteObject, RGB
from win32con import PATCOPY, DESKTOPHORZRES, DESKTOPVERTRES

def white_screen_effect(duration=5):
    """
    Flashes the screen white for a specified duration using GDI.
    
    Args:
        duration: The number of seconds the effect should run.
    """
    desk = GetDC(0) # Get the device context for the entire screen
    x = GetSystemMetrics(DESKTOPHORZRES) # Get screen width
    y = GetSystemMetrics(DESKTOPVERTRES) # Get screen height

    start_time = time.time()
    while time.time() - start_time < duration:
        # Create a white brush
        white_brush = CreateSolidBrush(RGB(255, 255, 255)) 
        # Select the white brush for drawing
        SelectObject(desk, white_brush)
        # Fill the entire screen area with the current brush (white)
        PatBlt(desk, 0, 0, x, y, PATCOPY) 
        # Delete the brush to free resources
        DeleteObject(white_brush)
        
        # Add a small sleep to control the speed of the flashing
        time.sleep(0.05) 

    # Clean up and release the device context
    ReleaseDC(desk, GetDesktopWindow())
    DeleteDC(desk)

if __name__ == '__main__':
    print("Starting screen whitening effect for 5 seconds...")
    white_screen_effect(duration=5)
    print("Effect finished.")

from GDI_effects.GDI import *
import time

def dark_effect(duration=5):
    """
    Applies a screen darkening/inversion effect for a specified duration.
    """
    # Invert the screen colors repeatedly to create a visual effect
    # The 'repeat' argument defines how many times the effect is applied 
    # (higher means faster, more intense effect in the library's context)
    # This might not be a pure "darken" but a "glitchy" visual effect
    print(f"Applying dark GDI effect for {duration} seconds...")
    
    start_time = time.time()
    while time.time() - start_time < duration:
        # Invert colors (makes bright things dark and vice versa)
        # This function runs for a number of repetitions internally.
        invert_screen(repeat=50) 

    print("Effect finished.")

if __name__ == "__main__":
    # !!! DISCLAIMER !!!
    # GDI effects can cause rapid, flashing visual changes and may be disruptive.
    # Use with caution, especially if you are sensitive to flashing lights.
    # It is a harmless visual effect in this context but can be annoying.
    dark_effect(duration=5)
