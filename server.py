import json
import random
from http.server import SimpleHTTPRequestHandler, HTTPServer

class AnalyticsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            # Backend API Endpoint Logic
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            
            platforms = ['Instagram', 'WhatsApp', 'Facebook', 'YouTube', 'TikTok']
            locations = ['New York', 'London', 'Mumbai', 'Sydney', 'Tokyo', 'Berlin', 'Paris', 'Toronto', 'Seoul']
            
            # Generate dataset dynamically
            data = []
            for i in range(1, 51): # Serve 50 rows from backend
                data.append({
                    'id': f'USR{i:03}',
                    'age': random.randint(15, 55),
                    'platform': random.choice(platforms),
                    'time': round(random.uniform(0.5, 6.0), 1),
                    'location': random.choice(locations)
                })
            
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            # Fallback to serving static frontend files
            super().do_GET()

if __name__ == '__main__':
    port = 8080
    server = HTTPServer(('', port), AnalyticsHandler)
    print("=" * 50)
    print(f"Backend API Server successfully started on port {port}")
    print(f"Full-stack Web App accessible at: http://localhost:{port}/")
    print("=" * 50)
    server.serve_forever()
