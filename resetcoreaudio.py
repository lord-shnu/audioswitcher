import os
import subprocess

def reset_coreaudiod():
    print("Restarting coreaudiod...")

    try:
        # Kill the coreaudiod process (it will restart automatically)
        subprocess.run(["sudo", "killall", "coreaudiod"], check=True)
        print("✅ coreaudiod has been restarted successfully.")
    except subprocess.CalledProcessError as e:
        print("❌ Error restarting coreaudiod.")
        print(f"Details: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

if __name__ == "__main__":
    reset_coreaudiod()
