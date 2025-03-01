FROM python:3.9-alpine

# Create necessary directories
RUN mkdir -p /home/data/output

# Copy Python script
COPY script.py /

# Set working directory
WORKDIR /

# Run the script when container starts
CMD ["python", "script.py"]