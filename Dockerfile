FROM python:3.9-alpine

# Create necessary directories
RUN mkdir -p /home/data/output

# Copy the text files
COPY IF-1.txt /home/data/
COPY AlwaysRememberUsThisWay-1.txt /home/data/

# Copy Python script
COPY script.py /

# Set working directory
WORKDIR /

# Run the script when container starts
CMD ["python", "script.py"]