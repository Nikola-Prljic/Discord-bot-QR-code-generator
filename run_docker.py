import subprocess

# Build the Docker image
subprocess.run(["docker", "build", "-t", "discord-qr-bot", "."], check=True)

# Run the Docker container
subprocess.run(["docker", "run", "--rm", "-it", "discord-qr-bot"], check=True)