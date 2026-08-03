import http.server
import socketserver
import webbrowser
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Ensure we serve from the root directory of the workspace
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(f"Starting server on http://localhost:{PORT}")
print("Press Ctrl+C to stop the server.")

# Open browser automatically
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
