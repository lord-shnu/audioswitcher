import os
import subprocess

def reset_coreaudiod():
    print("Restarting coreaudiod...")

    try:
        subprocess.run(["sudo", "killall", "coreaudiod"], check=True)
        print("coreaudiod has been reset successfully.")
    except subprocess.CalledProcessError as e:
        print("Error restarting coreaudiod.")
        print(f"Details: {e}")
    except KeyboardInterrupt:
        print("Operation terminated.")

if __name__ == "__main__":
    reset_coreaudiod()
